from kuju import Kuju

class Kolmnurk(Kuju):
    def __init__(self, ap, h):
        self.aluse_pikkus = ap
        self.korgus = h
    def pindala(self):
        return (self.aluse_pikkus * self.korgus) / 2