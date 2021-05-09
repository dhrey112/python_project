import re
import pyperclip

phoneregex = re.compile(r'''  ( ( (\d\d\d)|(\(\d\d\d\)))? # area code
(\s|-)?     # first seperator
\d\d\d-\d\d\d\d
(((ext(\.)?\s)|x)(\d{2,5}))?)''', re.VERBOSE)
print(phoneregex.findall("566-555-3333 and 888-9999"))

email = re.compile(r'''[a-zA-Z0-9+_.]+[@a-zA-Z0-9+_.]+''', re.VERBOSE)
print(email.findall("nigeria@africa.com"))

text = pyperclip.paste()
extracted_phone = phoneregex.findall(text)
extracted_email = email.findall(text)

all_phone_numbers = [phone_number[0] for phone_number in extracted_phone]

print(all_phone_numbers)
print(extracted_email)

results = 'our list is ready'+"\n".join(all_phone_numbers)+"\n"+"\n".join(extracted_email)
pyperclip.copy(results)
