import os
import pandas as pd


class UserPassDatabase(object):
    """
    A simple class to generate a database that includes username and password of clients.
    It requires users to sign-up first.
    The Database is stored in a csv file.
    """
    def __init__(self, filename):
        self._filename = filename
        self._database_dict = dict()

        if not os.path.exists(self._filename):
            self._initialise_database()
        else:
            self.read_database()
        self.active_user = None

    def get_active_user(self):
        return self.active_user

    def sign_up(self):
        print("\t ===============")
        user_input = input("\t Please Enter a Username: ")
        pass_input = input("\t Please Enter a Password ")
        temp_dict = pd.DataFrame([user_input, pass_input], columns=['username', 'password'])
        self._database_dict.append(temp_dict)
        return None

    def log_in(self):
        return None

    def read_database(self):
        self._database_dict = pd.read_csv(self._filename, sep=',')

    def write_to_database(self):
        return None

    def check_password(self):
        return None

    def username_exists(self):

        return False

    def _initialise_database(self):
        df = pd.DataFrame(columns=['username', 'password'])
        df.to_csv(self._filename, sep=',', index=False)
        self._database_dict = df
        return None


if __name__ == '__main__':
    database_file = 'first_database.csv'
    UPD = UserPassDatabase(database_file)

    """ Sign up new user """
    UPD.sign_up()

#
#
# with open('database.csv', 'w', newline='') as file:
#     fieldnames = ['username', 'password']
#     user_pass = csv.DictWriter(file, fieldnames=fieldnames)
#     user_pass.writeheader()
#     user_pass.writerow({'username': 'Magnus Carlsen', 'password': 2870})
#     user_pass.writerow({'username': 'Fabiano Caruana', 'password': 2822})
#     user_pass.writerow({'username': 'Ding Liren', 'password': 2801})
#
#
# class ID:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
# user_1 = ID("nima","1111")
#
# print(user_1.password)
#
#
#
#
# #with open('database.csv', 'r') as file:
# #   reader = csv.reader(file)
# #  for row in reader:
# #        print(row)
#
# #username = input("please write your username: ").capitalize()
# #password = input("please write your password: ")
#
