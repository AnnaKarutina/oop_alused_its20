from kuju import Kuju

class Ruut(Kuju):
    def __init__(self, kp):
        self.kylje_pikkus = kp
    def pindala(self):
        return self.kylje_pikkus * self.kylje_pikkus