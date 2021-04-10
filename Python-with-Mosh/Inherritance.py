class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):  # Inheritance
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog = Dog()
dog.bark()

cat = Cat()
cat.walk()