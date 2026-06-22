---
title: "Lokalisatie en adressering (Indexed Pull)"
uid: "TW-LAS-TA-002"
soort: "TA"
slug: "tw-las-ta-002"
samenvatting: "Technische afspraak voor het lokaliseren van gegevensbronnen via een verwijsindex en het gericht adresseren daarvan volgens het Indexed Pull-patroon."
permalink: ""
status: "Trial"
ingangsdatum: "2026-06-01"
ingang_stelselversie: "1.5"
vervaldatum: ""
vervaldatum_stelselversie: ""
domein: ["MSZ", "HA"]
uitwisseling: ["Verwijzing"]
patroon: ["Indexed Pull"]
functie: ["Localisatie", "Adressering", "Routering"]
voorwaarden: "Trial-use: van toepassing in de beproevingsfase voordat de afspraak normatief wordt."
conformiteitscriteria: "Bronnen registreren hun vindbaarheid in de verwijsindex; raadplegers gebruiken uitsluitend de index voor lokalisatie en adresseren conform de daarin opgenomen endpoints."
auteur: ["Working Group TA"]
autorisator:
  - naam: "VWS programma LDN"
    datum: "2026-06-01"
beheerder: ["Twiin"]
betreft_twiin:
  - titel: "Technische afspraak: Notified Pull via FHIR"
    link: "/register/tw-las-ta-001/"
    beheerder: "Twiin"
  - titel: "Specificatie: Netwerkbeveiliging mTLS 1.3"
    link: "/register/tw-las-sp-001/"
    beheerder: "Twiin"
betreft_extern:
  - titel: "IHE XCPD — Cross-Community Patient Discovery"
    link: "https://profiles.ihe.net/ITI/TF/Volume1/ch-27.html"
    beheerder: "IHE"
relaties: ["TW-LAS-TA-001", "TW-LAS-SP-001"]
toepassingen: ["AORTA", "NUTS"]
wijzigingslog:
  - datum: "2026-06-01"
    versie: "0.9"
    wijziging: "Vrijgegeven voor trial-use bij Stelselversie 1.5."
uitgelicht: true
prioriteit: 4
draft: false
---

Deze technische afspraak beschrijft het **Indexed Pull**-patroon: een verwijsindex geeft aan
welke bronnen relevante gegevens hebben, waarna de raadpleger die bron gericht bevraagt.
De afspraak bevindt zich in de **trial-use**-fase en wordt beproefd vóór normatieve
vaststelling.
