class Product:
    def __init__(self, name, price, isActive= False):
        self.name = name
        self.price = price
        self.isActive = isActive
        print("Product nesnesi oluşturuldu.")

p1 = Product("Samsung S24", 75000, True)
p2 = Product("Iphone 16", 95000) 

print(p1.name, p1.price, p1.isActive)
print(p2.name, p2.price, p2.isActive)