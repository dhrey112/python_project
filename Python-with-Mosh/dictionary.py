customer ={"name": "John Smith",
           "age": 30,
           "is_verified": True}

print(customer.get("birthday", "4 Jan 1990"))

print(customer)

phone = input("phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)