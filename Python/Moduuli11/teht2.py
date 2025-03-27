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


class Sähköauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akkukapasiteetti):
        self.mittari = akkukapasiteetti
        super().__init__(rekisteri, huippunopeus)

class Bensa_auto(Auto):
    def __init__(self, rekisteri, huippunopeus, litrat):
        self.mittari = litrat
        super().__init__(rekisteri, huippunopeus)

Autot = [Sähköauto("ABC-1", "250km/h", 78.25), Bensa_auto("ABC-2", "250km/h", 120)]

print("Autot kulki kolme tuntia\n")
for a in Autot:
    a.kiihdytä(75)
    a.kuljettu(3)
    a.mittari = a.mittari/3
    if a.rekisteri == "ABC-1":
        print(f"Sähköauto\nRekisteri {a.rekisteri} ja mittarilukema {a.mittari:.2f} kWh\n")
    if a.rekisteri == "ABC-2":
        print(f"Bensa auto\nRekisteri {a.rekisteri} ja mittarilukema {a.mittari:.2f} litraa")