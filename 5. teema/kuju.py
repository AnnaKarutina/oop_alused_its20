class Kuju:
    def pindala(self):
        return "Pindala arvutus"
    # sama moodi saab kasutada ka __repr__(self) meetodit
    def __str__(self):
        return str(self.__class__.__name__) + " klassi põhjal loodud eksemplaar(objekt)"