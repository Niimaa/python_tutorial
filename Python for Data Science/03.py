#Tuple
say_what = ('say', 'what', 'u', 'will')
print(say_what[-1])

A = (1,2,7,4,5,9)
print(A[1:4])

print(len(A))

B = sorted(A)
print(B)

#Nesting
NT = (1,2,('music','sport'),(3,4))
print(NT[2])
print(NT[2][0])
print(NT[2][0][4])

#List
L = ['Nima',1,[2,3],('A',4),5.2]
print(L[3][0])
print(L[-1])
print(L[2:4])
print([1,2,3]+[1,1,1])
#extend add elements as seperate element
L.extend(["singing",7])
print(L)
#append add element as one single element as a list
L.append(["Best",6])
print(L)
print(len(L))
L[0] = 0
print(L[0])
#delete element
del(L[-1])
print(L)

#convert string to list
C = "Hi, My name is Nima"
D = C.split()
print(D)
E = "Á,B,C,D"
#Seperate with comma
F = E.split(",")
print(F)

#Clone a list

G = ["Nima",1,(2,3.4)]
H = G[:]
print(H)
help(H)
