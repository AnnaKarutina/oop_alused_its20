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

class Admin(Kasutaja):
    def __init__(self, e, p, kn, parool):
        super().__init__(e, p, kn, parool)
        self.roll = "administraator"
        self.privileegid = Privileegid()

class Privileegid():
    def __init__(self):
        self.privileegid = ["lubatud lisada kasutajad", "lubatud eemaldada kasutajad", "lubatud blokeerida kasutajad"]

    def naita_privileegid(self):
        print("Admini privileegid")
        for privileeg in self.privileegid:
            print(privileeg)