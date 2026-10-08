#!/usr/bin/env python3
"""
Genereer static/inject.js : dunne loader die het register in een Scroll/Confluence-
pagina mount door de DOOR HUGO GEBOUWDE HTML op te halen (zelfde md-build als de
standalone /register/). Eenmalige bron voor de opmaak:

  - lijst   : fetch  https://register.twiin.nl/embed/  -> injecteer het .register-blok
              (SSR-kaarten + zoekformulier + filtercontainer), filters RECHTS.
  - detail  : bij kaartklik fetch de kaart-permalink  -> toon .kaart in de pagina
              (terug-knop), zodat de gebruiker op de Confluence-pagina blijft.

Alleen vocab-labels (voor de facetkoppen) en de scoped CSS worden meegebakken
(bron = data/vocab.yaml). GitHub Pages stuurt 'access-control-allow-origin: *',
dus de cross-origin fetch mag.

Laden via Scroll 'Custom JavaScript' (IIFE, raw JS zonder <script>-tags):
  (function(){
    var s=document.createElement('script');
    s.src='https://register.twiin.nl/inject.js';
    s.charset='utf-8';
    document.head.appendChild(s);
  })();

Pure ASCII uitvoer.
"""
import json, os, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
vocab = yaml.safe_load(open(os.path.join(ROOT, "data", "vocab.yaml"), encoding="utf-8"))

SITE = "https://register.twiin.nl/"
PAGEKEY = "landelijke-afspraken"

# Facetvolgorde + NL-koppen. data-attribuut op de kaart = data-<key>.
FACETS = [["soort", "Soort"], ["status", "Status"], ["domein", "Domein"],
          ["uitwisseling", "Uitwisseling"], ["patroon", "Communicatiepatroon"],
          ["functie", "Generieke functie"], ["toepassing", "Toepassing"], ["auteur", "Auteur"]]
# facetsleutel -> vocab-sleutel (voor labels bij de codes). 'auteur' heeft geen vocab.
FACET_VOCAB = {"soort": "soort", "status": "status", "domein": "domein",
               "uitwisseling": "uitwisseling", "patroon": "patroon",
               "functie": "functie", "toepassing": "stelsel"}

def labels_for(vkey):
    terms = (vocab.get(vkey) or {}).get("terms", {}) or {}
    return {code: (t or {}).get("label", code) for code, t in terms.items()}

LABELS = {fk: labels_for(vk) for fk, vk in FACET_VOCAB.items()}
LABELS["auteur"] = {}

CSS = r"""
.twiin-las{--accent:#e6396a;--bg:#fff;--bg-alt:#f6f4f7;--surface:#fff;--border:#e6e2e9;--text:#283340;--muted:#6a6675;--navy:#243140;--radius:12px;--radius-sm:8px;--shadow:0 1px 2px rgba(36,49,64,.06),0 4px 16px rgba(36,49,64,.07);--mono:ui-monospace,Menlo,Consolas,monospace;font-family:"Roboto",-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;color:var(--text);line-height:1.55;}
.twiin-las *{box-sizing:border-box;}
.twiin-las a{color:var(--accent);text-decoration:none;}
.twiin-las a:hover{text-decoration:underline;}
.twiin-las .muted{color:var(--muted);}
.twiin-las [hidden]{display:none!important;}
/* De filters monteren we in Scroll's eigen sticky-TOC-slot (makeTocHost); die regelt
   positie RECHTS en het verbergen-bij-smal. De hoofdkolom (zoeken+resultaten) staat
   vol-breed in de artikelkolom. */
.twiin-las .register__main{min-width:0;}
.twiin-las .register__filters{background:transparent;border:0;padding:0;}
.twiin-las-toc{overflow:auto;border:1px solid var(--_border-color,var(--border));border-radius:var(--K15t-radius-small,10px);background:var(--_background-color,var(--surface));}
.twiin-las-toc .register__filters{padding:12px 16px;}
.twiin-las.twiin-las-toc .register__filters h3{font:var(--K15t-font-body-small-strong, 600 .82rem/1.4 Roboto,sans-serif);color:var(--_foreground-color,var(--navy));text-transform:none;letter-spacing:normal;}
.twiin-las .filter-reset{display:flex;justify-content:flex-end;margin-bottom:.6rem;}
.twiin-las .register__filters h3{margin:.2rem 0 .6rem;font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);}
.twiin-las .facet{margin-bottom:1.1rem;}
.twiin-las .facet__option{display:flex;align-items:center;gap:.45rem;font-size:.85rem;padding:.12rem 0;cursor:pointer;}
.twiin-las .facet__option input{accent-color:var(--accent);}
.twiin-las .facet__count{margin-left:auto;color:var(--muted);font-size:.78rem;}
.twiin-las .search{display:flex;gap:.75rem;align-items:center;margin-bottom:1rem;flex-wrap:wrap;}
.twiin-las input[type=search],.twiin-las select{padding:.62rem .8rem;border:1px solid var(--border);border-radius:var(--radius-sm);background:var(--surface);color:var(--text);font-size:.95rem;font-family:inherit;}
.twiin-las input[type=search]{flex:1;min-width:220px;}
.twiin-las .search__sort{font-size:.85rem;color:var(--muted);display:flex;align-items:center;gap:.4rem;white-space:nowrap;}
.twiin-las .register__stats{color:var(--muted);font-size:.85rem;margin:.2rem 0 1rem;}
.twiin-las .btn{background:var(--accent);color:#fff;border:none;border-radius:999px;padding:.4rem .9rem;font-size:.82rem;font-weight:600;cursor:pointer;}
.twiin-las .card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1rem;}
.twiin-las .card{display:flex;flex-direction:column;justify-content:space-between;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1rem 1.1rem;box-shadow:var(--shadow);}
.twiin-las .card__link{color:inherit;display:block;cursor:pointer;}
.twiin-las .card__link:hover{text-decoration:none;}
.twiin-las .card__head{display:flex;align-items:center;justify-content:space-between;gap:.5rem;margin-bottom:.5rem;}
.twiin-las .card__uid{font-family:var(--mono);font-size:.72rem;color:var(--muted);}
.twiin-las .card__title{margin:.1rem 0 .4rem;font-size:1.02rem;line-height:1.3;color:var(--text);}
.twiin-las .card__summary{color:var(--muted);font-size:.86rem;margin:0;}
.twiin-las .card__foot{display:flex;flex-wrap:wrap;gap:.35rem;margin-top:.8rem;}
.twiin-las .badge{display:inline-block;padding:.15rem .55rem;border-radius:999px;font-size:.74rem;font-weight:600;line-height:1.5;white-space:nowrap;background:var(--c-grijs-bg,#eceef3);color:var(--c-grijs-fg,#444c5e);}
.twiin-las{--c-groen-bg:#e3f6ec;--c-groen-fg:#0f7a43;--c-blauw-bg:#e6effd;--c-blauw-fg:#1857c4;--c-paars-bg:#efe7fb;--c-paars-fg:#6936c9;--c-cyaan-bg:#e0f4f7;--c-cyaan-fg:#0d7a8c;--c-oranje-bg:#fdeede;--c-oranje-fg:#b35c00;--c-geel-bg:#fcf3d6;--c-geel-fg:#8a6a00;--c-rood-bg:#fde7e7;--c-rood-fg:#bb2222;--c-grijs-bg:#eceef3;--c-grijs-fg:#444c5e;}
.twiin-las .badge--groen{background:var(--c-groen-bg);color:var(--c-groen-fg);}.twiin-las .badge--blauw{background:var(--c-blauw-bg);color:var(--c-blauw-fg);}.twiin-las .badge--paars{background:var(--c-paars-bg);color:var(--c-paars-fg);}.twiin-las .badge--cyaan{background:var(--c-cyaan-bg);color:var(--c-cyaan-fg);}.twiin-las .badge--oranje{background:var(--c-oranje-bg);color:var(--c-oranje-fg);}.twiin-las .badge--geel{background:var(--c-geel-bg);color:var(--c-geel-fg);}.twiin-las .badge--rood{background:var(--c-rood-bg);color:var(--c-rood-fg);}.twiin-las .badge--grijs{background:var(--c-grijs-bg);color:var(--c-grijs-fg);}
.twiin-las .badges{display:flex;flex-wrap:wrap;gap:.35rem;}
.twiin-las .kaart__back{display:inline-block;margin-bottom:1rem;font-size:.85rem;background:none;border:none;color:var(--accent);cursor:pointer;padding:0;}
.twiin-las .kaart__badges{display:flex;gap:.4rem;margin-bottom:.5rem;}
.twiin-las .kaart__uid{font-family:var(--mono);color:var(--muted);font-size:.85rem;margin:0;}
.twiin-las .kaart__title{margin:.2rem 0 .5rem;font-size:1.7rem;line-height:1.2;color:var(--navy);}
.twiin-las .kaart__lead{font-size:1.05rem;max-width:70ch;margin:0 0 1.2rem;}
.twiin-las .kaart section{margin-bottom:1.6rem;}
.twiin-las .kaart h2{font-size:1.1rem;border-bottom:1px solid var(--border);padding-bottom:.35rem;margin:0 0 .7rem;}
.twiin-las .attr-grid{display:grid;grid-template-columns:200px 1fr;gap:0 1rem;margin:0;}
.twiin-las .attr-grid dt{font-weight:600;padding:.45rem 0;border-top:1px solid var(--border);}
.twiin-las .attr-grid dd{margin:0;padding:.45rem 0;border-top:1px solid var(--border);}
.twiin-las .attr-grid dt:first-of-type,.twiin-las .attr-grid dd:first-of-type{border-top:none;}
@media (max-width:600px){.twiin-las .attr-grid{grid-template-columns:1fr;}}
.twiin-las .ref-list{margin:0;padding-left:1.2rem;}.twiin-las .ref-list li{margin:.3rem 0;}
.twiin-las table.log-table{width:100%;border-collapse:collapse;font-size:.9rem;}
.twiin-las table.log-table th,.twiin-las table.log-table td{text-align:left;padding:.5rem .6rem;border-bottom:1px solid var(--border);vertical-align:top;}
.twiin-las table.log-table th{background:var(--bg-alt);}
.twiin-las .tag-prefix{font-family:var(--mono);font-size:.7rem;color:var(--muted);}
.twiin-las .permalink-box{background:var(--bg-alt);border:1px solid var(--border);border-radius:var(--radius);padding:1rem 1.1rem;margin-bottom:1.6rem;}
.twiin-las .permalink-box h2{border:0;margin:0 0 .3rem;font-size:1rem;}
.twiin-las .permalink-box__hint{font-size:.82rem;color:var(--muted);margin:0 0 .7rem;}
.twiin-las .permalink-box__row{display:flex;gap:.6rem;align-items:center;flex-wrap:wrap;}
.twiin-las .permalink-box__url{font-family:var(--mono);font-size:.82rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-sm);padding:.5rem .7rem;flex:1;word-break:break-all;}
.twiin-las .permalink-box__formats{font-size:.82rem;margin:.7rem 0 0;color:var(--muted);}
/* Donkere modus: volgt data-color-scheme van het ontwikkelsupplement/Scroll-thema. */
html[data-color-scheme="dark"] .twiin-las{--bg:#0f1113;--bg-alt:#1a1d21;--surface:#16191d;--border:#2b3038;--text:#e3e5e8;--muted:#9aa0a8;--navy:#e8eaed;--accent:#f2578a;--shadow:0 1px 2px rgba(0,0,0,.5),0 4px 16px rgba(0,0,0,.55);--c-groen-bg:#123524;--c-groen-fg:#5fce97;--c-blauw-bg:#15233f;--c-blauw-fg:#84b1ff;--c-paars-bg:#241a3a;--c-paars-fg:#b79bf0;--c-cyaan-bg:#0e2c33;--c-cyaan-fg:#57cfe0;--c-oranje-bg:#3a2410;--c-oranje-fg:#f0a95c;--c-geel-bg:#332a10;--c-geel-fg:#e0c46a;--c-rood-bg:#3a1414;--c-rood-fg:#f08a8a;--c-grijs-bg:#22262d;--c-grijs-fg:#aeb6c2;}
"""

JS = r"""
(function(){
  if(window.__twiinLasInit){return;} window.__twiinLasInit=true;
  var SITE=__SITE__, EMBED=SITE+'embed/', PAGEKEY=__PAGEKEY__;
  var FACETS=__FACETS__, LABELS=__LABELS__;
  var MAIN_SELECTORS=['.article-body.fb-layout-body','.fb-layout-container'];
  if(location.pathname.replace(/\/+$/,'').indexOf(PAGEKEY)<0){return;}

  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
  function qs(s,r){return (r||document).querySelector(s);}
  function labelOf(f,c){var m=LABELS[f]||{};return m[c]||c;}
  function absU(u){if(!u)return u;if(u.indexOf('http')===0)return u;return SITE.replace(/\/+$/,'')+(u.charAt(0)==='/'?u:'/'+u);}
  function css(){if(qs('#twlas-css'))return;var st=document.createElement('style');st.id='twlas-css';st.textContent=__CSS__;document.head.appendChild(st);}

  var box=null, tocEl=null, mainEl=null, filtersEl=null, resultsEl=null, cards=[], state={q:'',filters:{},sort:'relevance'};

  function vals(card,field){var v=card.getAttribute('data-'+field)||'';return v?v.split('|'):[];}

  function buildFacets(){
    var fc=filtersEl; if(!fc)return;
    var h=['<div class="filter-reset"><button type="button" class="btn" data-reset>Filters wissen</button></div>'];
    for(var i=0;i<FACETS.length;i++){
      var field=FACETS[i][0], title=FACETS[i][1], counts={};
      cards.forEach(function(c){vals(c,field).forEach(function(v){if(v)counts[v]=(counts[v]||0)+1;});});
      var keys=Object.keys(counts); if(!keys.length)continue;
      keys.sort(function(a,b){return labelOf(field,a).localeCompare(labelOf(field,b),'nl');});
      h.push('<div class="facet"><h3>'+esc(title)+'</h3>');
      keys.forEach(function(v){h.push('<label class="facet__option"><input type="checkbox" data-filter="'+esc(field)+'" value="'+esc(v)+'"><span>'+esc(labelOf(field,v))+'</span><span class="facet__count">'+counts[v]+'</span></label>');});
      h.push('</div>');
    }
    fc.innerHTML=h.join('');
  }

  function applyFilter(){
    var q=state.q.trim().toLowerCase(), vis=[];
    cards.forEach(function(c){
      var ok=true,k;
      for(k in state.filters){var sel=state.filters[k];if(sel&&sel.length){var cv=vals(c,k);if(!sel.some(function(s){return cv.indexOf(s)>-1;})){ok=false;break;}}}
      if(ok&&q&&(c.textContent||'').toLowerCase().indexOf(q)<0)ok=false;
      c.hidden=!ok; if(ok)vis.push(c);
    });
    if(state.sort!=='relevance'&&resultsEl){
      vis.sort(function(a,b){var x=a.getAttribute('data-ingang')||'',y=b.getAttribute('data-ingang')||'';return state.sort==='ingang_desc'?y.localeCompare(x):x.localeCompare(y);});
      vis.forEach(function(c){resultsEl.appendChild(c);});
    }
    var st=qs('#pf-stats',mainEl); if(st)st.textContent=vis.length+(vis.length===1?' resultaat':' resultaten')+(q?(' voor "'+state.q.trim()+'"'):'');
    var empty=qs('#twlas-empty',mainEl);
    if(!vis.length){
      if(!empty){empty=document.createElement('p');empty.id='twlas-empty';empty.className='muted';empty.textContent='Geen resultaten. Pas je zoekterm of filters aan.';if(resultsEl&&resultsEl.parentNode)resultsEl.parentNode.insertBefore(empty,resultsEl.nextSibling);}
      empty.hidden=false;
    } else if(empty){empty.hidden=true;}
  }

  // Scroll reserveert de TOC-kolom (grid-area "toc") alleen als de pagina breed genoeg
  // is; daarop sturen wij het tonen/verbergen van de filters (zelfde breekpunt als de
  // native "On this page"-TOC). Scroll's stylesheet zet onze nav default op display:none,
  // dus we forceren zelf block/none.
  function tocGridOk(){ var mc=qs('.main-content'); return !!(mc&&/toc/.test(getComputedStyle(mc).gridTemplateAreas||'')); }
  function applyTocDisplay(){ if(!tocEl)return; tocEl.style.setProperty('display', tocGridOk()?'block':'none','important'); }
  function showTocFilters(){
    if(!filtersEl)return;
    var mc=qs('.main-content');
    if(!mc){ if(box)box.appendChild(filtersEl); return; }
    tocEl=makeTocHost();
    if(tocEl){ tocEl.appendChild(filtersEl); applyTocDisplay(); try{requestAnimationFrame(applyTocDisplay);}catch(e){} }
  }
  function hideTocFilters(){
    var mc=qs('.main-content');
    if(mc){ var o=mc.querySelectorAll('nav[data-twiin]'); for(var k=0;k<o.length;k++)o[k].remove(); }
    tocEl=null;
  }
  function showList(){ if(box&&mainEl)box.replaceChildren(mainEl); showTocFilters(); }

  function openDetail(url){
    var u=absU(url);
    fetch(u).then(function(r){return r.text();}).then(function(html){
      var d=new DOMParser().parseFromString(html,'text/html'), art=d.querySelector('.kaart');
      if(!art){location.href=u;return;}
      var bc=art.querySelector('.breadcrumb'); if(bc)bc.remove();
      [].forEach.call(art.querySelectorAll('a[href]'),function(a){a.setAttribute('href',absU(a.getAttribute('href')));a.setAttribute('target','_top');a.setAttribute('rel','noopener');});
      var det=document.createElement('div'); det.className='twiin-las';
      var back=document.createElement('button'); back.type='button'; back.className='kaart__back'; back.setAttribute('data-back','1'); back.innerHTML='&larr; Terug naar het register';
      det.appendChild(back); det.appendChild(art);
      if(box)box.replaceChildren(det); hideTocFilters();
      try{window.scrollTo(0,0);}catch(e){}
    }).catch(function(){location.href=u;});
  }

  function hashUid(){var m=/[#&]la=([^&]+)/.exec(location.hash||'');return m?decodeURIComponent(m[1]):null;}
  function route(){var u=hashUid(); if(u){openDetail(SITE.replace(/\/+$/,'')+'/la/'+u.toLowerCase()+'/');} else {showList();}}

  function wire(){
    var s=qs('#pf-search',mainEl), so=qs('#pf-sort',mainEl), fc=filtersEl;
    if(s){var t;s.addEventListener('input',function(){clearTimeout(t);t=setTimeout(function(){state.q=s.value;applyFilter();},180);});}
    if(so){so.addEventListener('change',function(){state.sort=so.value;applyFilter();});}
    if(fc){
      fc.addEventListener('change',function(e){var cb=e.target.closest&&e.target.closest('input[data-filter]');if(!cb)return;var k=cb.getAttribute('data-filter');var a=state.filters[k]=state.filters[k]||[];if(cb.checked){if(a.indexOf(cb.value)<0)a.push(cb.value);}else{state.filters[k]=a.filter(function(x){return x!==cb.value;});}applyFilter();});
      fc.addEventListener('click',function(e){if(e.target.closest&&e.target.closest('[data-reset]')){state.filters={};[].forEach.call(fc.querySelectorAll('input[data-filter]'),function(cb){cb.checked=false;});applyFilter();}});
    }
    box.addEventListener('click',function(e){
      var cp=e.target.closest&&e.target.closest('[data-copy]');
      if(cp){e.preventDefault();var sel=cp.getAttribute('data-copy'),el=sel?qs(sel,box):null;
        if(el&&navigator.clipboard&&navigator.clipboard.writeText){
          navigator.clipboard.writeText((el.textContent||'').trim()).then(function(){var old=cp.textContent;cp.textContent='Gekopieerd '+String.fromCharCode(10003);setTimeout(function(){cp.textContent=old;},1500);}).catch(function(){});
        }return;}
      var back=e.target.closest&&e.target.closest('[data-back]'); if(back){e.preventDefault();if(location.hash)location.hash='';else route();return;}
      var a=e.target.closest&&e.target.closest('.card__link'); if(a){e.preventDefault();var card=a.closest('.card');var uid=card&&card.getAttribute('data-uid');if(uid){location.hash='la='+uid;}else{openDetail(a.getAttribute('href'));}}
    });
    window.addEventListener('hashchange',route);
  }

  // Maak Scroll's sticky-TOC-slot rechts (verwijdert de native TOC + oude eigen nav).
  // De zichtbaarheid sturen we zelf via applyTocDisplay(), op basis van Scroll's grid.
  function makeTocHost(){
    var mc=qs('.main-content'); if(!mc)return null;
    var olds=mc.querySelectorAll('nav[data-twiin]'); for(var k=0;k<olds.length;k++)olds[k].remove();
    var ex=mc.querySelector('.toc.sticky:not([data-twiin])'); if(ex)ex.remove();
    var nav=document.createElement('nav');
    nav.className='toc sticky twiin-las twiin-las-toc';
    nav.setAttribute('data-twiin','1');
    mc.appendChild(nav);
    return nav;
  }

  function mount(host, reg){
    css();
    var old=host.querySelector('.twiin-las-box'); if(old)old.remove();
    var kids=[].slice.call(host.children);
    for(var i=0;i<kids.length;i++){ if(!(kids[i].matches&&kids[i].matches('[data-component="panel"]'))) kids[i].remove(); }
    box=document.createElement('div'); box.className='twiin-las twiin-las-box'; host.appendChild(box);
    mainEl=qs('.register__main',reg); filtersEl=qs('.register__filters',reg);
    resultsEl=qs('#pf-results',mainEl); cards=[].slice.call(mainEl.querySelectorAll('.card'));
    [].forEach.call(mainEl.querySelectorAll('.card__link'),function(a){a.setAttribute('href',absU(a.getAttribute('href')));});
    buildFacets(); applyFilter(); wire();
    // Volg Scroll's eigen grid: als de TOC-kolom (her)verschijnt/verdwijnt bij resize of
    // zoom, tonen/verbergen we de filters mee (showTocFilters zet ze in de slot).
    var rt; window.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(applyTocDisplay,120);});
    try{var mc0=qs('.main-content'); if(mc0&&window.ResizeObserver){new ResizeObserver(function(){applyTocDisplay();}).observe(mc0);}}catch(e){}
    route();
  }

  function findHost(){for(var i=0;i<MAIN_SELECTORS.length;i++){var el=qs(MAIN_SELECTORS[i]);if(el)return el;}return null;}

  function start(host){
    fetch(EMBED).then(function(r){return r.text();}).then(function(html){
      var d=new DOMParser().parseFromString(html,'text/html'), reg=d.querySelector('.register');
      if(!reg){console.warn('[twiin-las] geen .register in embed');return;}
      mount(host, reg);
    }).catch(function(e){console.warn('[twiin-las] embed laden mislukt',e);});
  }

  var n=0, iv=setInterval(function(){n++;var host=findHost();if(host){clearInterval(iv);start(host);}else if(n>66){clearInterval(iv);}},150);
})();
"""

js = (JS.replace("__SITE__", json.dumps(SITE))
        .replace("__PAGEKEY__", json.dumps(PAGEKEY))
        .replace("__FACETS__", json.dumps(FACETS, ensure_ascii=True))
        .replace("__LABELS__", json.dumps(LABELS, ensure_ascii=True))
        .replace("__CSS__", json.dumps(CSS.strip(), ensure_ascii=True)))

dest = os.path.join(ROOT, "static", "inject.js")
out = "/* Twiin LA register - inject widget (fetch /embed/, gegenereerd) */\n" + js.strip() + "\n"
open(dest, "w", encoding="utf-8").write(out)
non_ascii = sum(1 for ch in out if ord(ch) > 127)
print("geschreven: %s | non-ascii: %d" % (dest, non_ascii))
