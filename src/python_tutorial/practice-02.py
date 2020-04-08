import csv
with open('database.csv', 'w', newline='') as file:
    fieldnames = ['username', 'password']
    user_pass = csv.DictWriter(file, fieldnames=fieldnames)
    user_pass.writeheader()
    user_pass.writerow({'username': 'Magnus Carlsen', 'password': 2870})
    user_pass.writerow({'username': 'Fabiano Caruana', 'password': 2822})
    user_pass.writerow({'username': 'Ding Liren', 'password': 2801})


class ID:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user_1 = ID("nima","1111")

print(user_1.password)




#with open('database.csv', 'r') as file:
#   reader = csv.reader(file)
#  for row in reader:
#        print(row)

#username = input("please write your username: ").capitalize()
#password = input("please write your password: ")

