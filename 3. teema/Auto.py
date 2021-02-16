class Auto():
    # lihtne auto
    # tootja, mudel, aasta
    def __init__(self, t, m, a):
        self.tootja = t
        self.mudel = m
        self.aasta = a

    def kirjeldus(self):
        pikk_nimi = str(self.aasta) + " " + self.tootja + " " + self.mudel
        return pikk_nimi.title()
