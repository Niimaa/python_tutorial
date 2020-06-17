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
#list methods - Sort
months.sort()
print(months)
months_numbers = [1,3,5,4,2,7,6]
months_numbers.sort()
print(months_numbers)
months_numbers.sort(reverse=True)
print(months_numbers)
sorted_months = sorted(months_numbers)
print(months_numbers)
print(sorted_months)
#list method - min, max, sum
print(min(months_numbers))
print(max(months_numbers))
print(sum(months_numbers))
print(months.index('aug'))
print(months)
print('jun' in months)
print('Nov' in months)

