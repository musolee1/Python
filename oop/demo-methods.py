# BankAccount isminde bir sınıf tanımlayınız.
# Üretilen her bir nesne owner isminde biz özelliğe sahip olmalıdır. BankAccount("Sadık Turan")
# Üretilen her bir nesne balance isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır.
# Üretilen her bir nesne için deposit metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp balance
# üzerine ekleyin ve balance miktarını geriye döndürün.
# Üretilen her bir nesne için withdraw metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp balance
# değerinden çıkarıp geriye döndürün.



class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

h1 = BankAccount("Mustafa Bayramoğlu")

print(h1.deposit(300))
print(h1.getBalance())
print(h1.withdraw(200))