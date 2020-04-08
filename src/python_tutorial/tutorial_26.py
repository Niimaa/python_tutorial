#unpack the arguments

numbers = [1,2,3,4,5]
print(numbers)

numbers = [1,2,3,4,5]
print(*numbers)

print("abc")
print(*"abc")

#pack the arguments

def add(x,y):
    return x+y

A = add(10,10)
print(A)

def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return(total)

B = add(1,2,3,4,5,6,7,8,9)
print(B)

#keyword arguments

def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return sentence

dictionary = {"name":"Nima", "age":35, "likes":"python"}#order does not matter in dictionary
C = about(**dictionary)
print(C)

def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key,value))

foo(Pardis = "Female", Nima = "male")
