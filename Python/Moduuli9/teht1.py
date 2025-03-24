class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.kuljettumatka = 0
        self.nopeus = 0

Auto1 = Auto("ABC-123", "200km/h")

print(f"Rekisteri: {Auto1.rekisteri}, huippunopeus {Auto1.huippunopeus}, nopeus {Auto1.nopeus} ja kuljettu matka {Auto1.kuljettumatka}")