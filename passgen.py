import random
import sys

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower() #uppercase_letters.lower() lowercases everything in uppercase_letters and uses that instead of just writing out another list.
symbols = "!@#$%^&*()[]{},.;:-_/\\+?*|`~"
digits = "0123456789"
korean = "ㅂㅋㅎㅭㅱㅶㅹㅺㅿㆁㆄㆅ"
russian = "БГДЁЖИЙЛПФфЦЧШЩЪЫЬЭЮЯ"
#Example |  new_list = "WHATERVER YOU WANT HERE"  | This can be named whatever you can think of, doesn't have to be "new_list". It's just what I am using for this example.
#You can add more and make it even more complex. Just make sure to update the rest of the code below.


#Here we would add "new" to the line below with one more True. | the word doesn't have to be "new", it can be anything you want. It's just what I am using for this example.
upper, lower, nums, syms, kor, rus = True, True, True, True, True, True #All are true so everything will be used in genrating your password. Setting one or more to False will exculde the False one(s) fron the generation.

all = ""

if upper:
    all += uppercase_letters #if upper = True it will be used and will add letters to all = "". Same for the others below.
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols
if kor:
    all += korean
if rus:
    all += russian
#if new:
#    all += new_list
#The above here is an example of what you would do if you wanted to add more.


print('Note: Your password(s) will be saved to pass.txt.\nPlease make sure to write it/them down or hash/encrypt the password(s) into a new text file before running this script again. \n')
print('\n')

with open('pass.txt', 'w'): pass #Clears txt file contents before writing into it with new passwords..or password.

length = input('How long do you want your password(s)?: ') #How long you want the password to be. (Longer and more complex, the better) You may need to change this depending on the limits some websites have for how long a password should be.
amount = input('How many do you want generated?: ') #How many passwords you want generated.

print('\n')

for x in range(int(amount)):
    password = "".join(random.sample(all, int(length))) #"int" was added/specified for it to know the variables are numbers/integers. And won't work if you type/use strings when given the option to type.
    with open('pass.txt', 'a') as f:
        print(f'{password}', file=f)
    print(f"Here is your newly generated random password: {password}")

