import matplotlib.pyplot as plt


Ratings = [10,9,6,5,10,8,9,6,2]

Ratings.sort()

print(Ratings)

Ratings.reverse()

print(Ratings)

#Creat a class
class Circle(object):
    #Data attributes used to initialize each instance of the class
    def __init__(self,radius, color):
        self.radius = radius;
        self.color = color;

Redcircle = Circle(10, "red")
print(Redcircle.radius)
print(Redcircle.color)
Redcircle.color = "blue"
print(Redcircle.color)

#Add method to the class
class Circle(object):
    #Data attributes used to initialize each instance of the class
    def __init__(self,radius, color):
        self.radius = radius;
        self.color = color;
    def add_radius(self,r):
        self.radius = self.radius + r
        return(self.radius)

C1 = Circle(2,'red')
C1.add_radius(8)
#so the radius now is changed from 2 to 10 by having a method inside the class
print(C1.radius)

#obtaining the list of data attributes the method associated with the class
#Objects method and attributes are the one without under score
print(dir(C1))

#Creat and draw a circle
class Circle(object):
    # Constructor
    def __init__(self,radius=3, color='blue'):
        self.radius = radius;
        self.color = color;
    # Method
    def add_radius(self,r):
        self.radius = self.radius + r
        return(self.radius)
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0), radius = self.radius, fc = self.color))
        plt.axis('scaled')
        plt.show()

C1 = Circle(5, "red")
C1.drawCircle()


class Rectangle(object):

    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height
        self.width = width
        self.color = color

    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()

R1 = Rectangle(2,4,"blue")
R1.drawRectangle()

#Example

class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p1=Points("A","B")
p1.print_point()

class Points(object):

  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p2=Points(1,2)

p2.x='A'

p2.print_point()