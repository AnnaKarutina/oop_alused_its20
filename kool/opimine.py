from random import randint

class Andmed():
    def __init__(self, info=None):
        if(info is not None):
            self.info = list(info)
        else:
            self.info = []
    def __getitem__(self, i):
        return self.info[i]
    def lisa_info(self, info):
        self.info.append(info)

class Opilane():
    def __init__(self, nimi):
        self.nimi = nimi
        self.teadmised = []
    def opib(self, teema):
        self.teadmised.append(teema)

    def unustab(self):
        teema_nr = randint(0, len(self.teadmised))
        self.teadmised.remove(self.teadmised[teema_nr])


    def kirjeldus(self):
        print("Õpilase " + self.nimi + " teadmised:")
        for teema in self.teadmised:
            print(teema)

class Opetaja():
    def opetab(self, teema, *opilased):
        for opilane in opilased:
            opilane.opib(teema)