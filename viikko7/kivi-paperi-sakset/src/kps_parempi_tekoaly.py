from kivi_paperi_sakset import KiviPaperiSakset
#from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, _ensimmaisen_siirto):
        tietokoneen_siirto = self.tekoaly.anna_siirto() 
        print(f"Tietokone valitsi: {tietokoneen_siirto}")
        self.tekoaly.aseta_siirto(_ensimmaisen_siirto)
        return tietokoneen_siirto

#    def pelaa(self):
#        tuomari = Tuomari()
#        tekoaly = TekoalyParannettu(10)

#        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
#        tokan_siirto = tekoaly.anna_siirto()

#        print(f"Tietokone valitsi: {tokan_siirto}")

#        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
#            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
#            print(tuomari)

#            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
#            tokan_siirto = tekoaly.anna_siirto()

#            print(f"Tietokone valitsi: {tokan_siirto}")
#            tekoaly.aseta_siirto(ekan_siirto)

#        print("Kiitos!")
#        print(tuomari)

#    def _onko_ok_siirto(self, siirto):
#        return siirto == "k" or siirto == "p" or siirto == "s"
