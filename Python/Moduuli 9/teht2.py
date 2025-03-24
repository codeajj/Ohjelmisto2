import time

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

Auto1 = Auto("ABC-123", "200km/h")

kmh = 30
Auto1.kiihdytä(kmh)
print(f"Auton rekisteri: {Auto1.rekisteri}, huippunopeus {Auto1.huippunopeus}, nopeus {Auto1.nopeus}km/h ja kuljettu matka {Auto1.kuljettumatka}")
time.sleep(1)
kmh = kmh + 70
Auto1.kiihdytä(kmh)
print(f"Auton rekisteri: {Auto1.rekisteri}, huippunopeus {Auto1.huippunopeus}, nopeus {Auto1.nopeus}km/h ja kuljettu matka {Auto1.kuljettumatka}")
time.sleep(1)
kmh = kmh + 50
Auto1.kiihdytä(kmh)
print(f"Auton rekisteri: {Auto1.rekisteri}, huippunopeus {Auto1.huippunopeus}, nopeus {Auto1.nopeus}km/h ja kuljettu matka {Auto1.kuljettumatka}")
time.sleep(1)
kmh = - 200
Auto1.kiihdytä(kmh)
print(f"Auton rekisteri: {Auto1.rekisteri}, huippunopeus {Auto1.huippunopeus}, nopeus {Auto1.nopeus}km/h ja kuljettu matka {Auto1.kuljettumatka}")