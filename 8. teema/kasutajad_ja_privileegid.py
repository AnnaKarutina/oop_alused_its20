class Kasutaja():
    """Kasutaja kirjeldav klass"""
    def __init__(self, e, p, kn, parool):
        """Kasutaja loomisel kasutatav konstruktor"""
        self.eesnimi = e
        self.perenimi = p
        self.kasutaja_nimi = kn
        self.parool = parool
        self.roll = "tavakasutaja"

    def kirjelda_kasutaja(self):
        """Kasutaja kirjeldus"""
        print("Eesnimi = " + self.eesnimi)
        print("Perenimi = " + self.perenimi)
        print("Kasutaja nimi = " + self.kasutaja_nimi)
        print("Parool = " + self.parool)
        print("Roll = " + self.roll)

    def tervita_kasutaja(self):
        """Kasutaja tervitus"""
        print("Tere, " + self.eesnimi + " " + self.perenimi + "!")

class Admin(Kasutaja):
    """Admin klass, laiendab Kasutaja klassi"""
    def __init__(self, e, p, kn, parool):
        """Admin tüüpi kasutaja loomiseks kasutatav konstruktor"""
        super().__init__(e, p, kn, parool)
        self.roll = "administraator"
        self.privileegid = Privileegid()

class Privileegid():
    """Privileegid klass"""
    def __init__(self):
        """Privileegide määramine"""
        self.privileegid = ["lubatud lisada kasutajad", "lubatud eemaldada kasutajad", "lubatud blokeerida kasutajad"]

    def naita_privileegid(self):
        """Privileegide näitamine"""
        print("Admini privileegid")
        for privileeg in self.privileegid:
            print(privileeg)