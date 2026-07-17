#!/usr/bin/env python3
"""
Genereer een self-contained HTML-export van het index/register-gedeelte
(class="register": filters + zoeken + resultaten), zonder header/footer/titel
en met alle CSS + JS + data inline. Bedoeld om als HTML in Confluence/Scroll
te plakken (test).

Gebruikt GEEN Pagefind (dat vereist losse wasm/index-bestanden). In plaats
daarvan staan de kaartgegevens als JSON inline en filtert/zoekt vanilla JS
client-side. Kaartlinks wijzen naar de absolute permalinks op de live site.

Invoer : public/index.json  (bouw eerst: hugo --minify)  + data/vocab.yaml
Uitvoer: export/register-embed.html
"""
import json, os, yaml, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(os.path.join(ROOT, "public", "index.json"), encoding="utf-8"))
vocab = yaml.safe_load(open(os.path.join(ROOT, "data", "vocab.yaml"), encoding="utf-8"))

# Facet-veld -> (NL-groepslabel, vocab-sleutel voor waardelabels)
FACETS = [
    ("soort",        "Soort",               "soort"),
    ("status",       "Status",              "status"),
    ("domein",       "Domein",              "domein"),
    ("uitwisseling", "Uitwisseling",        "uitwisseling"),
    ("patroon",      "Communicatiepatroon", "patroon"),
    ("functie",      "Generieke functie",   "functie"),
    ("toepassingen", "Toepassing",          "stelsel"),
]

def term(vkey, code):
    t = (vocab.get(vkey) or {}).get("terms", {}).get(code)
    if not t:
        return {"label": code, "kleur": "grijs"}
    return {"label": t.get("label", code), "kleur": t.get("kleur", "grijs")}

# Bouw een compacte vocab-map voor alleen de gebruikte facetten (code -> {label,kleur})
vocab_out = {}
for field, _lbl, vkey in FACETS:
    vocab_out[field] = {}
for it in data["items"]:
    for field, _lbl, vkey in FACETS:
        val = it.get(field)
        vals = val if isinstance(val, list) else ([val] if val else [])
        for code in vals:
            if code not in vocab_out[field]:
                vocab_out[field][code] = term(vkey, code)
# soort/status zijn enkelvoudig maar staan als string in de data
for field in ("soort", "status"):
    for it in data["items"]:
        code = it.get(field)
        if code and code not in vocab_out[field]:
            vocab_out[field][code] = term(field, code)

# Kaartgegevens die de JS nodig heeft (link = absolute permalink)
items = []
for it in data["items"]:
    items.append({
        "uid": it["uid"],
        "naam": it["naam"],
        "samenvatting": it.get("samenvatting", ""),
        "url": it.get("permalink") or it.get("url"),
        "ingangsdatum": it.get("ingangsdatum", ""),
        "soort": it.get("soort", ""),
        "status": it.get("status", ""),
        "domein": it.get("domein", []),
        "uitwisseling": it.get("uitwisseling", []),
        "patroon": it.get("patroon", []),
        "functie": it.get("functie", []),
        "toepassingen": it.get("toepassingen", []),
    })

facets_js = [{"field": f, "label": l} for f, l, _ in FACETS]

CSS = r"""
.twiin-embed{--accent:#e6396a;--bg:#fff;--bg-alt:#f6f4f7;--surface:#fff;--border:#e6e2e9;--text:#283340;--muted:#6a6675;--navy:#243140;--radius:12px;--radius-sm:8px;--shadow:0 1px 2px rgba(36,49,64,.06),0 4px 16px rgba(36,49,64,.07);
 font-family:"Roboto",-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;color:var(--text);line-height:1.55;
 --c-groen-bg:#e3f6ec;--c-groen-fg:#0f7a43;--c-blauw-bg:#e6effd;--c-blauw-fg:#1857c4;--c-paars-bg:#efe7fb;--c-paars-fg:#6936c9;--c-cyaan-bg:#e0f4f7;--c-cyaan-fg:#0d7a8c;--c-oranje-bg:#fdeede;--c-oranje-fg:#b35c00;--c-geel-bg:#fcf3d6;--c-geel-fg:#8a6a00;--c-rood-bg:#fde7e7;--c-rood-fg:#bb2222;--c-grijs-bg:#eceef3;--c-grijs-fg:#444c5e;}
.twiin-embed *{box-sizing:border-box;}
.twiin-embed [hidden]{display:none!important;}
.twiin-embed .register{display:grid;grid-template-columns:240px 1fr;gap:1.5rem;align-items:start;}
@media (max-width:820px){.twiin-embed .register{grid-template-columns:1fr;}}
.twiin-embed .register__filters{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1rem;}
.twiin-embed .register__filters h3{margin:.2rem 0 .6rem;font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);}
.twiin-embed .facet{margin-bottom:1.1rem;}
.twiin-embed .facet__option{display:flex;align-items:center;gap:.45rem;font-size:.85rem;padding:.12rem 0;cursor:pointer;}
.twiin-embed .facet__option input{accent-color:var(--accent);}
.twiin-embed .facet__count{margin-left:auto;color:var(--muted);font-size:.78rem;}
.twiin-embed .search{display:flex;gap:.75rem;align-items:center;margin-bottom:1rem;flex-wrap:wrap;}
.twiin-embed input[type=search],.twiin-embed select{padding:.62rem .8rem;border:1px solid var(--border);border-radius:var(--radius-sm);background:var(--surface);color:var(--text);font-size:.95rem;font-family:inherit;}
.twiin-embed input[type=search]{flex:1;min-width:220px;}
.twiin-embed .search__sort{font-size:.85rem;color:var(--muted);display:flex;align-items:center;gap:.4rem;white-space:nowrap;}
.twiin-embed .register__stats{color:var(--muted);font-size:.85rem;margin:.2rem 0 1rem;}
.twiin-embed .btn{background:var(--accent);color:#fff;border:none;border-radius:999px;padding:.4rem .9rem;font-size:.82rem;font-weight:600;cursor:pointer;}
.twiin-embed .card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1rem;}
.twiin-embed .card{display:flex;flex-direction:column;justify-content:space-between;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1rem 1.1rem;box-shadow:var(--shadow);}
.twiin-embed .card a.card__link{color:var(--text);display:block;text-decoration:none;}
.twiin-embed .card__head{display:flex;align-items:center;justify-content:space-between;gap:.5rem;margin-bottom:.5rem;}
.twiin-embed .card__uid{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.72rem;color:var(--muted);}
.twiin-embed .card__title{margin:.1rem 0 .4rem;font-size:1.02rem;line-height:1.3;}
.twiin-embed .card__summary{color:var(--muted);font-size:.86rem;margin:0;}
.twiin-embed .card__foot{display:flex;flex-wrap:wrap;gap:.35rem;margin-top:.8rem;}
.twiin-embed .badge{display:inline-block;padding:.15rem .55rem;border-radius:999px;font-size:.74rem;font-weight:600;line-height:1.5;white-space:nowrap;background:var(--c-grijs-bg);color:var(--c-grijs-fg);}
.twiin-embed .badge--groen{background:var(--c-groen-bg);color:var(--c-groen-fg);}
.twiin-embed .badge--blauw{background:var(--c-blauw-bg);color:var(--c-blauw-fg);}
.twiin-embed .badge--paars{background:var(--c-paars-bg);color:var(--c-paars-fg);}
.twiin-embed .badge--cyaan{background:var(--c-cyaan-bg);color:var(--c-cyaan-fg);}
.twiin-embed .badge--oranje{background:var(--c-oranje-bg);color:var(--c-oranje-fg);}
.twiin-embed .badge--geel{background:var(--c-geel-bg);color:var(--c-geel-fg);}
.twiin-embed .badge--rood{background:var(--c-rood-bg);color:var(--c-rood-fg);}
.twiin-embed .badge--grijs{background:var(--c-grijs-bg);color:var(--c-grijs-fg);}
"""

JS = r"""
(function(){
  var root=document.getElementById('twiin-index-embed');
  if(!root)return;
  var DATA=__DATA__, VOCAB=__VOCAB__, FACETS=__FACETS__;
  var state={q:'',filters:{}};
  var elFilters=root.querySelector('#te-filters'),
      elResults=root.querySelector('#te-results'),
      elStats=root.querySelector('#te-stats'),
      elSearch=root.querySelector('#te-search'),
      elSort=root.querySelector('#te-sort');
  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
  function norm(s){return (s||'').toString().toLowerCase();}
  function asList(v){return Array.isArray(v)?v:(v?[v]:[]);}
  function labelOf(field,code){var m=VOCAB[field]&&VOCAB[field][code];return m?m.label:code;}
  function kleurOf(field,code){var m=VOCAB[field]&&VOCAB[field][code];return m?m.kleur:'grijs';}
  function matches(it){
    if(state.q){var hay=norm(it.uid)+' '+norm(it.naam)+' '+norm(it.samenvatting);if(hay.indexOf(norm(state.q))===-1)return false;}
    for(var f in state.filters){var sel=state.filters[f];if(!sel.length)continue;var vals=asList(it[f]);var ok=false;for(var i=0;i<sel.length;i++){if(vals.indexOf(sel[i])!==-1){ok=true;break;}}if(!ok)return false;}
    return true;
  }
  function currentResults(){
    var r=DATA.filter(matches);
    if(elSort.value==='ingang_desc')r.sort(function(a,b){return (b.ingangsdatum||'').localeCompare(a.ingangsdatum||'');});
    else if(elSort.value==='ingang_asc')r.sort(function(a,b){return (a.ingangsdatum||'').localeCompare(b.ingangsdatum||'');});
    return r;
  }
  function renderResults(r){
    if(!r.length){elResults.innerHTML='<p style="color:var(--muted)">Geen resultaten. Pas je zoekterm of filters aan.</p>';return;}
    elResults.innerHTML=r.map(function(it){
      var domein=asList(it.domein).map(function(c){return '<span class="badge badge--'+kleurOf('domein',c)+'">'+esc(labelOf('domein',c))+'</span>';}).join('');
      return '<article class="card"><a class="card__link" href="'+esc(it.url)+'" target="_top">'
        +'<header class="card__head"><span class="badge badge--'+kleurOf('soort',it.soort)+'">'+esc(labelOf('soort',it.soort))+'</span>'
        +'<span class="card__uid">'+esc(it.uid)+'</span></header>'
        +'<h3 class="card__title">'+esc(it.naam)+'</h3>'
        +(it.samenvatting?'<p class="card__summary">'+esc(it.samenvatting)+'</p>':'')+'</a>'
        +'<footer class="card__foot"><span class="badge badge--'+kleurOf('status',it.status)+'">'+esc(labelOf('status',it.status))+'</span>'+domein+'</footer></article>';
    }).join('');
  }
  function countsFor(field,base){
    var c={};base.forEach(function(it){asList(it[field]).forEach(function(v){c[v]=(c[v]||0)+1;});});return c;
  }
  function renderFacets(){
    var base=DATA.filter(matches);
    var parts=['<button type="button" class="btn" id="te-reset">Filters wissen</button>'];
    FACETS.forEach(function(f){
      var counts=countsFor(f.field,base);
      var active=state.filters[f.field]||[];
      // toon alle waarden die voorkomen in de dataset (met live count binnen huidige selectie)
      var all={};DATA.forEach(function(it){asList(it[f.field]).forEach(function(v){all[v]=true;});});
      var values=Object.keys(all).filter(function(v){return (counts[v]||0)>0||active.indexOf(v)!==-1;}).sort(function(a,b){return labelOf(f.field,a).localeCompare(labelOf(f.field,b),'nl');});
      if(!values.length)return;
      parts.push('<div class="facet"><h3>'+esc(f.label)+'</h3>');
      values.forEach(function(v){
        parts.push('<label class="facet__option"><input type="checkbox" data-facet="'+esc(f.field)+'" value="'+esc(v)+'"'+(active.indexOf(v)!==-1?' checked':'')+'>'
          +'<span>'+esc(labelOf(f.field,v))+'</span><span class="facet__count">'+(counts[v]||0)+'</span></label>');
      });
      parts.push('</div>');
    });
    elFilters.innerHTML=parts.join('');
  }
  function run(){var r=currentResults();renderResults(r);renderFacets();elStats.textContent=r.length+(r.length===1?' resultaat':' resultaten')+(state.q?(' voor "'+state.q+'"'):'');}
  elSearch.addEventListener('input',function(){var t=this.value;clearTimeout(elSearch._t);elSearch._t=setTimeout(function(){state.q=t;run();},150);});
  elSort.addEventListener('change',run);
  elFilters.addEventListener('change',function(e){var cb=e.target.closest&&e.target.closest('input[data-facet]');if(!cb)return;var f=cb.getAttribute('data-facet');var a=state.filters[f]||(state.filters[f]=[]);if(cb.checked){if(a.indexOf(cb.value)===-1)a.push(cb.value);}else{state.filters[f]=a.filter(function(x){return x!==cb.value;});}run();});
  elFilters.addEventListener('click',function(e){if(e.target&&e.target.id==='te-reset'){state.filters={};run();}});
  run();
})();
"""

body = """<div class="twiin-embed" id="twiin-index-embed">
  <div class="register">
    <aside class="register__filters" id="te-filters" aria-label="Filters"></aside>
    <div class="register__main">
      <form class="search" onsubmit="return false">
        <input type="search" id="te-search" placeholder="Zoek op vrije tekst, UID, naam&hellip;" autocomplete="off" aria-label="Zoeken">
        <label class="search__sort">Sorteer:
          <select id="te-sort">
            <option value="relevance">Relevantie</option>
            <option value="ingang_desc">Ingangsdatum (nieuw&rarr;oud)</option>
            <option value="ingang_asc">Ingangsdatum (oud&rarr;nieuw)</option>
          </select>
        </label>
      </form>
      <p class="register__stats" id="te-stats" aria-live="polite"></p>
      <div class="card-grid" id="te-results"></div>
    </div>
  </div>
</div>"""

js = (JS
      .replace("__DATA__", json.dumps(items))
      .replace("__VOCAB__", json.dumps(vocab_out))
      .replace("__FACETS__", json.dumps(facets_js)))

out = "<style>\n" + CSS.strip() + "\n</style>\n" + body + "\n<script>\n" + js.strip() + "\n</script>\n"

os.makedirs(os.path.join(ROOT, "export"), exist_ok=True)
dest = os.path.join(ROOT, "export", "register-embed.html")
open(dest, "w", encoding="utf-8").write(out)
print("geschreven:", dest, "|", len(out), "bytes |", len(items), "kaarten")
