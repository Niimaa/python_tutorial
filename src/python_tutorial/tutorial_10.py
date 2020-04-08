C = 5
D = -1

if C>1 or D>1:
    print("it worked")

if C > 7 or D < -2:
    print("it worked")
else:
    print("non of the conditions are correct")

if not (C > 10 or D > 3):
    print("it worked")


C = 6
D = 2
if (C > 5 and D > 5) or (C > 2 and D > 1):
    print("it worked")

#this code is not going to print since it's False
if not ((C > 5 and D > 5) or (C > 2 and D > 1)):
    print("it worked")

    