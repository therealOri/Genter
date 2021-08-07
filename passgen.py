import secrets
from string import ascii_lowercase, ascii_uppercase, digits 

uppercase_letters = ascii_uppercase
lowercase_letters = ascii_lowercase
symbols = "!=<>'@#$%^&*()[]{},.;:-_/\\+?*|`~"
numbers = digits
korean = "ㅂㅋㅎㅭㅱㅶㅹㅺㅿㆁㆄㆅ"
russian = "БГДЁЖИЙЛПФфЦЧШЩЪЫЬЭЮЯ"
#Example |  new_list = "WHATERVER YOU WANT HERE"  | This can be named whatever you can think of, doesn't have to be "new_list". It's just what I am using for this example.
#You can add more and make it even more complex. Just make sure to update the rest of the code below.


#Here we would add "new" to the line below with one more True. | the word doesn't have to be "new", it can be anything you want. It's just what I am using for this example.
#All are true so everything will be used in genrating your password. Setting one or more to False will exculde the False one(s) fron the generation.
upper = True
lower = True
nums = True
syms = True
kor = True
rus = True



all = ""

if upper:
    all += uppercase_letters #if upper = True it will be used and will add letters to all = "". Same for the others below.
if lower:
    all += lowercase_letters
if nums:
    all += numbers
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


# These Try blocks are to catch any errors such as not entering a number/integer.
try:
    length = int(input('How long do you want your password(s)?: '))
except Exception as e:
    print(f'\nOops..The value you gave me is not a number/integer.\n[Error]: {e}')
    quit()
    
    
try:
    amount = int(input('How many do you want generated?: '))
except Exception as e:
    print(f'\nOops..The value you gave me is not a number/integer.\n[Error]: {e}')
    quit()



print('\n')

with open('pass.txt', 'w') as f:
    for x in range(amount):
        password = ''.join(secrets.choice(all) for i in range(length))
        print(password, file=f)
        print("Here is your newly generated random password:", password)
