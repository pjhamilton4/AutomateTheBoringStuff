#! python3
import re, pyperclip

# TODO: Create a regex for phone numbers
phone_regex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(((\d\d\d)|(\(\d\d\d\)))?       # area code (optional)
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # separator
\d\d\d\d                    # last 4 digits
(((ext(\.)?\s) | x)          # extension word-part (optional)
(\d{2,5}))?)                  # extension (optional)
''', re.VERBOSE)

# TODO: Create a regex for email addresses
email_regex = re.compile(r'''
# some.+_thing@something.com
[a-zA-Z0-9_.+]+             # name part
@                           # @ symbol
[a-zA-Z0-9_.+]+             # domain name part
''', re.VERBOSE)

# TODO: Get the text from the clipboard
text = pyperclip.paste()

# TODO: Extract the email/phone from the text
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phone_numbers = []

for number in extracted_phone:
    all_phone_numbers.append(number[0])

print(extracted_email)
print(all_phone_numbers)

# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(all_phone_numbers) + '\n' + '\n'.join(extracted_email)
pyperclip.copy(results)
