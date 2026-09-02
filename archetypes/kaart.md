---
# === Identiteit ===========================================================
title: "{{ replace .Name `-` ` ` | title }}"
uid: "TW-LA-XX-000"           # logica: TW-LA-[SOORT]-[NUMMER]
soort: "SP"                    # VA | PA | TA | SP | RI
slug: "tw-la-xx-000"           # = uid in kleine letters (bepaalt de URL)
samenvatting: "Korte omschrijving die in overzichten en zoekresultaten verschijnt."

# Permalink: laat leeg om automatisch de pagina-URL te gebruiken (huidige
# 'place of truth'). Vul een absolute URL in zodra een eigen domein gekoppeld is.
permalink: ""

# === Status & geldigheid ==================================================
status: "Draft"                # Draft | Candidate | Trial | Normatief | Informative | Uitgefaseerd | Vervallen
ingangsdatum: "2026-01-01"
ingang_stelselversie: "1.5"
vervaldatum: ""
vervaldatum_stelselversie: ""

# === Context ==============================================================
domein: []                     # MSZ, VVT, HA
uitwisseling: []               # Verwijzing, Overdracht
patroon: []                    # Notified Pull, Pull, Indexed Pull, Push
functie: []                    # Identificatie, Authenticatie, ... (zie data/vocab.yaml)

# === Voorwaarden & conformiteit ===========================================
voorwaarden: ""
conformiteitscriteria: ""

# === Verantwoordelijken ===================================================
auteur: ["Twiin"]              # Working Group TA | Twiin | Working Group TA NP
autorisator:
  - naam: "VWS programma LDN"
    datum: "2026-01-01"
beheerder: ["Twiin"]

# === Relaties =============================================================
# Bijbehorende specificaties binnen Twiin (1..*)
betreft_twiin:
  - titel: ""
    link: ""
    beheerder: "Twiin"
# Bijbehorende standaarden/normen buiten Twiin (0..*)
betreft_extern: []
# Relaties en afhankelijkheden — verwijzingen naar andere UIDs (0..*)
relaties: []
# Toepassingen in stelsels (0..*): MedMij, AORTA, NUTS
toepassingen: []

# === Wijzigingslog ========================================================
wijzigingslog:
  - datum: "2026-01-01"
    versie: "0.1"
    wijziging: "Initiële opzet."

# === Overzicht / homepage =================================================
uitgelicht: false              # true = tonen onder 'Belangrijk' op de homepage
prioriteit: 99                 # lager = belangrijker (sortering uitgelicht)
draft: true
---

Vrije, uitgebreide omschrijving van de afspraak/specificatie (markdown).
Deze tekst verschijnt onder "Omschrijving" en wordt geïndexeerd voor zoeken.
