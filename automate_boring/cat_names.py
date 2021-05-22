cat_names = []

while True:
    print("Enter the name of cat "+ str(len(cat_names) + 1) + " or enter nothing to quit")
    name = input(">> ")

    if name == "":
        break
    cat_names.append(name)
print(cat_names)

print(f"We collected {len(cat_names)} cats in total and names are:")
for i in cat_names:
    print(i)
    