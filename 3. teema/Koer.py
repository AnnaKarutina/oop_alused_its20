class Koer():
    # konstruktor
    def __init__(self, h, v = 0):
        self.hyydnimi = h
        self.vanus = v
        self.saba = True
    # destruktor
    def __del__(self):
        print("Kahjuks {} juba nii vana, et läheb ära".format(self.hyydnimi))
    # meetod
    def kirjeldus(self):
        print("Koer nimega {} on {} aastat vana".format(self.hyydnimi, self.vanus))



