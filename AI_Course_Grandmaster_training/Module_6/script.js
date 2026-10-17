/* ============================================================
   PORTFOLIO PROJECT — script.js
   ------------------------------------------------------------
   Three independent features. Each in its own block.
   Remove any block and the others keep working.
   ============================================================ */

/* ------------------------------------------------------------
   1. SCROLL SHADOW ON THE NAVBAR
   ------------------------------------------------------------
   The navbar has no shadow by default. After 10px of scroll
   we add .is-scrolled, which brings in a soft shadow and a
   subtle bottom border — the "glass got thicker" effect.
   `passive: true` tells the browser we never call preventDefault,
   so it can optimise scroll handling.
   ------------------------------------------------------------ */
const nav = document.getElementById("siteNav");

function handleScroll() {
  nav.classList.toggle("is-scrolled", window.scrollY > 10);
}

window.addEventListener("scroll", handleScroll, { passive: true });
handleScroll(); // run once on load in case the page is restored mid-scroll

/* ------------------------------------------------------------
   2. ACTIVE NAV LINK WHILE SCROLLING
   ------------------------------------------------------------
   IntersectionObserver fires when a section crosses a
   pre-defined "reading zone" — the middle of the viewport.
   The negative rootMargin (-40% from the top, -55% from the
   bottom) squeezes the observation area into a horizontal
   band, so a section is only active while its content is
   actually in front of the user.
   ------------------------------------------------------------ */
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll('.site-nav .nav-link[href^="#"]');

if ("IntersectionObserver" in window && sections.length) {
  const spy = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;

        const id = entry.target.id;
        navLinks.forEach((link) => {
          link.classList.toggle(
            "active",
            link.getAttribute("href") === "#" + id,
          );
        });
      });
    },
    {
      rootMargin: "-40% 0px -55% 0px",
      threshold: 0,
    },
  );

  sections.forEach((section) => spy.observe(section));
}

/* ------------------------------------------------------------
   3. CLOSE THE MOBILE MENU ON LINK CLICK
   ------------------------------------------------------------
   On small screens, clicking a nav link scrolls the page but
   leaves the menu tray open. Close it programmatically.
   Bootstrap 5.3 exposes `bootstrap.Collapse` on window once
   the JS bundle has loaded.
   ------------------------------------------------------------ */
const navMenu = document.getElementById("navMenu");

if (navMenu && window.bootstrap) {
  navMenu.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      if (window.innerWidth >= 992) return; // desktop — no menu to close
      const instance =
        bootstrap.Collapse.getInstance(navMenu) ||
        bootstrap.Collapse.getOrCreateInstance(navMenu, { toggle: false });
      instance.hide();
    });
  });
}

/* ------------------------------------------------------------
   4. FADE-IN ON SCROLL
   ------------------------------------------------------------
   .reveal starts invisible ONLY after JS has loaded — see
   .js-ready in style.css. Without JS, content stays visible.
   Elements fade in once and stay visible (unobserve after).
   ------------------------------------------------------------ */
const prefersReducedMotion = window.matchMedia(
  "(prefers-reduced-motion: reduce)",
).matches;

if (!prefersReducedMotion && "IntersectionObserver" in window) {
  document.body.classList.add("js-ready");

  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        revealObserver.unobserve(entry.target);
      });
    },
    { threshold: 0.15 },
  );

  document.querySelectorAll(".reveal").forEach((el) => {
    revealObserver.observe(el);
  });
}
