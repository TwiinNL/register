---
title: "Over het register"
---

Dit register is de **centrale vindplaats** voor de metadata van
afspraken, specificaties, richtlijnen en standaarden binnen het **Twiin Landelijk
Afsprakenstelsel voor gezondheidsgegevens**. Iedere kaart beschrijft één afspraak, of een combinatie van
afspraken vormt het permalink-anker voor verwijzing.

## Metadatakaarten

Elke kaart heeft een unieke identificatie volgens de logica **`TW-LA-[SOORT]-[NUMMER]`**,
waarbij `SOORT` een van de volgende waarden is:

| Code | Soort |
|------|-------|
| VA | Vertrouwensafspraak |
| PA | Procesafspraak |
| TA | Technische afspraak |
| SP | Specificatie |
| RI | Richtlijn |

## Permalinks

De permalink is de stabiele verwijzing naar een kaart. Zolang de site via GitHub Pages
gepubliceerd wordt, is de permalink de URL binnen deze publicatie. Zodra een eigen domein
gekoppeld is, verwijst de permalink daarnaartoe.

## RDF / JSON-LD

Iedere kaart publiceert een machineleesbare beschrijving als RDF. Deze is opgenomen in de pagina en los op te halen via `index.jsonld` bij
elke kaart. De beschrijving gebruikt Dublin Core Terms (`dct`),
ADMS (`adms`), SKOS (`skos`) en schema.org, aangevuld met een eigen LA-vocabulaire (`la:`)
voor domeinspecifieke eigenschappen.

## Zoeken en filteren

Het [register](../register/) is full-text doorzoekbaar en te filteren op
attributen: soort, status, domein, uitwisseling, communicatiepatroon, generieke functie,
toepassing en auteur.
