months = ['Jan', 'Marc', 'Apr', 'jun']
print(months)
print(len(months))
print(months[2])
print(months[-1])
#slicing
print(months[:3])
print(months[0:])
print(months[0:1])
print(months[:1])
#list methods - insert
months.insert(1,'Feb')
print(months)
new_months = ['aug','sep','nov']
months.insert(5,new_months)
print(months)
#list methods - extend
months = ['Jan', 'Feb', 'Marc', 'Apr', 'jun']
months.extend(new_months)
print(months)
#list methods - remove
months.remove('Feb')
print(months)
#remove the last value
months.pop()
print(months)
#list methods - Reverse
months.reverse()
print(months)
