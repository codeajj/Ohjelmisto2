import random


class Auto:

    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.kuljettumatka = 0
        self.nopeus = 0

    def kiihdytä(self, kmh):
        self.nopeus = self.nopeus + kmh
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        return

    def kuljettu(self, hours):
        self.kuljettumatka = self.kuljettumatka + (self.nopeus * hours)
        return


Autot = []

for i in range(10):
    huippunopeus = random.randint(100, 200)
    Autot.append(Auto(f"ABC {i + 1}", huippunopeus))

kisa = True
while kisa:
    for auto in Autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kuljettu(1)
        if auto.kuljettumatka >= 10000:
            kisa = False

Autot.sort(key=lambda a: a.kuljettumatka, reverse=True)
for auto in Autot:
    print(
        f"Rekisteri: {auto.rekisteri}, huippunopeus: {auto.huippunopeus}km/h, nopeus: {auto.nopeus}km/h, kulkenut: {auto.kuljettumatka}km")
