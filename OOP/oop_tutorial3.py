class Dog:

    # Use class attributes to define properties that should have the same value for every class instance.
    # Use instance attributes for properties that vary from one instance to another.

    # class attribute
    species = "mammal"

    def __init__(self, name, age):  #  instance attributes are between ()
        self.name = name
        self.age = age

    # instance method
    def __str__ (self):
        return f"{self.name} is {self.age} years old"
    
    # another instance method
    def speak (self, sound):
        return f"{self.name} says {sound}"


dog1 = Dog("Markus", "3")
dog2 = Dog("Henry", "4")
print (dog1.__str__())
print (dog1.speak("woof"))
