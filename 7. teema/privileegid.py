class Privileegid():
    def __init__(self):
        self.privileegid = ["lubatud lisada kasutajad", "lubatud eemaldada kasutajad", "lubatud blokeerida kasutajad"]

    def naita_privileegid(self):
        print("Admini privileegid")
        for privileeg in self.privileegid:
            print(privileeg)