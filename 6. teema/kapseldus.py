class YhendusServeriga():
    # contruct
    def __init__(self, ip, kn):
        self.__ip = ip
        self.__kasutajanimi = kn
    # getter
    def saadaIp(self):
        return self.__ip
    # setter
    def maaraIp(self, vaartus):
        self.__ip = vaartus


yhendusWEBmasinaga = YhendusServeriga("192.168.24.75", "user")
print(yhendusWEBmasinaga.saadaIp())
# yhendusWEBmasinaga.__ip = "192.168.23.12" - ei tööta, valesti
yhendusWEBmasinaga.maaraIp("192.168.23.12") # õige, töötab
print(yhendusWEBmasinaga.saadaIp())

