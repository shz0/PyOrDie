# Starting my Python Journey :D

# trying to make a simple csv storage manager.


class Artikelbezeichnung:
    def __init__(self, artikel=None):
        self._artikel = artikel

    def setze_artikel(self, neuer_artikel):
        if neuer_artikel is None:
            raise ValueError("Der Wert darf nicht None sein.")
        if self.artikel is not None and neuer_artikel == self.artikel:
            print(f"Der Artikel {neuer_artikel} ist bereits vorhanden.")
        else:
            self._artikel = neuer_artikel

    @property
    def artikel(self):
        return self._artikel

# testing
eingabe = Artikelbezeichnung('NDI')
eingabe.setze_artikel("MTO")
eingabe.setze_artikel("NDI")
eingabe.setze_artikel("NDI")