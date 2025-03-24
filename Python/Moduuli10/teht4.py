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
    def __init__(self, auto):
        self.kilpailu_nimi = "Suuri Romuralli"
        self.pituus = 8000

        self.autolista = []
        for i in range(10):
            auto.huippunopeus = random.randint(100, 200)
            self.autolista.append(Auto(f"ABC {i + 1}", auto.huippunopeus))

    def tunti_kului(self, kmh):
        auto.kiihdytä()

    def tilanne(self):
        for auto in self.autolista:
            print(f"Rekisteri: {auto.rekisteri}, huippunopeus: {auto.huippunopeus}km/h, nopeus: {auto.nopeus}km/h, kulkenut: {auto.kuljettumatka}km")

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.kuljettumatka >= self.pituus:
                Kisa_loppunut = True
        return Kisa_loppunut



        self.autolista.sort(key=lambda a: a.kuljettumatka, reverse=True)
        for auto in self.autolista:
            print(
                f"Rekisteri: {auto.rekisteri}, huippunopeus: {auto.huippunopeus}km/h, nopeus: {auto.nopeus}km/h, kulkenut: {auto.kuljettumatka}km")

Kisa_loppunut = False
while Kisa_loppunut:
    for auto in Kilpailu.autolista:
        auto.kiihdytä(random.randint(-10, 15))
        Kilpailu.tunti_kului(1)