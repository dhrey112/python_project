numbers = [5, 6, 3, 8, 8, 9, 20]

print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.remove(5)
print(numbers)
numbers.clear()
print(numbers)
numbers = [5, 6, 3, 8, 8, 9]
numbers.pop()
print(numbers)
numbers.index(3)
print(numbers)
print(100 in numbers)
numbers.count(8)
print(numbers)
print(numbers.sort())
print(numbers.reverse())
numbers2 = numbers.copy()
print(numbers2)


unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)