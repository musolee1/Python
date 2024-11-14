class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person nesnesi türetildi.")
    
    def intro(self):
        print(self.name,self.surname, self.age)

class Student(Person):
    def __init__(self,name,surname,age, number):
        super().__init__(name,surname,age)
        self.number = number
        print("Student nesnesi türetildi.")
    
    def intro(self):
        print(self.name,self.surname, self.age, self.number)
    
    def study(self):
        print(f"{self.number} numaralı öğrenci ders çalışıyor.")

class Teacher(Person):
    def __init__(self,name,surname,age,branch):
        super().__init__(name,surname,age)
        self.branch = branch
        print("Teacher nesnesi türetildi.")
    
    def teach(self):
        print(f"{self.name} isimli öğretmen {self.branch} eğitimi veriyor.")

p1 = Person("İlayda", "Bulut", 23)
p1.intro()
s1 = Student("Mustafa", "Bayramoğlu", 23, 101)
s1.intro()
s1.study()

t1 = Teacher("Bebis", "Bulut", 4, "English")
t1.intro()
t1.teach()