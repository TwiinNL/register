/* =============================================================================
   Register: zoeken (vrije tekst) + facet-filteren via Pagefind.
   Valt netjes terug op de server-gerenderde kaartenlijst als Pagefind
   (nog) niet beschikbaar is, bv. in `hugo server` zonder index.
   ============================================================================= */
const root = document.documentElement;
const base = root.dataset.basepath || '/';

const els = {
  filters: document.getElementById('pf-filters'),
  search: document.getElementById('pf-search'),
  sort: document.getElementById('pf-sort'),
  stats: document.getElementById('pf-stats'),
  results: document.getElementById('pf-results'),
  form: document.getElementById('pf-form'),
};

// NL-koppen voor de facetgroepen (raw Pagefind-filternaam -> label)
const FILTER_LABELS = {
  soort: 'Soort',
  status: 'Status',
  domein: 'Domein',
  uitwisseling: 'Uitwisseling',
  patroon: 'Communicatiepatroon',
  functie: 'Generieke functie',
  toepassing: 'Toepassing',
  auteur: 'Auteur',
};
const FILTER_ORDER = ['soort', 'status', 'domein', 'uitwisseling', 'patroon', 'functie', 'toepassing', 'auteur'];

function withBase(u) {
  if (!u) return u;
  if (u.startsWith(base)) return u;
  return base.replace(/\/$/, '') + u;
}

const state = { q: '', filters: {}, sort: 'relevance' };
let pagefind = null;

// --- URL-parameters inlezen (?q=... en ?filter=soort:Label) ---
function readUrlParams() {
  const params = new URLSearchParams(location.search);
  state.q = params.get('q') || '';
  if (els.search) els.search.value = state.q;
  params.getAll('filter').forEach((f) => {
    const [k, v] = f.split(':');
    if (k && v) {
      (state.filters[k] = state.filters[k] || []).push(v);
    }
  });
}

async function initPagefind() {
  try {
    pagefind = await import(/* @vite-ignore */ `${base}pagefind/pagefind.js`);
    await pagefind.options({ excerptLength: 25 });
    await pagefind.init();
    return true;
  } catch (err) {
    console.warn('[register] Pagefind niet beschikbaar — server-gerenderde lijst blijft staan.', err);
    if (els.stats) els.stats.textContent = '';
    return false;
  }
}

function buildSearchOptions() {
  const opts = {};
  const active = {};
  for (const [k, vals] of Object.entries(state.filters)) {
    if (vals && vals.length) active[k] = vals;
  }
  if (Object.keys(active).length) opts.filters = active;
  if (state.sort === 'ingang_desc') opts.sort = { ingang: 'desc' };
  else if (state.sort === 'ingang_asc') opts.sort = { ingang: 'asc' };
  return opts;
}

async function runSearch() {
  if (!pagefind) return;
  const term = state.q.trim() === '' ? null : state.q.trim();
  const search = await pagefind.search(term, buildSearchOptions());
  const results = await Promise.all(search.results.map((r) => r.data()));
  renderResults(results);
  // Pagefind levert geen facet-tellingen bij een lege zoekopdracht zonder
  // filters; val dan terug op de volledige facetlijst.
  let facetCounts = search.filters || {};
  if (!Object.keys(facetCounts).length) facetCounts = await pagefind.filters();
  renderFacets(facetCounts);
  if (els.stats) {
    els.stats.textContent = `${results.length} resulta${results.length === 1 ? 'at' : 'ten'}` +
      (term ? ` voor “${term}”` : '');
  }
  syncUrl(term);
}

function renderResults(results) {
  if (!els.results) return;
  if (!results.length) {
    els.results.innerHTML = '<p class="muted">Geen resultaten. Pas je zoekterm of filters aan.</p>';
    return;
  }
  els.results.innerHTML = results.map((d) => {
    const m = d.meta || {};
    const badges = [];
    if (m.soort) badges.push(`<span class="badge">${esc(m.soort)}</span>`);
    if (m.status) badges.push(`<span class="badge">${esc(m.status)}</span>`);
    return `<article class="card">
      <a class="card__link" href="${esc(withBase(d.url))}">
        <header class="card__head">
          ${m.soort ? `<span class="badge">${esc(m.soort)}</span>` : ''}
          <span class="card__uid">${esc(m.uid || '')}</span>
        </header>
        <h3 class="card__title">${esc(m.title || '')}</h3>
        <p class="card__summary">${d.excerpt || ''}</p>
      </a>
      <footer class="card__foot">
        ${m.status ? `<span class="badge">${esc(m.status)}</span>` : ''}
      </footer>
    </article>`;
  }).join('');
}

function renderFacets(filterCounts) {
  if (!els.filters) return;
  const parts = [`<button type="button" class="btn btn--small filter-reset" id="pf-reset">Filters wissen</button>`];
  FILTER_ORDER.forEach((key) => {
    const counts = filterCounts[key];
    if (!counts) return;
    const active = state.filters[key] || [];
    // Toon alleen waarden met resultaten, plus reeds aangevinkte waarden.
    const values = Object.keys(counts)
      .filter((v) => counts[v] > 0 || active.includes(v))
      .sort((a, b) => a.localeCompare(b, 'nl'));
    if (!values.length) return;
    parts.push(`<div class="facet"><h3>${FILTER_LABELS[key] || key}</h3>`);
    values.forEach((v) => {
      const checked = active.includes(v) ? 'checked' : '';
      parts.push(`<label class="facet__option">
        <input type="checkbox" data-filter="${esc(key)}" value="${esc(v)}" ${checked}>
        <span>${esc(v)}</span><span class="facet__count">${counts[v]}</span>
      </label>`);
    });
    parts.push('</div>');
  });
  els.filters.innerHTML = parts.join('');
}

function esc(s) {
  return String(s == null ? '' : s).replace(/[&<>"']/g, (c) => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
  }[c]));
}

function syncUrl(term) {
  const params = new URLSearchParams();
  if (term) params.set('q', term);
  for (const [k, vals] of Object.entries(state.filters)) {
    (vals || []).forEach((v) => params.append('filter', `${k}:${v}`));
  }
  const qs = params.toString();
  history.replaceState(null, '', qs ? `?${qs}` : location.pathname);
}

function wireEvents() {
  if (els.form) els.form.addEventListener('submit', (e) => e.preventDefault());
  if (els.search) {
    let t;
    els.search.addEventListener('input', () => {
      clearTimeout(t);
      t = setTimeout(() => { state.q = els.search.value; runSearch(); }, 200);
    });
  }
  if (els.sort) els.sort.addEventListener('change', () => { state.sort = els.sort.value; runSearch(); });
  if (els.filters) {
    els.filters.addEventListener('change', (e) => {
      const cb = e.target.closest('input[data-filter]');
      if (!cb) return;
      const key = cb.getAttribute('data-filter');
      const arr = state.filters[key] = state.filters[key] || [];
      if (cb.checked) { if (!arr.includes(cb.value)) arr.push(cb.value); }
      else { state.filters[key] = arr.filter((v) => v !== cb.value); }
      runSearch();
    });
    els.filters.addEventListener('click', (e) => {
      if (e.target.id === 'pf-reset') { state.filters = {}; runSearch(); }
    });
  }
}

(async function () {
  readUrlParams();
  const ok = await initPagefind();
  if (!ok) return; // fallback: SSR-lijst blijft staan
  wireEvents();
  await runSearch();
})();
