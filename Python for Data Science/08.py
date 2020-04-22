#Python function: sum, len, and so many other complicated functions

#sorted function
#sorted is a function and returns a new list, it does not change the existing list
album_ratings = [10.0,8.5,9.5,7.0,7.0,9.5,9.0,9.5]
sorted_album_ratings = sorted(album_ratings)
print(sorted_album_ratings)

#sort method does not need a new list and apply the method sort to the existing list
album_ratings.sort()
print(album_ratings)

#making function

def add1(a):
    """
    add 1 to a
    """
    b=a+1
    return b
add1(5)
print(add1(5))
print(add1(10))

#get the help and documentation on the function
help(add1)

def Mult(a,b):
    c=a*b
    return c
print(Mult(3,2))
print(Mult(2,"Michael Jackson "))
#In many cases function does not have a return statement

def MJ():
    print("Michael Jackson")
MJ()

def NoWork():
    pass
print(NoWork())

def add1(a):
    b = a+1
    print(a, "plus 1 equals", b)
    return b
add1(2)

#using loop

def printStuff(Stuff):
    for i,s in enumerate(Stuff):
        print("Album",i,"Rating is", s)

album_ratings = [10.0,8.5,9.5]
printStuff(album_ratings)

#Collecting arguments
def ArtistNames (*names):
    for name in names:
        print(name)
ArtistNames("Michael","Andy")