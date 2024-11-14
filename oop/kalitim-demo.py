# User
# Moderator

class User:
    active_users = 0

    @classmethod

    def display_active_users(cls):
        return f"Şu anda aktif {cls.active_users} user var."
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        User.active_users += 1

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

class Moderator(User):
    def __init__(self, firstname, lastname, community):
        super().__init__(firstname,lastname)
        self.community = community
    
    def remove_post(self):
        return f"{self.fullname()} {self.community} grubundan bir post sildi."

    def update_post(self):
        return f"{self.fullname()} {self.community} grubunda bir postu güncelledi."

print(User.display_active_users())

u1 = User("Ali", "Korkmaz")
m1 = Moderator("Yağmur", "Korkmaz", "Product")

print(m1.remove_post())
print(m1.update_post())

print(User.display_active_users())

# print(u1.fullname())


# print(isinstance(u1 ,Moderator))
# print(isinstance(u1 ,User))
# print(isinstance(m1 ,Moderator))
# print(isinstance(m1 ,User))
