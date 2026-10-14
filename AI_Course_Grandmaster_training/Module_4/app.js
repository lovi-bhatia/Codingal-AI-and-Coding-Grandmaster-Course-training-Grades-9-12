/* ============================================================
   app.js — Live Task Manager
   ------------------------------------------------------------
   This file contains ONLY JavaScript.
   No <script> tags. No HTML. It is linked from index.html with:
       <script src="app.js" defer></script>
   ============================================================ */

/* ------------------------------------------------------------
   1. STATE — the single source of truth
   ------------------------------------------------------------ */
let tasks = loadTasks(); // array of { id, text, done }
let currentFilter = "all"; // "all" | "active" | "done"

/* ------------------------------------------------------------
   2. DOM REFERENCES — grab every element once
   ------------------------------------------------------------ */
const form = document.getElementById("taskForm");
const input = document.getElementById("taskInput");
const list = document.getElementById("taskList");
const empty = document.getElementById("emptyState");
const filterBar = document.getElementById("filterBar");
const clearBtn = document.getElementById("clearBtn");
const clock = document.getElementById("clock");

const statTotal = document.getElementById("statTotal");
const statDone = document.getElementById("statDone");
const statLeft = document.getElementById("statLeft");

/* ------------------------------------------------------------
   3. STORAGE — persist tasks across reloads
   ------------------------------------------------------------ */
function loadTasks() {
  try {
    const saved = localStorage.getItem("tasks");
    if (saved) return JSON.parse(saved);
  } catch (err) {
    console.warn("Could not read saved tasks:", err);
  }
  // First run: seed with a couple of demo tasks
  return [
    { id: "1", text: "Read the external JS file structure", done: true },
    { id: "2", text: "Add your own task using the form", done: false },
  ];
}

function saveTasks() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

/* ------------------------------------------------------------
   4. RENDER — the ONLY function allowed to touch the UI
   ------------------------------------------------------------ */
function visibleTasks() {
  if (currentFilter === "active") return tasks.filter((t) => !t.done);
  if (currentFilter === "done") return tasks.filter((t) => t.done);
  return tasks;
}

function render() {
  const items = visibleTasks();

  /* 4a. Empty state toggle */
  empty.classList.toggle("d-none", items.length > 0);

  /* 4b. Build all rows off-screen in a DocumentFragment.
         One insert = one reflow, instead of one per task. */
  const frag = document.createDocumentFragment();

  items.forEach((task) => {
    const li = document.createElement("li");
    li.className = "list-group-item d-flex align-items-center gap-2";
    li.dataset.id = task.id;

    /* Structure is static — user text is inserted separately below */
    li.innerHTML = `
      <input class="form-check-input mt-0 flex-shrink-0"
             type="checkbox"
             data-action="toggle"
             ${task.done ? "checked" : ""}>
      <span class="flex-grow-1"></span>
      <button class="btn btn-sm btn-outline-danger px-2"
              data-action="delete"
              title="Delete task">&times;</button>
    `;

    /* SAFE insert — never put user input into innerHTML */
    const label = li.querySelector("span");
    label.textContent = task.text;
    if (task.done)
      label.classList.add("text-decoration-line-through", "text-muted");

    frag.appendChild(li);
  });

  list.innerHTML = ""; // clear old rows
  list.appendChild(frag); // single insert

  /* 4c. Stats */
  updateStats();
}

function updateStats() {
  const total = tasks.length;
  const done = tasks.filter((t) => t.done).length;

  statTotal.textContent = total;
  statDone.textContent = done;
  statLeft.textContent = total - done;
}

/* ------------------------------------------------------------
   5. ACTIONS — change the state, then re-render
   ------------------------------------------------------------ */
function addTask(text) {
  const clean = text.trim();
  if (!clean) return;

  tasks.unshift({
    id: Date.now().toString(),
    text: clean,
    done: false,
  });

  saveTasks();
  render();
}

function toggleTask(id) {
  const task = tasks.find((t) => t.id === id);
  if (!task) return;

  task.done = !task.done;
  saveTasks();
  render();
}

function deleteTask(id) {
  tasks = tasks.filter((t) => t.id !== id);
  saveTasks();
  render();
}

function clearCompleted() {
  tasks = tasks.filter((t) => !t.done);
  saveTasks();
  render();
}

function setFilter(filter) {
  currentFilter = filter;
  render();
}

/* ------------------------------------------------------------
   6. EVENTS — wire the UI to the actions
   ------------------------------------------------------------ */

/* 6a. Add via form submit (covers Enter key too) */
form.addEventListener("submit", (e) => {
  e.preventDefault(); // stop the page from reloading
  addTask(input.value);
  input.value = "";
  input.focus();
});

/* 6b. EVENT DELEGATION on the list.
       One listener handles every checkbox and delete button,
       even rows created later. */
list.addEventListener("click", (e) => {
  const action = e.target.dataset.action;
  if (!action) return;

  const id = e.target.closest("li").dataset.id;

  if (action === "toggle") toggleTask(id);
  if (action === "delete") deleteTask(id);
});

/* 6c. Filter buttons — also delegation */
filterBar.addEventListener("click", (e) => {
  const filter = e.target.dataset.filter;
  if (!filter) return;

  // move the "active" class to the clicked button
  [...filterBar.children].forEach((btn) =>
    btn.classList.toggle("active", btn === e.target),
  );

  setFilter(filter);
});

/* 6d. Clear completed */
clearBtn.addEventListener("click", clearCompleted);

/* ------------------------------------------------------------
   7. LIVE CLOCK — the "real time" part
   ------------------------------------------------------------ */
function tick() {
  clock.textContent = new Date().toLocaleTimeString();
}

setInterval(tick, 1000);
tick(); // run once immediately so there is no 1-second delay

/* ------------------------------------------------------------
   8. BOOT — start the app
   ------------------------------------------------------------ */
render();
