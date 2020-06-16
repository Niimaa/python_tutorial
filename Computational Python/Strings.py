greeting = 'Hi, thanks for joining us today'
print (greeting)
#multi line string
greeting = """" Hi everyone,
It\'s nice to have you all here"""
print(greeting)
#length
print(len(greeting))
#string indexes
print(greeting[6])
#slicing
print(greeting[:10])
print(greeting[12:])

#strings methods
print(greeting.lower())
print(greeting.upper())
print(greeting.count('n'))
print(greeting.find('nice'))
#string replacement
print(greeting.replace('nice','good'))
#string concatnation
string1 = "good"
string2 = "Morning"
string3 = string1 + " " + string2
print(string3)
#string formatting
string3 = '{} ! {} Welcome!'.format(string1, string2)
print(string3)
#easier way for string formatting
string3 = f'{string1} ! {string2} Welcome!'
print(string3)

string3 = f'{string1.upper()} ! {string2.lower()} Welcome!'
print(string3)
#help
print(help(str.upper))
