def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return(sentence)


#name,age and likes are function parameters but Jack, 23 and python are arguments
A = about("Jack", 23, "Python") #these are positional arguments
print(A)

A = about(age=23, name="Jack", likes= "Python") #these are keyword arguments
print(A)

def about(name, age, likes="python"):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return(sentence)

B = about("Nima", 35)
print(B)

def about(name, age, likes="python"): #default values (here is likes) should be written at the end
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return(sentence)

C = about("Nima", 35, "Music")
print(C)