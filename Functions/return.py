a = 20
b = 10

def plus():
    return f'Sum of a and b is: {a+b}'

print(plus())

def now():
    import datetime
    return datetime.datetime.now().year

def hour():
    import datetime
    return datetime.datetime.now().hour

def ageCalculation():
    return now() - 1995

print(ageCalculation())

def greeting():
    if (hour()<12):
        return "Good Morning"
    elif (hour()>=12 and hour()<18):
        return "Good Afternoon"
    else:
        return "Good Night"
    
print(greeting())