#!/usr/bin/env python3
"""
Genereer static/inject.js : self-contained widget dat het index/register
client-side rendert en in een Scroll/Confluence-pagina mount.

Split-mount:
  - FILTERS (register__filters)  -> .toc.sticky   (rechterkolom)
  - ZOEKEN + RESULTATEN + DETAIL -> .article-body.fb-layout-body (of .fb-layout-container)
Zo houdt de content volle breedte en staan de filters in de sticky TOC rechts.
Valt terug op één mount (filters+resultaten samen) als er geen .toc.sticky is.

Alle data/CSS/JS inline (geen runtime fetch -> geen CORS). Kaartklik -> detail
in dezelfde container via hash (#las=<uid>); gebruiker blijft op de pagina.
Pure ASCII uitvoer.

Laden via Scroll 'Custom JavaScript' (met paginaguard):
  <script>if(location.pathname.indexOf('index-landelijke-afspraken')>-1){
    var s=document.createElement('script');
    s.src='https://las.codeberg.page/playground/inject.js';s.charset='utf-8';
    document.head.appendChild(s);}</script>

Invoer : content/index/*/index.md + data/vocab.yaml
Uitvoer: static/inject.js  (-> /playground/inject.js)
"""
import json, os, glob, re, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
vocab = yaml.safe_load(open(os.path.join(ROOT, "data", "vocab.yaml"), encoding="utf-8"))

def term(vkey, code):
    t = (vocab.get(vkey) or {}).get("terms", {}).get(code)
    return {"label": (t or {}).get("label", code), "kleur": (t or {}).get("kleur", "grijs")}

FIELD_VOCAB = {"soort":"soort","status":"status","domein":"domein","uitwisseling":"uitwisseling",
               "patroon":"patroon","functie":"functie","toepassingen":"stelsel"}

def parse_card(path):
    raw = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.S)
    fm = yaml.safe_load(m.group(1)) if m else {}
    return fm, (m.group(2) if m else "").strip()

cards = []
for p in sorted(glob.glob(os.path.join(ROOT, "content", "index", "*", "index.md"))):
    fm, body = parse_card(p)
    cards.append({
        "uid": fm.get("uid",""), "naam": fm.get("title",""), "soort": fm.get("soort",""),
        "status": fm.get("status",""), "samenvatting": fm.get("samenvatting",""),
        "ingangsdatum": str(fm.get("ingangsdatum","") or ""), "ingang_stelselversie": str(fm.get("ingang_stelselversie","") or ""),
        "vervaldatum": str(fm.get("vervaldatum","") or ""), "vervaldatum_stelselversie": str(fm.get("vervaldatum_stelselversie","") or ""),
        "domein": fm.get("domein",[]) or [], "uitwisseling": fm.get("uitwisseling",[]) or [],
        "patroon": fm.get("patroon",[]) or [], "functie": fm.get("functie",[]) or [],
        "toepassingen": fm.get("toepassingen",[]) or [],
        "voorwaarden": fm.get("voorwaarden","") or "", "conformiteitscriteria": fm.get("conformiteitscriteria","") or "",
        "auteur": fm.get("auteur",[]) or [], "beheerder": fm.get("beheerder",[]) or [],
        "autorisator": fm.get("autorisator",[]) or [],
        "betreft_twiin": fm.get("betreft_twiin",[]) or [], "betreft_extern": fm.get("betreft_extern",[]) or [],
        "relaties": fm.get("relaties",[]) or [], "wijzigingslog": fm.get("wijzigingslog",[]) or [],
        "body": body,
    })

vocab_out = {f: {} for f in FIELD_VOCAB}
for c in cards:
    for f, vk in FIELD_VOCAB.items():
        v = c[f]; vals = v if isinstance(v, list) else ([v] if v else [])
        for code in vals:
            vocab_out[f].setdefault(code, term(vk, code))

DATA = json.dumps(cards, ensure_ascii=True)
VOCAB = json.dumps(vocab_out, ensure_ascii=True)

CSS = r"""
.twiin-las{--accent:#e6396a;--bg:#fff;--bg-alt:#f6f4f7;--surface:#fff;--border:#e6e2e9;--text:#283340;--muted:#6a6675;--navy:#243140;--radius:12px;--radius-sm:8px;--shadow:0 1px 2px rgba(36,49,64,.06),0 4px 16px rgba(36,49,64,.07);--mono:ui-monospace,Menlo,Consolas,monospace;font-family:"Roboto",-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;color:var(--text);line-height:1.55;}
.twiin-las *{box-sizing:border-box;}
.twiin-las a{color:var(--accent);text-decoration:none;}
.twiin-las a:hover{text-decoration:underline;}
.twiin-las .muted{color:var(--muted);}
.twiin-las .register{display:grid;grid-template-columns:240px 1fr;gap:1.5rem;align-items:start;}
@media (max-width:820px){.twiin-las .register{grid-template-columns:1fr;}}
.twiin-las .register__filters{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1rem;}
.twiin-las-filters .register__filters{border:0;padding:0;background:transparent;}
.twiin-las .register__filters h3{margin:.2rem 0 .6rem;font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);}
.twiin-las .facet{margin-bottom:1.1rem;}
.twiin-las .facet__option{display:flex;align-items:center;gap:.45rem;font-size:.85rem;padding:.12rem 0;cursor:pointer;}
.twiin-las .facet__count{margin-left:auto;color:var(--muted);font-size:.78rem;}
.twiin-las .search{display:flex;gap:.75rem;align-items:center;margin-bottom:1rem;flex-wrap:wrap;}
.twiin-las input[type=search],.twiin-las select{padding:.62rem .8rem;border:1px solid var(--border);border-radius:var(--radius-sm);background:var(--surface);color:var(--text);font-size:.95rem;font-family:inherit;}
.twiin-las input[type=search]{flex:1;min-width:220px;}
.twiin-las .search__sort{font-size:.85rem;color:var(--muted);display:flex;align-items:center;gap:.4rem;white-space:nowrap;}
.twiin-las .register__stats{color:var(--muted);font-size:.85rem;margin:.2rem 0 1rem;}
.twiin-las .btn{background:var(--accent);color:#fff;border:none;border-radius:999px;padding:.4rem .9rem;font-size:.82rem;font-weight:600;cursor:pointer;}
.twiin-las .card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1rem;}
.twiin-las .card{display:flex;flex-direction:column;justify-content:space-between;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1rem 1.1rem;box-shadow:var(--shadow);cursor:pointer;}
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
.twiin-las table.log{width:100%;border-collapse:collapse;font-size:.9rem;}
.twiin-las table.log th,.twiin-las table.log td{text-align:left;padding:.5rem .6rem;border-bottom:1px solid var(--border);vertical-align:top;}
.twiin-las table.log th{background:var(--bg-alt);}
.twiin-las .tag-prefix{font-family:var(--mono);font-size:.7rem;color:var(--muted);}
"""

JS = r"""
(function(){
  var DATA=__DATA__, VOCAB=__VOCAB__;
  var MAIN_SELECTORS=['.article-body.fb-layout-body','.fb-layout-container'];
  var FILTER_SELECTOR='.toc.sticky';
  var HASHKEY='las';
  var FACETS=[['soort','Soort'],['status','Status'],['domein','Domein'],['uitwisseling','Uitwisseling'],['patroon','Communicatiepatroon'],['functie','Generieke functie'],['toepassingen','Toepassing']];
  var byUid={}; DATA.forEach(function(c){byUid[c.uid]=c;});
  var slugToUid={}; DATA.forEach(function(c){slugToUid[c.uid.toLowerCase()]=c.uid;});
  var state={q:'',filters:{},sort:'relevance'};
  var mainMount=null, filterMount=null, split=false;

  function qs(s){return document.querySelector(s);}
  function css(){if(document.getElementById('twiin-las-css'))return;var s=document.createElement('style');s.id='twiin-las-css';s.textContent=__CSS__;document.head.appendChild(s);}
  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
  function asList(v){return Array.isArray(v)?v:(v?[v]:[]);}
  function lbl(f,code){var m=VOCAB[f]&&VOCAB[f][code];return m?m.label:code;}
  function kl(f,code){var m=VOCAB[f]&&VOCAB[f][code];return m?m.kleur:'grijs';}
  function badge(f,code){return '<span class="badge badge--'+kl(f,code)+'">'+esc(lbl(f,code))+'</span>';}
  function badges(f,arr){arr=asList(arr);return arr.length?arr.map(function(c){return badge(f,c);}).join(''):'<span class="muted">--</span>';}
  function linkFor(url){var m=/(?:^|\/)index\/([a-z0-9-]+)\/?$/i.exec(url||'');if(m&&slugToUid[m[1].toLowerCase()])return '#'+HASHKEY+'='+slugToUid[m[1].toLowerCase()];return url;}
  function isInternal(url){return String(url||'').indexOf('#'+HASHKEY+'=')===0;}

  function matches(c){
    if(state.q){var h=(c.uid+' '+c.naam+' '+c.samenvatting).toLowerCase();if(h.indexOf(state.q.toLowerCase())===-1)return false;}
    for(var f in state.filters){var sel=state.filters[f];if(!sel.length)continue;var vals=asList(c[f]),ok=false;for(var i=0;i<sel.length;i++)if(vals.indexOf(sel[i])!==-1){ok=true;break;}if(!ok)return false;}
    return true;
  }
  function facetsHtml(){
    var base=DATA.filter(matches);
    var parts=['<aside class="register__filters"><button type="button" class="btn" data-reset>Filters wissen</button>'];
    FACETS.forEach(function(fp){var f=fp[0];var counts={};base.forEach(function(c){asList(c[f]).forEach(function(v){counts[v]=(counts[v]||0)+1;});});
      var all={};DATA.forEach(function(c){asList(c[f]).forEach(function(v){all[v]=true;});});
      var active=state.filters[f]||[];
      var vals=Object.keys(all).filter(function(v){return (counts[v]||0)>0||active.indexOf(v)!==-1;}).sort(function(a,b){return lbl(f,a).localeCompare(lbl(f,b),'nl');});
      if(!vals.length)return; parts.push('<div class="facet"><h3>'+esc(fp[1])+'</h3>');
      vals.forEach(function(v){parts.push('<label class="facet__option"><input type="checkbox" data-facet="'+esc(f)+'" value="'+esc(v)+'"'+(active.indexOf(v)!==-1?' checked':'')+'><span>'+esc(lbl(f,v))+'</span><span class="facet__count">'+(counts[v]||0)+'</span></label>');});
      parts.push('</div>');
    });
    parts.push('</aside>'); return parts.join('');
  }
  function resultsHtml(){
    var r=DATA.filter(matches);
    if(state.sort==='ingang_desc')r.sort(function(a,b){return (b.ingangsdatum||'').localeCompare(a.ingangsdatum||'');});
    else if(state.sort==='ingang_asc')r.sort(function(a,b){return (a.ingangsdatum||'').localeCompare(b.ingangsdatum||'');});
    var cards=r.length?r.map(function(c){
      return '<article class="card" data-uid="'+esc(c.uid)+'"><div class="card__head">'+badge('soort',c.soort)+'<span class="card__uid">'+esc(c.uid)+'</span></div>'
        +'<h3 class="card__title">'+esc(c.naam)+'</h3>'+(c.samenvatting?'<p class="card__summary">'+esc(c.samenvatting)+'</p>':'')
        +'<div class="card__foot">'+badge('status',c.status)+asList(c.domein).map(function(d){return badge('domein',d);}).join('')+'</div></article>';
    }).join(''):'<p class="muted">Geen resultaten. Pas je zoekterm of filters aan.</p>';
    return '<div class="register__main"><form class="search" onsubmit="return false">'
      +'<input type="search" data-search placeholder="Zoek op vrije tekst, UID, naam" value="'+esc(state.q)+'">'
      +'<label class="search__sort">Sorteer: <select data-sort><option value="relevance">Relevantie</option><option value="ingang_desc">Ingangsdatum (nieuw-oud)</option><option value="ingang_asc">Ingangsdatum (oud-nieuw)</option></select></label></form>'
      +'<p class="register__stats">'+r.length+(r.length===1?' resultaat':' resultaten')+(state.q?(' voor "'+esc(state.q)+'"'):'')+'</p>'
      +'<div class="card-grid">'+cards+'</div></div>';
  }
  function para(body){
    if(!body)return '';
    return body.split(/\n{2,}/).map(function(p){
      p=esc(p).replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>')
        .replace(/\[([^\]]+)\]\(([^)]+)\)/g,function(_,t,u){var h=linkFor(u);return '<a href="'+esc(h)+'"'+(isInternal(h)?'':' target="_top" rel="noopener"')+'>'+t+'</a>';});
      return '<p>'+p.replace(/\n/g,'<br>')+'</p>';
    }).join('');
  }
  function detailHtml(uid){
    var c=byUid[uid]; if(!c)return '';
    var h=['<article class="kaart"><button type="button" class="kaart__back" data-back>&larr; Terug naar index</button>'];
    h.push('<div class="kaart__badges">'+badge('soort',c.soort)+badge('status',c.status)+'</div>');
    h.push('<p class="kaart__uid">'+esc(c.uid)+'</p><h1 class="kaart__title">'+esc(c.naam)+'</h1>');
    if(c.samenvatting)h.push('<p class="kaart__lead">'+esc(c.samenvatting)+'</p>');
    h.push('<section><h2>Kerngegevens</h2><dl class="attr-grid">');
    h.push('<dt>UID</dt><dd>'+esc(c.uid)+'</dd>');
    h.push('<dt>Soort</dt><dd>'+badge('soort',c.soort)+' <span class="muted">'+esc(lbl('soort',c.soort))+'</span></dd>');
    h.push('<dt>Status</dt><dd>'+badge('status',c.status)+'</dd>');
    h.push('<dt>Ingangsdatum</dt><dd>'+(c.ingangsdatum?esc(c.ingangsdatum):'<span class="muted">--</span>')+(c.ingang_stelselversie?' <span class="muted">(vanaf Stelselversie '+esc(c.ingang_stelselversie)+')</span>':'')+'</dd>');
    h.push('<dt>Vervaldatum</dt><dd>'+(c.vervaldatum?esc(c.vervaldatum):'<span class="muted">--</span>')+'</dd>');
    h.push('<dt>Auteur / Opsteller</dt><dd>'+(asList(c.auteur).join(', ')||'--')+'</dd>');
    var aut=asList(c.autorisator).map(function(a){return esc(a.naam||'')+(a.datum?' <span class="muted">('+esc(String(a.datum))+')</span>':'');}).join(', ');
    h.push('<dt>Autorisator</dt><dd>'+(aut||'<span class="muted">--</span>')+'</dd>');
    h.push('<dt>Beheerder</dt><dd>'+(asList(c.beheerder).join(', ')||'--')+'</dd></dl></section>');
    h.push('<section><h2>Context</h2><dl class="attr-grid">'
      +'<dt>Domein</dt><dd class="badges">'+badges('domein',c.domein)+'</dd>'
      +'<dt>Uitwisseling</dt><dd class="badges">'+badges('uitwisseling',c.uitwisseling)+'</dd>'
      +'<dt>Communicatiepatroon <span class="tag-prefix">[P]</span></dt><dd class="badges">'+badges('patroon',c.patroon)+'</dd>'
      +'<dt>Generieke functies <span class="tag-prefix">[F]</span></dt><dd class="badges">'+badges('functie',c.functie)+'</dd></dl></section>');
    if(c.voorwaarden)h.push('<section><h2>Voorwaarden / Uitzonderingen</h2><p>'+esc(c.voorwaarden)+'</p></section>');
    if(c.conformiteitscriteria)h.push('<section><h2>Conformiteitscriteria</h2><p>'+esc(c.conformiteitscriteria)+'</p></section>');
    if(c.body)h.push('<section><h2>Omschrijving</h2>'+para(c.body)+'</section>');
    if(asList(c.betreft_twiin).length)h.push('<section><h2>Bijbehorende specificaties in Twiin</h2><ul class="ref-list">'+c.betreft_twiin.map(function(r){var hf=linkFor(r.link);return '<li><a href="'+esc(hf)+'"'+(isInternal(hf)?'':' target="_top" rel="noopener"')+'>'+esc(r.titel)+'</a> <span class="muted">-- beheerder: '+esc(r.beheerder||'Twiin')+'</span></li>';}).join('')+'</ul></section>');
    if(asList(c.betreft_extern).length)h.push('<section><h2>Bijbehorende standaarden &amp; normen buiten Twiin</h2><ul class="ref-list">'+c.betreft_extern.map(function(r){return '<li><a href="'+esc(r.link)+'" target="_top" rel="noopener">'+esc(r.titel)+'</a>'+(r.beheerder?' <span class="muted">-- '+esc(r.beheerder)+'</span>':'')+'</li>';}).join('')+'</ul></section>');
    if(asList(c.relaties).length)h.push('<section><h2>Relaties en afhankelijkheden</h2><ul class="ref-list">'+c.relaties.map(function(u){var t=byUid[u];return t?('<li><a href="#'+HASHKEY+'='+esc(u)+'">'+esc(u)+' -- '+esc(t.naam)+'</a></li>'):('<li>'+esc(u)+' <span class="muted">(niet in index)</span></li>');}).join('')+'</ul></section>');
    if(asList(c.toepassingen).length)h.push('<section><h2>Toepassingen in</h2><p class="badges">'+badges('toepassingen',c.toepassingen)+'</p></section>');
    if(asList(c.wijzigingslog).length)h.push('<section><h2>Wijzigingslog</h2><table class="log"><thead><tr><th>Datum</th><th>Versie</th><th>Wijziging</th></tr></thead><tbody>'+c.wijzigingslog.map(function(w){return '<tr><td>'+esc(String(w.datum||''))+'</td><td>'+esc(String(w.versie||''))+'</td><td>'+esc(w.wijziging||'')+'</td></tr>';}).join('')+'</tbody></table></section>');
    h.push('</article>'); return h.join('');
  }

  function paintFilters(){ if(split&&filterMount)filterMount.innerHTML=facetsHtml(); }
  function restoreInputs(){
    var si=mainMount.querySelector('[data-search]'); if(si){si.value=state.q; if(state.q){si.focus();si.setSelectionRange(si.value.length,si.value.length);}}
    var so=mainMount.querySelector('[data-sort]'); if(so)so.value=state.sort;
  }
  function renderList(){
    if(split){ mainMount.innerHTML=resultsHtml(); paintFilters(); }
    else { mainMount.innerHTML='<div class="register">'+facetsHtml()+resultsHtml()+'</div>'; }
    restoreInputs();
  }
  function renderDetail(uid){ mainMount.innerHTML=detailHtml(uid); paintFilters(); try{window.scrollTo(0,0);}catch(e){} }
  function hashUid(){var m=new RegExp('[#&]'+HASHKEY+'=([^&]+)').exec(location.hash||'');return m?decodeURIComponent(m[1]):null;}
  function render(){var u=hashUid(); if(u&&byUid[u])renderDetail(u); else renderList();}
  function toList(){ if(location.hash&&hashUid())history.pushState('','',location.pathname+location.search); }

  function wire(){
    document.addEventListener('click',function(e){
      if(!e.target.closest||!e.target.closest('.twiin-las'))return;
      if(e.target.closest('[data-back]')){toList();render();return;}
      if(e.target.closest('[data-reset]')){state.filters={};toList();render();return;}
      var card=e.target.closest('.card[data-uid]'); if(card){location.hash=HASHKEY+'='+card.getAttribute('data-uid');}
    });
    document.addEventListener('input',function(e){var t=e.target; if(t.matches&&t.matches('.twiin-las [data-search]')){var v=t.value;clearTimeout(window.__twlas);window.__twlas=setTimeout(function(){state.q=v;render();},150);}});
    document.addEventListener('change',function(e){var t=e.target;
      if(t.matches&&t.matches('.twiin-las [data-sort]')){state.sort=t.value;render();return;}
      var cb=t.closest&&t.closest('.twiin-las input[data-facet]'); if(!cb)return;
      var f=cb.getAttribute('data-facet'),a=state.filters[f]||(state.filters[f]=[]);
      if(cb.checked){if(a.indexOf(cb.value)===-1)a.push(cb.value);}else{state.filters[f]=a.filter(function(x){return x!==cb.value;});}
      toList(); render();
    });
    window.addEventListener('hashchange',render);
  }

  function mkdiv(cls){var d=document.createElement('div');d.className=cls;return d;}
  function boot(main,toc){
    css();
    if(toc && main.contains(toc)){ var ab=qs('.article-body.fb-layout-body'); if(ab&&!ab.contains(toc))main=ab; }
    split = !!toc && !main.contains(toc) && !toc.contains(main);
    mainMount=mkdiv('twiin-las twiin-las-main'); main.replaceChildren(mainMount);
    if(split){ filterMount=mkdiv('twiin-las twiin-las-filters'); toc.replaceChildren(filterMount); }
    wire(); render(); return true;
  }
  var n=0, iv=setInterval(function(){
    n++;
    var main=qs('.article-body.fb-layout-body')||qs('.fb-layout-container');
    var toc=qs(FILTER_SELECTOR);
    if(main && (toc || n>25)){ clearInterval(iv); boot(main,toc); }
    else if(n>66){ clearInterval(iv); }
  },150);
})();
"""

js = (JS.replace("__DATA__", DATA).replace("__VOCAB__", VOCAB)
        .replace("__CSS__", json.dumps(CSS.strip(), ensure_ascii=True)))

dest = os.path.join(ROOT, "static", "inject.js")
open(dest, "w", encoding="utf-8").write("/* Twiin LAS index - self-contained inject widget (gegenereerd) */\n" + js.strip() + "\n")
nonascii = sum(1 for ch in open(dest, encoding="utf-8").read() if ord(ch) > 127)
print("geschreven:", dest, "|", len(cards), "kaarten | non-ascii:", nonascii)
