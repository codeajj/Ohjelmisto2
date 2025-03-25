class Hissi:
    def __init__(self, alin, ylin):
        self.kerros_alin = alin
        self.kerros_ylin = ylin
        self.nyky_kerros = alin

    def siirry_kerrokseen(self, kerrokseen):
        while kerrokseen > self.nyky_kerros:
            self.kerrosYlös()
        while kerrokseen < self.nyky_kerros:
            self.kerrosAlas()

    def kerrosYlös(self):
        if self.nyky_kerros < self.kerros_ylin:
            print(f"Liikutaan ylös...")
            self.nyky_kerros = self.nyky_kerros + 1

    def kerrosAlas(self):
        if self.nyky_kerros > self.kerros_alin:
            print(f"Liikutaan ylös...")
            self.nyky_kerros = self.nyky_kerros - 1

class Talo:
    Hissit = []
    def __init__(self, alin, ylin, hissi_lkm):
        self.hissi_lista = [Hissi(alin, ylin) for i in range(hissi_lkm)]

    def aja(self, hissi_numero, kohde):
        self.hissi_lista[hissi_numero].siirry_kerrokseen(kohde)
        print(f"Hissi {hissi_numero} on kerroksessa {kohde}")

talo = Talo(1, 10, 5)

talo.aja(0, 2)
talo.aja(1, 4)
talo.aja(2, 6)
talo.aja(3, 8)
talo.aja(4, 10)