class Person:
    #constructor (yapıcı methodlar)
    def __init__(self, name, surname, year):
        
        #object attributes
        self.name = name
        self.surname = surname
        self.year = year
    #instance method!
    def intro(self):
        return f"Benim adım {self.name}, soyadım {self.surname}, doğum tarihim {self.year}"
    def calculate_age(self):
        return f"{2024-self.year}"

p1 = Person("Mustafa", "Bayramoğlu", 2001)

print(p1.intro())
print(p1.calculate_age())