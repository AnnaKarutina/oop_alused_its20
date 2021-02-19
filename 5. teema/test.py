from kuju import Kuju
from ruut import Ruut
from kolmnurk import Kolmnurk
from ring import Ring

kuju = Kuju()
ruut = Ruut(2)
kolmnurk = Kolmnurk(5, 2)
ring = Ring(5)

print(kuju)
print(ruut)
print(kolmnurk)
print(ring)

print("kuju pindala " + str(kuju.pindala()))
print("ruut pindala " + str(ruut.pindala()))
print("kolmnurga pindala " + str(kolmnurk.pindala()))
print("ringi pindala " + str(ring.pindala()))