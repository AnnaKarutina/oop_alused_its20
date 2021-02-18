from Restoraan import Restoraan
class JaatiseKiosk(Restoraan):
    def __init__(self, n, t):
        super().__init__(n, t)
        self.jaatise_valik = [] # valik on veel tühi
    def naita_jaatise_valik(self):
        jk = 1
        for jaatis in self.jaatise_valik:
            print(str(jk) + " " + jaatis + " jäätis")
            jk += 1
    def lisaJaatisValikusse(self, jaatise_sort):
        self.jaatise_valik.append(jaatise_sort)