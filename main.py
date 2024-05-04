import random

text = '0123456789'
password = ''

for i in range(8):
    password += random.choice(text)

print(password)