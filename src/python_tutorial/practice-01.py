
id = {"Nima": "1984"}

#print("username is: {}".format(list(id.keys())))

username = input("please write your username: ").capitalize()
password = input("please write your password: ")

user_pass = False
attempts = 1

while user_pass is False:
    if username in id:
        if id[username] == password:
            print("OK")
            user_pass = True
        else:
            print("Wrong password!")
            attempts = attempts + 1
            if attempts <= 3:
                password = input("please write your password: ")
            else:
                print("Sorry your username is blocked, try again later")
                break


    else:
        raise ValueError("Invalid username. Please try again!")