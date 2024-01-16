class Kniha:
    def __init__(self, nazov, autor, ISBN, dostupna, rok):
        self.nazov = nazov
        self.autor = autor
        self.ISBN = ISBN
        self.dostupna = True
        self.rok = rok

    def vypozicaj(self):
        self.dostupna = False

class Kniznica:
    def __init__(self):
        self.zoznam = []

    def pridaj_knihu(self, kniha):
        self.zoznam.append(kniha)

    def pozicaj_knihu(self, kniha):
        for kniha in self.zoznam:
            if (kniha.ISBN == ISBN_knihy):
                kniha.vypozicaj()