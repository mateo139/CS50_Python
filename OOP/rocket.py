class Rocket:
    def __init__(self):
        self.x = 0
        self.y = 0

    # One of the first things you do with a class is to define the _init_() method. The __init__() method sets the values for any parameters that need to be defined when an object is first created. The self part will be explained later; basically, it's a syntax that allows you to access a variable from anywhere else in the class.

    def move_up(self):
        self.y += 1


# Create a Rocket object.
my_rocket = Rocket()
print(my_rocket)

print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)
