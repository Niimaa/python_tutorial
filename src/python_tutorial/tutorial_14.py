our_tuple = 1,2,3,"A","B", "C"

print(type(our_tuple))

our_tuple = (1,2,3,"A","B","C")

print(type(our_tuple))

A = our_tuple[0:3]
print(A)

our_list = [1,2,3,4,5,6,7]
B = our_list[2] = 100
print(B)
#but it is not working for tuple, cuz tuple same as strings opjects do not support item assignment(they are immutable)
#our_tuple[3] = 100
#print(our_tuple)
A = [1,2,3]
#change it to tuple
B = tuple(A)
print(type(B))

(A,B,C) = 1,2,3
print(A)
print(B)
print(C)
D,E,F = [1,2,3]
print(D)
G,H,I = "567"
print(I)