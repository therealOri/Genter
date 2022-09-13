#Imports
import base64 as b64
import beaupy
from hashlib import blake2b
import json
from ocryptor import oCrypt
import os
import secrets
import sqlite3
from string import ascii_lowercase, ascii_uppercase, digits


#AES stoof
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

#KeyGen
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


#Languages
uppercase_letters = ascii_uppercase
lowercase_letters = ascii_lowercase
symbols = "!=<>'@#$%^&*()[]{},.;:-_/\\+?*|`€≡‗"
unicode = "¡¢£¤¥¦§¨©ª«¬®™️¯°±²³´µ¶·¸¹º»¼½¾¿×Ø÷øÞßƒðÐıæ𐐘𐑀ඞඕᔕ"
emojis = "⚔☣️⚛️〰️🗝️🔒⛓️✨🫠🫧🫥💢"
ascii_boxes = "░▒▓█▄▀■"
ascii_draw_box = "╣╗╝┴┬╩╦═╬"
numbers = digits
korean = "ㅂㅋㅎㅭㅱㅶㅹㅺㅿㆁㆄㆅ"
russian = "БГДЁЖИЙЛПФфЦЧШЩЪЫЬЭЮЯ"
chinese = "诶比西迪伊尺杰大水开勒哦屁吉吾儿诶比西迪伊弗吉尺艾弗吉杰屁吉吾儿?八九十开勒马娜哦月人马娜口"
greekU = "ΓΔΘΛΞΠΣΦΨΩ" # Greek Uppercase.
greekL = "αβγδεζηθικλμνξπρστυφχψω" # Greek Lowercase.
portuL = "ãáàâçéêíõóôúü"
portuU = "ÃÁÀÂÇÉÊÍÕÓÔÚÜ"
hindi = "ऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऽॐॠॡ।॥०१२३४५६७८९॰ॲॳॴॵॶॷॹॺॻॼॽॾॿೱೲऀँंःऺऻ़ािीुूृॄॅॆेैॉॊोौ्ॎॏ॒॑॓॔ॕॖॗॢॣ"
arabic = "شسژزڑرذڈدخحچجثٹتپبآاےیھہوںنملگکقفغعظطضصءئؤڙڐٿ٘ ًَُِّٰٗ؟،۰۱۲۳۴۵۶۷۸۹"
amharic = "ሀሁሂሃሄህሆሎልሌላሊሉለሐሑሒሓሔሕሖሞምሜማሚሙመሠሡሢሣሤሥሦሮርሬራሪሩረሰሱሲሳሴስሶሾሽሼሻሺሹሸቀቁቂቃቄቅቆቦብቤባቢቡበቨቩቪቫቬቭቮቶትቴታቲቱተቸቹቺቻቼችቾኆኅኄኃኂኁኀነኑኒናኔንኖኞኝኜኛኚኙኘአኡኢኣኤእኦኮክኬካኪኩከኸኹኺኻኼኽኾዎውዌዋዊዉወዐዑዒዓዔዕዖዞዝዜዛዚዙዘዠዡዢዣዤዥዦዮይዬያዪዩየደዱዲዳዴድዶጆጅጄጃጂጁጀገጉጊጋጌግጎጦጥጤጣጢጡጠጨጩጪጫጬጭጮጶጵጴጳጲጱጰጸጹጺጻጼጽጾፆፅፄፃፂፁፀፈፉፊፋፌፍፎፖፕፔፓፒፑፐ፩፪፫፬፭፮፯፰፱፲፳፴፵፶፷፸፹፺፻፼፡።፣፤፥"
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



#Make master key for encrypting stuff.
def keygen(master):
    salt = os.urandom(16)

    # derive
    kdf = PBKDF2HMAC(
        algorithm=hashes.BLAKE2b(digest_size=64),
        length=72,
        salt=salt,
        iterations=1562174,
    )
    key = kdf.derive(master)
    bkey = b64.b64encode(key) #Base64 encode the bytes. (We decode this before encrypting, using bytes instead of the base64 encoded string.)
    return bkey.decode()




# CLEANING
## ------------------------------------------------------------------------ ##
def clear():
    os.system('cls||clear')


# Cleaning up files.
def cleanup():
    # Remove current pwords.pgen db.
    if os.path.isfile('pwords.pgen'):
        os.remove('pwords.pgen')
    else:
        pass

    # Rename new database to the name of the original database.
    if os.path.isfile('pwords2.pgen'):
        os.rename('pwords2.pgen', 'pwords.pgen')
    else:
        pass
## ------------------------------------------------------------------------ ##
  






# ENCRYPTION STUFF
## ------------------------------------------------------------------------ ##

# Encrypting the passwords with master key and AES encryption.
def stringME(password, master_key, salt):
    key = PBKDF2(master_key, salt)
    rb = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, rb)
    cipher_data = b64.b64encode(rb + cipher.encrypt(pad(password.encode('unicode_escape'), AES.block_size)))
    return cipher_data.decode()


#Decrypting the passwords with master key and AES encryption.
def stringMD(passw, master_key, salt):
    passwdE = b64.b64decode(passw) # Decoding the base64 bytes and giving me the aes data to decrypt.
    try:
        key = PBKDF2(master_key, salt)
        cipher = AES.new(key, AES.MODE_CBC, passwdE[:AES.block_size])
        d_cipher_data = unpad(cipher.decrypt(passwdE[AES.block_size:]), AES.block_size)
    except Exception as e:
        strd_e = f'The provided credentials do not match what was was used to encrypt the data...\nError: {e}'
        raise Exception(strd_e) from None
    return d_cipher_data.decode('unicode-escape')



#Reading a password for selected domain/website
def readMD(web, master_key, salt):
    d_master_key = b64.b64decode(master_key)
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT passwd FROM pwd_tables WHERE website LIKE '{web}'")

    if b64passwd := c.fetchone():
        passwdE = b64.b64decode(b64passwd[0])
        try:
            key = PBKDF2(d_master_key, salt)
            cipher = AES.new(key, AES.MODE_CBC, passwdE[:AES.block_size])
            d_cipher_data = unpad(cipher.decrypt(passwdE[AES.block_size:]), AES.block_size)
        except Exception as e:
            strd_e = f'The provided credentials do not match what was was used to encrypt the data...\nError: {e}'
            raise Exception(strd_e) from None
        return print(f"Password for {web}: {d_cipher_data.decode('unicode-escape')}")
    else:
        print('Oof..nothing here but us foxos...')




# Add and remove data from database.
def add_data(website, passwd, notes, master_key, salt):
    b64_note = b64.b64encode(notes.encode('unicode-escape'))
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT website FROM pwd_tables")
    sites = c.fetchall()
    ldb = str(sites).replace("(", "").replace(",)", "").replace("'", "")
    dlist = ldb.strip('][').split(', ')

    if website in dlist:
        return print(f'[Warning] - A website entry with the name of "{website}" exists in database already.\nTo avoid breaking the "reading passwords" functionality, please change the name slightly.')
    if not website:
        return print('I need a domain/website to add to the database...\n[Error]: "web" can not be empty.')
    else:
        c.execute(f"INSERT INTO pwd_tables VALUES ('{website}', '{stringME(passwd, master_key, salt)}', '{b64_note.decode('unicode-escape')}')")
        database.commit()
        database.close()
        return print(f'"{website}" and your password has been stored/saved to the database!')



def rmv_data(website):
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT website FROM pwd_tables")
    sites = c.fetchall()
    ldb = str(sites).replace("(", "").replace(",)", "").replace("'", "")
    dlist = ldb.strip('][').split(', ')

    if website in dlist:
        c.execute(f"DELETE FROM pwd_tables WHERE website LIKE '{website}'")
        database.commit()
        database.close()
        return print(f'"{website}" has been removed from the database!')
    else:
        return print(f'"{website}" is not a valid option or does not exist.')
## ------------------------------------------------------------------------ ##







# OTHER STUFF
## ------------------------------------------------------------------------ ##
# Hashing
def hash(password: str):
    alphabet = uppercase_letters + lowercase_letters + numbers
    
    while True:
        try:
            option = int(input(f"{banner()}\n\nHow do you want to make a key for hashing?\n\n1. Custom Key?\n2. Generate Key?\n3. Quit?\n\nEnter: "))
        except Exception as e:
            clear()
            print(f'Value given is not an integer.\nError: {e}\n\n')
            input('Press "enter" to continue...')
            clear()
            continue


        if option == 1:
            clear()
            print('[Note]: Press "q" to go back.\n')
            c_key = input('Enter/Load key to use for hashing: ')
            if c_key.lower() == 'q':
                clear()
                continue

            try:
                salt = input('Enter phrase for salting (16 letters max): ')
                if salt.lower() == 'q':
                    clear()
                    continue

                salt = bytes(salt, 'utf-8')
                clear()
                result1 = blake2b(bytes(password, 'utf-8'), key=bytes(c_key, 'utf-8'), salt=salt, digest_size=32).hexdigest()
            except Exception as e:
                clear()
                print(f'Oops..An error has occured.\n[Error]: {e}')
                input('\nPress "enter" to continue...')
                clear()
                continue

            print(f'Password: {password}  |  Hash: {result1}\nSalt: {salt.decode()}  |  Key: {c_key}\n')
            return result1


        if option == 2:
            clear()
            gen_key = ''.join(secrets.choice(alphabet) for _ in range(25))
            salt = bytes(''.join(secrets.choice(alphabet) for _ in range(16)), 'utf-8')
            
            result2 = blake2b(bytes(password, 'utf-8'), key=bytes(gen_key, 'utf-8'), salt=salt, digest_size=32).hexdigest()
            print(f'Password: {password}  |  Hash: {result2}\nSalt: {salt.decode()}  |  Key: {gen_key}\n')
            return result2

        if option == 3:
            clear()
            return None

        elif option < 1 or option > 3:
            clear()
            print("Incorrect value given. Please choose a valid option from the menu/list.\n\n")
            input('Press "enter" to continue...')
            clear()




# For automatically hashing the newly generated password in the main function.
def d_conv(password):
    alphabet = uppercase_letters + lowercase_letters + numbers
    clear()
    
    default_key = ''.join(secrets.choice(alphabet) for _ in range(25)) #Can be as long as you want.
    salt = bytes(''.join(secrets.choice(alphabet) for _ in range(16)), 'utf-8') #MUST be 16 or less.
    
    result = blake2b(bytes(password, 'utf-8'), key=bytes(default_key, 'utf-8'), salt=salt, digest_size=32).hexdigest()
    return result, salt, default_key


# config.json file loading.
def j_load():
    with open('config.json') as f:
        data = json.load(f)
        options_flag = data['options_flag']
        secure_prompts = data['secure_prompts']
    return options_flag, secure_prompts


# Showing contents of pass.txt and clearing it.
def show_pass():
    clear()
    with open('pass.txt', 'r') as f:
        result = f.read()
        if not result:
            return None
        else:
            return result
        
def clr_pass():
    clear()
    with open('pass.txt', 'r+') as f:
        f.truncate(0)


# Reading passwords functinality.
def domains():
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT website FROM pwd_tables")
    sites = c.fetchall()
    ldb = str(sites).replace("(", "").replace(",)", "").replace("'", "")
    dlist = ldb.strip('][').split(', ')

    c.execute(f"SELECT notes FROM pwd_tables")
    notes = c.fetchall()

    clean_list = []
    for x in notes:
        try:
            cl = b64.b64decode(x[0])
            clean_list.append(cl.decode())
        except Exception:
            clean_list.append(x[0])

    
    if not sites:
        print("Hmmm...Maybe you should add something to the database first. ^-^")
    else:
        for d,n in zip(dlist, clean_list):
            with open('.lst', 'a') as f:
                f.writelines(f"{d}  [{n}]\n")


def read():
    clear()
    domains()
    try:
        with open(".lst", "r+") as f:
            data = f.read()
            print(data)
            f.truncate(0)
            f.close()

        os.remove(".lst")
        web_to_get = input('-----------------------------------------------------\nPress "q" to go back/quit.\n\nWebsite domain/name for password: ')
        clear()
        if web_to_get.lower() == 'q':
            return web_to_get.lower()
        else:
            if j_load()[1] == True:
                master_key = beaupy.prompt("Please provide your master key to decrypt the password: ", secure=True)
                salt = beaupy.prompt("Encryption Salt: ", secure=True)
            else:
                master_key = beaupy.prompt("Please provide your master key to decrypt the password: ", secure=False)
                salt = beaupy.prompt("Encryption Salt: ", secure=False)
            clear()
            readMD(web_to_get.lower(), master_key, salt)
    except Exception:
        pass




# Locking and unlocking files.
def lock(file_path, enc_key, enc_salt):
    oCrypt().file_encrypt(file_path, enc_key, enc_salt)

def unlock(file_path2, enc_key2, enc_salt2):
    oCrypt().file_decrypt(file_path2, enc_key2, enc_salt2)





# Making new DB for the following functions for changing your encryption.
def make_db():
    database = sqlite3.connect('pwords2.pgen')
    c = database.cursor()
    c.execute('''CREATE TABLE pwd_tables(website text, passwd text, notes text)''')
    database.commit()
    database.close()


def change_creds(old_master_key, new_master_key, old_salt, new_salt):
    D_old_key = b64.b64decode(old_master_key)
    D_new_key = b64.b64decode(new_master_key)

    # Get list of domains/websites from original database.
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT website FROM pwd_tables")
    sites = c.fetchall()
    ldb = str(sites).replace("(", "").replace(",)", "").replace("'", "")
    dlist = ldb.strip('][').split(', ')
    

    # Get list of passwords from original database.
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT passwd FROM pwd_tables")
    words = c.fetchall()
    lpw = str(words).replace("(", "").replace(",)", "").replace("'", "")
    plist = lpw.strip('][').split(', ')


    # Get list of notes from original database.
    database = sqlite3.connect('pwords.pgen')
    c = database.cursor()
    c.execute(f"SELECT notes FROM pwd_tables")
    notes = c.fetchall()
    ndb = str(notes).replace("(", "").replace(",)", "").replace("'", "")
    nlist = ndb.strip('][').split(', ')

    # Get all of the passwords in plist above and decrypt them, then append
    lst = []
    for y in plist:
        if not y:
            pass
        else:
            old_pwords = stringMD(y, D_old_key, old_salt)
            lst.append(old_pwords)
    

    # Get all of the passwords in lst and encrypt them using the new credentials.
    lst2 = []
    for z in lst:
        if not z:
            pass
        else:
            new_pwords = stringME(z, D_new_key, new_salt)
            lst2.append(new_pwords)


    # Get all of the websites and all of the newly encrypted passwords and iterate through them both and then write to a new database file.
    for a,b,d in zip(dlist, lst2, nlist):
        database = sqlite3.connect('pwords2.pgen')
        c = database.cursor()
        c.execute(f"INSERT INTO pwd_tables VALUES ('{a}', '{b}', '{d}')")
        database.commit()
        database.close()

## ------------------------------------------------------------------------ ##




def main():
    try:
        #You can configure what you want to do in the config.json file.
        if j_load()[0] == True:
            langs = ['uppercase', 'lowercase', 'numbers', 'symbols', 'korean', 'russian', 'chinese', 'GreekUppercase', 'GreekLowercase', 'PortugueseLowercase', 'PortugueseUppercase', 'unicode', 'ascii_boxes', 'ascii_draw_box', 'hindi', 'arabic', 'emojis', 'amharic']

            # Choose multiple options from a list
            clear()
            print('Chose your options! (If no options are selected you will be returned back to the main menu.)\nPress "CTRL+C" to exit this menu.\n\n')
            langs_config = beaupy.select_multiple(langs, ticked_indices=[0,1,2,3], tick_style="#ed1dd3", cursor_style="#ffa533", tick_character="x")

            all = ""


            if langs[0] in langs_config:
                all += uppercase_letters

            if langs[1] in langs_config:
                all += lowercase_letters

            if langs[2] in langs_config:
                all += numbers

            if langs[3] in langs_config:
                all += symbols

            if langs[4] in langs_config:
                all += korean

            if langs[5] in langs_config:
                all += russian

            if langs[6] in langs_config:
                all += chinese

            if langs[7] in langs_config:
                all += greekU

            if langs[8] in langs_config:
                all += greekL

            if langs[9] in langs_config:
                all += portuL

            if langs[10] in langs_config:
                all += portuU

            if langs[11] in langs_config:
                all += unicode

            if langs[12] in langs_config:
                all += ascii_boxes

            if langs[13] in langs_config:
                all += ascii_draw_box

            if langs[14] in langs_config:
                all += hindi

            if langs[15] in langs_config:
                all += arabic

            if langs[16] in langs_config:
                all += emojis

            if langs[17] in langs_config:
                all += amharic

            if not langs_config:
                clear()
                return

        else:
            upper = True
            lower = True
            nums = True
            syms = True
            kor = True
            rus = True
            chi = True
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
            amha = True


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
            if chi:
                all += chinese
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
            if amha:
                all += amharic
            
    except Exception as e:
        clear()
        print(f"Oops! Something went wrong...\nERROR: {e}\n\n")
        input('Press "enter" to continue...')
        clear()
        return


    clear()
    print('Note: Please make sure to write your password(s) down or save the password(s) into a new text file before running this script again.\nPress "q" to go back. \n\n')



    try:
        length = input('How long do you want your password(s)?: ')
        if length.lower() == 'q':
            clear()
            return None
        else:
            length = int(length)
    except Exception as e:
        clear()
        print(f'Oops..The value you gave me is not a number/integer.\n[Error]: {e}')
        input('\nPress "enter" to continue...')
        return None



    try:
        amount = input('How many do you want generated?: ')
        if amount.lower() == 'q':
            clear()
            return None
        else:
            amount = int(amount)
    except Exception as e:
        clear()
        print(f'Oops..The value you gave me is not a number/integer.\n[Error]: {e}')
        input('\nPress "enter" to continue...')
        return None



    print('\n')


    with open('pass.txt', 'w') as f:
        for _ in range(amount):
            password = ''.join(secrets.choice(all) for _ in range(length))
            print(f'Pass: {password}  |  Hash: {d_conv(password)[0]}\nSalt: {d_conv(password)[1].decode()}  |  Key: {d_conv(password)[2]}\n', file=f)
        print('Your newly generated random password(s) and hash info has been saved to "pass.txt".\n\n')
        input('Press "enter" to continue...')
        clear()


##-------------- ^^ Functions End ^^ --------------##




if __name__ == '__main__':
    while True:
        clear()
        try:
            option = int(input(f"{banner()}\n\nWhat would you like to do?\n\n1. Make a password?\n2. Generate Key?\n3. Manage passwords?\n4. Get hash for a password?\n5. Show pass.txt?\n6. Clear pass.txt?\n7. Quit?\n\nEnter: "))
        except Exception as e:
            clear()
            print(f'Value given is not an integer.\nError: {e}\n\n')
            input('Press "enter" to continue...')
            clear()
            continue


        if option == 1:
            clear()
            main()

        if option == 2:
            clear()
            m_gen = beaupy.prompt('(It is reccomended to use passgen to make the password)\nPress "q" to go back.\n\nPassword to generate master_key - (100+ characters long.): ', secure=True)
            if m_gen.lower() == 'q':
                clear()
            else:
                m_gen = bytes(m_gen, 'unicode-escape')
                m_key = keygen(m_gen)
                print(f'Key: {m_key}\nIf you have made this key to encrypt your data...DO NOT LOSE THIS KEY. If you lose this key, you can not recover your passwords or change encrypted data.\nThis key will be used when encrypting & decrypting passwords.\n\n')
                input('Press "enter" to continue...')
                clear()


        if option == 3:
            clear()
            while True:
                try:
                    sub_option = int(input(f"{banner()}\n\nWhat do you want to manage?\n\n1. Add password?\n2. Remove password?\n3. Show saved websites\n4. Lock database?\n5. Unlock database?\n6. Change encryption?\n7. Back?\n\nEnter: "))
                except Exception as e:
                    clear()
                    print(f'Value given is not an integer.\nError: {e}\n\n')
                    input('Press "enter" to continue...')
                    clear()
                    continue


                if sub_option == 1: # Add passwords
                    if os.path.isfile('pwords.pgen.oCrypted'):
                        clear()
                        print("Database file does not exist or is encrypted...")
                        input('\n\nPress "enter" to continue...')
                        clear()
                        continue
                    else:
                        clear()
                        web = input('Press "q" to go back/quit.\n\nWhat is the website/domain name you would like to store in the Database?: ')
                        if web.lower() == 'q':
                            clear()
                            continue
                        
                        if j_load()[1] == True:
                            passwd = beaupy.prompt(f'Password to save for "{web.lower()}"?: ', secure=True)
                        else:
                            passwd = beaupy.prompt(f'Password to save for "{web.lower()}"?: ', secure=False)
                        if passwd.lower() == 'q':
                            clear()
                            continue

                        notes = beaupy.prompt("(Optional) - Additional Information/notes: ")
                        if notes.lower() == 'q':
                            clear()
                            continue

                        if j_load()[1] == True:
                            master = beaupy.prompt("Master Key for encryption: ", secure=True)
                        else:
                            master = beaupy.prompt("Master Key for encryption: ", secure=False)
                        if master.lower() == 'q':
                            clear()
                            continue

                        if j_load()[1] == True:
                            salt = beaupy.prompt("Encryption salt: ", secure=True)
                        else:
                            salt = beaupy.prompt("Encryption salt: ", secure=False)
                        if master.lower() == 'q':
                            clear()
                            continue
                        clear()
                        master = b64.b64decode(master)
                        add_data(web.lower(), passwd, notes, master, salt)
                        input('\n\nPress "enter" to continue...')
                        clear()


                if sub_option == 2: # Remove passwords
                    if os.path.isfile('pwords.pgen.oCrypted'):
                        clear()
                        print("Database file does not exist or is encrypted...")
                        input('\n\nPress "enter" to continue...')
                        clear()
                        continue
                    else:
                        clear()
                        domains()
                        if os.path.isfile('.lst'):
                            with open(".lst", "r+") as f:
                                data = f.read()
                                print(data)
                                f.truncate(0)
                                f.close()
                            os.remove(".lst")
                        
                            web_to_rmv = input('-----------------------------------------------------\n(This will remove notes and passwords for the website/domain as well)\nPress "q" to go back/quit.\n\nWhat is the website/domain name you would like to remove from the Database?: ')
                            clear()

                            if web_to_rmv.lower() == 'q':
                                clear()
                                continue
                            else:
                                rmv_data(web_to_rmv.lower())
                                input('\n\nPress "enter" to continue...')
                                clear()
                        else:
                            input('Press "enter" to continue...')
                            clear()
                            continue


                #Reading/show passwords
                if sub_option == 3:
                    if os.path.isfile('pwords.pgen.oCrypted'):
                        clear()
                        print("Database file does not exist or is encrypted...")
                        input('\n\nPress "enter" to continue...')
                        clear()
                        continue
                    else:
                        clear()
                        data = read()
                        if data == 'q':
                            clear()
                        else:
                            input('\n\nPress "enter" to continue...')
                            clear()


                #Lock Database
                if sub_option == 4:
                    if os.path.isfile('pwords.pgen.oCrypted'):
                        clear()
                        print("Database file already encrypted...")
                        input('\n\nPress "enter" to continue...')
                        clear()
                        continue
                    else:
                        clear()
                        print('Please provide credentials to lock the database. (Do NOT forget them as you will never be able to decrypt without them.)\nPress "q" to go back/quit.\n\n')
                        if j_load()[1] == True:
                            enc_key = beaupy.prompt("Encryption Key: ", secure=True)
                        else:
                            enc_key = beaupy.prompt("Encryption Key: ", secure=False)
                        if enc_key.lower() == 'q':
                            clear()
                            continue

                        if j_load()[1] == True:
                            enc_salt = beaupy.prompt("Encryption Salt: ", secure=True)
                        else:
                            enc_salt = beaupy.prompt("Encryption Salt: ", secure=False)
                        if enc_salt.lower() == 'q':
                            clear()
                            continue

                        file_path = input("File path? - (Drag & drop): ").replace('\\ ', ' ').strip()
                        if file_path.lower() == 'q':
                            clear()
                            continue
                        try:
                            enc_key = b64.b64decode(enc_key)
                            lock(file_path, enc_key, enc_salt)
                            clear()
                        except Exception:
                            lock(file_path, enc_key, enc_salt)
                            clear()


                #unlock Database
                if sub_option == 5:
                    clear()
                    print('Please provide the correct credentials to unlock the database. (Do not forget them as you will NOT be able to decrypt without them.)\nPress "q" to go back/quit.\n\n')

                    if j_load()[1] == True:
                        enc_key2 = beaupy.prompt("Encryption Key: ", secure=True)
                    else:
                        enc_key2 = beaupy.prompt("Encryption Key: ", secure=False)
                    if enc_key2.lower() == 'q':
                        clear()
                        continue

                    if j_load()[1] == True:
                        enc_salt2 = beaupy.prompt("Encryption Salt: ", secure=True)
                    else:
                        enc_salt2 = beaupy.prompt("Encryption Salt: ", secure=False)
                    if enc_salt2.lower() == 'q':
                        clear()
                        continue

                    file_path2 = input("File path? - (Drag & drop): ").replace('\\ ', ' ').strip()
                    if file_path2.lower() == 'q':
                        clear()
                        continue
                    try:
                        enc_key2 = b64.b64decode(enc_key2)
                        unlock(file_path2, enc_key2, enc_salt2)
                        clear()
                    except Exception:
                        unlock(file_path2, enc_key2, enc_salt2)
                        clear()



                if sub_option == 6:
                    if os.path.isfile('pwords.pgen.oCrypted'):
                        clear()
                        print("Database file does not exist or is encrypted...")
                        input('\n\nPress "enter" to continue...')
                        clear()
                        continue
                    else:
                        clear()

                        print(f'Changing encryption master key for the encryption...\n\nPress "enter" to continue or "q" to go back/quit...: ')
                        new_pass = beaupy.prompt("(It is reccomended to use passgen to make the password)\nPassword to generate master_key - (100+ characters long.): ", secure=True)
                        if new_pass.lower() == 'q':
                            clear()
                            continue
                        else:
                            clear()
                            new_pass = bytes(new_pass, 'unicode_escape')
                            new_master = keygen(new_pass)
                            print(f'New Master Key: {new_master}\nDO NO LOSE THIS KEY. If you lose this key, you can not recover your passwords or change keys.\nThis key will be used when encrypting & decrypting passwords.')
                            input('\n\nPress "enter" to continue...')
                            clear()
                            print("Making new database for passwords...")
                            if os.path.isfile('pwords2.pgen'):
                                print("Database already exists, deleting and trying again..")
                                os.remove('pwords2.pgen')
                                make_db()
                            else:
                                make_db()
                            print("New database created!\n---------------------------------------------------------------")

                            print("\n\nWorking my magic!...")
                            if j_load()[1] == True:
                                old_master_key = beaupy.prompt("Old master key: ", secure=True)
                                old_salt = beaupy.prompt("Old Encryption salt: ", secure=True)
                                new_master_key = beaupy.prompt("Newly just generated master key: ", secure=True)
                                new_salt = beaupy.prompt("New encryption salt: ", secure=True)
                            else:
                                old_master_key = beaupy.prompt("Old master key: ", secure=False)
                                old_salt = beaupy.prompt("Old Encryption salt: ", secure=False)
                                new_master_key = beaupy.prompt("Newly just generated master key: ", secure=False)
                                new_salt = beaupy.prompt("New encryption salt: ", secure=False)

                            change_creds(old_master_key, new_master_key, old_salt, new_salt)
                            input('Credentials have been changed and all data is now using the new encryption & credentials.\n\nPress "enter" to continue...')
                            clear()

                            print("Cleaning up!...")
                            cleanup()
                            input('\n\nFiles have been cleaned up!\nPress "enter" to quit/reload the passgen...')
                            clear()
                            exit("Goodbye! <3")


                if sub_option == 7:
                    break


                elif sub_option < 1 or sub_option > 7:
                    clear()
                    print("Incorrect value given. Please choose a valid option from the menu/list.\n\n")
                    input('Press "enter" to quit...')
                    clear()

        if option == 4:
            clear()
            pword = input('Press "q" to go back/quit.\n\nWhat would you like to hash?: ')
            if pword.lower() == 'q':
                clear()
            else:
                clear()
                check = hash(pword)
                if not check:
                    clear()
                    continue
                else:
                    input('Press "enter" to continue...')
                    clear()  

        
        if option == 5:
            passwords = show_pass()
            if not passwords:
                clear()
                print('No passwords found in "pass.txt"\n\n')
                input('Press "enter" to continue...')
                clear()
            else:
                print(passwords)
                input('Press "enter" to continue...')
                clear()
        

        if option == 6:
            clr_pass()
            print("pass.txt has been wiped clean.\n\n")
            input('Press "enter" to continue...')
            clear()
        
        
        if option == 7:
            clear()
            exit("Goodbye! <3")

        
        elif option < 1 or option > 7:
            clear()
            print("Incorrect value given. Please choose a valid option from the menu/list.\n\n")
            input('Press "enter" to continue...')
            clear()
            
