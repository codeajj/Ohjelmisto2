class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.kuljettumatka = 0
        self.nopeus = 0

    def kiihdytä(self, kmh):
            self.nopeus = + kmh
            if self.nopeus < 0:
                self.nopeus = 0
            return

    def kuljettu(self, hours):
        self.kuljettumatka = self.kuljettumatka + (self.nopeus * hours)
        return

Auto1 = Auto("ABC-123", "200km/h")

kmh = 30
Auto1.kiihdytä(kmh)
Auto1.kuljettu(1.5)
print(f"Auton rekisteri: {Auto1.rekisteri}, huippunopeus {Auto1.huippunopeus}, nopeus {Auto1.nopeus}km/h ja kuljettu matka {Auto1.kuljettumatka:.0f}")

kmh = kmh + 70
Auto1.kiihdytä(kmh)
Auto1.kuljettu(1)
print(f"Auton rekisteri: {Auto1.rekisteri}, huippunopeus {Auto1.huippunopeus}, nopeus {Auto1.nopeus}km/h ja kuljettu matka {Auto1.kuljettumatka:.0f}")

kmh = kmh + 50
Auto1.kiihdytä(kmh)
Auto1.kuljettu(1)
print(f"Auton rekisteri: {Auto1.rekisteri}, huippunopeus {Auto1.huippunopeus}, nopeus {Auto1.nopeus}km/h ja kuljettu matka {Auto1.kuljettumatka:.0f}")

kmh = - 200
Auto1.kiihdytä(kmh)
print(f"Auton rekisteri: {Auto1.rekisteri}, huippunopeus {Auto1.huippunopeus}, nopeus {Auto1.nopeus}km/h ja kuljettu matka {Auto1.kuljettumatka:.0f}")

kmh = + 90
Auto1.kiihdytä(kmh)
Auto1.kuljettu(1)
print(f"Auton rekisteri: {Auto1.rekisteri}, huippunopeus {Auto1.huippunopeus}, nopeus {Auto1.nopeus}km/h ja kuljettu matka {Auto1.kuljettumatka:.0f}")