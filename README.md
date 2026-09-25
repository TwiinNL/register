# Twiin Landelijk afsprakenstelsel | Register

De centrale vindplaats voor de metadata van afspraken,
specificaties, richtlijnen en standaarden binnen het **Twiin Landelijk Afsprakenstelsel
voor gezondheidsgegevens**. Elke **metadatakaart** beschrijft één afspraak (of combinatie van afspraken),
biedt een **stabiele permalink** waar andere partijen naar verwijzen, en publiceert een
machineleesbare **RDF/JSON-LD**-representatie.

Gebouwd met **[Hugo](https://gohugo.io/)** (statische site) en
**[Pagefind](https://pagefind.app/)** (zoeken + facet-filteren), gepubliceerd via
**GitHub Pages** met **GitHub Actions**.

---

## Snel starten (lokaal)

Vereist: Hugo *extended* en (optioneel) de Pagefind-binary.

```bash
# macOS
brew install hugo
# Pagefind via npx werkt ook zonder installatie

# Bouwen + zoekindex + lokaal serveren
./scripts/build.sh local
python3 -m http.server 8088 --directory public
# → http://localhost:8088/
```

Voor live bewerken zonder zoekindex: `hugo server` (Pagefind-zoeken werkt dan niet,
de server-gerenderde kaartenlijst blijft als fallback zichtbaar).

---

## Een nieuwe kaart toevoegen

```bash
hugo new --kind kaart content/register/TW-LA-SP-003/index.md
```

Dit maakt een kaart op basis van [`archetypes/kaart.md`](archetypes/kaart.md). Vul de
front-matter in (zie veldenoverzicht hieronder) en zet `draft: false`. De URL volgt uit
`slug` (= UID in kleine letters), bijvoorbeeld `/la/tw-la-sp-003/`.

### Velden (front-matter)

| Veld | Betekenis |
|------|-----------|
| `title` | Naam van de afspraak |
| `uid` | `TW-LA-[SOORT]-[NUMMER]` |
| `soort` | `VA`, `PA`, `TA`, `SP`, `RI` |
| `slug` | UID in kleine letters (bepaalt de URL) |
| `samenvatting` | Korte tekst voor overzichten/zoekresultaten |
| `permalink` | Leeg = automatische URL; vul absolute URL bij eigen domein |
| `status` | `Draft`, `Candidate`, `Trial`, `Normatief`, `Informative`, `Uitgefaseerd`, `Vervallen` |
| `ingangsdatum` / `ingang_stelselversie` | Datum + stelselversie |
| `vervaldatum` / `vervaldatum_stelselversie` | Datum + stelselversie |
| `domein` | `MSZ`, `VVT`, `HA` |
| `uitwisseling` | `Verwijzing`, `Overdracht` |
| `patroon` | `Notified Pull`, `Pull`, `Indexed Pull`, `Push` |
| `functie` | `Identificatie`, `Authenticatie`, … (zie `data/vocab.yaml`) |
| `voorwaarden`, `conformiteitscriteria` | Vrije tekst |
| `auteur`, `autorisator`, `beheerder` | Organisaties/rollen |
| `betreft_twiin` | Bijbehorende specificaties binnen Twiin (link + beheerder) |
| `betreft_extern` | Standaarden/normen buiten Twiin (link + beheerder) |
| `relaties` | Verwijzingen naar andere UIDs |
| `toepassingen` | `MedMij`, `AORTA`, `NUTS` |
| `wijzigingslog` | Datum + versie + wijziging |
| `uitgelicht` / `prioriteit` | Tonen onder “Belangrijk” op de homepage |

Alle toegestane waarden en hun labels staan in **[`data/vocab.yaml`](data/vocab.yaml)** —
dit is de enige plek om vocabulaires uit te breiden.

---

## Architectuur

```
hugo.toml                 # config: baseURL, permalinks, JSON-LD output format
data/vocab.yaml           # gecontroleerde vocabulaires (codes, labels, kleuren)
archetypes/kaart.md       # sjabloon voor nieuwe kaarten
content/
  _index.md               # landingspagina
  over.md                 # uitleg register/permalinks/RDF
  register/
    _index.md             # register (zoeken + filteren)
    TW-LA-*/index.md       # de metadatakaarten
layouts/
  index.html              # landingspagina (uitgelicht + categorieën)
  index.json              # machineleesbare index van alle kaarten
  register/list.html      # zoek-/filterpagina (Pagefind)
  register/single.html    # kaart-detailpagina (alle velden)
  _default/single.jsonld  # RDF/JSON-LD per kaart (index.jsonld)
  partials/jsonld-data.html  # opbouw van de RDF-graf
static/css, static/js     # styling en gedrag (thema, filter-UI)
.github/workflows/deploy.yml  # CI: build + publish
```

### RDF / JSON-LD

Elke kaart bevat een `<script type="application/ld+json">` in de pagina én een los
`index.jsonld`-bestand. De beschrijving gebruikt Dublin Core Terms (`dct`), ADMS (`adms`),
SKOS (`skos`) en schema.org, aangevuld met een eigen LA-vocabulaire (`la:`). De
namespace staat in `hugo.toml` (`params.rdfNamespace`).

### Zoeken & filteren

Pagefind indexeert alleen de kaarten (`data-pagefind-body`). Facetten worden afgeleid uit
verborgen `data-pagefind-filter`-elementen op elke kaart: soort, status, domein,
uitwisseling, communicatiepatroon, generieke functie, toepassing, auteur.

---

## Publicatie (GitHub Pages)

De workflow [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) bouwt bij elke
push naar `main` de site + zoekindex en publiceert via de officiele GitHub Pages
artifact-flow. Live URL: **https://register.twiin.nl/** (custom domain, serveert op de root).
`twiinnl.github.io/register/` redirect daarheen.

> Eenmalig instellen: **Settings → Pages → Build and deployment → Source = "GitHub Actions"**.

### Custom domain `register.twiin.nl`

* **`static/CNAME`** bevat `register.twiin.nl` — Hugo kopieert dit naar `public/CNAME`, zodat
  elke Actions-build het custom domain meepubliceert (anders wist elke deploy het domain en
  krijg je de "Create CNAME / Delete CNAME"-lus).
* **DNS** (bij de twiin.nl-provider): `register.twiin.nl` → **CNAME** → `twiinnl.github.io`
  (of vier A-records: `185.199.108.153`, `.109.153`, `.110.153`, `.111.153`). Het mag NIET naar
  een andere server wijzen. Pas ná deze DNS-wijziging geeft GitHub een TLS-certificaat uit en
  serveert het domein — domein-*verificatie* (TXT) alleen is niet genoeg.
* `baseURL` = `https://register.twiin.nl/`, permalinks `register = "/la/:slug/"` →
  `register.twiin.nl/la/<slug>/`.

---

## Licentie / beheer

Beheerder: **Twiin**. Inhoudelijke vaststelling via de betreffende *Working Group* en
autorisatie door het VWS-programma LDN.
