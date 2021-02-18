from Restoraan import Restoraan
class JaatiseKiosk(Restoraan):
    def __init__(self, n, t, v):
        super().__init__(n, t)
        self.jaatise_valik = v
    def naita_jaatise_valik(self):
        jk = 1
        for jaatis in self.jaatise_valik:
            print(str(jk) + " " + jaatis + " jäätis")
            jk += 1