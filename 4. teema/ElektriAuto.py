from Auto import Auto
# ElektriAuto - alamklass, laps
# Auto - vanemklass, vanem, super()
class ElektriAuto(Auto):
    def __init__(self, t, m, a):
        super().__init__(t, m, a)
        self.aku_suurus = 50

    def aku_kirjeldus(self):
        print("Antud auto sisaldab " + str(self.aku_suurus) + " patareid")