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

    def __init__(self, kilpailun_nimi, pituus):
        self.kilpailu_nimi = kilpailun_nimi
        self.pituus = pituus
        self.Autot = []

        for i in range(10):
            huippunopeus = random.randint(100, 200)
            self.Autot.append(Auto(f"ABC {i + 1}", huippunopeus))

    def tunti_kului(self):
        for auto in self.Autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kuljettu(1)

    def kisa_tilanne(self):
        print(f"\n{'Rekisteri':<10} {'Huippunopeus':<15} {'Nopeus':<10} {'Kulkenut':<10}")
        for auto in self.Autot:
            self.Autot.sort(key=lambda a: a.kuljettumatka, reverse=True)
            print(f"{auto.rekisteri:<10} {auto.huippunopeus:<15} {auto.nopeus:<10} {auto.kuljettumatka:<10}")

    def kilpailu_ohi(self):
        return any(auto.kuljettumatka >= self.pituus for auto in self.Autot)

kilpailu = Kilpailu("Suuri Romuralli", 8000)
tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kului()
    tunnit +=1
    if tunnit % 10 == 0:
        print(f"\nTunnin {tunnit} tilanne:")
        kilpailu.kisa_tilanne()

print("\nKilpailu päättyi!")
kilpailu.kisa_tilanne()