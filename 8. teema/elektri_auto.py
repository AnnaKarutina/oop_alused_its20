from auto import Auto

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