set_month = {'jan', 'feb', 'mar', 'apr'}
print(set_month)

#Check if some value is present inside the set
print('mar' in set_month)
print('dec' in set_month)

#set operations
set_month2 = {'mar', 'apr', 'may', 'jun'}

#intersection
print(set_month.intersection(set_month2))

#union
print(set_month.union(set_month2))

#Difference
print(set_month.difference(set_month2))

#Define an empty set
empty_set = set()

#define an empty list
empty_list = []
#or
empty_list = list()
empty_tuple = ()
empty_tuple = tuple()
