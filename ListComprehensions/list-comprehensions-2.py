# for item in liste:
#     if(koşul):
#         expression

# [expression for item in liste if koşul]


sayilar = [1,2,5,6,47,8]
sonuc=[]


for sayi in sayilar:
    if(sayi%2==0):
        sonuc.append(sayi)

sonuc = [sayi for sayi in sayilar if sayi%2==0]

sonuc = [sayi if sayi%2==0 else "tek sayi" for sayi in sayilar]

sonuc = []

for x in range(3):
    for y in range(3):
        sonuc.append((x,y))

sonuc = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]       

print(sonuc)

