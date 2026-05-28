# Skole-fraværssystem

## Prosjekttittel

**Skole-fraværssystem**

Dette prosjektet er et skoleprosjekt laget i VG2 Informasjonsteknologi. Prosjektet er en webapplikasjon der brukere kan registrere seg, logge inn, se elever, legge til elever, registrere fravær og bruke en FAQ-side.

Systemet er laget med:

- Python
- Flask
- MariaDB
- HTML
- CSS
- JavaScript
- Jinja2

Prosjektet viser hvordan frontend, backend og database kan jobbe sammen i ett system.

---

## 1. Prosjektidé og problemstilling

### Prosjektidé

Prosjektidéen min var å lage et digitalt skole-fraværssystem. Systemet skal gjøre det enklere å holde oversikt over elever og fravær.

I appen kan man registrere elever, legge dem i klasser, registrere fravær i ulike fag og se en samlet oversikt over fraværet. I tillegg har systemet innlogging, registrering av brukere, admin-side og FAQ-side.

### Problemstilling

Problemstillingen for prosjektet er:

**Hvordan kan jeg lage et enkelt og oversiktlig websystem som registrerer og viser skolefravær ved hjelp av Flask, MariaDB, HTML, CSS og JavaScript?**

### Hva applikasjonen gjør

Applikasjonen har disse hovedfunksjonene:

- Forside
- Registrering av bruker
- Innlogging
- Utlogging
- Rollebasert tilgang med admin og vanlig bruker
- Dashboard med enkel statistikk
- Vise alle elever
- Legge til ny elev
- Slette elev
- Se detaljer om én elev
- Registrere fravær
- Vise alt registrert fravær
- Admin-side
- FAQ-side med brukerveiledning
- Brukere kan sende inn spørsmål på FAQ-siden
- Admin kan svare på FAQ-spørsmål
- Admin kan anonymisere personinformasjon

### Hva jeg planla å gjøre

Jeg planla å lage en Flask-applikasjon som kunne kobles til en MariaDB-database. Først måtte jeg lage mappestrukturen, deretter databasen og tabellene. Etter det laget jeg HTML-sidene og koblet dem sammen med Flask-routes.

Etter at grunnsystemet fungerte, la jeg til flere funksjoner som login/register, admin-side, FAQ-system og anonymisering. Jeg jobbet også med CSS for å gjøre systemet mer oversiktlig og responsivt.

---

## 2. Systembeskrivelse

### Formål med applikasjonen

Formålet med applikasjonen er å lage et enkelt digitalt system for registrering av skolefravær. Systemet skal vise at jeg forstår hvordan man bygger en webapplikasjon med backend, database og frontend.

Prosjektet er ikke ment som et ferdig profesjonelt system for en ekte skole, men som et skoleprosjekt som viser kompetanse i systemutvikling, database, sikkerhet, drift og feilsøking.

### Brukerflyt

Brukeren starter på forsiden. Derfra kan brukeren logge inn eller registrere seg.

Når brukeren har logget inn, kan brukeren gå til dashboardet. Dashboardet viser statistikk fra databasen, for eksempel antall elever, antall fravær og antall fag.

Brukeren kan gå til elevsiden for å se alle elever. Der kan brukeren også se detaljer om en elev eller legge til en ny elev.

Når brukeren skal registrere fravær, går brukeren til siden for fraværsregistrering. Der velger brukeren elev, fag, dato, status og skriver eventuelt en kommentar. Når skjemaet sendes inn, lagres dataene i MariaDB.

Brukeren kan også gå til FAQ-siden. Der kan brukeren lese vanlige spørsmål og sende inn egne spørsmål. Admin kan senere svare på disse spørsmålene på FAQ-admin-siden.

### Admin-flyt

Admin logger inn som vanlig, men brukeren må ha rollen `admin` i databasen. Når admin er logget inn, kan admin åpne admin-sidene.

Admin kan se en samlet oversikt over registrert fravær. Admin kan også gå til FAQ-admin-siden og se spørsmål som brukere har sendt inn.

På FAQ-admin-siden kan admin skrive svar på spørsmål. Admin kan også anonymisere personinformasjon slik at navn og e-post ikke vises lenger.

### Teknologier brukt

| Teknologi | Bruk |
|---|---|
| Python | Programmeringsspråk for backend |
| Flask | Webrammeverk for routes, session og templates |
| MariaDB | SQL-database |
| HTML | Struktur på nettsidene |
| CSS | Design og responsivt oppsett |
| JavaScript | Bekreftelse før sletting |
| Jinja2 | Viser data fra Flask i HTML |
| Git/GitHub | Versjonskontroll og dokumentasjon |

---

## 3. Server-, infrastruktur- og nettverksoppsett

### Servermiljø

Prosjektet kjører som en Flask-applikasjon. Flask-appen kjører på PC-en under utvikling, mens MariaDB-databasen kan ligge på en annen maskin/server, for eksempel en Raspberry Pi eller en Linux-server.

Appen kobler seg til MariaDB via IP-adresse.

Eksempel på databasekobling i `app.py`:

```python
def get_db_connection():
    return mariadb.connect(
        host="10.200.14.18",
        user="webuser",
        password="DITT_PASSORD_HER",
        database="skole_fravaer_db",
    )
```

### Nettverksoppsett

I prosjektet kommuniserer Flask-applikasjonen med MariaDB-serveren over nettverket.

En enkel forklaring av flyten er:

```text
Nettleser → Flask-applikasjon → MariaDB-database → Flask-applikasjon → HTML-side
```

Når en bruker åpner en side, sender nettleseren en forespørsel til Flask. Flask henter eller lagrer data i MariaDB og sender deretter en HTML-side tilbake til brukeren.

### IP-adresser

I prosjektet brukes en MariaDB-server med IP-adresse:

```text
10.200.14.18
```

PC-en som kobler til databasen kan ha en annen IP, for eksempel:

```text
10.2.1.128
```

Hvis MariaDB nekter tilgang, kan feilen se slik ut:

```text
Access denied for user 'webuser'@'10.2.1.128'
```

Dette betyr at MariaDB-brukeren ikke har tilgang fra den IP-adressen, eller at passordet er feil.

### Porter

MariaDB bruker vanligvis port:

```text
3306
```

Hvis brannmur blokkerer port 3306, klarer ikke Flask-applikasjonen å koble til databasen.

### Brannmur

For å sjekke brannmurstatus på Linux kan man bruke:

```bash
sudo ufw status
```

Hvis brannmuren blokkerer MariaDB, kan det føre til at applikasjonen ikke får kontakt med databasen.

### Databasebruker og rettigheter

I stedet for å bruke root-brukeren, bruker appen en egen databasebruker:

```text
webuser
```

Dette er bedre fordi applikasjonen bare trenger tilgang til databasen den faktisk bruker.

Eksempel på SQL for å gi tilgang:

```sql
CREATE USER IF NOT EXISTS 'webuser'@'%' IDENTIFIED BY 'DITT_PASSORD_HER';

GRANT ALL PRIVILEGES ON skole_fravaer_db.* TO 'webuser'@'%';

FLUSH PRIVILEGES;
```

`%` betyr at brukeren kan koble til fra andre maskiner. I en mer sikker produksjonsløsning ville man begrenset dette mer.

---

## 4. Prosjektstyring med GitHub Projects / Kanban

Jeg brukte Kanban for å planlegge og strukturere arbeidet. Kanban gjorde det lettere å se hva som var ferdig, hva jeg jobbet med, og hva som fortsatt manglet.

### Kanban-kolonner

Jeg brukte disse kolonnene:

```text
To Do
In Progress
Done
```

Eller på norsk:

```text
Planlagt
Jobber med
Ferdig
```

### Eksempler på Kanban-oppgaver

| Oppgave | Status |
|---|---|
| Planlegge prosjektidé | Ferdig |
| Lage mappestruktur | Ferdig |
| Lage database | Ferdig |
| Koble Flask til MariaDB | Ferdig |
| Lage forside | Ferdig |
| Lage elevliste | Ferdig |
| Lage legg til elev | Ferdig |
| Lage fraværsregistrering | Ferdig |
| Lage dashboard | Ferdig |
| Lage login/register | Ferdig |
| Lage admin-side | Ferdig |
| Lage FAQ-side | Ferdig |
| Lage FAQ-admin | Ferdig |
| Lage anonymisering | Ferdig |
| Skrive README | Ferdig |
| Teste prosjektet | Ferdig |
| Pushe til GitHub | Ferdig |

### Hvordan Kanban hjalp arbeidet

Kanban hjalp meg med å dele prosjektet inn i mindre deler. I stedet for å se på hele prosjektet som én stor oppgave, kunne jeg jobbe med én funksjon av gangen.

Det gjorde det også lettere å dokumentere prosessen. Jeg kunne vise hvilke deler som var planlagt, hvilke deler som var under arbeid, og hva som var ferdig.

---

## 5. Databasebeskrivelse

### Databasenavn

```text
skole_fravaer_db
```

### Tabeller

Prosjektet bruker disse tabellene:

```text
klasser
elever
fag
fravaer
brukere
faq_sporsmal
```

### Oversikt over tabellene

| Tabell | Beskrivelse |
|---|---|
| klasser | Lagrer skoleklasser |
| elever | Lagrer elever |
| fag | Lagrer fag |
| fravaer | Lagrer fraværsregistreringer |
| brukere | Lagrer brukere for login/register |
| faq_sporsmal | Lagrer spørsmål fra FAQ-siden |

### Tabell: klasser

| Felt | Datatype | Beskrivelse |
|---|---|---|
| id | INT | Primærnøkkel |
| navn | VARCHAR(50) | Klassenavn |

### Tabell: elever

| Felt | Datatype | Beskrivelse |
|---|---|---|
| id | INT | Primærnøkkel |
| fornavn | VARCHAR(50) | Elevens fornavn |
| etternavn | VARCHAR(50) | Elevens etternavn |
| klasse_id | INT | Fremmednøkkel til klasser |

### Tabell: fag

| Felt | Datatype | Beskrivelse |
|---|---|---|
| id | INT | Primærnøkkel |
| navn | VARCHAR(100) | Navn på fag |

### Tabell: fravaer

| Felt | Datatype | Beskrivelse |
|---|---|---|
| id | INT | Primærnøkkel |
| elev_id | INT | Fremmednøkkel til elever |
| fag_id | INT | Fremmednøkkel til fag |
| dato | DATE | Dato for fravær |
| status | VARCHAR(50) | Type/status for fravær |
| kommentar | TEXT | Kommentar til fraværet |

### Tabell: brukere

| Felt | Datatype | Beskrivelse |
|---|---|---|
| id | INT | Primærnøkkel |
| brukernavn | VARCHAR(50) | Brukernavn |
| passord_hash | VARCHAR(255) | Hashet passord |
| rolle | VARCHAR(20) | Rolle, for eksempel bruker eller admin |

### Tabell: faq_sporsmal

| Felt | Datatype | Beskrivelse |
|---|---|---|
| id | INT | Primærnøkkel |
| navn | VARCHAR(100) | Navn på personen som sender spørsmål |
| epost | VARCHAR(150) | E-post |
| navn_hash | VARCHAR(255) | Hash av navn ved anonymisering |
| epost_hash | VARCHAR(255) | Hash av e-post ved anonymisering |
| sporsmal | TEXT | Spørsmål fra bruker |
| svar | TEXT | Svar fra admin |
| status | VARCHAR(30) | Status, for eksempel ny, besvart eller slettet |
| er_slettet | BOOLEAN | Viser om personinfo er anonymisert |
| opprettet | DATETIME | Tidspunkt spørsmålet ble opprettet |

### SQL for tabeller

```sql
USE skole_fravaer_db;

CREATE TABLE IF NOT EXISTS klasser (
    id INT AUTO_INCREMENT PRIMARY KEY,
    navn VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS elever (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fornavn VARCHAR(50) NOT NULL,
    etternavn VARCHAR(50) NOT NULL,
    klasse_id INT,
    FOREIGN KEY (klasse_id) REFERENCES klasser(id)
);

CREATE TABLE IF NOT EXISTS fag (
    id INT AUTO_INCREMENT PRIMARY KEY,
    navn VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS fravaer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    elev_id INT NOT NULL,
    fag_id INT NOT NULL,
    dato DATE NOT NULL,
    status VARCHAR(50) NOT NULL,
    kommentar TEXT,
    FOREIGN KEY (elev_id) REFERENCES elever(id),
    FOREIGN KEY (fag_id) REFERENCES fag(id)
);

CREATE TABLE IF NOT EXISTS brukere (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brukernavn VARCHAR(50) NOT NULL UNIQUE,
    passord_hash VARCHAR(255) NOT NULL,
    rolle VARCHAR(20) DEFAULT 'elev'
);

CREATE TABLE IF NOT EXISTS faq_sporsmal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    navn VARCHAR(100),
    epost VARCHAR(150),
    navn_hash VARCHAR(255),
    epost_hash VARCHAR(255),
    sporsmal TEXT NOT NULL,
    svar TEXT,
    status VARCHAR(30) DEFAULT 'ny',
    er_slettet BOOLEAN DEFAULT FALSE,
    opprettet DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Testdata

```sql
INSERT INTO klasser (navn)
VALUES 
('2ITA'),
('2ITB');

INSERT INTO elever (fornavn, etternavn, klasse_id)
VALUES
('Stefanos', 'Gkiokas', 1),
('Sara', 'Olsen', 1),
('Jonas', 'Berg', 2);

INSERT INTO fag (navn)
VALUES
('Informasjonsteknologi'),
('Matematikk'),
('Norsk'),
('Engelsk');
```

---

## 6. Programstruktur

### Mappestruktur

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
```

### Forklaring av filene

| Fil | Beskrivelse |
|---|---|
| app.py | Hovedfilen med Flask-routes, databasekobling, login og funksjoner |
| static/style.css | Design og responsivt oppsett |
| static/script.js | JavaScript for bekreftelse før sletting |
| templates/base.html | Felles HTML-mal med navbar og footer |
| templates/index.html | Forside |
| templates/login.html | Innloggingsside |
| templates/register.html | Registreringsside |
| templates/dashboard.html | Viser statistikk |
| templates/elever.html | Viser alle elever |
| templates/legg_til_elev.html | Skjema for å legge til elev |
| templates/elev_detaljer.html | Detaljer om én elev |
| templates/registrer_fravaer.html | Skjema for fraværsregistrering |
| templates/fravaer.html | Viser alt fravær |
| templates/admin.html | Admin-oversikt |
| templates/faq.html | FAQ-side og skjema for spørsmål |
| templates/admin_faq.html | Admin-side for FAQ-spørsmål |

### Databasestrøm

En typisk datastrøm i prosjektet er:

```text
HTML-skjema → Flask route → MariaDB → Flask → HTML-tabell
```

Eksempel:

1. Brukeren fyller ut skjema for å legge til elev.
2. Skjemaet sendes til Flask med POST.
3. Flask leser data fra `request.form`.
4. Flask kjører en SQL INSERT.
5. MariaDB lagrer eleven.
6. Flask sender brukeren tilbake til elevlisten.
7. Elevlisten henter data fra MariaDB og viser eleven i tabellen.

---

## 7. Kodeforklaring

### Databasekobling

Funksjonen `get_db_connection()` kobler Flask-applikasjonen til MariaDB.

```python
def get_db_connection():
    return mariadb.connect(
        host="10.200.14.18",
        user="webuser",
        password="DITT_PASSORD_HER",
        database="skole_fravaer_db",
    )
```

Denne funksjonen brukes hver gang applikasjonen skal hente eller lagre data.

### Hash-funksjon

```python
def hash_text(text):
    if text is None or text == "":
        return None

    return hashlib.sha256(text.encode()).hexdigest()
```

Denne funksjonen brukes når personinformasjon i FAQ-systemet skal anonymiseres.

### Admin-sjekk

```python
def er_admin():
    return session.get("rolle") == "admin"
```

Denne funksjonen sjekker om brukeren har rollen `admin`.

### Viktige routes

| Route | Hva den gjør |
|---|---|
| `/` | Viser forsiden |
| `/register` | Registrerer ny bruker |
| `/login` | Logger inn bruker |
| `/logout` | Logger ut bruker |
| `/dashboard` | Viser statistikk |
| `/elever` | Viser alle elever |
| `/legg-til-elev` | Legger til ny elev |
| `/slett-elev/<id>` | Sletter elev |
| `/elev/<id>` | Viser detaljer om én elev |
| `/registrer-fravaer` | Registrerer fravær |
| `/fravaer` | Viser alt fravær |
| `/admin` | Admin-oversikt |
| `/faq` | FAQ-side |
| `/admin/faq` | Admin-side for FAQ |
| `/admin/faq/svar/<id>` | Admin svarer på spørsmål |
| `/admin/faq/slett/<id>` | Admin anonymiserer spørsmål |

---

## 8. Sikkerhet og pålitelighet

### Passord-hashing

Passord lagres ikke som vanlig tekst. Når en bruker registrerer seg, blir passordet hashet.

```python
passord_hash = generate_password_hash(passord)
```

Ved innlogging sjekkes passordet slik:

```python
check_password_hash(bruker["passord_hash"], passord)
```

Dette er tryggere enn å lagre passord direkte i databasen.

### Session

Når en bruker logger inn, lagres informasjon i session.

```python
session["bruker_id"] = bruker["id"]
session["brukernavn"] = bruker["brukernavn"]
session["rolle"] = bruker["rolle"]
```

Dette gjør at Flask vet hvem som er logget inn.

### Rollebasert tilgang

Systemet bruker rollen `admin` for å beskytte admin-sider.

```python
if not er_admin():
    return redirect("/dashboard")
```

Vanlige brukere kan ikke åpne admin-sidene.

### Parameteriserte spørringer

Prosjektet bruker parameteriserte SQL-spørringer.

```python
cursor.execute("SELECT * FROM brukere WHERE brukernavn = ?", (brukernavn,))
```

Dette er bedre enn å sette brukerinput direkte inn i SQL-strengen. Det beskytter mot mange typer SQL injection.

### Anonymisering

Når et FAQ-spørsmål anonymiseres, blir navn og e-post byttet ut med:

```text
ANONYMISERT
```

I tillegg lagres hash av navn og e-post. Dette viser at prosjektet tar hensyn til personvern.

### Debug-modus

Under utvikling brukes:

```python
app.run(debug=True)
```

Dette er nyttig for feilsøking. I ekte drift bør debug slås av, fordi debug kan vise sensitiv informasjon.

### Passord i kode

I prosjektet må passordet i `app.py` ikke deles offentlig. I en mer profesjonell løsning ville jeg brukt miljøvariabler, slik at passord ikke ligger direkte i koden.

---

## 9. Feilsøking og testing

### Typiske feil

Underveis i prosjektet møtte jeg flere typer feil.

#### Access denied

Eksempel:

```text
Access denied for user 'webuser'@'10.2.1.128'
```

Dette betyr at MariaDB-brukeren ikke har tilgang fra den IP-adressen, eller at passordet er feil.

Løsning:

- Sjekke passordet i `app.py`
- Sjekke MariaDB-brukeren
- Sjekke host/IP
- Sjekke grants/rettigheter
- Gi brukeren tilgang til databasen

Eksempel:

```sql
GRANT ALL PRIVILEGES ON skole_fravaer_db.* TO 'webuser'@'%';
FLUSH PRIVILEGES;
```

#### Can't connect to server

Eksempel:

```text
Can't connect to server on '10.200.14.18'
```

Dette betyr at Flask ikke får kontakt med MariaDB-serveren.

Mulige årsaker:

- Feil IP-adresse
- MariaDB kjører ikke
- Brannmur blokkerer port 3306
- Serveren er ikke på samme nettverk
- MariaDB lytter bare på localhost

#### TemplateNotFound

Hvis Flask ikke finner en HTML-fil, kan man få `TemplateNotFound`.

Mulige årsaker:

- Filen ligger ikke i `templates`
- Filnavnet er skrevet feil
- Route peker til feil template

#### Manglende tabell

Hvis en tabell ikke finnes i MariaDB, kan appen få feil.

Eksempel:

```text
Table 'skole_fravaer_db.brukere' doesn't exist
```

Løsning:

- Sjekke `SHOW TABLES;`
- Opprette tabellen med riktig SQL
- Sjekke at databasenavnet er riktig

### Testmetoder

Jeg testet prosjektet ved å:

- Starte Flask-appen
- Åpne forsiden i nettleseren
- Registrere bruker
- Logge inn
- Logge ut
- Gjøre bruker til admin i MariaDB
- Åpne admin-sider som admin
- Teste at vanlig bruker ikke får admin-tilgang
- Legge til elever
- Se elevliste
- Se elevdetaljer
- Registrere fravær
- Vise fravær
- Sende inn FAQ-spørsmål
- Svare på FAQ-spørsmål som admin
- Anonymisere FAQ-spørsmål

### Sluttkontroll

Før prosjektet regnes som ferdig, bør dette være testet:

- Appen starter uten feil
- Databasen kobler til
- Login fungerer
- Register fungerer
- Logout fungerer
- Admin-rolle fungerer
- Elevliste fungerer
- Legg til elev fungerer
- Slett elev fungerer
- Fraværsregistrering fungerer
- FAQ-siden fungerer
- FAQ-admin fungerer
- CSS ser ryddig ut
- GitHub har oppdatert kode
- README er ferdig

---

## 10. Drift

### Hva drift betyr i prosjektet

Drift betyr at systemet ikke bare er laget, men at det faktisk kan kjøres og fungere i praksis. Det handler om server, database, nettverk, sikkerhet, tilgang og feilsøking.

I prosjektet viser jeg drift ved at appen kobler til en MariaDB-database over nettverket. Jeg har også jobbet med brukerrettigheter, brannmur, IP-adresse, databasekobling og feilsøking.

### Drift-kompetanse jeg viser

Jeg viser drift-kompetanse gjennom:

- Databasekobling med IP-adresse
- MariaDB-bruker med rettigheter
- Feilsøking av tilgangsfeil
- Brannmur og port-forståelse
- Login og sessions
- Rollebasert tilgangskontroll
- Passord-hashing
- Anonymisering av personinformasjon
- Testing av systemet
- GitHub og versjonskontroll

### Backup

Hvis dette systemet skulle vært brukt i ekte drift, ville backup vært viktig. Da kunne man tatt backup av databasen med:

```bash
mysqldump -u webuser -p skole_fravaer_db > backup.sql
```

Backup gjør at data ikke går tapt hvis databasen blir ødelagt.

### Produksjon

I ekte produksjon burde systemet kjøres med:

- Debug av
- Sterkere secret key
- Miljøvariabler for passord
- Jevnlig backup
- Logging av feil
- Bedre rollefordeling
- HTTPS
- Bedre validering av skjemaer

---

## 11. GitHub og versjonskontroll

Jeg brukte Git og GitHub for å lagre prosjektet og ha kontroll på endringer.

Eksempler på Git-kommandoer:

```bash
git add .
git commit -m "Update project"
git push
```

Hvis GitHub-repoet allerede hadde innhold, kunne man få en `fetch first`-feil. Da kunne løsningen være:

```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

GitHub er nyttig fordi man kan se tidligere versjoner av prosjektet og dokumentere arbeidet.

---

## 12. Videre forbedringer

Prosjektet kan forbedres videre på flere måter.

### Flere roller

Akkurat nå har systemet admin og vanlig bruker. En forbedring kunne vært å ha flere roller:

```text
admin
lærer
elev
```

Da kunne lærere registrert fravær, elever sett sitt eget fravær, og admin styrt hele systemet.

### Redigere elever

Systemet kan forbedres med mulighet til å redigere elever. Da kan man endre navn eller klasse uten å slette eleven.

### Redigere fravær

Systemet kan også få funksjon for å redigere fravær. Det er nyttig hvis noen registrerer feil dato, fag eller status.

### Søk og filter

En annen forbedring er søk og filter. Brukeren kunne søkt etter elever med navn eller filtrert fravær etter dato, klasse eller fag.

### Fraværsprosent

Systemet kunne regnet ut fraværsprosent per elev. Det ville gjort systemet mer realistisk og mer nyttig.

### Bedre sikkerhet

I en mer profesjonell versjon ville jeg brukt miljøvariabler, HTTPS, bedre validering og mer detaljert tilgangskontroll.

---

## 13. Konklusjon og refleksjon

### Hva jeg lærte

I dette prosjektet lærte jeg hvordan man lager en webapplikasjon med Flask og MariaDB. Jeg lærte hvordan HTML-skjemaer sender data til Flask, og hvordan Flask kan lagre data i en SQL-database.

Jeg lærte også mer om SQL. Jeg brukte SELECT, INSERT, UPDATE, DELETE og JOIN. Jeg lærte hvordan PRIMARY KEY og FOREIGN KEY brukes for å koble tabeller sammen.

Jeg lærte også hvordan innlogging fungerer med sessions. I tillegg lærte jeg hvordan passord kan lagres tryggere med hashing.

Jeg fikk også erfaring med drift. Jeg måtte koble appen til en MariaDB-server via IP-adresse, jobbe med databasebruker, rettigheter og feilsøke tilkoblingsfeil.

### Hva fungerte bra

Det som fungerte bra var at prosjektet ble delt opp i tydelige deler. Først laget jeg grunnstrukturen, deretter databasen, og så bygde jeg funksjonene én etter én.

Flask og MariaDB fungerte bra sammen når databasekoblingen var riktig. Det var også nyttig å bruke templates i Flask, fordi alle sidene kunne bruke samme `base.html`.

Login/register og admin-rollen gjorde prosjektet mer realistisk. FAQ-systemet gjorde også prosjektet mer komplett, fordi brukere kan sende inn spørsmål og admin kan svare.

### Hva var utfordrende

Det mest utfordrende var databasekoblingen. Jeg måtte forstå IP-adresse, databasebruker, passord, host og brannmur.

Det var også utfordrende å passe på at tabellnavn og kolonnenavn i MariaDB stemte med koden i Flask. Hvis et navn var feil, fikk appen 500-feil.

En annen utfordring var tilgangskontroll. Først kunne alle innloggede brukere åpne admin-sider, men dette ble forbedret med rollen `admin`.

### Hva jeg ville gjort annerledes

Hvis jeg skulle gjort prosjektet på nytt, ville jeg planlagt rollene tidligere. Da kunne jeg laget admin, lærer og elev fra starten.

Jeg ville også brukt miljøvariabler for passord tidligere, slik at passord ikke måtte ligge direkte i koden under utvikling.

Jeg ville også laget mer feilhåndtering, for eksempel egne feilsider hvis databasen ikke svarer.

### Oppsummering

Prosjektet viser at jeg kan lage en fullstack webapplikasjon med Flask, MariaDB, HTML, CSS og JavaScript. Det viser også at jeg kan jobbe med database, innlogging, roller, admin-sider, FAQ, personvern og drift.

---

## 14. Kildeliste

- Flask dokumentasjon: https://flask.palletsprojects.com
- MariaDB dokumentasjon: https://mariadb.org/documentation/
- W3Schools HTML: https://www.w3schools.com/html/
- W3Schools CSS: https://www.w3schools.com/css/
- W3Schools SQL: https://www.w3schools.com/sql/
- Python dokumentasjon: https://docs.python.org/3/
- GitHub Docs: https://docs.github.com/
