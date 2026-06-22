/* Uitgelicht-schakelaar: wissel tussen 'Belangrijk' en 'Recent'. */
(function () {
  const buttons = document.querySelectorAll('.switch__btn[data-featured]');
  const panels = document.querySelectorAll('[data-featured-panel]');
  if (!buttons.length) return;

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      const key = btn.getAttribute('data-featured');
      buttons.forEach(b => b.classList.toggle('is-active', b === btn));
      panels.forEach(p => { p.hidden = p.getAttribute('data-featured-panel') !== key; });
    });
  });
})();
