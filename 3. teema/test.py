from Koer import Koer
nublu = Koer("Nublu", 5)
nublu.kirjeldus()

puppy = Koer("Puppy")
puppy.kirjeldus()
if(puppy.saba):
    print("Puppy liputab")

vanus = 5
while(vanus <= 15):
    puppy.vanus = vanus
    puppy.kirjeldus()
    if(puppy.vanus == 15):
        del puppy
    vanus += 5
input()


