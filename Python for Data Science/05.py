#Creating a SET
set1 = {"A", "AB", "A"}
#There are no duplicate values in a set
print(set1)

#Change a list to a set

list = ["Nima", "Afshar", "Nima", 1984]
set = set(list)
print(set)

#Add item to the set
set1.add("C")
print(set1)
#remove an item from the set
set1.remove("C")
print(set1)

#check if the item is in the set

print("AA" in set1)
print("AB" in set1)

#Find the intersectin of two sets
Album1 = {"AC/DC", "Thriller", "Back in Black"}
Album2 = {"The dark side of the moon", "Thriller", "Back in Black"}
Album3 = Album1 & Album2
print(Album3)
#combine all the elements of two sets
Album4 = Album1.union(Album2)
print(Album4)
#to check if a set is a subset of other set
print(Album3.issubset(Album4))

