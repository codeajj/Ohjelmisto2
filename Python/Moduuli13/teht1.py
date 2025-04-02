from flask import Flask

app = Flask(__name__)

@app.route("/alkuluku/<int:luku>")
def alkuluku(luku):
    prime = luku
    määrä = 2

    for i in range(1, prime + 1):
        if prime % i == 0:
            määrä -= 1

    if määrä < 0:
        vastaus = {
            "Number": prime,
            "isPrime": False
        }
    else:
        vastaus = {
            "Number": prime,
            "isPrime": True
        }
    return vastaus

if __name__ == "__main__":
    app.run(use_reloader=True, host="0.0.0.0", port=5000)