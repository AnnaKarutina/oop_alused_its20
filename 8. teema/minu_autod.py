#from auto import Auto
#from elektri_auto import ElektriAuto
import auto
import elektri_auto

uus_auto = auto.Auto("audi", "a6", "2017")
print(uus_auto.kirjeldus())

minu_tesla = elektri_auto.ElektriAuto('tesla', 'model s', 2016)
print(minu_tesla.kirjeldus())