# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

# kelime = str(input("Kelime yazınız: "))
# adet = int(input("Adet giriniz: "))


# def kelimeYazdir(y, x):

#     print(x * y)
    
# sonuc = kelimeYazdir (kelime,adet)
# print(sonuc)

# 2- Dikdörtgenin alanı ve çevresini hesaplayan fonksiyonu yazınız.

# def hesapla(x,y):
#     print(f"Dikdörtgenin çevresi: {2 * x + 2 * y}. Dikdörtgenin alanı: {x*y}")

# a = int(input("Kısa kenarı giriniz: "))
# b = int(input("Uzun kenarı giriniz: "))

# sonuc = hesapla(a,b)

# 3- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

# def asalBul(x,y):
#     for sayi in range(x,y+1):
#         if(sayi>1):
#             for i in range(2,sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)

# sonuc = asalBul(50,100)

# print(sonuc)

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenleriBul(50))