/* Thema-toggle (licht/donker) + kopieer-knoppen. */
(function () {
  const root = document.documentElement;
  const stored = localStorage.getItem('theme');
  if (stored) root.setAttribute('data-theme', stored);

  const toggle = document.querySelector('.theme-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      const current = root.getAttribute('data-theme')
        || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      const next = current === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    });
  }

  document.addEventListener('click', function (e) {
    const btn = e.target.closest('[data-copy]');
    if (!btn) return;
    const el = document.querySelector(btn.getAttribute('data-copy'));
    if (!el) return;
    navigator.clipboard.writeText(el.textContent.trim()).then(function () {
      const old = btn.textContent;
      btn.textContent = 'Gekopieerd ✓';
      setTimeout(function () { btn.textContent = old; }, 1500);
    });
  });
})();
