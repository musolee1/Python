liste = [1,2,3]
print(len(liste))

s = "Hello World!"

print(len(s))

class Film:
    def __init__(self, title, director, time):
        self.title = title
        self.director = director
        self.time = time

    def __str__(self):
        return f"{self.title}, {self.director} tarafından yönetiliyor."

    def __repr__(self):
        return f"{self.title}, {self.director} tarafından yönetiliyor."

    def __len__(self):
        return self.time

    def __del__(self):
        print("film objesi silindi.")

f = Film("Film Adı", "Yönetmen", 120)

# print(len(f))
print(str(liste))
print(str(f))
print(f)
print(len(f))

del f