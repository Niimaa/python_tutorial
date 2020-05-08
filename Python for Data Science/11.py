with open("C:/Users/nafs080/work/codes/python_packages/python_tutorial/Python for Data Science/file2.txt","w") as file2:
    file2.write("This is line A\n")
    file2.write("This is line B\n")

Lines=["This is line A\n","This is line B\n","This is line C\n"]
with open("Example2.txt", "w") as file1:
    for line in Lines:
        file1.write(line)
#append
with open("Example2.txt","a") as file1:
    file1.write("This is line D")
#copy
with open("Example1.txt","r") as readfile:
    with open("Example3.txt","w") as writefile:
        for line in readfile:
            writefile.write(line)