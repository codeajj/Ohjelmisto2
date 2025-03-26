import random

from geopy.distance import lonlat


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


class Kilpailu:
    autolista = []

    def __init__(self):
        self.kilpailu_nimi = "Suuri Romuralli"
        self.pituus = 8000

        self.autolista = []
        for i in range(10):
            auto.huippunopeus = random.randint(100, 200)
            self.autolista.append(Auto(f"ABC {i + 1}", auto.huippunopeus))

    def tunti_kului(self):
        auto.kiihdytä(random.randint(-10, 15))
        auto.kuljettu(1)

    def tilanne(self):
        for Auto.auto in self.autolista:
            Kilpailu.autolista.sort(key=lambda a: a.kuljettumatka, reverse=True)
            print(f"Rekisteri: {auto.rekisteri}, huippunopeus: {auto.huippunopeus}km/h, nopeus: {auto.nopeus}km/h, kulkenut: {auto.kuljettumatka}km")

    def kilpailu_ohi(self):
        if auto.kuljettumatka >= self.pituus:
            Kisa_loppunut = True
        else: Kisa_loppunut = False
        return Kisa_loppunut


Kisa_loppunut = False
while not Kisa_loppunut:
    for auto in Kilpailu.autolista:
        Kilpailu.tunti_kului(auto)
        Kilpailu.tilanne(auto)
        if auto.kuljettumatka >= 8000:
            Kilpailu.kilpailu_ohi(auto)

Kilpailu.autolista.sort(key=lambda a: a.kuljettumatka, reverse=True)
for auto in Kilpailu.autolista:
    print(f"Rekisteri: {auto.rekisteri}, huippunopeus: {auto.huippunopeus}km/h, nopeus: {auto.nopeus}km/h, kulkenut: {auto.kuljettumatka}km")