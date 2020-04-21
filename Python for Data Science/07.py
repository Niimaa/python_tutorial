squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0,5):
    squares[i] = "white"
    print(squares)

# Loop through the list and iterate on both index and element value
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i,square in enumerate(squares):
    print(i,square)


squares = ['orange', 'orange', 'orange', 'purple', 'blue']
Newsquares =[]
i=0
while(squares[i] =='orange'):
    Newsquares.append(squares[i])
    i=i+1
print(Newsquares)

# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])

# Example of for loop

for i in range(0, 8):
    print(i)
# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'weight'
    print("After square ", i, 'is',  squares[i])

# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = 0

while(year != 1973):
    year = dates[i]
    i = i + 1
    print(year)

print("It took ", i ,"repetitions to get out of loop.")
#Exercises:
# Write your code below and press Shift+Enter to execut
for i in range(-5,6):
    print(i)
# Write your code below and press Shift+Enter to execute
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

# Write your code below and press Shift+Enter to execute
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
values = []
while (PlayListRatings[i] >= 6):
    values = PlayListRatings[i]
    i = i + 1
    print(values)

# Write your code below and press Shift+Enter to execute

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while squares[i] == 'orange':
    new_squares.append(squares[i])
    i = i + 1
print(new_squares)

A=[1,2,3]

for a in A:

    print(2*a)

x=5
while(x!=2):
  print(x)
  x=x-1

for i,x in enumerate(['A','B','C']):
    print(i+1,x)

for i in range(1,5):
    if (i==2):
        print(i)

