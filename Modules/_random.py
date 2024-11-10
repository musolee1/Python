import random

# result = dir(random)
# result = help(random)

result = random.random() # 0.0 - 1.0
result = random.random() * 100 # 0.0 - 100.0
result = int(random.uniform(10,100)) #10-100 arasında rastgele bir sayı üretir
result = random.randint(1,100)  #1-100 arasında rastgele bir sayı üretir

greeting = 'hello there'
names = ['ali','yağmur','deniz','cenk','ahmet','efe']
# result = names[random.randint(0,len(names)-1)]

result = random.choice(names) #names listesinden rastgele bir eleman seçilir
result = random.choice(greeting) #greeting içerisinden rastgele bir karakter seçilir

liste = list(range(10))
random.shuffle(liste)
result = liste #liste elemanları karıştırılır

liste = range(100)
result = random.sample(liste, 3) #liste içerisinden 3 eleman rastgele seçilir
result = random.sample(names, 2) #names listesinden 2 eleman rastgele seçilir
print(result)

