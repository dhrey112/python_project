class Person:

    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age

    def talk(self):
        print(f"Hi, I am {self.person_name}")

    def birthday(self):
        self.person_age += 1

    def getName(self):
        return self.person_name


person = Person("Dare", 6)
person.talk()
print(person.person_name)
person.birthday()
print(person.person_age)