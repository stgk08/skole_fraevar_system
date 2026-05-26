from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import mariadb
import hashlib

app = Flask(__name__)

# Brukes for login-session
app.secret_key = "superhemmeligkey123"

# Databasekobling
def get_db_connection():
    return mariadb.connect(
        host="10.200.14.18",
        user="webuser",
        password="IMIKuben1337!",
        database="skole_fravaer_db",
    )


# Gjør tekst om til hash
def hash_text(text):
    if text is None or text == "":
        return None

    return hashlib.sha256(text.encode()).hexdigest()


# Sjekker om brukeren er admin
def er_admin():
    return session.get("rolle") == "admin"


# Forside
@app.route("/")
def index():
    return render_template("index.html")


# Registrer bruker
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        brukernavn = request.form["brukernavn"]
        passord = request.form["passord"]

        passord_hash = generate_password_hash(passord)

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("""
                INSERT INTO brukere (brukernavn, passord_hash, rolle)
                VALUES (?, ?, ?)
            """, (brukernavn, passord_hash, "bruker"))

            conn.commit()

            cursor.close()
            conn.close()

            return redirect("/login")

        except mariadb.IntegrityError:
            cursor.close()
            conn.close()

            return render_template(
                "register.html",
                error="Brukernavnet finnes allerede."
            )

    return render_template("register.html")


# Logg inn
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        brukernavn = request.form["brukernavn"]
        passord = request.form["passord"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM brukere
            WHERE brukernavn = ?
        """, (brukernavn,))

        bruker = cursor.fetchone()

        cursor.close()
        conn.close()

        if bruker and check_password_hash(bruker["passord_hash"], passord):
            session["bruker_id"] = bruker["id"]
            session["brukernavn"] = bruker["brukernavn"]
            session["rolle"] = bruker["rolle"]

            return redirect("/dashboard")

        return render_template(
            "login.html",
            error="Feil brukernavn eller passord."
        )

    return render_template("login.html")


# Logg ut
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# Dashboard
@app.route("/dashboard")
def dashboard():
    if "bruker_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS antall_elever FROM elever")
    antall_elever = cursor.fetchone()["antall_elever"]

    cursor.execute("SELECT COUNT(*) AS antall_fravaer FROM fravaer")
    antall_fravaer = cursor.fetchone()["antall_fravaer"]

    cursor.execute("SELECT COUNT(*) AS antall_fag FROM fag")
    antall_fag = cursor.fetchone()["antall_fag"]

    cursor.close()
    conn.close()

    return render_template(
        "dashboard.html",
        antall_elever=antall_elever,
        antall_fravaer=antall_fravaer,
        antall_fag=antall_fag
    )


# Viser alle elever
@app.route("/elever")
def elever():
    if "bruker_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            elever.id,
            elever.fornavn,
            elever.etternavn,
            klasser.navn AS klasse
        FROM elever
        JOIN klasser ON elever.klasse_id = klasser.id
        ORDER BY elever.id DESC
    """)

    elever_liste = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("elever.html", elever=elever_liste)


# Legg til elev
@app.route("/legg-til-elev", methods=["GET", "POST"])
def legg_til_elev():
    if "bruker_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        fornavn = request.form["fornavn"]
        etternavn = request.form["etternavn"]
        klasse_id = request.form["klasse_id"]

        cursor.execute("""
            INSERT INTO elever (fornavn, etternavn, klasse_id)
            VALUES (?, ?, ?)
        """, (fornavn, etternavn, klasse_id))

        conn.commit()

        cursor.close()
        conn.close()

        return redirect("/elever")

    cursor.execute("SELECT * FROM klasser ORDER BY navn")
    klasser = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("legg_til_elev.html", klasser=klasser)


# Slett elev
@app.route("/slett-elev/<int:id>")
def slett_elev(id):
    if "bruker_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM fravaer WHERE elev_id = ?", (id,))
    cursor.execute("DELETE FROM elever WHERE id = ?", (id,))

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/elever")


# Elevdetaljer
@app.route("/elev/<int:id>")
def elev_detaljer(id):
    if "bruker_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            elever.id,
            elever.fornavn,
            elever.etternavn,
            klasser.navn AS klasse
        FROM elever
        JOIN klasser ON elever.klasse_id = klasser.id
        WHERE elever.id = ?
    """, (id,))

    elev = cursor.fetchone()

    cursor.execute("""
        SELECT 
            fag.navn AS fag,
            fravaer.dato,
            fravaer.status,
            fravaer.kommentar
        FROM fravaer
        JOIN fag ON fravaer.fag_id = fag.id
        WHERE fravaer.elev_id = ?
        ORDER BY fravaer.dato DESC
    """, (id,))

    fravaer_liste = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "elev_detaljer.html",
        elev=elev,
        fravaer=fravaer_liste
    )


# Registrer fravær
@app.route("/registrer-fravaer", methods=["GET", "POST"])
def registrer_fravaer():
    if "bruker_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        elev_id = request.form["elev_id"]
        fag_id = request.form["fag_id"]
        dato = request.form["dato"]
        status = request.form["status"]
        kommentar = request.form["kommentar"]

        cursor.execute("""
            INSERT INTO fravaer (elev_id, fag_id, dato, status, kommentar)
            VALUES (?, ?, ?, ?, ?)
        """, (elev_id, fag_id, dato, status, kommentar))

        conn.commit()

        cursor.close()
        conn.close()

        return redirect("/fravaer")

    cursor.execute("""
        SELECT 
            elever.id,
            elever.fornavn,
            elever.etternavn,
            klasser.navn AS klasse
        FROM elever
        JOIN klasser ON elever.klasse_id = klasser.id
        ORDER BY elever.fornavn
    """)

    elever_liste = cursor.fetchall()

    cursor.execute("SELECT * FROM fag ORDER BY navn")
    fag_liste = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "registrer_fravaer.html",
        elever=elever_liste,
        fag=fag_liste
    )


# Viser alt fravær
@app.route("/fravaer")
def fravaer():
    if "bruker_id" not in session:
        return redirect("/login")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            fravaer.id,
            elever.fornavn,
            elever.etternavn,
            fag.navn AS fag,
            fravaer.dato,
            fravaer.status,
            fravaer.kommentar
        FROM fravaer
        JOIN elever ON fravaer.elev_id = elever.id
        JOIN fag ON fravaer.fag_id = fag.id
        ORDER BY fravaer.dato DESC
    """)

    fravaer_liste = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("fravaer.html", fravaer=fravaer_liste)


# Admin-side
@app.route("/admin")
def admin():
    if "bruker_id" not in session:
        return redirect("/login")

    if not er_admin():
        return redirect("/dashboard")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            fravaer.id,
            elever.fornavn,
            elever.etternavn,
            fag.navn AS fag,
            fravaer.dato,
            fravaer.status,
            fravaer.kommentar
        FROM fravaer
        JOIN elever ON fravaer.elev_id = elever.id
        JOIN fag ON fravaer.fag_id = fag.id
        ORDER BY fravaer.dato DESC
    """)

    fravaer_liste = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("admin.html", fravaer=fravaer_liste)


# FAQ-side
@app.route("/faq", methods=["GET", "POST"])
def faq():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        navn = request.form["navn"]
        epost = request.form["epost"]
        sporsmal = request.form["sporsmal"]

        cursor.execute("""
            INSERT INTO faq_sporsmal (navn, epost, sporsmal, status)
            VALUES (?, ?, ?, ?)
        """, (navn, epost, sporsmal, "ny"))

        conn.commit()

        cursor.close()
        conn.close()

        return redirect("/faq")

    cursor.execute("""
        SELECT id, sporsmal, svar, status
        FROM faq_sporsmal
        WHERE status = 'besvart'
        ORDER BY opprettet DESC
    """)

    faq_liste = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("faq.html", faq_liste=faq_liste)


# Admin FAQ-side
@app.route("/admin/faq")
def admin_faq():
    if "bruker_id" not in session:
        return redirect("/login")

    if not er_admin():
        return redirect("/dashboard")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM faq_sporsmal
        ORDER BY opprettet DESC
    """)

    sporsmal_liste = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("admin_faq.html", sporsmal=sporsmal_liste)


# Admin svarer på FAQ-spørsmål
@app.route("/admin/faq/svar/<int:id>", methods=["POST"])
def svar_faq(id):
    if "bruker_id" not in session:
        return redirect("/login")

    if not er_admin():
        return redirect("/dashboard")

    svar = request.form["svar"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE faq_sporsmal
        SET svar = ?, status = 'besvart'
        WHERE id = ?
    """, (svar, id))

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/admin/faq")


# Admin anonymiserer FAQ-spørsmål
@app.route("/admin/faq/slett/<int:id>")
def slett_faq(id):
    if "bruker_id" not in session:
        return redirect("/login")

    if not er_admin():
        return redirect("/dashboard")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT navn, epost
        FROM faq_sporsmal
        WHERE id = ?
    """, (id,))

    person = cursor.fetchone()

    if person:
        navn_hash = hash_text(person["navn"])
        epost_hash = hash_text(person["epost"])

        cursor.execute("""
            UPDATE faq_sporsmal
            SET 
                navn = 'ANONYMISERT',
                epost = 'ANONYMISERT',
                navn_hash = ?,
                epost_hash = ?,
                er_slettet = TRUE,
                status = 'slettet'
            WHERE id = ?
        """, (navn_hash, epost_hash, id))

        conn.commit()

    cursor.close()
    conn.close()

    return redirect("/admin/faq")


# Starter appen
if __name__ == "__main__":
    app.run(debug=True)
