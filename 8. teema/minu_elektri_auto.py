from auto import ElektriAuto

minu_tesla = ElektriAuto('tesla', 'model s', 2016)
print(minu_tesla.kirjeldus())
minu_tesla.aku_suurus.kirjeldus()
minu_tesla.aku_suurus.saada_soidu_varu()