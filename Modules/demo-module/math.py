# import math as islem

# value = dir(math)

# value = help(math)

# value = help(math.factorial)

# value = math.sqrt(49)

# value = math.factorial(4)

# # value = math.floor(5.9)

# value = math.ceil(5.9)

# value = islem.factorial(5)

# from math import *

# value = factorial(5)

# value = sqrt(25)

# print(value)


#bankamatik fonksiyonu oluşturalım ve içerisinde bakiye sorgulama, para yatırma, para çekme fonksiyonlarını yazalım

def bakiye_sorgula(bakiye):
    print(f"Bakiyeniz: {bakiye} TL'dir.")

def para_yatir(bakiye, miktar):
    bakiye += miktar
    print(f"{miktar} TL yatırıldı. Yeni bakiyeniz: {bakiye} TL'dir.")
    return bakiye

def para_cek(bakiye, miktar):
    if bakiye - miktar < 0:
        print("Yetersiz bakiye!")
    else:
        bakiye -= miktar
        print(f"{miktar} TL çekildi. Yeni bakiyeniz: {bakiye} TL'dir.")
        return bakiye

bakiye = 1000

bakiye_sorgula(bakiye)
para_yatir(bakiye, 500)