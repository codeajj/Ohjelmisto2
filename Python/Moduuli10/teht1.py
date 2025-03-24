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
            self.nyky_kerros = self.nyky_kerros + 1

    def kerrosAlas(self):
        if self.nyky_kerros > self.kerros_alin:
            self.nyky_kerros = self.nyky_kerros - 1



h = Hissi(1, 10)

h.siirry_kerrokseen(5)
print(f"Hissi on kerroksessa: {h.nyky_kerros}")
h.siirry_kerrokseen(1)
print(f"Hissi on kerroksessa: {h.nyky_kerros}")