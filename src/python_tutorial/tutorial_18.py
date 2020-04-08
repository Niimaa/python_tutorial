from random import choice

number = 1
while number <= 10:
    print(number)
    number = number + 1


number = 1
while number <= 1500:
    if number % 2 == 0:
        print(number)
    number = number + 1

L = []
while len(L) < 3:
    new_name = input("please add a new name").strip().capitalize()
    L.append(new_name)
print("Sorry the list is full")
print(L)



questions = ["Why is the sky blue? ", "Why is there a face on the moon? ", "Where are all the dinosaurs? "]
question = choice(questions)
answer = input(question).strip().lower()
while answer != "just because":
    answer = input("Why? ").strip().lower()
print("Oh ... Okay")