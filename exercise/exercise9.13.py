from random import randint


class Dadu:
    def __init__(self, sisi=6):
        self.sisi = sisi

    def lempar_dadu(self):
        print(randint(1, self.sisi), end=" ")


dadu_6 = Dadu()
print("Dadu 6 sisi:")
for lemparan in range(10):
    dadu_6.lempar_dadu()

dadu_10 = Dadu(10)
print("\n\nDadu 10 sisi:")
for lemparan in range(10):
    dadu_10.lempar_dadu()

dadu_20 = Dadu(20)
print("\n\nDadu 20 sisi:")
for lemparan in range(10):
    dadu_20.lempar_dadu()
print()