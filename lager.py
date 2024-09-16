class Artikelbezeichnung:
    def __init__(self, artikel=None, lagerort=None):
        self._artikel = artikel
        self._lagerort = lagerort

    def set_artikel(self, neuer_artikel):
        if neuer_artikel is None:
            raise ValueError("Der Wert darf nicht None sein.")
        if self.artikel is not None and neuer_artikel == self.artikel:
            print(f"Der Artikel {neuer_artikel} ist bereits vorhanden.")
        else:
            self._artikel = neuer_artikel

    def set_lagerort(self, neuer_lagerort):
        if neuer_lagerort is not None and not 1 <= neuer_lagerort <= 4:
            raise ValueError('Lagerort 1 - 4 verfügbar')
        self._lagerort = neuer_lagerort

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
eingabe.set_lagerort(6)  # raising Error!