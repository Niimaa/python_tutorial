a = 250

def f1():
    global a
    a = 50 #global , here we change the global variable value
    print(a)

def f2():
    a = 150
    print(a) #local


f1()
f2()
print(a)

a = [1,2,3]

def f1():
    a[0] = 0#work as global for lists and dictionaries
    print(a) #local

def f2():
    a = 150
    print(a) #local


f1()
f2()
print(a)