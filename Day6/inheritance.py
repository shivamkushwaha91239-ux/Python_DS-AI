class vehicle:
    #the initializer method runs automatically when an object of the class is created
    def __init__(self, brand, year):
        self.brand = brand # public attribute: can be accessed from outside the class

        self.year = year # public attribute: can be accessed from outside the class

#define a method to display the vehicle information
    def display_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")  
    
#define a child that automatically copy everything from the parent class
class car(vehicle):
    # "pass" is used to indicate that the class has no additional attributes or methods
    pass

#create an new object of the car class
#then automatically calls the __init_ method inherited from the parent class vehicle
my_car = car("Toyota", 2020) # create an object of the car class

print(my_car.brand) # access the public attribute brand from the parent class
print(my_car.year) # access the public attribute year from the parent class

print(my_car.display_info()) # call the method display_info() inherited from the parent class



# create a animal class inheerit their properties and methods to the child class

class animal:
    def sound(self):
        print("Animal makes a sound")

# create an child class dog that inherits from the parent class animal
class Dog(animal):
    def bark(self):
        print("Dog barks")

# create an object of the dog class
d = Dog() # create an object of the dog class
d.sound() # call the sound() method of the dog class, which overrides the parent class method
d.bark() # call the bark() method of the dog class