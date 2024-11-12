class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def logout(self):
        User.active_users -= 1
        return f"{self.full_name()} uygulamadan çıkış yaptı."

print(User.active_users)

userA = User("Mustafa", "Bayramoğlu", 23)
userB = User("İlayda", "Bulut", 23)
userC = User("Alp", "Koç", 4)

print(User.active_users)

print(userC.logout())

print(User.active_users)