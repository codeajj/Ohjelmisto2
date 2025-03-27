class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumäärä):
        self.kirjailija = kirjailija
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tiedot(self):
        print(f"Julkaisu {self.nimi}, kirjailija {self.kirjailija} pituus {self.sivumäärä}")
        return

class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        self.toimittaja = toimittaja
        super().__init__(nimi)

    def tiedot(self):
        print(f"Julkaisu {self.nimi} ja päätoimittaja {self.toimittaja}")
        return

Julkaisut = [Kirja("Hytti no6", "Rosa Liksom", "200"), Lehti("Aku Ankka", "Aki Hyyppä")]

for j in Julkaisut:
    j.tiedot()