x = "Happy birthday"
y = x.index("birthday")

print(y)

N = "0000Nima Afshar0000"
M = N.strip("0")
print(M)
M = N.rstrip("0")
print(M)

name = input("what is your name?").strip()

print(len(name))

string = "I am full of positive energy"

print(string[0])

# string[start:end:step]
B = string[13:21:1]
print(B)

C = "supercalifhgkrjblrjblgjfl"

D = C[5:9:1]
print(D)

E = C[5:]
print(E)

F = C[5::2]
print(F)

G = C[:7]
print(G)

H=C[0:7:1]
print(H)
#to reverse the string
I = C[::-1]
print(I)