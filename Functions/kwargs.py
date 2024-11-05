# def displayUser(*args):
#     print(type(args))
#     print(args)

# displayUser()

def displayUser(**kwargs):

    for key,value in kwargs.items():
        print(f"{key}: {value}")

    print(type(kwargs))
    print(kwargs)

displayUser(email="mustafabayramoglu29@gmail.com", name="Mustafa", surname="Bayramoğlu", country="Turkey")

def myFunc(a,b,c,*args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,70, key1="value1", key2="value2")