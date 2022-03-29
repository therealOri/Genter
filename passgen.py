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
unicode = "¡¢£¤¥¦§¨©ª«¬®™️¯°±²³´µ¶·¸¹º»¼½¾¿×Ø÷øÞßƒðÐıæ𐐘𐑀ඞඕᔕ"
emojis = "⚔☣️⚛️〰️🗝️🔒⛓️"
ascii_boxes = "░▒▓█▄▀■"
ascii_draw_box = "╣╗╝┴┬╩╦═╬"
numbers = digits
korean = "ㅂㅋㅎㅭㅱㅶㅹㅺㅿㆁㆄㆅ"
russian = "БГДЁЖИЙЛПФфЦЧШЩЪЫЬЭЮЯ"
greekU = "ΓΔΘΛΞΠΣΦΨΩ" # Greek Uppercase.
greekL = "αβγδεζηθικλμνξπρστυφχψω" # Greek Lowercase.
portuL = "ãáàâçéêíõóôúü"
portuU = "ÃÁÀÂÇÉÊÍÕÓÔÚÜ"
hindi = "ऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऽॐॠॡ।॥०१२३४५६७८९॰ॲॳॴॵॶॷॹॺॻॼॽॾॿೱೲऀँंःऺऻ़ािीुूृॄॅॆेैॉॊोौ्ॎॏ॒॑॓॔ॕॖॗॢॣ"
arabic = "شسژزڑرذڈدخحچجثٹتپبآاےیھہوںنملگکقفغعظطضصءئؤڙڐٿ٘ ًَُِّٰٗ؟،۰۱۲۳۴۵۶۷۸۹"
#Example |  new_list = "WHATERVER YOU WANT HERE"  | This can be named whatever you can think of, doesn't have to be "new_list". It's just what I am using for this example.
#You can add more and make it even more complex. Just make sure to update the rest of the code below.



##-------------- Functions --------------##
def banner():
    return """
        ██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗
        ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║
        ██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║
        ██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║
        ██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║
        ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                           
      Made by Ori#6338 | @therealOri_ | https://github.com/therealOri
    """


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


    if b64passwd := c.fetchone():
        passwdE = b64.b64decode(b64passwd[0]) # Decoding the base64 bytes and giving me the aes data to decrypt.

        c.execute(f"SELECT iv FROM pwd_tables WHERE website LIKE '{web}'")
        ivD = c.fetchone()
        iv = b64.b64decode(ivD[0])

        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        original = unpad(cipher.decrypt(passwdE), AES.block_size)
        return print(f"Password for {web}: {original.decode('unicode_escape')}")
    else:
        print('Oof..nothing here but us foxos...')


    
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
    
    while True:
        try:
            option = int(input(f"{banner()}\n\nHow do you want to make a key for hashing?\n\n1. Custom Key?\n2. Generate Key?\n\nEnter: "))
        except Exception as e:
            clear()
            print(f'Value given is not an integer.\nError: {e}\n\n')
            input('Press enter to continue...')
            clear()
            continue


        if option == 1:
            clear()
            c_key = input('Enter/Load key to use for hashing: ')
            salt = bytes(input('Enter phrase for salting (16 letters max): '), 'utf-8')
            clear()
            result1 = blake2b(bytes(password, 'utf-8'), key=bytes(c_key, 'utf-8'), salt=salt, digest_size=32).hexdigest()

            print(f'Password: {password}  |  Hash: {result1}\nSalt: {salt.decode()}  |  Key: {c_key}\n')
            return result1


        if option == 2:
            clear()
            gen_key = ''.join(secrets.choice(alphabet) for _ in range(25))
            salt = bytes(''.join(secrets.choice(alphabet) for _ in range(16)), 'utf-8')
            
            result2 = blake2b(bytes(password, 'utf-8'), key=bytes(gen_key, 'utf-8'), salt=salt, digest_size=32).hexdigest()
            print(f'Password: {password}  |  Hash: {result2}\nSalt: {salt.decode()}  |  Key: {gen_key}\n')
            return result2


        elif option == 0 or option > 2:
            clear()
            print("Incorrect value given. Please choose a valid option from the menu/list.\n\n")
            input('Press enter to continue...')
            clear()
# End of Hashing




# This if for when you generate passwords.
def d_conv(password):
    alphabet = uppercase_letters + lowercase_letters + numbers
    clear()
    
    default_key = ''.join(secrets.choice(alphabet) for _ in range(25)) #Can be as long as you want.
    salt = bytes(''.join(secrets.choice(alphabet) for _ in range(16)), 'utf-8') #MUST be 16 or less.
    
    result = blake2b(bytes(password, 'utf-8'), key=bytes(default_key, 'utf-8'), salt=salt, digest_size=32).hexdigest()
    return result, salt, default_key



def main():
    #Set this flag to False if you want to use the manual way on lines 244 - 259.
    options_FLAG = False

    #Please god let there be a better way to do this....
    #(Help wanted)
    # Something, perhaps am unput with 15 variables that you can set via yynnynnyyyyynyn..Idk
    try:
        if options_FLAG:
            answers = ['TRUE', 'True', 'true', 'YES', 'Yes', 'yes', 'Y', 'y']
            print('Note: Pressing "Enter" will just skip and set the arguments as Fasle.\n')

            upper = input("(1/15) - Want to use uppercase letters? (y/n): ")
            upper = upper in answers

            lower = input("(2/15) - Want to use lowercase letters? (y/n): ")
            lower = lower in answers

            nums = input("(3/15) - Want to use numbers? (y/n): ")
            nums = nums in answers

            syms = input("(4/15) - Want to use symbols? (y/n): ")
            syms = syms in answers

            kor = input("(5/15) - Want to use korean characters? (y/n): ")
            kor = kor in answers

            rus = input("(6/15) - Want to use russian characters? (y/n): ")
            rus = rus in answers

            GU = input("(7/15) - Want to use uppercase greek letters? (y/n): ")
            GU = GU in answers

            GL = input("(8/15) - Want to use lowercase greek letters? (y/n): ")
            GL = GL in answers

            PL = input("(9/15) - Want to use lowercase portuguese letters? (y/n): ")
            PL = PL in answers

            PU = input("(10/15) - Want to use uppercase portuguese letters? (y/n): ")
            PU = PU in answers

            spec = input("(11/15) - Want to use unicode characters? (y/n): ")
            spec = spec in answers

            block = input("(12/15) - Want to use ascii blocks? (y/n): ")
            block = block in answers

            a_box = input("(13/15) - Want to use ascii boxes? (y/n): ")
            a_box = a_box in answers
            
            hin = input("(14/15) - Want to use hindi letters? (y/n): ")
            hin = hin in answers
            
            arab = input("(15/15) - Want to use arabic letters? (y/n): ")
            arab = arab in answers
            
            emote = input("(15/15) - Want to use arabic letters? (y/n): ")
            emote = emote in answers
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
            hin = True
            arab = True
            emote = True
            
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
        all += ascii_boxes
    if a_box:
        all += ascii_draw_box
    if hin:
        all += hindi
    if arab:
        all += arabic
    if emote:
        all += emojis

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
        for _ in range(amount):
            password = ''.join(secrets.choice(all) for _ in range(length))
            print(f'Pass: {password}  |  Hash: {d_conv(password)[0]}\nSalt: {d_conv(password)[1].decode()}  |  Key: {d_conv(password)[2]}\n', file=f)
        print('Your newly generated random password(s) and hash info has been saved to "pass.txt".\n\n\n')
        input('Press enter to continue...')
        clear()
        
        

def show_pass():
    clear()
    with open('pass.txt', 'r') as f:
        result = f.read()
        return print(result)

    
def clr_pass():
    clear()
    with open('pass.txt', 'r+') as f:
        f.truncate(0)        

##-------------- ^^ Functions End ^^ --------------##




if __name__ == '__main__':
    if os.getenv("FLAG") == '#src':
        alphabet = uppercase_letters + lowercase_letters + numbers
        print('The .env file that is needed for passgen.py has not been set up yet. Setting up the file now!...')
        time.sleep(5)
        clear()
        SALT = get_random_bytes(1024)
        PASS = ''.join(secrets.choice(alphabet) for _ in range(16))

        with open(".env", "w") as f:
            f.write(f"SALT={SALT}\n")
            f.write(f"PASS={PASS}")
            f.close()
        print("The .env file should now be all set up!")
        input('Press enter to exit...')
        clear()
    else:
        while True:
            clear()
            try:
                option = int(input(f"{banner()}\n\nWhat would you like to do?\n\n1. Make a password?\n2. Get hash for a password?\n3. Manage passwords?\n4. Show pass.txt?\n5. Clear pass.txt?\n6. Quit?\n\nEnter: "))
            except Exception as e:
                clear()
                print(f'Value given is not an integer.\nError: {e}\n\n')
                input('Press enter to continue...')
                clear()
                continue


            if option == 1:
                clear()
                main()


            if option == 2:
                clear()
                pword = input('What would you like to hash?: ')
                clear()
                hash(pword)
                input('Press enter to continue...')
                clear()


            if option == 3:
                clear()
                while True:
                    try:
                        sub_option = int(input(f"{banner()}\n\nWhat do you want to manage?\n\n1. Add password?\n2. Remove password?\n3. View password?\n4. Back?\n\nEnter: "))
                    except Exception as e:
                        clear()
                        print(f'Value given is not an integer.\nError: {e}\n\n')
                        input('Press enter to continue...')
                        clear()
                        continue

                    if sub_option == 1: # Add passwords
                        clear()
                        web = input('What is the website/domain name you would like to store in the Database?: ')
                        passwd = input('Password to save?: ')
                        clear()
                        add_data(web.lower(), passwd)
                        input('\n\nPress enter to continue...')
                        clear()

                    if sub_option == 2: # Remove passwords
                        clear()
                        web_to_rmv = input('What is the website/domain name you would like to remove from the Database?: ')
                        print('(This will remove the password for the website as well)')
                        clear()

                        rmv_data(web_to_rmv.lower())
                        input('\n\nPress enter to continue...')
                        clear()

                    if sub_option == 3: # View/get passwords
                        clear()
                        web_to_get = input('Website domain/name for password: ')
                        clear()
                        read_data(web_to_get.lower())
                        input('\n\nPress enter to continue...')
                        clear()

                    if sub_option == 4:
                        break


                    elif sub_option == 0 or sub_option > 4:
                        clear()
                        print("Incorrect value given. Please choose a valid option from the menu/list.\n\n")
                        input('Press enter to quit...')
                        clear()
                        



            
            if option == 4:
                show_pass()
                input('Press enter to continue...')
                clear()            
            
            if option == 5:
                clr_pass()
                print("pass.txt has been wiped clean.\n\n")
                input('Press enter to continue...')
                clear()
             
            if option == 6:
                clear()
                quit()

            
            elif option == 0 or option > 6:
                clear()
                print("Incorrect value given. Please choose a valid option from the menu/list.\n\n")
                input('Press enter to continue...')
                clear()
                
