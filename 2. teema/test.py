from Kasutaja import Kasutaja
# 1. kasutaja
alice = Kasutaja() # loome objekt nimega alice
# määrame alice oma atribuutide väärtused
alice.eesnimi = "Alice"
alice.perenimi = "Ime"
alice.kasutaja_nimi = "alice"
alice.parool = "qwerty"
# kutsume tööle alice oma meetodid
alice.kirjelda_kasutaja()
print()
alice.tervita_kasutaja()

