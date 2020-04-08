# "in" condition
L = [1, 5, 2, 6, 2, 9]
print(2 in L)
# "del" command (we use it when we dont know the instance inside the list, we just want to delete the certain index)
del L[0]
print(L)

example = ["A", "B", "A", "C"]
del example[0:2]
print(example)


known_users = ["Alice", "Bob", "Clair", "Dan", "Emma", "Fred", "Georgie", "Harry"]
print(len(known_users))

while True:
    print("Hi! My name is Travis")
    name = input("What is your name? ").strip().capitalize()

    if name in known_users:
        print("Hello {}".format(name))
        remove = input("Would you like to be removed from the system? (y/n)").strip().lower()
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem I did not want you to leave")
    else:
        print("I do not think I have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system? (y/n)".strip().lower())
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries, I'll see you around")
#ctrl + C to stop the loop


