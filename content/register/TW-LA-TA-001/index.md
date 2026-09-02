---
title: "Netwerkbeveiliging (mTLS 1.3)"
uid: "TW-LA-TA-001"
soort: "TA"
slug: "tw-la-ta-001"
samenvatting: "Technische afspraak voor netwerk-niveau beveiliging met wederzijds geauthenticeerde TLS 1.3 (mTLS) op basis van PKIoverheid-certificaten, inclusief revocatiecontrole via CRL/OCSP."
permalink: ""
status: "Normatief"
ingangsdatum: "2026-04-09"
ingang_stelselversie: "1.5"
vervaldatum: ""
vervaldatum_stelselversie: ""
domein: ["MSZ", "VVT", "HA"]
uitwisseling: ["Verwijzing", "Overdracht"]
patroon: ["Notified Pull", "Pull", "Indexed Pull", "Push"]
functie: ["Netwerkbeveiliging", "Authenticatie", "Identificatie"]
voorwaarden: "Geldt voor alle systeem-tot-systeem-verbindingen binnen het stelsel, ongeacht het communicatiepatroon."
conformiteitscriteria: "Verbindingen gebruiken uitsluitend TLS 1.3 met wederzijdse authenticatie (mTLS). Systemen die de geldigheid van het PKIoverheid-servercertificaat van andere systemen controleren, MOETEN dit volgens de meest recent gepubliceerde Certificaten Revocatie Lijst (CRL) of via het Online Certificate Status Protocol (OCSP) minimaal ieder uur doen."
auteur: ["Working Group TA"]
autorisator:
  - naam: "VWS programma LDN"
    datum: "2026-04-09"
beheerder: ["Twiin"]
betreft_twiin:
  - titel: "10.4.7 | Network level security: mTLS 1.3"
    link: "https://afsprakenstelsel.twiin.nl/normatief/ta150/10-2-10-netwerk-level-security-mtls-1-3#Network-level-security:-mTLS-1.3"
    beheerder: "Twiin"
  - titel: "PvE | Netwerkbeveiliging: mTLS"
    link: "https://afsprakenstelsel.twiin.nl/normatief/ta150/pve-netwerkbeveiliging#mTLS"
    beheerder: "Twiin"
betreft_extern: []
relaties: []
toepassingen: ["MedMij", "AORTA", "NUTS"]
wijzigingslog:
  - datum: "2026-04-09"
    versie: "1.0"
    wijziging: "Vastgesteld bij Stelselversie 1.5 (TLS 1.3 verplicht)."
uitgelicht: true
prioriteit: 1
draft: false
---

Deze technische afspraak legt de beveiliging van het transportkanaal tussen systemen vast.
Alle systeem-tot-systeem-verbindingen binnen het stelsel verlopen via **wederzijds
geauthenticeerde TLS 1.3** (mTLS) met servercertificaten uit het PKIoverheid-stelsel.

Systemen die de geldigheid van het PKIoverheid-servercertificaat van andere systemen
controleren, MOETEN dit volgens de meest recent gepubliceerde Certificaten Revocatie Lijst
(CRL) of via het Online Certificate Status Protocol (OCSP), minimaal ieder uur, doen.

De normatieve tekst en de bijbehorende eisen staan in het Twiin Afsprakenstelsel onder
**Netwerkbeveiliging**; zie de verwijzingen hieronder onder *Bijbehorende
specificaties in Twiin*.
