from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class PeliTehdas:
    def __init__(self):
        self.__pelit = {
            "a": KPSPelaajaVsPelaaja(),
            "b": KPSTekoaly(),
            "c": KPSParempiTekoaly()
        }

    def luo_peli(self, vastaus):
        if vastaus in self.__pelit:
            return self.__pelit[vastaus]
        else:
            return None