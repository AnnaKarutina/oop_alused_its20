from kasutaja import Kasutaja
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