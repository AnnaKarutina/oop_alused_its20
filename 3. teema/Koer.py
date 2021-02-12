class Koer():
    # konstruktor
    def __init__(self, h, v):
        self.hyydnimi = h
        self.vanus = v
    # meetod
    def kirjeldus(self):
        print("Koer nimega {} on {} aastat vana".format(self.hyydnimi, self.vanus))



