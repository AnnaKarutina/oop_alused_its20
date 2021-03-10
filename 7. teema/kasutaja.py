class Kasutaja():
    def __init__(self, e, p, kn, parool):
        self.eesnimi = e
        self.perenimi = p
        self.kasutaja_nimi = kn
        self.parool = parool
        self.roll = "tavakasutaja"

    def kirjelda_kasutaja(self):
        print("Eesnimi = " + self.eesnimi)
        print("Perenimi = " + self.perenimi)
        print("Kasutaja nimi = " + self.kasutaja_nimi)
        print("Parool = " + self.parool)
        print("Roll = " + self.roll)

    def tervita_kasutaja(self):
        print("Tere, " + self.eesnimi + " " + self.perenimi + "!")