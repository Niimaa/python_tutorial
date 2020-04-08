#local scope can only be seen in an specific local scope but global scope can be see anywhere in the code, only function can make a local scope

# a is now defined in a global scope but if we move that into the function f1() then it is not going to work for f(2)
a = 100
def f1():
    print(a)

def f2():
    print(a)

f1()
f2()


def f1():
    a = 50
    print(a)

def f2():
    a = 150
    print(a)

f1()
f2()

def word():
    new_word = input("Write down a word please").strip().capitalize()
    print("The new word is {}".format(new_word))

word()

#When the function can not find the variable inside the local scope it is going to look for that variable outside the scope

