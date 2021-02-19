from kuju import Kuju

class Ring(Kuju):
    def __init__(self, r):
        self.raadius = r
    def pindala(self):
        return 3.14 * self.raadius * self.raadius