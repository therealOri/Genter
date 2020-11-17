import random
import sys

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower() #uppercase_letters.lower() lowercases everything in uppercase_letters and uses that instead of just writing out another list.
symbols = "!@#$%^&*()[]{},.;:-_/\\+?*|`~"
digits = "0123456789"
#Example |  new_list = "WHATERVER YOU WANT HERE"  | This can be named whatever you can think of, doesn't have to be "new_list". It's just what I am using for this example.
#You can add more and make it even more complex. Just make sure to update the rest of the code below.


#Here we would add "new" to the line below with one more True. | the word doesn't have to be "new", it can be anything you want. It's just what I am using for this example.
upper, lower, nums, syms = True, True, True, True #All are true so everything will be used in genrating your password. Setting one or more to False will exculde the False one(s) fron the generation.

all = ""

if upper:
    all += uppercase_letters #if upper = True it will be used and will add letters to all = "". Same for the others below.
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols
#if new:
#    all += new_list
#The above here is an example of what you would do if you wanted to add more.

length = 40 #How long you want the password to be. (Longer and more complex, the better) You may need to change this depending on the limits some websites have for how long a password should be.
amount = 1 #How many passwords you want generated.

for x in range(amount):
    password = "".join(random.sample(all, length))
    with open('pass.txt', 'w') as f:
        print(f'Your new password: {password}', file=f)
    print(f"Here is your newly generated random password: {password}")
    print("\n Your password has been saved to pass.txt. Please make sure to write it down or hash/encrypt the password/text in pass.txt.")
