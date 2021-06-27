# OVERWRITING METHODS

"""When one class inherits from another class, it can overwrite its methods.
This is automatically done by defining a method with the same name and
the same amount of parameters."""


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some sound")


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)

    def make_sound(self):
        print("{} Bark!"
              .format(self.name))


class Cat(Animal):
    def __init__(self, name, age):
        super(Cat, self).__init__(name)
        self.age = age

    def make_sound(self):
        print("\nMeew!")

    def show_age(self):
        print("{}'s age is {} years old."
              .format(self.name, self.age))


obj_dog = Dog("Wicked")
print(obj_dog.name)
obj_dog.make_sound()

obj_cat = Cat("Spur", "5")
obj_cat.make_sound()
obj_cat.show_age()

