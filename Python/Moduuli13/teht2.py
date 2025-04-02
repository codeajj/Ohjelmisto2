from flask import Flask
import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",
    port = 3306,
    database="Flight",
    user="root",
    passwd="13522",
    autocommit = True
    )

def hae_icao(gps):
    sql = f"select gps_code from airport where gps_code = '{gps}';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    return tulos

def hae_nimi(gps):
    sql = f"select name from airport where gps_code = '{gps}';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    return tulos

def hae_kunta(gps):
    sql = f"select Municipality from airport where gps_code = '{gps}';"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    return tulos

app = Flask(__name__)

@app.route("/kenttä/<ICAO>")
def kenttä(ICAO):
    gps = hae_icao(ICAO)
    nimi = hae_nimi(ICAO)
    kunta = hae_kunta(ICAO)

    vastaus = {
        "ICAO": gps[0][0],
        "Name": nimi[0][0],
        "Municipality": kunta[0][0]
        }
    return vastaus

if __name__ == "__main__":
    app.run(use_reloader=True, host="0.0.0.0", port=5000)