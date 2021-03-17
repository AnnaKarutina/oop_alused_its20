from opimine import *

def menuu():
    print("Tunni programm")
    print("1 - lisa aine teemad")
    print("2 - trüki aine teemad")
    print("3 - lisa õpilased klassi")
    print("4 - õpeta teema õpilastele")
    print("5 - kontrolli õpilaste teadmised")
    print("6 - lase õpilasele unustada teemat")
    valik = int(input("Vali sobilik tegevus: "))
    return valik

def lisa_teemad():
    teemad = Andmed()
    while(True):
        teema = input("Sisesta teema: ")
        if(teema == ""):
            break
        teemad.lisa_info(teema)
    return teemad

def valjasta_teemad(aine_teemad):
    if(len(aine_teemad.info) == 0):
        print("Teemad on veel sisestamata")
    else:
        print("Aine teemad: ")
        for teema in aine_teemad:
            print(teema)
        print("----------------------")
# katsed

aine_teemad = []
while(True):
    valik = menuu()
    if(valik == 1):
        aine_teemad = lisa_teemad()
    if(valik == 2):
        valjasta_teemad(aine_teemad)
    if(valik > 6 or valik < 1):
        break
'''    
aine_teemad = Andmed("OOP põhimõtted", "Klassid ja objektid", "Konstruktor")

kadi = Opilane("Kadi")
mati = Opilane("Mati")
anna = Opetaja()
anna.opetab(aine_teemad[0], kadi, mati)
print("Tunni teema - " + aine_teemad[0])
kadi.kirjeldus()
mati.kirjeldus()
print("----------------------")
anna.opetab(aine_teemad[1], mati)
kadi.kirjeldus()
mati.kirjeldus()

mati.opib(aine_teemad[2])
mati.kirjeldus()

mati.unustab()
mati.kirjeldus()
'''