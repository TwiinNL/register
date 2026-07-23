---
title: "Identificatie en authenticatie zorgaanbieder"
uid: "TW-LAS-SP-002"
soort: "SP"
slug: "tw-las-sp-002"
samenvatting: "Specificatie voor het identificeren en authenticeren van zorgaanbieders en hun systemen met behulp van UZI en organisatie-identificaties."
permalink: ""
status: "Candidate"
ingangsdatum: "2026-09-01"
ingang_stelselversie: "1.6"
vervaldatum: ""
vervaldatum_stelselversie: ""
domein: ["MSZ", "VVT", "HA"]
uitwisseling: ["Verwijzing", "Overdracht"]
patroon: ["Pull", "Notified Pull"]
functie: ["Identificatie", "Authenticatie", "Autorisatie"]
voorwaarden: "Kandidaat-versie; van toepassing zodra vastgesteld bij Stelselversie 1.6."
conformiteitscriteria: "Systemen authenticeren zorgaanbieders met UZI-middelen en koppelen elke transactie aan een geverifieerde organisatie-identificatie (URA)."
auteur: ["Working Group TA"]
autorisator: []
beheerder: ["Twiin"]
betreft_twiin:
  - titel: "Specificatie: Netwerkbeveiliging mTLS 1.3"
    link: "/index/tw-las-sp-001/"
    beheerder: "Twiin"
betreft_extern:
  - titel: "UZI-register (CIBG)"
    link: "https://www.uziregister.nl/"
    beheerder: "CIBG"
relaties: ["TW-LAS-SP-001", "TW-LAS-PA-001"]
toepassingen: ["MedMij", "AORTA"]
wijzigingslog:
  - datum: "2026-05-15"
    versie: "0.8"
    wijziging: "Kandidaat-versie ter besluitvorming voor Stelselversie 1.6."
uitgelicht: false
prioriteit: 15
draft: false
---

Deze specificatie beschrijft hoe zorgaanbieders en hun systemen worden geïdentificeerd en
geauthenticeerd, als basis voor autorisatiebeslissingen. Zij bouwt voort op de
transportbeveiliging uit [TW-LAS-SP-001](/index/tw-las-sp-001/) en is op dit moment een
**kandidaat**-versie voor Stelselversie 1.6.
