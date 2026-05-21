# Skole-fraværssystem

Prosjektet er et enkelt fraværssystem der man kan registrere elever, klasser, fag og fravær ved hjelp av Flask, MariaDB, HTML, CSS og JavaScript.

Målet med prosjektet er å vise hvordan en webapplikasjon kan kobles sammen med en SQL-database. Prosjektet viser hvordan data kan hentes fra databasen, vises på nettsiden, legges til gjennom skjemaer og slettes fra systemet.

---

## Om prosjektet

Skole-fraværssystemet er laget for å simulere et enkelt digitalt system som kan brukes på en skole. Systemet lar brukeren se elever, legge til nye elever, registrere fravær og se oversikt over registrert fravær.

Prosjektet er ikke ment som et ferdig profesjonelt system, men som et skoleprosjekt som viser forståelse for backend, frontend og database. Det viktigste i prosjektet er å vise hvordan Flask, HTML og MariaDB kan jobbe sammen i en enkel fullstack-applikasjon.

---

## Funksjoner

Systemet har flere enkle funksjoner som viser hvordan en databasebasert webapplikasjon fungerer.

Brukeren kan åpne en forside som forklarer systemet. Det finnes også et dashboard som viser enkel statistikk, for eksempel antall elever, antall fravær og antall fag.

Systemet kan vise alle elever som er lagret i databasen. Man kan også legge til nye elever gjennom et HTML-skjema, og elevene blir lagret direkte i MariaDB-databasen.

Det er også mulig å slette elever. Før en elev slettes, kan JavaScript brukes til å vise en bekreftelse slik at man ikke sletter feil elev ved et uhell.

Systemet har en side for å registrere fravær. Der kan man velge elev, fag, dato, status og skrive en kommentar.

Alt registrert fravær kan vises i en egen tabell. Denne tabellen bruker data fra flere tabeller i databasen, for eksempel elever, fag og fravær.

Prosjektet har også en enkel admin-side og en FAQ-side. FAQ-siden forklarer hva systemet gjør, hvordan data lagres og hvilke SQL-funksjoner som brukes.

---

## Teknologi brukt

Prosjektet bruker Python og Flask som backend. Flask brukes til å lage routes, koble til HTML-sider og sende data mellom nettsiden og databasen.

MariaDB brukes som SQL-database. Databasen lagrer informasjon om elever, klasser, fag og fravær.

HTML brukes til å lage strukturen på nettsidene. CSS brukes til design, layout, farger, knapper, tabeller og responsivt design.

JavaScript brukes til små funksjoner på nettsiden, for eksempel bekreftelse før sletting av en elev.

Jinja2 brukes i HTML-filene for å vise data fra Flask. For eksempel brukes Jinja til å loope gjennom elever og fravær som kommer fra databasen.

---

## Mappestruktur

Prosjektet har en enkel mappestruktur uten ekstra filer som ikke trengs.

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
    ├── base.html
    ├── dashboard.html
    ├── elev_detaljer.html
    ├── elever.html
    ├── faq.html
    ├── fravaer.html
    ├── index.html
    ├── legg_til_elev.html
    └── registrer_fravaer.html
