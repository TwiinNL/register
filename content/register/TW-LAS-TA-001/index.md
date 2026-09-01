---
title: "Notified Pull via FHIR"
uid: "TW-LAS-TA-001"
soort: "TA"
slug: "tw-las-ta-001"
samenvatting: "Technische afspraak voor het notificeren en vervolgens gericht bevragen (Notified Pull) van medische gegevens op basis van HL7 FHIR R4."
permalink: ""
status: "Normatief"
ingangsdatum: "2026-04-09"
ingang_stelselversie: "1.5"
vervaldatum: ""
vervaldatum_stelselversie: ""
domein: ["MSZ", "VVT"]
uitwisseling: ["Verwijzing"]
patroon: ["Notified Pull"]
functie: ["Adressering", "Routering", "Logging"]
voorwaarden: "Van toepassing op verwijzing tussen MSZ en VVT waarbij de ontvanger pas na notificatie de gegevens ophaalt."
conformiteitscriteria: "Systemen ondersteunen de FHIR-profielen en interacties zoals beschreven in de bijbehorende specificatie; notificaties worden bevestigd en bevragingen gelogd conform TW-LAS-SP-001."
auteur: ["Working Group TA"]
autorisator:
  - naam: "VWS programma LDN"
    datum: "2026-04-09"
beheerder: ["Twiin"]
betreft_twiin:
  - titel: "Specificatie: Netwerkbeveiliging mTLS 1.3"
    link: "/register/tw-las-sp-001/"
    beheerder: "Twiin"
betreft_extern:
  - titel: "HL7 FHIR R4"
    link: "https://hl7.org/fhir/R4/"
    beheerder: "HL7 International"
  - titel: "Nictiz — Bibliotheek (zibs)"
    link: "https://nationalebibliotheek.nictiz.nl/bibliotheek/"
    beheerder: "Nictiz"
relaties: ["TW-LAS-SP-001", "TW-LAS-TA-002"]
toepassingen: ["AORTA", "NUTS"]
wijzigingslog:
  - datum: "2026-04-09"
    versie: "1.1"
    wijziging: "Profielen geactualiseerd naar FHIR R4; vastgesteld bij Stelselversie 1.5."
  - datum: "2025-11-01"
    versie: "1.0"
    wijziging: "Eerste normatieve versie."
uitgelicht: true
prioriteit: 2
draft: false
---

Deze technische afspraak beschrijft het **Notified Pull**-patroon: de bronhouder verstuurt
een notificatie naar de geadresseerde, die vervolgens op een zelfgekozen moment de
betreffende gegevens gericht opvraagt. De uitwisseling verloopt over een wederzijds
geauthenticeerde TLS-verbinding (zie [TW-LAS-SP-001](/register/tw-las-sp-001/)) en maakt
gebruik van HL7 FHIR R4-resources en -interacties.

De afspraak legt de minimale set FHIR-profielen, de notificatie-payload en de
bevragingsinteracties vast, evenals de eisen aan logging en bevestiging.
