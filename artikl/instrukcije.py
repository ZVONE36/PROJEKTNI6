from .usluga import Usluga
from .artikl import Artikl

class Instrukcije(Artikl, Usluga):
    def __init__(self, naslov, opis, cijena):
        super().__init__(naslov, opis, cijena)

    def cijena_po_satu(self):
        cijena_po_satu = self.cijena/30
        return cijena_po_satu

    def ispis(self):
        print("Info o instrukcijama:")
        print(f"\t Naslov: {self.naslov}")
        print(f"\t Opis: {self.opis}")
        print(f"\t Cijena po satu: {self.cijena_po_satu()}")