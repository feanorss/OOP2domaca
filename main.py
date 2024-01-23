class Kniha:
    def __init__(self, nazov, autor, ISBN, rok):
        self.nazov = nazov
        self.autor = autor
        self.ISBN = ISBN
        self.dostupna = True
        self.rok = rok

    def vypozicaj(self):
        self.dostupna = False

    def __str__(self):
        status = "Dostupna" if self.dostupna else "Nedostupna"
        return f"Kniha: {self.nazov}, Autor: {self.autor}, ISBN: {self.ISBN}, Dostupna: {status}, Rok: {self.rok}"


class Kniznica:
    def __init__(self):
        self.zoznam = []

    def pridaj_knihu(self, kniha):
        self.zoznam.append(kniha)

    def pozicaj_knihu(self, ISBN_knihy):
        for kniha in self.zoznam:
            if (kniha.ISBN == ISBN_knihy):
                kniha.vypozicaj()
                # print(f"Pozical si knihu {kniha.nazov} od {kniha.autor}, ISBN: {kniha.ISBN}, ROK: {kniha.rok}, Status: {kniha.dostupna}")

    def najdi_knihu(self, kniha_nazov):
        for kniha in self.zoznam:
            if kniha.nazov == kniha_nazov:
                return kniha

                # print(f"najdenal si knihu {kniha.nazov} od {kniha.autor}, ISBN: {kniha.ISBN}, ROK: {kniha.rok}, Status: {kniha.dostupna}")

    def vypis(self):
        dostupne_knihy = []
        for kniha in self.zoznam:
            status = "Dostupna" if kniha.dostupna else "Nedostupna"
            dostupne_knihy.append(
                f"Dostupne knihy su: {kniha.nazov} od {kniha.autor}, ISBN: {kniha.ISBN}, ROK: {kniha.rok}, Status: {status}")
        return dostupne_knihy
        # print(f"Dostupne knihy su: {kniha.nazov} od {kniha.autor}, ISBN: {kniha.ISBN}, ROK: {kniha.rok}, Status: {kniha.dostupna}, ")


kniha1 = Kniha("Harry Potter", "Rowlingova", 123, 1923)
kniha2 = Kniha("Pan prstenov", "Tolkien", 222, 2005)
kniha3 = Kniha("Kniha", "Milos", 333, 1995)

kniznica = Kniznica()
kniznica.pridaj_knihu(kniha1)
kniznica.pridaj_knihu(kniha2)
kniznica.pridaj_knihu(kniha3)
kniznica.pozicaj_knihu(123)
print(kniha1)
print(kniha2)
print("---------")
result = kniznica.vypis()
for i in result:
    print(i)

# kniznica.vypis()