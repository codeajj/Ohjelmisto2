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
            print(f"Liikutaan alas...")
            self.nyky_kerros = self.nyky_kerros - 1

class Talo:
    def __init__(self, alin, ylin, hissi_lkm):
        self.hissit = []
        for i in range(hissi_lkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja(self, hissi_numero, kohde):
        self.hissit[hissi_numero].siirry_kerrokseen(kohde)
        print(f"Hissi {hissi_numero} on kerroksessa {kohde}")

    def palohälytys(self):
        for i, hissi in enumerate(self.hissit): #Ihme koodi pätkä jonka löysin geeksforgeeks.orgista.
            hissi.siirry_kerrokseen(hissi.kerros_alin)
            print(f"Hissi {i} on kerroksessa {hissi.nyky_kerros}")

talo = Talo(1, 10, 5) #Luodaan hissit

#Siirretään hissit
talo.aja(0, 2)
talo.aja(1, 4)
talo.aja(2, 6)
talo.aja(3, 8)
talo.aja(4, 10)

print("\nPalohälytys!\n")
talo.palohälytys()