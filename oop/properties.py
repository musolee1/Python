class Product:
    def __init__(self, name, price,description):
        self.name = name
        self.description = description
        if price >=0:
            self._price = price
        else:
            # self.price = 0
            raise ValueError("0'dan büyük bir değer giriniz!")
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("0'dan büyük bir değer giriniz!")

    @property
    def short_description(self):
        return self.description[:10]

    # def set_price(self, value):
    #     if value > 0:
    #         self._price = value
    #     else:
    #         raise ValueError("0'dan büyük bir değer giriniz!")

    # def get_price(self):
    #     return self._price


p = Product("Iphone 16", 9000, "Iphone 16 çok iyi bir üründür ancak apple görünümünü daha da iyileştirebilirdi.")

print(p.short_description)

# print(p.get_price())

# p.set_price(-8000)

# print(p.get_price())