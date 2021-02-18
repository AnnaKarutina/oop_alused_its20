class Inimene():
    jk = 0 # järjekorra number, vaikimisi 0
    # konstruktor
    def __init__(self):
        self.id = Inimene.jk + 1
        Inimene.jk += 1 # suurendame jk väärtus 1 võrra
    # info väljastamine
    def info(self):
        print("Inimese id = " + str(self.id))
        print()