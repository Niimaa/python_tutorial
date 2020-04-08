A = [5, 12, 72, 55, 89]
print(A)
A = A + [1]
print(A)

A = A + ["BCD"]
print(A)

A = A + list("BCD")
print(A)

#is not working for intereger objects since they are not iterable
#A = A + list(123)

A = A + [1,2,3]
print(A)

A = A + list(str(456))
print(A)

A = [5, 12, 72, 55, 89]

A = A + [[5,6,7,8]]
print(A)

print(A[-1])

A.append([10,11,12,13,14])
print(A)
#add "100" in the index 2 of the list A
A.insert(2,100)
print(A)

A.insert(3,[2,3,4,5,6,7])
print(A)
# this is not working
A = A.append(3)
print(A)
#it should be written like this
A = [2,3,4,[5,6,7]]
A.append(10)
print(A)