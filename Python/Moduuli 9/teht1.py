class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus, kuljettumatka):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.kuljettumatka = kuljettumatka
        self.nopeus = nopeus

Auto1 = Auto("ABC-123", "200km/h","0", "0")

print(f"Rekisteri: {Auto1.rekisteri}, huippunopeus {Auto1.huippunopeus}, nopeus {Auto1.nopeus} ja kuljettu matka {Auto1.kuljettumatka}")