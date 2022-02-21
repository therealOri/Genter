import secrets
from string import ascii_lowercase, ascii_uppercase, digits
import os
from hashlib import blake2b
import sqlite3
import base64 as b64
from dotenv import load_dotenv
import time


from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


# I'm storing these variables in a .env file so it allows you to do whatever you want to the .env file. (Like encrypting the .env file, encoding then decoding teh stored values, idk) to make things more secure.
load_dotenv()
salt = os.getenv("SALT")
password = os.getenv("PASS") #Anything can be a password really..


key = PBKDF2(password, salt, dkLen=32)
cipher = AES.new(key, AES.MODE_CBC)



uppercase_letters = ascii_uppercase
lowercase_letters = ascii_lowercase
symbols = "!=<>'@#$%^&*()[]{},.;:-_/\\+?*|`€≡‗"
unicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿×Ø÷øÞßƒðÐı"
boxes = "░▒▓█▄▀■"
ascii_draw_box = "╣╗╝┴┬╩╦═╬"
numbers = digits
korean = "ㅂㅋㅎㅭㅱㅶㅹㅺㅿㆁㆄㆅ"
russian = "БГДЁЖИЙЛПФфЦЧШЩЪЫЬЭЮЯ"
greekU = "ΓΔΘΛΞΠΣΦΨΩ" # Greek Uppercase.
greekL = "αβγδεζηθικλμνξπρστυφχψω" # Greek Lowercase.
portuL = "ãáàâçéêíõóôúü"
portuU = "ÃÁÀÂÇÉÊÍÕÓÔÚÜ"
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
  

    
def cipherE(password):
    msg = bytes(password, 'unicode_escape')
    cipher_data = cipher.encrypt(pad(msg, AES.block_size))
    cipher_bcode = b64.b64encode(cipher_data)
    return cipher_bcode.decode()



def read_data(web):
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT passwd FROM pwd_tables WHERE website LIKE '{web}'")

    
    b64passwd = c.fetchone() # get base64 string from DB.
    if not b64passwd:
        print('Oof..nothing here but us foxos...\n')
        input('Press enter to quit...')
        quit()
    else:
        passwdE = b64.b64decode(b64passwd[0]) # Decoding the base64 bytes and giving me the aes data to decrypt.

        c.execute(f"SELECT iv FROM pwd_tables WHERE website LIKE '{web}'")
        ivD = c.fetchone()
        iv = b64.b64decode(ivD[0])
        
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        original = unpad(cipher.decrypt(passwdE), AES.block_size)
        return print(f"Password for {web}: {original.decode('unicode_escape')}")


    
def add_data(website, passwd):
    iv = cipher.iv
    b64iv = b64.b64encode(iv)
    b64iv = b64iv.decode('unicode_escape')

    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()

    c.execute(f"INSERT INTO pwd_tables VALUES ('{website}', '{cipherE(passwd)}', '{b64iv}')")
    database.commit()
    database.close()
    return print(f'"{website}" and your password has been stored/saved to the database!')



def rmv_data(website):
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()

    c.execute(f"DELETE FROM pwd_tables WHERE website LIKE '{website}'")
    database.commit()
    database.close()
    return print(f'"{website}" has been removed from the database!')



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
        salt = bytes(input('Enter phrase for salting (16 letters max): '), 'utf-8')
        clear()
        h = blake2b(key=bytes(c_key, 'utf-8'), salt=salt, digest_size=30)
        h.update(bytes(password, 'utf-8'))
        result1 = h.hexdigest()
        print(f'Password: {password}  |  Hash: {result1}\nSalt: {salt.decode()}  |  Key: {c_key}\n')
        return result1


    if option == 2:
        clear()
        gen_key = ''.join(secrets.choice(alphabet) for i in range(16))
        salt = bytes(''.join(secrets.choice(alphabet) for i in range(16)), 'utf-8')
        h = blake2b(key=bytes(gen_key, 'utf-8'), salt=salt, digest_size=30)
        h.update(bytes(password, 'utf-8'))
        result2 = h.hexdigest()
        print(f'Password: {password}  |  Hash: {result2}\nSalt: {salt.decode()}  |  Key: {gen_key}\n')
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
    #Set this flag to False if you want to use the manual way on lines 309 - 321.
    options_FLAG = True

    #Please god let there be a better way to do this....
    #(Help wanted)
    try:
        if options_FLAG == True:
            answers = ['TRUE', 'True', 'true', 'YES', 'Yes', 'yes', 'Y', 'y']
            print('Note: Pressing "Enter" will just skip and set the arguments as Fasle.\n')
            upper = input("(1/13) - Want to use uppercase letters? (y/n): ")
            if upper in answers:
                upper = True
            else:
                if not upper in answers:
                    upper = False

            lower = input("2/13) - Want to use lowercase letters? (y/n): ")
            if lower in answers:
                lower = True
            else:
                if not lower in answers:
                    lower = False

            nums = input("3/13) - Want to use numbers? (y/n): ")
            if nums in answers:
                nums = True
            else:
                if not nums in answers:
                    nums = False

            syms = input("4/13) - Want to use symbols? (y/n): ")
            if syms in answers:
                syms = True
            else:
                if not syms in answers:
                    syms = False

            kor = input("5/13) - Want to use korean characters? (y/n): ")
            if kor in answers:
                kor = True
            else:
                if not kor in answers:
                    kor = False

            rus = input("6/13) - Want to use russian characters? (y/n): ")
            if rus in answers:
                rus = True
            else:
                if not rus in answers:
                    rus = False

            GU = input("7/13) - Want to use uppercase greek letters? (y/n): ")
            if GU in answers:
                GU = True
            else:
                if not GU in answers:
                    GU = False

            GL = input("8/13) - Want to use lowercase greek letters? (y/n): ")
            if GL in answers:
                GL = True
            else:
                if not GL in answers:
                    GL = False

            PL = input("9/13) - Want to use lowercase portuguese letters? (y/n): ")
            if PL in answers:
                PL = True
            else:
                if not PL in answers:
                    PL = False

            PU = input("10/13) - Want to use uppercase portuguese letters? (y/n): ")
            if PU in answers:
                PU = True
            else:
                if not PU in answers:
                    PU = False

            spec = input("11/13) - Want to use unicode characters? (y/n): ")
            if spec in answers:
                spec = True
            else:
                if not spec in answers:
                    spec = False

            block = input("12/13) - Want to use ascii blocks? (y/n): ")
            if block in answers:
                block = True
            else:
                if not block in answers:
                    block = False

            a_box = input("13/13) - Want to use ascii boxes? (y/n): ")
            if a_box in answers:
                a_box = True
            else:
                if not a_box in answers:
                    a_box = False
        else:
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
            spec = True
            block = True
            a_box = True

    except Exception as e:
        print(f"Oops! Something went wrong...\nERROR: {e}")
        quit()
        
        
        
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
    if spec:
        all += unicode
    if block:
        all += boxes
    if a_box:
        all += ascii_draw_box
        

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


    with open(f'pass.txt', 'w') as f:
        for x in range(amount):
            password = ''.join(secrets.choice(all) for i in range(length))
            print(f'Pass: {password}  |  Hash: {d_conv(password)[0]}\nSalt: {d_conv(password)[1].decode()}  |  Key: {d_conv(password)[2]}\n', file=f)    
        print('Your newly generated random password(s) and hash info has been saved to "pass.txt".')

##-------------- ^^ Functions End ^^ --------------##




if __name__ == '__main__':
    if os.getenv("FLAG") == '#src':
        alphabet = uppercase_letters + lowercase_letters + numbers
        print('The .env file that is needed for passgen.py has not been set up yet. Setting up the file now!...')
        time.sleep(5)
        clear()
        SALT = get_random_bytes(1024)
        PASS = ''.join(secrets.choice(alphabet) for i in range(16))

        with open(".env", "w") as f:
            f.write(f"SALT={SALT}\n")
            f.write(f"PASS={PASS}")
            f.close()
        print("The .env file should now be all set up!")
        input('Press enter to exit...')
        clear()
    else:
        clear()
        try:
            option = int(input(f"{banner()}\n\nWhat would you like to do?\n\n1. Make a password?\n2. Get hash for a password?\n3. Compare hashes?\n4. Manage passwords?\n\nEnter: "))
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


        if option == 4:
            clear()
            try:
                sub_option = int(input(f"{banner()}\n\nWhat do you want to manage?\n\n1. Add password?\n2. Remove password?\n3. View password?\n\nEnter: "))
            except Exception as e:
                clear()
                print(f'Value given is not an integer.\nError: {e}\n\n')
                input('Press enter to quit...')
                clear()
                quit()

            if sub_option == 1: # Add passwords
                clear()
                web = input('What is the website/domain name you would like to store in the Database?: ')
                passwd = input('Password to save?: ')
                clear()

                add_data(web.lower(), passwd)

            if sub_option == 2: # Remove passwords
                clear()
                web_to_rmv = input('What is the website/domain name you would like to remove from the Database?: ')
                print('(This will remove the password for the website as well)')
                clear()

                rmv_data(web_to_rmv.lower())

            if sub_option == 3: # View/get passwords
                clear()
                web_to_get = input('Website domain/name for password: ')
                clear()
                read_data(web_to_get.lower())



            elif sub_option == 0 or sub_option > 3:
                clear()
                print("Incorrect value given. Please choose a valid option from the menu/list.\n\n")
                input('Press enter to quit...')
                clear()
                quit()




        elif option == 0 or option > 4:
            clear()
            print("Incorrect value given. Please choose a valid option from the menu/list.\n\n")
            input('Press enter to quit...')
            clear()
            quit()

        input('\n\nPress enter to quit...')
        quit()
