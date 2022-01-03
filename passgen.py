import secrets
from string import ascii_lowercase, ascii_uppercase, digits
import os
from hashlib import blake2b


uppercase_letters = ascii_uppercase
lowercase_letters = ascii_lowercase
symbols = "!=<>'@#$%^&*()[]{},.;:-_/\\+?|`€"
numbers = digits
korean = "ㅂㅋㅎㅭㅱㅶㅹㅺㅿㆁㆄㆅ"
russian = "БГДЁЖИЙЛПФфЦЧШЩЪЫЬЭЮЯ"
greekU = "ΓΔΘΛΞΠΣΦΨΩ" # Greek Uppercase.
greekL = "αβγδεζηθικλμνξπρστυφχψω" # Greek Lowercase.
portugueseL = "ãáàâçéêíõóôúü"
portugueseU = "ÃÁÀÂÇÉÊÍÕÓÔÚÜ"
#Example |  new_list = "WHATERVER YOU WANT HERE"  | This can be named whatever you can think of, doesn't have to be "new_list". It's just what I am using for this example.
#You can add more and make it even more complex. Just make sure to update the rest of the code below.



##-------------- Functions --------------##
def banner():
    banner = """
        ██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗
        ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║
        ██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║
        ██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║
        ██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║
        ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                           
      Made by Ori#6338 | @therealOri_ | https://github.com/therealOri
    """
    return banner


def clear():
    os.system('cls||clear')


# Hashing
def hash(password: str):
    alphabet = uppercase_letters + lowercase_letters + numbers

    try:
        option = int(input(f"{banner()}\n\nHow do you want to make a key for hashing?\n\n1. Custom Key?\n2. Generate Key?\n\nEnter: "))
    except Exception as e:
        clear()
        print(f'Value given is not an integer.\nError: {e}\n\n')
        input('Press enter to quit...')
        clear()
        quit()


    if option == 1:
        clear()
        c_key = input('Enter/Load key to use for hashing: ')
        salt = bytes(input('Enter phrase for salting: '), 'utf-8')
        clear()
        h = blake2b(key=bytes(c_key, 'utf-8'), salt=salt, digest_size=30)
        h.update(bytes(password, 'utf-8'))
        result1 = h.hexdigest()
        print(f'Key: {c_key} (Save me for later, to use when hashing.)\nSalt: {salt.decode()}\nPassword: {password}\nHash: {result1}')
        return result1


    if option == 2:
        clear()
        gen_key = ''.join(secrets.choice(alphabet) for i in range(16))
        salt = bytes(''.join(secrets.choice(alphabet) for i in range(16)), 'utf-8')
        h = blake2b(key=bytes(gen_key, 'utf-8'), salt=salt, digest_size=30)
        h.update(bytes(password, 'utf-8'))
        result2 = h.hexdigest()
        print(f'Key: {gen_key} (Save me for later, to use when hashing.)\nSalt: {salt.decode()} (Save me for later, to use when hashing.)\nPassword: {password}\nHash: {result2}')
        return result2


    elif option == 0 or option > 2:
        clear()
        print("Incorrect value given. Please choose a valid option from the menu/list.\n\n")
        input('Press enter to quit...')
        clear()
        quit()
# End of Hashing


# Compare hash
def compare(phash):
    clear()
    pword = input('Password: ')
    h_key = input("Hash Key: ")
    salt = bytes(input('Salt: '), 'utf-8')

    h = blake2b(key=bytes(h_key, 'utf-8'), salt=salt, digest_size=30)
    h.update(bytes(pword, 'utf-8'))
    result = h.hexdigest()


    if phash == result:
        clear()
        return print(f"The hash you provided matches!\n\n[INFO]\nKey: {h_key}\nSalt: {salt.decode()}\nPassword: {pword}\nYour Provided Hash - (blake2b): {phash}\nHash of Password - (blake2b): {result}")

    else:
        clear()
        return print(f"The hash you provided does not match!\n\n[INFO]\nKey: {h_key}\nSalt: {salt.decode()}\nPassword: {pword}\nYour Provided Hash - (blake2b): {phash}\nHash of Password - (blake2b): {result}")
# End Compare hash




# This will always use the default key. (For when you generate passwords instead of hashing an already existing password.)
# You could also generate a key and use it here instead if you want. Or change it to whatever. Either way, it is reccomended to change the default_key and salt.
def d_conv(password):
    clear()
    default_key = 'vGb2ZPk0tsfxWy1B'
    salt = bytes('fehNc4L2GnU53RTF', 'utf-8')
    h = blake2b(key=bytes(default_key, 'utf-8'), salt=salt, digest_size=30)
    h.update(bytes(password, 'utf-8'))
    result = h.hexdigest()
    return result, salt, default_key



def main():
    upper = True
    lower = True
    nums = True
    syms = True
    kor = True
    rus = True
    GU = True
    GL = True
    PL = True
    PU = True

    all = ""

    if upper:
        all += uppercase_letters
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
    if GU:
        all += greekU
    if GL:
        all += greekL
    if PL:
        all += portuL
    if PU:
        all += portuU

    clear()
    print('Note: Please make sure to write your password(s) down or save the password(s) into a new text file before running this script again. \n\n')



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
            print(f'Pass: {password}  |  Hash: {d_conv(password)[0]}\nSalt: {d_conv(password)[1].decode()}  |  Key: {d_conv(password)[2]}\n', file=f)
            print('Your newly generated random password(s) can be found in "pass.txt".')

##-------------- ^^ Functions End ^^ --------------##




if __name__ == '__main__':
    clear()
    try:
        option = int(input(f"{banner()}\n\nWhat would you like to do?\n\n1. Make a password?\n2. Get hash for a password?\n3. Compare hashes?\n\nEnter: "))
    except Exception as e:
        clear()
        print(f'Value given is not an integer.\nError: {e}\n\n')
        input('Press enter to quit...')
        clear()
        quit()
    

    if option == 1:
        clear()
        main()


    if option == 2:
        clear()
        pword = input('What would you like to hash?: ')
        clear()
        hash(pword)
    

    if option == 3:
        clear()
        phash = input('Hash - (blake2b): ')
        clear()
        compare(phash)


    elif option == 0 or option > 3:
        clear()
        print("Incorrect value given. Please choose a valid option from the menu/list.\n\n")
        input('Press enter to quit...')
        clear()
        quit()

    input('\n\nPress enter to quit...')
    quit()
