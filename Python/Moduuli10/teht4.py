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


class Kilpailu:

    def __init__(self):
        self.kilpailu_nimi = "Suuri Romuralli"
        self.pituus = 8000
        self.Autot = []

        for i in range(10):
            huippunopeus = random.randint(100, 200)
            self.Autot.append(Auto(f"ABC {i + 1}", huippunopeus))

    def tunti_kului(self):
        for auto in self.Autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kuljettu(1)

    def kisa_tilanne(self):
        self.Autot.sort(key=lambda a: a.kuljettumatka, reverse=True)
        print(f"Rekisteri: {Auto.rekisteri}, huippunopeus: {Auto.huippunopeus}km/h, nopeus: {Auto.nopeus}km/h, kulkenut: {Auto.kuljettumatka}km")

Kilpailu.tunti_kului(Kilpailu())