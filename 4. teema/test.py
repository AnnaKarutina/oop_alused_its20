from Auto import Auto
from ElektriAuto import ElektriAuto

ainari_uus_auto = Auto("audi", "a6", 2017)

print(ainari_uus_auto.kirjeldus())
ainari_uus_auto.odomeeter()
# 1 - objekti atribuuti otse väärtustamine
# ainari_uus_auto.odomeetri_nait = 2
ainari_uus_auto.uuenda_odomeeter(2)
ainari_uus_auto.odomeeter()
ainari_uus_auto.suurenda_odomeeter(30)
ainari_uus_auto.odomeeter()
ainari_uus_auto.tangi(30)

tesla = ElektriAuto("tesla", "mudel s", 2019)
print(tesla.kirjeldus())
tesla.aku_kirjeldus()
tesla.odomeeter()
tesla.suurenda_odomeeter(50)
tesla.odomeeter()
tesla.tangi(30)