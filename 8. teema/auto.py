class Auto():
    # lihtne auto
    # tootja, mudel, aasta
    def __init__(self, t, m, a):
        self.tootja = t
        self.mudel = m
        self.aasta = a
        self.odomeetri_nait = 0

    def kirjeldus(self):
        pikk_nimi = str(self.aasta) + " " + self.tootja + " " + self.mudel
        return pikk_nimi.title()

    def odomeeter(self):
        print("Antud auto sõitnud läbi " + str(self.odomeetri_nait) + " km.")
    # 2 - atribuuti väärtuse muutmine meetodi abil
    def uuenda_odomeeter(self, km):
        if km >= self.odomeetri_nait:
            self.odomeetri_nait = km
        else:
            print("Ei ole võimalik tagasi keerata odomeetri näit")

    def suurenda_odomeeter(self, km):
        self.odomeetri_nait += km

    def tangi(self, l):
        print("Tangid " + str(l) + " liitrit kütust")

class Aku():
    def __init__(self, aku_s = 60):
        self.aku_suurus = aku_s
    def kirjeldus(self):
        print("Antud auto aku suurus on " + str(self.aku_suurus) + " kWh")
    def saada_soidu_varu(self):
        soidu_varu = 240
        if(self.aku_suurus == 70):
            soidu_varu = 240
        elif(self.aku_suurus == 85):
            soidu_varu = 270
        teade = "Antud auto saab sõita umbes " + str(soidu_varu) + "km"
        print(teade)

class ElektriAuto(Auto):
    def __init__(self, t, m, a):
        super().__init__(t, m, a)
        self.aku_suurus = Aku()

    def aku_kirjeldus(self):
        print("Antud auto sisaldab " + str(self.aku_suurus) + " patareid")

    def tangi(self, l):
        print("Antud auto ei vaja kütust sõitmiseks")