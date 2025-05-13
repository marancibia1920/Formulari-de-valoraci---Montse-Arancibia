from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="usuari",
        password="P@ssw0rd",
        database="votacions"
    )

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        dni = request.form["dni"].strip()
        poblacion = request.form["poblacion"].strip()
        valoracio = request.form["valoracio"].strip()
        
        conn   = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO votacion (dni, poblacio, valoracio) VALUES (%s, %s, %s)"
        cursor.execute(query, (dni, poblacion, valoracio))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/")

    conn   = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT opcioVotacio FROM opcionsVotacio")
    opciones = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("index.html", opciones=opciones)

@app.route("/votacions")
def votacions():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT dni, poblacio, valoracio FROM votacion")
    opcions = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("votacions.html", opciones=opcions)

if __name__ == "__main__":
    app.run(debug=True)

