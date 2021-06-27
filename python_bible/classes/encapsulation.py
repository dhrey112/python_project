class Persons:
    def __init__(self, name, _age):
        self.name = name
        self._age = _age

    def display(self):
        print(self.name, self._age)


p1 = Persons("Anita", 36)
p1._age = 20
p1.display()
print(p1._age)