import random
import sys

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
symbols = "!@#$%^&*()[]{},.;:-_/\\+?*|`~"
digits = "0123456789"


upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 40
amount = 1

for x in range(amount):
    password = "".join(random.sample(all, length))
    with open('pass.txt', 'w') as f:
        print(f'Your new password: {password}', file=f)
    print(f"Here is your newly generated random password: {password}")
    print("\n Your password has been saved to pass.txt. Please make sure to write it down or hash/encrypt the text.")