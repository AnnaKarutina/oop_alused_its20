class Restoraan():
    # konstruktor
    def __init__(self, n, t):
        self.restoraani_nimi = n
        self.soogi_tyyp = t
    # meetodid
    def restoraani_kirjeldus(self):
        print("Restoraan " + str(self.restoraani_nimi) + ", söögi tüüp " + str(self.soogi_tyyp))

    def ava_restoraan(self):
        print("Restoraan on avatud")