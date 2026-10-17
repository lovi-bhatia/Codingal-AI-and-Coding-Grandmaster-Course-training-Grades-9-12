/* ============================================================
   validator.js — reusable form validation module
   ------------------------------------------------------------
   WHY THIS FILE EXISTS
   ------------------------------------------------------------
   The browser ships the Constraint Validation API for free.
   It handles:
       required, minlength, maxlength, type="email",
       type="number", type="url", pattern, min, max, step

   Every app needs MORE than that:
       - custom rules    (phone, password strength)
       - cross-field     (password === confirm password)
       - error UI        (Bootstrap .is-invalid / .is-valid)
       - quiet re-checking once the user fixes the field

   This module wraps the Constraint Validation API and adds
   everything above, so every form on every page can reuse
   the same rules and the same submit handling.

   ------------------------------------------------------------
   HOW TO USE IN THE MAIN FILE
   ------------------------------------------------------------
       <script src="validator.js"></script>

       FormValidator.bind(document.getElementById("myForm"));

       form.addEventListener("validated", e => {
         console.log("form OK, data:", e.detail);
       });

   ------------------------------------------------------------
   HOW TO DECLARE A RULE ON A FIELD
   ------------------------------------------------------------
       <input required>                               ← HTML5
       <input type="email" required>                  ← HTML5

       <input data-rule="phone">                      ← custom
       <input data-rule="password">                   ← custom
       <input data-rule="min:5">                      ← custom + arg

       <input data-match="#passwordField">            ← cross-field
       <input data-message="Please enter a valid email">

   ------------------------------------------------------------
   PUBLIC API (window.FormValidator)
   ------------------------------------------------------------
       .rules               → flat map of every available rule
       .addRule(name, fn)   → register a new rule everywhere
       .bind(form)          → attach live checks + submit handler
       .validateForm(form)  → returns true / false; focuses first bad
       .validateField(el, form)
       .attachLive(form)
   ============================================================ */

(function (global) {
  "use strict";

  // ------------------------------------------------------------
  // 1. CUSTOM RULES
  // Each rule receives (value, arg) and returns true / false.
  // An empty value always passes — `required` is HTML5's job.
  // ------------------------------------------------------------
  const RULES = {
    required: (v) => v !== null && String(v).trim() !== "",
    email: (v) => v === "" || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v),
    phone: (v) => v === "" || /^\d{10}$/.test(v.replace(/\s/g, "")),
    password: (v) => v === "" || /^(?=.*[A-Za-z])(?=.*\d).{8,}$/.test(v),
    number: (v) => v === "" || !Number.isNaN(Number(v)),
    min: (v, arg) => v === "" || Number(v) >= Number(arg),
    max: (v, arg) => v === "" || Number(v) <= Number(arg),
    minlength: (v, arg) => v === "" || v.length >= Number(arg),
    maxlength: (v, arg) => v === "" || v.length <= Number(arg),
  };

  // ------------------------------------------------------------
  // 2. DIRTY TRACKING
  // Do not mark a field invalid before the user has touched it.
  // This WeakSet remembers which fields have been blurred once
  // or checked on submit.
  // ------------------------------------------------------------
  const dirty = new WeakSet();

  // ------------------------------------------------------------
  // 3. VALIDATE A SINGLE FIELD
  // Runs the checks in this order:
  //   a. reset any previous custom error
  //   b. HTML5 checks via el.checkValidity()
  //   c. data-rule="name" or "name:arg"
  //   d. data-match="#other"
  //   e. update the visuals and the .invalid-feedback text
  // ------------------------------------------------------------
  function validateField(el, form) {
    el.setCustomValidity("");

    let ok = true;
    let message = "";

    // a. Native HTML5 checks (required, minlength, type, pattern…)
    if (!el.checkValidity()) {
      ok = false;
      message = el.validationMessage;
    }

    // b. Custom rule declared with data-rule
    if (ok && el.dataset.rule) {
      const [name, arg] = el.dataset.rule.split(":");
      const rule = RULES[name];
      if (rule && !rule(el.value, arg)) {
        ok = false;
        message = el.dataset.message || "Invalid value for " + name;
        el.setCustomValidity(message); // propagates to form.checkValidity()
      }
    }

    // c. Cross-field rule: value must equal another field
    if (ok && el.dataset.match) {
      const other = form.querySelector(el.dataset.match);
      if (other && el.value !== other.value) {
        ok = false;
        message = el.dataset.message || "Values do not match";
        el.setCustomValidity(message);
      }
    }

    // d. Visual state
    const touched = dirty.has(el);
    el.classList.toggle("is-invalid", !ok && touched);
    el.classList.toggle("is-valid", ok && el.value !== "" && touched);

    // e. Feedback text
    const feedback = el.parentElement
      ? el.parentElement.querySelector(".invalid-feedback")
      : null;
    if (feedback && !ok) feedback.textContent = message;

    return ok;
  }

  // ------------------------------------------------------------
  // 4. VALIDATE THE WHOLE FORM
  // Skips disabled, hidden, and submit inputs.
  // Focuses the first invalid field so the page scrolls to it.
  // ------------------------------------------------------------
  function validateForm(form) {
    let ok = true;
    let firstInvalid = null;

    form.querySelectorAll("input, select, textarea").forEach((el) => {
      if (el.disabled || el.type === "hidden" || el.type === "submit") return;
      dirty.add(el);
      if (!validateField(el, form)) {
        ok = false;
        if (!firstInvalid) firstInvalid = el;
      }
    });

    if (firstInvalid) firstInvalid.focus();
    return ok;
  }

  // ------------------------------------------------------------
  // 5. LIVE RE-VALIDATION
  // - On blur: run the checks (a field the user has left).
  // - On input: re-check ONLY if the field is already showing
  //   an error or has been touched, so the error disappears
  //   the moment the user fixes it.
  // - data-match: also re-check the dependant when the source
  //   field changes.
  // ------------------------------------------------------------
  function attachLive(form) {
    form.querySelectorAll("input, select, textarea").forEach((el) => {
      el.addEventListener("blur", () => {
        dirty.add(el);
        validateField(el, form);
      });
      el.addEventListener("input", () => {
        if (dirty.has(el) || el.classList.contains("is-invalid")) {
          validateField(el, form);
        }
      });
    });

    form.querySelectorAll("[data-match]").forEach((el) => {
      const other = form.querySelector(el.dataset.match);
      if (!other) return;
      other.addEventListener("input", () => {
        if (dirty.has(el) || el.classList.contains("is-invalid")) {
          validateField(el, form);
        }
      });
    });
  }

  // ------------------------------------------------------------
  // 6. PUBLIC API
  // ------------------------------------------------------------
  const FormValidator = {
    rules: RULES,

    // Register a new rule available to every form
    addRule(name, fn) {
      RULES[name] = fn;
      return FormValidator;
    },

    validateField,
    validateForm,
    attachLive,

    // Bind a form: attach live checks + intercept submit
    bind(form) {
      form.setAttribute("novalidate", ""); // hide native bubbles
      attachLive(form);

      form.addEventListener("submit", (event) => {
        event.preventDefault();

        const ok = validateForm(form);
        const payload = Object.fromEntries(new FormData(form).entries());

        // Dispatch a custom event so app code can react
        form.dispatchEvent(
          new CustomEvent(ok ? "validated" : "invalid", {
            detail: payload,
          }),
        );
      });

      return FormValidator;
    },
  };

  global.FormValidator = FormValidator;
})(window);
