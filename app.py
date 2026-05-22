from flask import Flask, render_template, request, redirect
import mariadb

app = Flask(__name__)


# Databasekobling
# Denne funksjonen brukes hver gang appen skal hente eller lagre data
def get_db_connection():
    return mariadb.connect(
        host="10.200.14.18",
        user="webuser",
        password="*",
        database="skole_fravaer_db",
    )



# Forside
@app.route("/")
def index():
    return render_template("index.html")


# Dashboard med enkel statistikk
@app.route("/dashboard")
def dashboard():
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


# Legg til ny elev
@app.route("/legg-til-elev", methods=["GET", "POST"])
def legg_til_elev():
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
    conn = get_db_connection()
    cursor = conn.cursor()

    # Sletter først fravær som hører til eleven
    cursor.execute("DELETE FROM fravaer WHERE elev_id = ?", (id,))

    # Deretter sletter vi selve eleven
    cursor.execute("DELETE FROM elever WHERE id = ?", (id,))

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/elever")


# Viser detaljer for én elev
@app.route("/elev/<int:id>")
def elev_detaljer(id):
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


# Viser alt registrert fravær
@app.route("/fravaer")
def fravaer():
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

# Enkel admin-side
@app.route("/admin")
def admin():
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
@app.route("/faq")
def faq():
    return render_template("faq.html")


# Starter Flask-appen
if __name__ == "__main__":
    app.run(debug=True)
