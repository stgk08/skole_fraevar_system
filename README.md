# Skole Fraværssystem

## 1. Prosjektidé og problemstilling

### Beskrivelse

Skole Fraværssystem er en webapplikasjon utviklet med Flask og MariaDB. Systemet gjør det mulig å registrere, administrere og vise elevfravær gjennom et nettbasert grensesnitt.

Prosjektet ble utviklet for å gjøre registrering og administrasjon av fravær enklere for lærere og administratorer, samtidig som elever kan se sitt eget fravær.

### Problemstilling

Hvordan kan man utvikle et sikkert og brukervennlig system for registrering og administrasjon av elevfravær?

### Hva skal jeg gjøre på eksamensdagen

På eksamensdagen skal jeg:

* Presentere prosjektet
* Forklare systemarkitektur
* Demonstrere funksjonaliteten
* Forklare databasen
* Forklare sikkerhetstiltak
* Vise GitHub og Kanban-board
* Demonstrere rollebasert tilgangskontroll

### GitHub Project

Repository:

```text
https://github.com/stgk08/skole_fraevar_system
```

---

## 2. Systembeskrivelse

### Formål

Formålet med systemet er å registrere og administrere elevfravær på en enkel og sikker måte.

### Brukerflyt

1. Brukeren åpner nettsiden.
2. Brukeren registrerer konto eller logger inn.
3. Systemet identifiserer brukerrollen.
4. Administrator kan administrere systemet.
5. Lærer kan registrere og administrere fravær.
6. Elev kan se sitt eget fravær.
7. Data lagres i MariaDB.

### Teknologier brukt

* Python
* Flask
* MariaDB
* HTML
* CSS
* Jinja2
* Waitress
* GitHub

---

## 3. Server-, infrastruktur- og nettverksoppsett

### Servermiljø

Applikasjonen kjører på Linux-server med Waitress som WSGI-server.

### Nettverksoppsett

```text
Klient
   ↓
Waitress
   ↓
Flask
   ↓
MariaDB
```

### Porter

```text
TCP 5000 - Flask / Waitress
TCP 3306 - MariaDB
```

### Miljøvariabler

```env
DB_HOST=
DB_USER=
DB_PASSWORD=
DB_NAME=
```

---

## 4. Prosjektstyring – GitHub Projects (Kanban)

Prosjektet ble planlagt og organisert ved hjelp av GitHub Projects.

Eksempler på oppgaver:

* Lage innlogging
* Lage registrering
* Lage elevoversikt
* Registrere fravær
* Lage FAQ-system
* Lage adminpanel
* Koble bruker og elev
* Lage rollebasert tilgangskontroll

### Refleksjon

Kanban gjorde det enklere å holde oversikt over oppgaver, prioritere arbeid og dokumentere fremdriften i prosjektet.

---

## 5. Databasebeskrivelse

### Databasenavn

```text
skole_fravaer_db
```

### Tabeller

#### brukere

| Felt         | Datatype |
| ------------ | -------- |
| id           | INT      |
| brukernavn   | VARCHAR  |
| passord_hash | VARCHAR  |
| rolle        | VARCHAR  |

#### elever

| Felt      | Datatype |
| --------- | -------- |
| id        | INT      |
| fornavn   | VARCHAR  |
| etternavn | VARCHAR  |
| klasse_id | INT      |
| bruker_id | INT      |

#### klasser

| Felt | Datatype |
| ---- | -------- |
| id   | INT      |
| navn | VARCHAR  |

#### fag

| Felt | Datatype |
| ---- | -------- |
| id   | INT      |
| navn | VARCHAR  |

#### fravaer

| Felt      | Datatype |
| --------- | -------- |
| id        | INT      |
| elev_id   | INT      |
| fag_id    | INT      |
| dato      | DATE     |
| status    | VARCHAR  |
| kommentar | TEXT     |

#### faq_sporsmal

| Felt       | Datatype |
| ---------- | -------- |
| id         | INT      |
| navn       | VARCHAR  |
| epost      | VARCHAR  |
| navn_hash  | VARCHAR  |
| epost_hash | VARCHAR  |
| sporsmal   | TEXT     |
| svar       | TEXT     |
| status     | VARCHAR  |
| er_slettet | BOOLEAN  |

### SQL-eksempel

```sql
CREATE TABLE brukere (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brukernavn VARCHAR(50) UNIQUE,
    passord_hash VARCHAR(255),
    rolle VARCHAR(20)
);
```

---

## 6. Programstruktur

```text
skole_fravaer_system/
│
├── app.py
├── .env
├── requirements.txt
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── elever.html
│   ├── elev_detaljer.html
│   ├── registrer_fravaer.html
│   ├── fravaer.html
│   ├── admin.html
│   └── faq.html
│
├── static/
│   └── style.css
│
└── README.md
```

### Databasestrøm

```text
HTML
 ↓
Flask Route
 ↓
MariaDB
 ↓
Flask
 ↓
HTML-tabell
```

---

## 7. Kodeforklaring

### app.py

Inneholder alle Flask-ruter, databasekoblinger og tilgangskontroll.

### Login

Logger inn brukeren og oppretter session.

### Register

Oppretter nye brukerkontoer.

### Fravær

Viser fravær basert på brukerrolle.

### Admin

Administrerer brukere, elever, roller, FAQ og fravær.

### FAQ

Lar brukere sende inn spørsmål som kan besvares av administrator.

---

## 8. Sikkerhet og pålitelighet

Tiltak som er brukt:

* Passord hashing med Werkzeug
* Session-håndtering
* Rollebasert tilgangskontroll
* Parameteriserte SQL-spørringer
* Miljøvariabler i `.env`
* Anonymisering av FAQ-data
* Begrenset tilgang til admin-funksjoner

---

## 9. Feilsøking og testing

### Typiske feil

* SQL-syntaksfeil
* Feil databasekobling
* Feil brukerroller
* Feil kobling mellom elev og bruker
* Manglende data i tabeller

### Hvordan feilene ble løst

* Analyse av Flask traceback
* Testing av SQL-spørringer
* Kontroll av databasen
* Testing av alle brukerroller

### Testmetoder

* Manuell testing
* Testing av innlogging
* Testing av fraværsregistrering
* Testing av adminfunksjoner
* Testing av FAQ-system

---

## 10. Konklusjon og refleksjon

Gjennom prosjektet lærte jeg:

* Flask-utvikling
* MariaDB og SQL
* Rollebasert tilgangskontroll
* GitHub Projects
* Feilsøking
* Dokumentasjon
* Webutvikling

Det mest utfordrende var å koble sammen brukere, elever, roller og fravær på en sikker måte.

Prosjektet fungerer som et komplett system for registrering og administrasjon av elevfravær.

---

## 11. Kildeliste

* https://www.w3schools.com
* https://flask.palletsprojects.com
* https://mariadb.com/docs
* https://github.com
* https://docs.pylonsproject.org/projects/waitress
