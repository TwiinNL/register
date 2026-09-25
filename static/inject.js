/* Twiin LAS index - self-contained inject widget (gegenereerd) */
(function(){
  if(window.__twiinLasInit){return;} window.__twiinLasInit=true;   // voorkom dubbele injectie
  var DATA=[{"uid": "TW-LA-TA-001", "naam": "Netwerkbeveiliging (mTLS 1.3)", "soort": "TA", "status": "Normatief", "samenvatting": "Technische afspraak over beveiliging op netwerkniveau met TLS 1.3 en wederzijdse authenticatie (mTLS), op basis van PKIoverheid-certificaten, inclusief controle op ingetrokken certificaten via CRL/OCSP.", "ingangsdatum": "2026-04-09", "ingang_stelselversie": "1.5", "vervaldatum": "", "vervaldatum_stelselversie": "", "domein": ["MSZ", "VVT", "HA"], "uitwisseling": ["Verwijzing", "Overdracht"], "patroon": ["Notified Pull", "Pull", "Indexed Pull", "Push"], "functie": ["Netwerkbeveiliging", "Authenticatie", "Identificatie"], "toepassingen": ["MedMij", "AORTA", "NUTS"], "voorwaarden": "Geldt voor alle systeem-tot-systeem-verbindingen binnen het stelsel, ongeacht het communicatiepatroon.", "conformiteitscriteria": "Verbindingen gebruiken uitsluitend TLS 1.3 met wederzijdse authenticatie (mTLS). Systemen die de geldigheid van het PKIoverheid-servercertificaat van andere systemen controleren, MOETEN dit volgens de meest recent gepubliceerde Certificate Revocation List (CRL) of via het Online Certificate Status Protocol (OCSP) minimaal ieder uur doen.", "auteur": ["Working Group TA"], "beheerder": ["Twiin"], "autorisator": [{"naam": "VWS programma LDN", "datum": "2026-04-09"}], "betreft_twiin": [{"titel": "10.4.7 | Network level security: mTLS 1.3", "link": "https://afsprakenstelsel.twiin.nl/normatief/ta150/10-2-10-netwerk-level-security-mtls-1-3#Network-level-security:-mTLS-1.3", "beheerder": "Twiin"}, {"titel": "PvE | Netwerkbeveiliging: mTLS", "link": "https://afsprakenstelsel.twiin.nl/normatief/ta150/pve-netwerkbeveiliging#mTLS", "beheerder": "Twiin"}], "betreft_extern": [{"titel": "RFC 8705: OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens", "link": "https://datatracker.ietf.org/doc/html/rfc8705"}, {"titel": "Transport Layer Security (TLS)", "link": "https://www.ncsc.nl/documenten/publicaties/2025/juni/01/ict-beveiligingsrichtlijnen-voor-transport-layer-security-2025-05"}, {"titel": "PKIoverheid certificates", "link": "https://cert.pkioverheid.nl/"}], "relaties": [], "wijzigingslog": [{"datum": "2026-04-09", "versie": "1.0", "wijziging": "Vastgesteld bij Stelselversie 1.5 (TLS 1.3 verplicht)."}], "body": "Deze technische afspraak legt de beveiliging van het transportkanaal tussen systemen vast.\nAlle systeem-tot-systeem-verbindingen binnen het stelsel verlopen via wederzijds\ngeauthenticeerde TLS 1.3 (mTLS) met servercertificaten uit het PKIoverheid-stelsel.\n\nSystemen die de geldigheid van het PKIoverheid-servercertificaat van andere systemen\ncontroleren, MOETEN dit volgens de meest recent gepubliceerde Certificate Revocation List\n(CRL) of via het Online Certificate Status Protocol (OCSP), minimaal ieder uur, doen.\n\nDe normatieve tekst en de bijbehorende eisen staan in het Twiin Afsprakenstelsel onder\nNetwerkbeveiliging; zie de verwijzingen hieronder onder *Bijbehorende\nspecificaties in Twiin*."}], VOCAB={"soort": {"TA": {"label": "Technische afspraak", "kleur": "paars"}}, "status": {"Normatief": {"label": "Normatief", "kleur": "groen"}}, "domein": {"MSZ": {"label": "MSZ", "kleur": "blauw"}, "VVT": {"label": "VVT", "kleur": "groen"}, "HA": {"label": "HA", "kleur": "oranje"}}, "uitwisseling": {"Verwijzing": {"label": "Verwijzing", "kleur": "paars"}, "Overdracht": {"label": "Overdracht", "kleur": "cyaan"}}, "patroon": {"Notified Pull": {"label": "Notified Pull", "kleur": "blauw"}, "Pull": {"label": "Pull", "kleur": "groen"}, "Indexed Pull": {"label": "Indexed Pull", "kleur": "oranje"}, "Push": {"label": "Push", "kleur": "paars"}}, "functie": {"Netwerkbeveiliging": {"label": "Netwerkbeveiliging", "kleur": "grijs"}, "Authenticatie": {"label": "Authenticatie", "kleur": "grijs"}, "Identificatie": {"label": "Identificatie", "kleur": "grijs"}}, "toepassingen": {"MedMij": {"label": "MedMij", "kleur": "grijs"}, "AORTA": {"label": "AORTA", "kleur": "grijs"}, "NUTS": {"label": "NUTS", "kleur": "grijs"}}};
  var MAIN_SELECTORS=['.article-body.fb-layout-body','.fb-layout-container'];
  var HASHKEY='la';
  var PAGEKEY='landelijke-afspraken';  // herkent de register-pagina aan de URL (index-/register-landelijke-afspraken)
  var SITE='https://register.twiin.nl/la/';  // permalink-basis (github pages): /register/la/<slug>/
  // De infobox is het native Scroll-'panel' uit de Confluence-pagina; het blijft op zijn
  // plek staan (niet meegebakken, niet verplaatst) zodat het niet reflowt/resizet.
  var INDEXNAME='';  // naam van de indexpagina (uit h1), voor de breadcrumb
  var ON_INDEX = location.pathname.replace(/\/+$/,'').indexOf(PAGEKEY)>-1;  // staan we op de indexpagina?
  var FACETS=[['soort','Soort'],['status','Status'],['domein','Domein'],['uitwisseling','Uitwisseling'],['patroon','Communicatiepatroon'],['functie','Generieke functie'],['toepassingen','Toepassing']];
  var byUid={}; DATA.forEach(function(c){byUid[c.uid]=c;});
  var slugToUid={}; DATA.forEach(function(c){slugToUid[c.uid.toLowerCase()]=c.uid;});
  var state={q:'',filters:{},sort:'relevance'};
  var mainArea=null, sideArea=null, tocMode=false;

  function qs(s){return document.querySelector(s);}
  function css(){if(document.getElementById('twiin-las-css'))return;var s=document.createElement('style');s.id='twiin-las-css';s.textContent=".twiin-las{--accent:#e6396a;--bg:#fff;--bg-alt:#f6f4f7;--surface:#fff;--border:#e6e2e9;--text:#283340;--muted:#6a6675;--navy:#243140;--radius:12px;--radius-sm:8px;--shadow:0 1px 2px rgba(36,49,64,.06),0 4px 16px rgba(36,49,64,.07);--mono:ui-monospace,Menlo,Consolas,monospace;font-family:\"Roboto\",-apple-system,BlinkMacSystemFont,\"Segoe UI\",Helvetica,Arial,sans-serif;color:var(--text);line-height:1.55;}\n.twiin-las *{box-sizing:border-box;}\n.twiin-las a{color:var(--accent);text-decoration:none;}\n.twiin-las a:hover{text-decoration:underline;}\n.twiin-las .muted{color:var(--muted);}\n.twiin-las-split{display:flex;gap:1.5rem;align-items:flex-start;}\n.twiin-las-col-main{flex:1;min-width:0;}\n.twiin-las-col-side{width:260px;flex:none;position:sticky;top:1rem;max-height:calc(100vh - 2rem);overflow:auto;}\n@media (max-width:860px){.twiin-las-split{flex-direction:column;}.twiin-las-col-side{width:100%;position:static;max-height:none;overflow:visible;}}\n.twiin-las .register__filters{background:transparent;border:0;padding:0;}\n.twiin-las-col-side .register__filters h3:first-child{margin-top:.4rem;}\n.twiin-las-toc{overflow:auto;border:1px solid var(--_border-color,var(--border));border-radius:var(--K15t-radius-small,10px);background:var(--_background-color,var(--surface));}\n.twiin-las-toc .register__filters{padding:12px 16px;}\n.twiin-las.twiin-las-toc .register__filters h3{font:var(--K15t-font-body-small-strong, 600 .82rem/1.4 Roboto,sans-serif);color:var(--_foreground-color,var(--navy));text-transform:none;letter-spacing:normal;margin:.9rem 0 .4rem;}\n.twiin-las .filter-reset{display:flex;justify-content:flex-end;margin-bottom:.6rem;}\n.twiin-las .register__filters h3{margin:.2rem 0 .6rem;font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);}\n.twiin-las .facet{margin-bottom:1.1rem;}\n.twiin-las .facet__option{display:flex;align-items:center;gap:.45rem;font-size:.85rem;padding:.12rem 0;cursor:pointer;}\n.twiin-las .facet__count{margin-left:auto;color:var(--muted);font-size:.78rem;}\n.twiin-las .search{display:flex;gap:.75rem;align-items:center;margin-bottom:1rem;flex-wrap:wrap;}\n.twiin-las input[type=search],.twiin-las select{padding:.62rem .8rem;border:1px solid var(--border);border-radius:var(--radius-sm);background:var(--surface);color:var(--text);font-size:.95rem;font-family:inherit;}\n.twiin-las input[type=search]{flex:1;min-width:220px;}\n.twiin-las .search__sort{font-size:.85rem;color:var(--muted);display:flex;align-items:center;gap:.4rem;white-space:nowrap;}\n.twiin-las .register__stats{color:var(--muted);font-size:.85rem;margin:.2rem 0 1rem;}\n.twiin-las .btn{background:var(--accent);color:#fff;border:none;border-radius:999px;padding:.4rem .9rem;font-size:.82rem;font-weight:600;cursor:pointer;}\n.twiin-las .card-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:1rem;}\n.twiin-las .card{display:flex;flex-direction:column;justify-content:space-between;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1rem 1.1rem;box-shadow:var(--shadow);cursor:pointer;}\n.twiin-las .card__head{display:flex;align-items:center;justify-content:space-between;gap:.5rem;margin-bottom:.5rem;}\n.twiin-las .card__uid{font-family:var(--mono);font-size:.72rem;color:var(--muted);}\n.twiin-las .card__title{margin:.1rem 0 .4rem;font-size:1.02rem;line-height:1.3;color:var(--text);}\n.twiin-las .card__summary{color:var(--muted);font-size:.86rem;margin:0;}\n.twiin-las .card__foot{display:flex;flex-wrap:wrap;gap:.35rem;margin-top:.8rem;}\n.twiin-las .badge{display:inline-block;padding:.15rem .55rem;border-radius:999px;font-size:.74rem;font-weight:600;line-height:1.5;white-space:nowrap;background:var(--c-grijs-bg,#eceef3);color:var(--c-grijs-fg,#444c5e);}\n.twiin-las{--c-groen-bg:#e3f6ec;--c-groen-fg:#0f7a43;--c-blauw-bg:#e6effd;--c-blauw-fg:#1857c4;--c-paars-bg:#efe7fb;--c-paars-fg:#6936c9;--c-cyaan-bg:#e0f4f7;--c-cyaan-fg:#0d7a8c;--c-oranje-bg:#fdeede;--c-oranje-fg:#b35c00;--c-geel-bg:#fcf3d6;--c-geel-fg:#8a6a00;--c-rood-bg:#fde7e7;--c-rood-fg:#bb2222;--c-grijs-bg:#eceef3;--c-grijs-fg:#444c5e;}\n.twiin-las .badge--groen{background:var(--c-groen-bg);color:var(--c-groen-fg);}.twiin-las .badge--blauw{background:var(--c-blauw-bg);color:var(--c-blauw-fg);}.twiin-las .badge--paars{background:var(--c-paars-bg);color:var(--c-paars-fg);}.twiin-las .badge--cyaan{background:var(--c-cyaan-bg);color:var(--c-cyaan-fg);}.twiin-las .badge--oranje{background:var(--c-oranje-bg);color:var(--c-oranje-fg);}.twiin-las .badge--geel{background:var(--c-geel-bg);color:var(--c-geel-fg);}.twiin-las .badge--rood{background:var(--c-rood-bg);color:var(--c-rood-fg);}.twiin-las .badge--grijs{background:var(--c-grijs-bg);color:var(--c-grijs-fg);}\n.twiin-las .badges{display:flex;flex-wrap:wrap;gap:.35rem;}\n.twiin-las .kaart__back{display:inline-block;margin-bottom:1rem;font-size:.85rem;background:none;border:none;color:var(--accent);cursor:pointer;padding:0;}\n.twiin-las .kaart__badges{display:flex;gap:.4rem;margin-bottom:.5rem;}\n.twiin-las .kaart__uid{font-family:var(--mono);color:var(--muted);font-size:.85rem;margin:0;}\n.twiin-las .kaart__title{margin:.2rem 0 .5rem;font-size:1.7rem;line-height:1.2;color:var(--navy);}\n.twiin-las .kaart__lead{font-size:1.05rem;max-width:70ch;margin:0 0 1.2rem;}\n.twiin-las .kaart section{margin-bottom:1.6rem;}\n.twiin-las .kaart h2{font-size:1.1rem;border-bottom:1px solid var(--border);padding-bottom:.35rem;margin:0 0 .7rem;}\n.twiin-las .attr-grid{display:grid;grid-template-columns:200px 1fr;gap:0 1rem;margin:0;}\n.twiin-las .attr-grid dt{font-weight:600;padding:.45rem 0;border-top:1px solid var(--border);}\n.twiin-las .attr-grid dd{margin:0;padding:.45rem 0;border-top:1px solid var(--border);}\n.twiin-las .attr-grid dt:first-of-type,.twiin-las .attr-grid dd:first-of-type{border-top:none;}\n@media (max-width:600px){.twiin-las .attr-grid{grid-template-columns:1fr;}}\n.twiin-las .ref-list{margin:0;padding-left:1.2rem;}.twiin-las .ref-list li{margin:.3rem 0;}\n.twiin-las table.log{width:100%;border-collapse:collapse;font-size:.9rem;}\n.twiin-las table.log th,.twiin-las table.log td{text-align:left;padding:.5rem .6rem;border-bottom:1px solid var(--border);vertical-align:top;}\n.twiin-las table.log th{background:var(--bg-alt);}\n.twiin-las .tag-prefix{font-family:var(--mono);font-size:.7rem;color:var(--muted);}\n.twiin-las .permalink-box{background:var(--bg-alt);border:1px solid var(--border);border-radius:var(--radius);padding:1rem 1.1rem;margin-bottom:1.6rem;}\n.twiin-las .permalink-box h2{border:0;margin:0 0 .3rem;font-size:1rem;}\n.twiin-las .permalink-box__hint{font-size:.82rem;color:var(--muted);margin:0 0 .7rem;}\n.twiin-las .permalink-box__row{display:flex;gap:.6rem;align-items:center;flex-wrap:wrap;}\n.twiin-las .permalink-box__url{font-family:var(--mono);font-size:.82rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-sm);padding:.5rem .7rem;flex:1;word-break:break-all;}\n.twiin-las .permalink-box__formats{font-size:.82rem;margin:.7rem 0 0;color:var(--muted);}\n/* Mobiel: geef het hoofdcontent volle breedte. De geinjecteerde filterkolom\n   (.twiin-las-toc) heeft de klasse .toc, waardoor de Scroll-grid via :has(.toc) een\n   ~200px zijkolom blijft reserveren en de content halve breedte krijgt. Onder 768px\n   klappen we die grid uit tot een kolom; de filters komen dan onder de resultaten\n   (net als dat Scroll de sticky TOC op mobiel niet in een zijkolom houdt). */\n@media (max-width:767px){\n  .main-content:has(.twiin-las-toc){display:block !important;}\n  .twiin-las-toc{position:static !important;width:auto !important;max-height:none !important;overflow:visible !important;margin:1.2rem 0 0 !important;}\n}\n/* Donkere modus: volgt data-color-scheme van het ontwikkelsupplement/Scroll-thema.\n   Alleen de kleur-tokens worden omgezet; de infobox is het native Scroll-'panel'\n   en volgt het thema al vanzelf. */\nhtml[data-color-scheme=\"dark\"] .twiin-las{--bg:#0f1113;--bg-alt:#1a1d21;--surface:#16191d;--border:#2b3038;--text:#e3e5e8;--muted:#9aa0a8;--navy:#e8eaed;--accent:#f2578a;--shadow:0 1px 2px rgba(0,0,0,.5),0 4px 16px rgba(0,0,0,.55);--c-groen-bg:#123524;--c-groen-fg:#5fce97;--c-blauw-bg:#15233f;--c-blauw-fg:#84b1ff;--c-paars-bg:#241a3a;--c-paars-fg:#b79bf0;--c-cyaan-bg:#0e2c33;--c-cyaan-fg:#57cfe0;--c-oranje-bg:#3a2410;--c-oranje-fg:#f0a95c;--c-geel-bg:#332a10;--c-geel-fg:#e0c46a;--c-rood-bg:#3a1414;--c-rood-fg:#f08a8a;--c-grijs-bg:#22262d;--c-grijs-fg:#aeb6c2;}";document.head.appendChild(s);}
  function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}
  function asList(v){return Array.isArray(v)?v:(v?[v]:[]);}
  function lbl(f,code){var m=VOCAB[f]&&VOCAB[f][code];return m?m.label:code;}
  function kl(f,code){var m=VOCAB[f]&&VOCAB[f][code];return m?m.kleur:'grijs';}
  function badge(f,code){return '<span class="badge badge--'+kl(f,code)+'">'+esc(lbl(f,code))+'</span>';}
  function badges(f,arr){arr=asList(arr);return arr.length?arr.map(function(c){return badge(f,c);}).join(''):'<span class="muted">--</span>';}
  function linkFor(url){var m=/(?:^|\/)(?:la|register|index)\/([a-z0-9-]+)\/?$/i.exec(url||'');if(m&&slugToUid[m[1].toLowerCase()])return '#'+HASHKEY+'='+slugToUid[m[1].toLowerCase()];return url;}
  function isInternal(url){return String(url||'').indexOf('#'+HASHKEY+'=')===0;}

  function matches(c){
    if(state.q){var h=(c.uid+' '+c.naam+' '+c.samenvatting).toLowerCase();if(h.indexOf(state.q.toLowerCase())===-1)return false;}
    for(var f in state.filters){var sel=state.filters[f];if(!sel.length)continue;var vals=asList(c[f]),ok=false;for(var i=0;i<sel.length;i++)if(vals.indexOf(sel[i])!==-1){ok=true;break;}if(!ok)return false;}
    return true;
  }
  function facetsHtml(){
    var base=DATA.filter(matches);
    var parts=['<aside class="register__filters"><div class="filter-reset"><button type="button" class="btn" data-reset>Filters wissen</button></div>'];
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
    var pl=SITE+c.uid.toLowerCase()+'/', jl=pl+'index.jsonld';
    h.push('<section class="permalink-box"><h2>Permalink</h2>'
      +'<p class="permalink-box__hint">Verwijs naar deze metadata via onderstaande permalink. Deze blijft stabiel zodra een eigen domein is gekoppeld.</p>'
      +'<div class="permalink-box__row"><code class="permalink-box__url" id="twlas-permalink">'+esc(pl)+'</code>'
      +'<button type="button" class="btn" data-copy="#twlas-permalink">Kopieer</button></div>'
      +'<p class="permalink-box__formats">Machineleesbaar: <a href="'+esc(jl)+'" target="_top" rel="noopener">JSON-LD (RDF)</a></p></section>');
    h.push('<section><h2>Kerngegevens</h2><dl class="attr-grid">');
    h.push('<dt>UID</dt><dd>'+esc(c.uid)+'</dd>');
    h.push('<dt>Soort</dt><dd>'+badge('soort',c.soort)+' <span class="muted">'+esc(lbl('soort',c.soort))+'</span></dd>');
    h.push('<dt>Status</dt><dd>'+badge('status',c.status)+'</dd>');
    h.push('<dt>Ingangsdatum</dt><dd>'+(c.ingangsdatum?esc(c.ingangsdatum):'<span class="muted">--</span>')+(c.ingang_stelselversie?' <span class="muted">(vanaf Stelselversie '+esc(c.ingang_stelselversie)+')</span>':'')+'</dd>');
    h.push('<dt>Vervaldatum</dt><dd>'+(c.vervaldatum?esc(c.vervaldatum):'<span class="muted">--</span>')+'</dd>');
    h.push('<dt>Auteur / Opsteller</dt><dd>'+(asList(c.auteur).join(', ')||'-')+'</dd>');
    var aut=asList(c.autorisator).map(function(a){return esc(a.naam||'')+(a.datum?' <span class="muted">('+esc(String(a.datum))+')</span>':'');}).join(', ');
    h.push('<dt>Autorisator</dt><dd>'+(aut||'<span class="muted">--</span>')+'</dd>');
    h.push('<dt>Beheerder</dt><dd>'+(asList(c.beheerder).join(', ')||'-')+'</dd></dl></section>');
    h.push('<section><h2>Context</h2><dl class="attr-grid">'
      +'<dt>Domein</dt><dd class="badges">'+badges('domein',c.domein)+'</dd>'
      +'<dt>Uitwisseling</dt><dd class="badges">'+badges('uitwisseling',c.uitwisseling)+'</dd>'
      +'<dt>Communicatiepatroon <span class="tag-prefix">[P]</span></dt><dd class="badges">'+badges('patroon',c.patroon)+'</dd>'
      +'<dt>Generieke functies <span class="tag-prefix">[F]</span></dt><dd class="badges">'+badges('functie',c.functie)+'</dd></dl></section>');
    if(c.voorwaarden)h.push('<section><h2>Voorwaarden / Uitzonderingen</h2><p>'+esc(c.voorwaarden)+'</p></section>');
    if(c.conformiteitscriteria)h.push('<section><h2>Conformiteitscriteria</h2><p>'+esc(c.conformiteitscriteria)+'</p></section>');
    if(c.body)h.push('<section><h2>Omschrijving</h2>'+para(c.body)+'</section>');
    if(asList(c.betreft_twiin).length)h.push('<section><h2>Bijbehorende specificaties in Twiin</h2><ul class="ref-list">'+c.betreft_twiin.map(function(r){var hf=linkFor(r.link);return '<li><a href="'+esc(hf)+'"'+(isInternal(hf)?'':' target="_top" rel="noopener"')+'>'+esc(r.titel)+'</a></li>';}).join('')+'</ul></section>');
    if(asList(c.betreft_extern).length)h.push('<section><h2>Bijbehorende standaarden &amp; normen buiten Twiin</h2><ul class="ref-list">'+c.betreft_extern.map(function(r){return '<li><a href="'+esc(r.link)+'" target="_top" rel="noopener">'+esc(r.titel)+'</a>'+(r.beheerder?' <span class="muted">- '+esc(r.beheerder)+'</span>':'')+'</li>';}).join('')+'</ul></section>');
    if(asList(c.relaties).length)h.push('<section><h2>Relaties en afhankelijkheden</h2><ul class="ref-list">'+c.relaties.map(function(u){var t=byUid[u];return t?('<li><a href="#'+HASHKEY+'='+esc(u)+'">'+esc(u)+' - '+esc(t.naam)+'</a></li>'):('<li>'+esc(u)+' <span class="muted">(niet in index)</span></li>');}).join('')+'</ul></section>');
    if(asList(c.toepassingen).length)h.push('<section><h2>Toepassingen in</h2><p class="badges">'+badges('toepassingen',c.toepassingen)+'</p></section>');
    if(asList(c.wijzigingslog).length)h.push('<section><h2>Wijzigingslog</h2><table class="log"><thead><tr><th>Datum</th><th>Versie</th><th>Wijziging</th></tr></thead><tbody>'+c.wijzigingslog.map(function(w){return '<tr><td>'+esc(String(w.datum||''))+'</td><td>'+esc(String(w.versie||''))+'</td><td>'+esc(w.wijziging||'')+'</td></tr>';}).join('')+'</tbody></table></section>');
    h.push('</article>'); return h.join('');
  }

  // Verberg filters zonder de kolom te laten inklappen (voorkomt dat de content
  // hercentreert/verspringt); de TOC-kolom blijft gereserveerd, net als in Scroll.
  function setFiltersVisible(v){ if(sideArea)sideArea.style.visibility=v?'visible':'hidden'; }
  function paintFilters(){ if(sideArea)sideArea.innerHTML=facetsHtml(); }
  function restoreInputs(){
    var si=mainArea.querySelector('[data-search]'); if(si){si.value=state.q; if(state.q){si.focus();si.setSelectionRange(si.value.length,si.value.length);}}
    var so=mainArea.querySelector('[data-sort]'); if(so)so.value=state.sort;
  }
  function renderList(){ mainArea.innerHTML=resultsHtml(); setFiltersVisible(true); paintFilters(); restoreInputs(); setCrumb(null); }
  function renderDetail(uid){ mainArea.innerHTML=detailHtml(uid); setFiltersVisible(false); setCrumb(uid); try{window.scrollTo(0,0);}catch(e){} }

  // --- Scroll-thema-integraties: breadcrumb (kaart-UID) + paginaboom (kaarten) ---
  function setCrumb(uid){
    var ol=document.querySelector('.breadcrumbs ol, theme-breadcrumbs ol'); if(!ol)return;
    var prev=ol.querySelector('[data-twiin-crumb]'); if(prev)prev.remove();
    if(uid){
      // Bij een geopende kaart wijst de laatste crumb naar de INDEXpagina (niet de kaart).
      var li=document.createElement('li'); li.setAttribute('data-twiin-crumb','1');
      var a=document.createElement('a'); a.href=location.pathname; a.setAttribute('data-twiin-index','1');
      a.textContent=INDEXNAME || 'Register Landelijke afspraken';
      li.appendChild(a); ol.appendChild(li);
    }
  }
  function hashUid(){var m=new RegExp('[#&]'+HASHKEY+'=([^&]+)').exec(location.hash||'');return m?decodeURIComponent(m[1]):null;}
  function render(){var u=hashUid(); if(u&&byUid[u])renderDetail(u); else renderList();}
  function toList(){ if(location.hash&&hashUid())history.pushState('','',location.pathname+location.search); }

  function wire(){
    document.addEventListener('click',function(e){
      // Breadcrumb-crumb 'Index...' -> terug naar de lijst (in-page, geen reload).
      var ix=e.target.closest&&e.target.closest('[data-twiin-index]');
      if(ix){ e.preventDefault(); toList(); render(); return; }
      if(!e.target.closest||!e.target.closest('.twiin-las'))return;
      if(e.target.closest('[data-back]')){toList();render();return;}
      var cp=e.target.closest('[data-copy]');
      if(cp){ var t=document.querySelector(cp.getAttribute('data-copy')); if(t&&navigator.clipboard){ navigator.clipboard.writeText(t.textContent.trim()); var o=cp.textContent; cp.textContent='Gekopieerd'; setTimeout(function(){cp.textContent=o;},1500); } return; }
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

  function makeTocHost(){
    var mc=qs('.main-content'); if(!mc)return null;
    // Ruim eventuele eerdere injectie op (voorkomt dubbele filterkolommen).
    var olds=mc.querySelectorAll('nav[data-twiin]'); for(var k=0;k<olds.length;k++)olds[k].remove();
    // Verwijder een bestaande Scroll-TOC, zodat alleen onze filters tonen.
    var ex=mc.querySelector('.toc.sticky:not([data-twiin])'); if(ex)ex.remove();
    var nav=document.createElement('nav');
    nav.className='toc sticky twiin-las twiin-las-toc';
    nav.setAttribute('data-twiin','1');
    nav.style.display='flex'; nav.style.flexDirection='column';
    mc.appendChild(nav);
    return nav;
  }
  function boot(host){
    css();
    var h1=host.querySelector('h1'); if(h1&&h1.textContent.trim())INDEXNAME=h1.textContent.trim();
    // Laat het native infobox-'panel' (uit Confluence) exact staan waar Scroll het rendert,
    // zodat het zijn eigen opmaak/hoogte houdt (geen reflow/resize bij het mounten). We
    // verwijderen alleen overige native inhoud en hangen het register eronder.
    var _kids=[].slice.call(host.children);
    for(var _i=0;_i<_kids.length;_i++){ var _k=_kids[_i]; if(!(_k.matches&&_k.matches('[data-component="panel"]'))) _k.remove(); }
    var mw=document.createElement('div'); mw.className='twiin-las twiin-las-content';
    host.appendChild(mw);
    var toc=makeTocHost();
    if(toc){ mainArea=mw; sideArea=toc; tocMode=true; }
    else {
      mw.innerHTML='<div class="twiin-las-split"><div class="twiin-las-col-main" data-main></div><aside class="twiin-las-col-side" data-side></aside></div>';
      mainArea=mw.querySelector('[data-main]'); sideArea=mw.querySelector('[data-side]');
    }
    wire(); render(); return true;
  }
  function findHost(){for(var i=0;i<MAIN_SELECTORS.length;i++){var el=qs(MAIN_SELECTORS[i]);if(el)return el;}return null;}

  // Register (filters + resultaten + detail) mounten op de indexpagina.
  // Op andere pagina's doet het script niets (index blijft binnen de pagina).
  if(ON_INDEX){
    var n=0, iv=setInterval(function(){ n++; var host=findHost();
      if(host){ clearInterval(iv); boot(host); } else if(n>66){ clearInterval(iv); } },150);
  }
})();
