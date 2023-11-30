KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        #if kapasiteetti is None:
        #    self.kapasiteetti = KAPASITEETTI
        #elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
        #    raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        #else:
        #    self.kapasiteetti = kapasiteetti

        #if kasvatuskoko is None:
        #    self.kasvatuskoko = OLETUSKASVATUS
        #elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
        #    raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        #else:
        #    self.kasvatuskoko = kasvatuskoko

        self.kapasiteetti = kapasiteetti if kapasiteetti is not None else KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko if kasvatuskoko is not None else OLETUSKASVATUS

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        # tarkistaa onko luku n listassa
        return n in self.ljono    

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = n
            self.alkioiden_lkm += 1
            return True

        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                self._kasvata_tietorakennetta()

            return True

        return False

    def _kasvata_tietorakennetta(self):
        taulukko_vanha = self.ljono
        self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(taulukko_vanha, self.ljono)

    def poista(self, n):
        # poistaa luvun n listasta, jos löytyy ja päivittää listan pituuden
        if n in self.ljono:
            self.ljono.remove(n)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True
        return False
   
    def kopioi_lista(self, lahde, kohde):
        for i in range(0, len(lahde)):
            kohde[i] = lahde[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return list(self.ljono[:self.alkioiden_lkm])

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        
        x = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        y = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(joukko_a, joukko_b):
        z = IntJoukko()
        a_taulu = joukko_a.to_int_list()
        b_taulu = joukko_b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
