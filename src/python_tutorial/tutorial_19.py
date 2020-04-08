for number in range(1,11,2):
    print(number)

for letter in "ABCD":
    print(letter)

vowels = 0
consonants = 0

for letter in "Hello, My name is Nima and I am learning Python programming":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1
print("There are {} vowels.".format(vowels))
print("There are {} consonants.".format(consonants))


students = {
    "male":["Tom","Harry", "Frank"],
    "female":["Sarah","Emily","Elizabeth"]
}

for key in students.keys():
    print(key)
    for name in students[key]:
        if "a" in name:
            print(name)