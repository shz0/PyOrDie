class Artikelbezeichnung:
    def __init__(self, artikel=None, lagerort=None):
        self._artikel = artikel
        self._lagerort = lagerort

    def set_artikel(self, neuer_artikel):
        print(f'{neuer_artikel} wurde eingelagert')
        if neuer_artikel is None:
            raise ValueError("Der Wert darf nicht None sein.")
        if self.artikel is not None and neuer_artikel == self.artikel:
            print(f"Der Artikel {neuer_artikel} ist bereits vorhanden.")
        else:
            self._artikel = neuer_artikel

    def set_lagerort(self, neuer_lagerort):
        match neuer_lagerort:
            case 1 | 2 | 3 | 4:
                self._lagerort = neuer_lagerort
            case _:
                raise ValueError('Nur Lagerort 1 - 4 verfügbar')

    @property
    def artikel(self):
        return self._artikel

    @property
    def lagerort(self):
        return self._lagerort

# testing artikel
eingabe = Artikelbezeichnung('NDI')
eingabe.set_artikel("MTO")
eingabe.set_artikel("NDI")
eingabe.set_artikel("NDI")

# testing lagerort
eingabe.set_lagerort(4)
