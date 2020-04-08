#to get the user email address
email = input("What is your email address? ").strip()
print(email)

username = email[:email.index("@")]
print(username)

domain = email[email.index("@")+1:]
print(domain)

output = "your user name is {} and your domain is {}".format(username,domain)
print(output)