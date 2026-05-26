# Skole-fraværssystem

Prosjektet er et enkelt skole-fraværssystem der brukere kan registrere seg, logge inn, se elever, legge til elever, registrere fravær og bruke en FAQ-side.

Prosjektet bruker Flask, MariaDB, HTML, CSS og JavaScript. Målet med prosjektet er å vise hvordan en webapplikasjon kan kobles til en SQL-database, og hvordan man kan bruke backend, frontend og database sammen i et realistisk system.

---

## Om prosjektet

Skole-fraværssystemet er laget for å simulere et enkelt digitalt system som kan brukes på en skole. Systemet lar brukere registrere seg, logge inn og bruke funksjoner som elevliste, fraværsregistrering, dashboard og admin-side.

Prosjektet er ikke ment som et ferdig profesjonelt system, men som et skoleprosjekt som viser forståelse for Flask, MariaDB, SQL, HTML, CSS, JavaScript og enkel brukersikkerhet.

---

## Funksjoner

Systemet har disse funksjonene:

- Forside
- Registrering av bruker
- Innlogging
- Utlogging
- Beskyttede sider som krever innlogging
- Dashboard med enkel statistikk
- Vise alle elever
- Legge til ny elev
- Slette elev
- Se detaljer om én elev
- Registrere fravær
- Vise alt registrert fravær
- Enkel admin-side
- FAQ-side med brukerveiledning
- Brukere kan sende inn spørsmål på FAQ-siden
- Admin kan se spørsmål som er sendt inn
- Admin kan svare på spørsmål
- Admin kan anonymisere personinformasjon på innsendte spørsmål
- Responsivt design for ulike skjermstørrelser

---

## Teknologi brukt

Prosjektet bruker Python og Flask som backend. Flask brukes til å lage routes, håndtere skjemaer, koble til databasen og sende data til HTML-sidene.

MariaDB brukes som SQL-database. Databasen lagrer elever, klasser, fag, fravær, brukere og FAQ-spørsmål.

HTML brukes til å lage strukturen på nettsidene. CSS brukes til design, layout, knapper, skjemaer, tabeller og responsivt design.

JavaScript brukes til små funksjoner på nettsiden, for eksempel bekreftelse før sletting av en elev. Jinja2 brukes i HTML-filene for å vise data fra Flask og MariaDB.

---

## Mappestruktur

```text
SKOLE-FRAVAER-SYSTEM/
│
├── app.py
│
├── static/
│   ├── script.js
│   └── style.css
│
└── templates/
    ├── admin.html
    ├── admin_faq.html
    ├── base.html
    ├── dashboard.html
    ├── elev_detaljer.html
    ├── elever.html
    ├── faq.html
    ├── fravaer.html
    ├── index.html
    ├── legg_til_elev.html
    ├── login.html
    ├── register.html
    └── registrer_fravaer.html
