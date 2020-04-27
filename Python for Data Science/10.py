# open function

file1 = open("C:/Nima/Data_science course/Course 04/Example1.txt","w")
print(file1.name)
print(file1.mode)
file1.close()

#with open is better to open the file because it automatically closes the file

with open("Example1.txt") as file1:
    file_stuff = file1.read()
    print(file_stuff)
print(file1.closed)
print(file_stuff)

# store all the lines in the list
with open("Example1.txt") as file1:
    file_stuff = file1.readlines()
    print(file_stuff)

# Read first four characters
with open("Example1.txt", "r") as file1:
    print(file1.read(4))

# Read certain amount of characters

with open("example1.txt", "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
#read only first line
with open("Example1.txt") as file1:
    file_stuff=file1.readline()
    print(file_stuff)
# we can use that function twice to read two lines seperately
with open("Example1.txt") as file1:
    file_stuff=file1.readline()
    print(file_stuff)
    file_stuff=file1.readline()
    print(file_stuff)

# or we can use the loop
with open("Example1.txt") as file1:
    for line in file1:
        print(line)
#we can specify the number of caracters we would like to read from string as an argument
print("hello")
with open("Example1.txt","r") as file1:
    file_stuff=file1.readline(16)
    print(file_stuff)
    file_stuff=file1.readline(9)
    print(file_stuff)
    file_stuff=file1.readline(5)
    print(file_stuff)
    
with open("Example1.txt", "r") as File1:
    file_stuff = File1.readline()

    print(file_stuff)