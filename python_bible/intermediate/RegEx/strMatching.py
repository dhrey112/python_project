import re

text = "test@mail.com"
result = re.fullmatch(r"^[a-zA-Z0-9.!#$%&'*+/=?"
                      r"^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?"
                      r"(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", text)

if result is not None:
    print("VALID!")
else:
    print("INVALID")

text1 = """
Mike is 20 years old and George is 29!
My grandma is even 104 years old!
"""

text1 = re.sub(r'\d{1, 3}', "100", text1)
print(text1)

try:
    print(10 / 0)
except:
    print("Error!")
finally:
    print("Everything OK!")


