class Car(object):
    condition = "new"



    def __init__ (self, model, colour, mpg):
        self.model = model
        self.colour=colour
        self.mpg=mpg

    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.colour, self.model, str(self.mpg))

my_car = Car("Delorean", "silver",88)

print(my_car.model)
print(my_car.colour)
print(my_car.mpg)
print(my_car.condition)

print(my_car.display_car())