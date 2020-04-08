print("Hello World")

hello = "Hello World!"

print(type(hello))

message = 'John said to me "I will see you later"'
print(message)

# Ask user for name
name = input("What is your name?: ")
print(name)
# Ask user for age
Age = input("What is your age?: ")
print(Age)
# Ask user for city
City = input("What is your city?: ")
print(City)
# Ask user what they enjoy
Love = input("What do you enjoy doing?: ")
print(Love)
# Create output text
string = "your name is {} and you are {} years old. you live in {} and you love {}"
output = string.format(name, Age, City, Love)
# Print output to screen

print(output)