from kasutaja import Kasutaja
from admin import Admin

tavakasutaja = Kasutaja("Tava", "Kasutaja", "user", "qwerty")
tavakasutaja.tervita_kasutaja()

administraator = Admin("Admin", "Istraator", "root", "qwerty")
administraator.privileegid.naita_privileegid()