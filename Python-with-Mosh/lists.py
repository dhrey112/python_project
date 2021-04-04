name = ['Bob', 'Mosh', 'Goke']
print(name[-1])



number = [45, 1000, 8, 9, 500, 500, 3, 300, 5, 6]
max = number[0]

for num in number:
    if num > max:
        max = num

print(max)

min = number[0]
for num in number:
    if num < min:
        min = num
print(min)
