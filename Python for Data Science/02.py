A = 'Michael Jackson is the best'
B = A.upper()
print(B)

C = A.replace('Michael','Janet')
print(C)

D = C.lower()
print(D)

#string can be a combination of numbers letters and spaces

E = 'Ab #42'
print(E)

#print the fitrst index in the string "A"
print(A[0])
#negative indexing
#print the index -1 in the string "A"
print(A[-1])
#the length
print(len(D))

#slicing
print (A[0:4])

# Get every second element. The elments on index 1, 3, 5 ...

print(D[::2])

# Get every second element in the range from index 0 to index 4

print(D[0:5:2])

# Concatenate two strings

Statement = A + "singer in the world "
print(Statement)

Statement = 3 * Statement
print(Statement)

# New line escape sequence

print(" Michael Jackson \n is the best" )
# Tab escape sequence

print(" Michael Jackson \t is the best" )

# Include back slash in string

print(" Michael Jackson \\ is the best" )

# r will tell python that string will be display as raw string

print(r" Michael Jackson \ is the best" )

# Convert all the characters in string to upper case

F = "Thriller is the sixth studio album"
print("before upper:", F)
G = F.upper()
print("After upper:", G)
# Find the substring in the string. Only the index of the first elment of substring in string will be the output

Name = "Michael Jackson"
print(Name.find('el'))

# If cannot find the substring in the string
print(Name.find('Jasd'))