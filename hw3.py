"""
Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
○ __init__ : instanțiem numărător și numitor
○ __str__ : afisam "numărător/numitor"
○ __add__ : returnam o noua fractie care reprezinta adunarea
○ __sub__: returnam o nouă fracție care reprezinta scădearea
○ inverse: returnează o nouă fracție (inversa fracției)
"""

class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f'{self.numarator}/{self.numitor}'

    def __add__(self, other):
        new_numarator = self.numarator * other.numitor + other.numarator * self.numitor
        new_numitor = self.numitor * other.numitor
        return Fractie(new_numarator, new_numitor)

    def __sub__(self, other):
        new_numarator = self.numarator * other.numitor - other.numarator * self.numitor
        new_numitor = self.numitor * other.numitor
        return Fractie(new_numarator, new_numitor)

    def inverse(self):
        try:
            inversed = Fractie(self.numitor, self.numarator)
        except ZeroDivisionError:
            print("division by 0")
            inversed = None
        return inversed

fractie1 = Fractie(2, 3)
fractie2 = Fractie(5, 7)

print("fractie1: ", fractie1)
print("fractie2: ", fractie2)

sum_fractie = fractie1 + fractie2
print("sum: ", sum_fractie)

diff_fractie = fractie1 - fractie2
print("difference: ", diff_fractie)

inverse_fractie1 = fractie1.inverse()
print("inverse of fractie1: ", inverse_fractie1)