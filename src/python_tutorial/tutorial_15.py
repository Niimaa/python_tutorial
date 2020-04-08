students = {}
students = {"Alice":25, "Bob":27, "Clair":17, "Dan":21, "Emma":22}
print(students)

print(students["Dan"])
students["Fred"] = 25
print(students)
students["Alice"] = 26
print(students)

del students["Fred"]
print(students)

A = students.keys()
print(A)
#change the dic to the list so we can have access to every index
B = list(students.keys())
C = B[4]
print(C)

print(students.values())
D = list(students.values())
print(D)
E = D[2:]
print(E)

F = students.items()
print(F)