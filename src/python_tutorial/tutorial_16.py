students = {"Alice":["ID0001",26,"A"],
            "Bob":["ID0002",27,"B"],
            "Clair":["ID0003",17, "C"],
            "Dan":["ID0004",21,"D"],
            "Emma":["ID0005",22,"E"],
            }
print(students)

print(students["Clair"])
print(students["Clair"][0])
print(students["Dan"][1:])

#in order to make the dictionary better

students = {
            "Alice":{"ID":"ID0001","age":26,"grade":"A"},
            "Bob":{"ID":"ID0002","age":25,"grade":"B"},
            "Clair":{"ID":"ID0003","age":29,"grade":"C"},
            "Dan":{"ID":"ID0004","age":24,"grade":"D"},
            "Emma":{"ID":"ID0005","age":16,"grade":"E"},
            }
print(students["Dan"]["age"])

print(students["Emma"]["ID"],students["Emma"]["grade"])
