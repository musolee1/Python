class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def full_name(self):
        return f"{self.first} {self.last}"

userA = User("Mustafa", "Bayramoğlu", 23)
userB = User("İlayda", "Bulut", 23)

print(userA.full_name())
print(userB.full_name())