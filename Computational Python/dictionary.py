#Key and its value in the dictionary
employee = {'name': 'Tom', 'age': '30', 'expertise': ['Java', '.net']}
print(employee)
print(employee['name'])
print(employee.get('address'))
print(employee.get('age'))
print(employee.get('address','Value is not found'))

#add, edit values from dictionary

employee['years']= 5
print(employee['years'])
employee['years']= 6
print(employee['years'])

del employee['years']
print(employee)

age = employee.pop('age')
print(age)

#methods
print(len(employee))
print(employee)

employee['age']=30
print(employee)
print(employee.keys())
print(employee.values())
print(employee.items())

#loop through dictionary
for key in employee:
    print(key)

for key, value in employee.items():
    print(key, value)