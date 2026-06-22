---
title: "Netwerkbeveiliging mTLS 1.3"
uid: "TW-LAS-SP-001"
soort: "SP"
slug: "tw-las-sp-001"
samenvatting: "Specificatie voor wederzijds geauthenticeerde transportbeveiliging (mutual TLS 1.3) met PKIoverheid-certificaten, inclusief revocatiecontrole via CRL/OCSP."
permalink: ""
status: "Normatief"
ingangsdatum: "2026-04-09"
ingang_stelselversie: "1.5"
vervaldatum: ""
vervaldatum_stelselversie: ""
domein: ["MSZ", "VVT", "HA"]
uitwisseling: ["Verwijzing", "Overdracht"]
patroon: ["Notified Pull", "Pull", "Push", "Indexed Pull"]
functie: ["Netwerkbeveiliging", "Authenticatie", "Identificatie"]
voorwaarden: "Geldt voor alle systeem-tot-systeem-verbindingen binnen het stelsel, ongeacht het communicatiepatroon."
conformiteitscriteria: "Systemen die de geldigheid van het PKIoverheid-servercertificaat van andere systemen controleren, MOETEN dit volgens de meest recent gepubliceerde Certificaten Revocatie Lijst (CRL) of via het Online Certificate Status Protocol (OCSP) minimaal ieder uur doen. Verbindingen gebruiken uitsluitend TLS 1.3."
auteur: ["Working Group TA"]
autorisator:
  - naam: "VWS programma LDN"
    datum: "2026-04-09"
beheerder: ["Twiin"]
betreft_twiin: []
betreft_extern:
  - titel: "RFC 8446 — TLS 1.3"
    link: "https://www.rfc-editor.org/rfc/rfc8446"
    beheerder: "IETF"
  - titel: "PKIoverheid Programma van Eisen"
    link: "https://www.logius.nl/domeinen/toegang/pkioverheid"
    beheerder: "Logius"
relaties: ["TW-LAS-VA-001"]
toepassingen: ["MedMij", "AORTA", "NUTS"]
wijzigingslog:
  - datum: "2026-04-09"
    versie: "2.0"
    wijziging: "Overstap naar verplicht TLS 1.3; vastgesteld bij Stelselversie 1.5."
  - datum: "2025-06-01"
    versie: "1.0"
    wijziging: "Eerste versie op basis van TLS 1.2."
uitgelicht: true
prioriteit: 3
draft: false
---

Deze specificatie legt de eisen vast voor de beveiliging van het transportkanaal tussen
systemen. Alle verbindingen verlopen via **wederzijds geauthenticeerde TLS 1.3** (mTLS) met
servercertificaten uit het PKIoverheid-stelsel.

Systemen die de geldigheid van het PKIoverheid-servercertificaat van de andere systemen
dienen te controleren, MOETEN dit volgens de meest recent gepubliceerde Certificaten
Revocatie Lijst (CRL) of via het Online Certificate Status Protocol (OCSP), minimaal ieder
uur, doen.
