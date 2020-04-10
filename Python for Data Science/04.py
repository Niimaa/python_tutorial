#Dictionary
dict = {"Key1":1, "Key2":2, "Key3":3}
print(dict)
#print the value of one of the keys
print(dict["Key1"])
#Add a key to the dictionary
dict["Key4"] = 4
print(dict)
#delete
del(dict["Key4"])
print(dict)

#to see if the key exists in the dictionary
print("Key3" in dict)
print("Key4" in dict)

#to show all the keys in the dictionary

keys = dict.keys()
print(keys)

#to show all the keys in the dictionary
values = dict.values()
print(values)