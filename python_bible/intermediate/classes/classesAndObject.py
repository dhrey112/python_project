# CREATING CLASSES
class Car:
    # CLASS VARIABLES
    amount_cars = 0

    # CONSTRUCTOR
    def __init__(self, manufacturer, model, hp):
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp

        Car.amount_cars += 1

    # ADDING FUNCTIONS
    def print_info(self):
        print("Manufacturer: {}, Model: {}, HP: {}"
              .format(self.manufacturer,
                      self.model,
                      self.hp))

    def print_car_amount(self):
        print("Amount: {}"
              .format(Car.amount_cars))

    # DESTRUCTORS
    def __del__(self):
        print("Object gets deleted")
        Car.amount_cars -= 1


# CREATING OBJECTS
myCar1 = Car("Tesla", "Model X", 525)
myCar2 = Car("BMW", "X3", 200)
myCar3 = Car("VW", "Golf", 100)
myCar4 = Car("Porsche", "911", 520)

# del myCar3

"""Notice that all the objects get deleted automatically when our program ends.
But we can manually delete them before that happens by using the del
keyword.
"""
# myCar1.print_info()
# myCar1.print_car_amount()


# HIDDEN ATTRIBUTES
class MyClass:
    def __init__(self):
        self.__hidden = "hello"
        print(self.__hidden) # Will work


m1 = MyClass()
print(m1.__hidden) # Doesn't Work