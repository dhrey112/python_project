import re

text = '''
Mike is 20 years old and George is 29!
My grandma is even 104 years old!
'''

ages = re.findall(r"\d{1, 3}", text)
print(ages)
