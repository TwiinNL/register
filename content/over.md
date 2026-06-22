---
title: "Over dit register"
---

Dit register is de **centrale vindplaats (single source of truth)** voor de metadata van
afspraken, specificaties, richtlijnen en standaarden binnen het **Twiin Landelijk
Afsprakenstelsel (LAS)**. Iedere kaart beschrijft één afspraak — of een combinatie van
afspraken — en vormt het permalink-anker waar andere partijen naar verwijzen.

## Metadatakaarten

Elke kaart heeft een unieke identificatie volgens de logica **`TW-LAS-[SOORT]-[NUMMER]`**,
waarbij `SOORT` een van de volgende waarden is:

| Code | Soort |
|------|-------|
| VA | Vertrouwensafspraak |
| PA | Procesafspraak |
| TA | Technische afspraak |
| SP | Specificatie |
| RI | Richtlijn |

## Permalinks

De permalink is de stabiele verwijzing naar een kaart. Zolang de site via Codeberg Pages
gepubliceerd wordt, is de permalink de URL binnen deze publicatie. Zodra een eigen domein
gekoppeld is, verwijst de permalink daarnaartoe — de inhoud en het pad blijven gelijk.

## RDF / JSON-LD

Iedere kaart publiceert een machineleesbare beschrijving als **JSON-LD** (een
RDF-serialisatie). Deze is opgenomen in de pagina en los op te halen via `index.jsonld` bij
elke kaart. De beschrijving gebruikt gangbare vocabulaires — Dublin Core Terms (`dct`),
ADMS (`adms`), SKOS (`skos`) en schema.org — aangevuld met een eigen LAS-vocabulaire (`las:`)
voor domeinspecifieke eigenschappen.

## Zoeken en filteren

Het [register](../register/) is full-text doorzoekbaar (via Pagefind) en te filteren op
attributen: soort, status, domein, uitwisseling, communicatiepatroon, generieke functie,
toepassing en auteur.
