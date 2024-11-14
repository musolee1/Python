# Kart sınıfı

# Kart sınıfından türetilen her bir nesne bir kart türünü temsil edecek.
# Kart sınıfının tip ve deger isminde 2 instance özelliği olsun. (tip:sinek deger:5)

# sinek5 = Kart("sinek","5")
# karoAs = Kart("karo","A")

# Kart sınıfının kartıGetir() ismindeki instance metodu kart bilgilerini yazdırsın.

# sinek5.kartıGetir() => sinek 5

# Deste sınıfı

# deste1 = Deste()

# kart tipleri   => karo,sinek,kupa,maça
# kart değerleri => A,2,3,4,5,6,7,8,9,10,J,Q,K

# Deste sınıfındaki kartlar listesine 52 kartı for ve list comphension ile ekleyiniz.
# Destede kalan kart sayısı için kartSayisi() isminde bir metot.
# Destedeki kartları karıştırmak için KartlariKaristir() isminde bir metot.
# kartDagit() ismindeki metot belirtilen adet kadar kartı dağıtmalıdır. Destedeki kalan kart sayısına dikkat.
# kartAt() ismindeki metot elden bir kart atmak için kullanılsın.

from random import shuffle

class Card:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    # def getCard(self):
    #     return f"{self.type} {self.value}"
    
    def __repr__(self):
        return f"{self.type} {self.value}"

# kart tipleri   => karo,sinek,kupa,maça
# kart değerleri => A,2,3,4,5,6,7,8,9,10,J,Q,K
# Deste sınıfındaki kartlar listesine 52 kartı for ve list comphension ile ekleyiniz.

class Deste:
    types = ["karo","sinek","kupa","maça"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        self.kartlar = [Card(type,value) for type in Deste.types for value in Deste.values]
        # for type in types: Alternative
        #     for value in values:
        #         self.kartlar.append(Card(type,value))

    def kartSayisi(self):
        return len(self.kartlar)
    
    def kartlariKaristir(self):
        if (self.kartSayisi() < 52):
            raise ValueError("Oyun başladıktan sonra kartları karıştıramazsınız.")
        else:
            shuffle(self.kartlar)
    
    def kartDagit(self,adet):
        kartSayisi = self.kartSayisi()
        if kartSayisi == 0:
            raise ValueError("Tüm Kartlar Dağıtıldı!")
        adet = min([kartSayisi,adet])
        kartlar = self.kartlar[-adet:]
        self.kartlar = self.kartlar[:-adet]
        return kartlar

    def kartAt(self):
        return self.kartDagit(1)[0]
        


deste1 = Deste()

deste1.kartlariKaristir()

print("Dağıtılan kartlar:","\n",deste1.kartDagit(5), "\n", deste1.kartDagit(5),"\n",deste1.kartDagit(5),"\n",deste1.kartDagit(5),"\n",deste1.kartAt())
print("Kalan kart adedi:", deste1.kartSayisi())

print(deste1.kartlar)


# Destede kalan kart sayısı için kartSayisi() isminde bir metot.
# Destedeki kartları karıştırmak için KartlariKaristir() isminde bir metot.
# kartDagit() ismindeki metot belirtilen adet kadar kartı dağıtmalıdır. Destedeki kalan kart sayısına dikkat.
# kartAt() ismindeki metot elden bir kart atmak için kullanılsın.