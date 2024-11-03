# 1-100 arasında rastgele üretilecek bir sayı aşağı yukarı ifadeleri ile buldurmaya çalışın.
#random modülü" için python random" şeklinde arama yapın.
# 100 üzerinden puanlama yapın her soru 20 puan.
# Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hessaplansın.

import random
sayi = random.randint(1,100)
hak = int(input("Hakkınızı Girin: "))
can = hak 

sayac = 0
while hak > 0:
    hak -= 1
    tahmin = int(input("Tahmininizi giriniz: "))
    sayac += 1

    if tahmin == sayi:
        print(f"Tebrikler, doğru yanıt! {sayac} denemede bildiniz! Puanınız {100 - (100/can) * (sayac -1)}")
        break
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")
    
    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı: {sayi}")





