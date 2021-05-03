for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

number = [5, 2, 5, 2, 2]
for x_count in number:
    output = "".join('x' for _ in range(x_count))
    print(output)
