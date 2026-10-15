(() => {
  const storageKey = "repere-salon-demo-selection-v1";
  const modelNames = { A: "Ligne A — 2 places", B: "Ligne B — 3 places", C: "Ligne C — angle" };
  let selection = [];
  try {
    const stored = JSON.parse(localStorage.getItem(storageKey) || "[]");
    if (Array.isArray(stored)) selection = stored.filter((key) => Object.hasOwn(modelNames, key));
  } catch (_) {
    selection = [];
  }

  const save = () => {
    try { localStorage.setItem(storageKey, JSON.stringify(selection)); } catch (_) { /* local storage may be unavailable */ }
  };

  const updateSelectionUI = () => {
    document.querySelectorAll(".saved-count").forEach((node) => { node.textContent = String(selection.length); });
    document.querySelectorAll("[data-save]").forEach((button) => {
      const active = selection.includes(button.dataset.save);
      button.setAttribute("aria-pressed", String(active));
      if (!button.dataset.originalLabel) button.dataset.originalLabel = button.textContent.trim();
      button.textContent = active ? "✓ Dans ma sélection" : button.dataset.originalLabel;
    });
    const list = document.getElementById("saved-list");
    if (list) {
      list.replaceChildren();
      if (selection.length === 0) {
        const empty = document.createElement("li");
        empty.textContent = "Aucun modèle sélectionné.";
        list.append(empty);
      } else {
        selection.forEach((key) => {
          const item = document.createElement("li");
          item.textContent = modelNames[key];
          list.append(item);
        });
      }
    }
  };

  document.querySelectorAll("[data-save]").forEach((button) => {
    button.addEventListener("click", () => {
      const key = button.dataset.save;
      selection = selection.includes(key) ? selection.filter((item) => item !== key) : [...selection, key];
      save();
      updateSelectionUI();
    });
  });

  const clearButton = document.getElementById("clear-saved");
  if (clearButton) clearButton.addEventListener("click", () => { selection = []; save(); updateSelectionUI(); });
  updateSelectionUI();

  const widthSlider = document.getElementById("width-range");
  const widthOutput = document.getElementById("width-output");
  const fitRows = [...document.querySelectorAll("#fit-model-list [data-width]")];
  const fitCount = document.getElementById("fit-count");
  const fitCaption = document.getElementById("fit-caption");
  if (widthSlider && widthOutput) {
    const refreshWidthTool = () => {
      const width = Number(widthSlider.value);
      widthOutput.value = `${width} cm`;
      widthOutput.textContent = `${width} cm`;
      const compatible = fitRows.filter((row) => Number(row.dataset.width) <= width);
      fitRows.forEach((row) => { row.hidden = Number(row.dataset.width) > width; });
      if (fitCount) fitCount.textContent = `${compatible.length} modèle${compatible.length === 1 ? "" : "s"} d’exemple`;
      if (fitCaption) fitCaption.textContent = compatible.length ? "entrent dans cette largeur." : "ne correspond à cette largeur.";
    };
    widthSlider.addEventListener("input", refreshWidthTool);
    refreshWidthTool();
  }

  const maxWidth = document.getElementById("max-width");
  const productRows = [...document.querySelectorAll("#product-list [data-width]")];
  const categoryResult = document.getElementById("category-result");
  const emptyState = document.getElementById("empty-state");
  if (maxWidth && productRows.length) {
    const filterCategory = () => {
      const raw = Number(maxWidth.value);
      const width = Number.isFinite(raw) && raw > 0 ? raw : 0;
      let count = 0;
      productRows.forEach((row) => {
        const visible = Number(row.dataset.width) <= width;
        row.hidden = !visible;
        if (visible) count += 1;
      });
      if (categoryResult) categoryResult.textContent = `${count} modèle${count === 1 ? "" : "s"} d’exemple affiché${count === 1 ? "" : "s"}`;
      if (emptyState) emptyState.hidden = count !== 0;
    };
    maxWidth.addEventListener("input", filterCategory);
    maxWidth.addEventListener("change", filterCategory);
    filterCategory();
  }

  document.querySelectorAll(".menu-toggle").forEach((button) => {
    const nav = document.getElementById(button.getAttribute("aria-controls"));
    if (!nav) return;
    button.addEventListener("click", () => {
      const open = button.getAttribute("aria-expanded") !== "true";
      button.setAttribute("aria-expanded", String(open));
      nav.classList.toggle("is-open", open);
    });
    nav.addEventListener("click", (event) => {
      if (event.target.closest("a")) {
        button.setAttribute("aria-expanded", "false");
        nav.classList.remove("is-open");
      }
    });
  });

  document.querySelectorAll("[data-current-year]").forEach((node) => { node.textContent = String(new Date().getFullYear()); });
})();
