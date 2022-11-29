#Imports
import base64 as b64
import beaupy
from hashlib import blake2b
import json
from ocryptor import oCrypt
import os
import sys
import wget
import secrets
import sqlite3
from string import ascii_lowercase, ascii_uppercase, digits
from alive_progress import alive_bar


#AES stoof
from Crypto.Cipher import AES
from Crypto.Random import random


#To help with brand name changes.
project_name = "Genter"
project_ext = ".gter"

#The header that's used with the aes encryption for the json object is not encrypted, just base64 encoded and I don't really know of its importance.
header = f"Encrypted using {project_name}. DO NOT TAMPER WITH.  |  Made by therealOri  |  {os.urandom(8)}"
header = bytes(header, 'utf-8')


#KeyGen
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt


#Languages
uppercase_letters = ascii_uppercase
lowercase_letters = ascii_lowercase
symbols = "!=<>'@#$%^&*()[\],.;:-_/+?{|}`~"
unicode = "¡¢£¤¥¦§¨©ª«¬®™️¯°±²³´µ¶·¸¹º»¼½¾¿×Ø÷øÞßƒðÐıæᔕ€≡‗"
emojis = "⚔☣️⚛️〰️🗝️🔒⛓️✨🫠🫧🫥💢🪬"
ascii_boxes = "░▒▓█▄▀■"
ascii_draw_box = "╣╗╝┴┬╩╦═╬"
numbers = digits
korean = "ㅂㅋㅎㅭㅱㅶㅹㅺㅿㆁㆄㆅ"
russian = "БГДЁЖИЙЛПФфЦЧШЩЪЫЬЭЮЯ"
chinese = "诶比西迪伊尺杰大水开勒哦屁吉吾儿诶比西迪伊弗吉尺艾弗吉杰屁吉吾儿八九十开勒马娜哦月人马娜口"
greekU = "ΓΔΘΛΞΠΣΦΨΩ" # Greek Uppercase.
greekL = "αβγδεζηθικλμνξπρστυφχψω" # Greek Lowercase.
portuL = "ãáàâçéêíõóôúü"
portuU = "ÃÁÀÂÇÉÊÍÕÓÔÚÜ"
hindi = "ऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऽॐॠॡ।॥०१२३४५६७८९॰ॲॳॴॵॶॷॹॺॻॼॽॾॿೱೲऀँंःऺऻ़ािीुूृॄॅॆेैॉॊोौ्ॎॏ॒॑॓॔ॕॖॗॢॣ"
arabic = "شسژزڑرذڈدخحچجثٹتپبآاےیھہوںنملگکقفغعظطضصءئؤڙڐٿ٘ ًَُِّٰٗ؟،۰۱۲۳۴۵۶۷۸۹"
amharic = "ሀሁሂሃሄህሆሎልሌላሊሉለሐሑሒሓሔሕሖሞምሜማሚሙመሠሡሢሣሤሥሦሮርሬራሪሩረሰሱሲሳሴስሶሾሽሼሻሺሹሸቀቁቂቃቄቅቆቦብቤባቢቡበቨቩቪቫቬቭቮቶትቴታቲቱተቸቹቺቻቼችቾኆኅኄኃኂኁኀነኑኒናኔንኖኞኝኜኛኚኙኘአኡኢኣኤእኦኮክኬካኪኩከኸኹኺኻኼኽኾዎውዌዋዊዉወዐዑዒዓዔዕዖዞዝዜዛዚዙዘዠዡዢዣዤዥዦዮይዬያዪዩየደዱዲዳዴድዶጆጅጄጃጂጁጀገጉጊጋጌግጎጦጥጤጣጢጡጠጨጩጪጫጬጭጮጶጵጴጳጲጱጰጸጹጺጻጼጽጾፆፅፄፃፂፁፀፈፉፊፋፌፍፎፖፕፔፓፒፑፐ፩፪፫፬፭፮፯፰፱፲፳፴፵፶፷፸፹፺፻፼፡።፣፤፥"
sinhala = "්‍රඤචදසමහඒරැඅුටොි්යවනකතගලපබංජඩඉ𐐘𐑀ඞඕ"
hieroglyphs = "𓀨𓁢𓂀𓂁𓂄𓂉𓃣𓄯𓉢𓊇𓊆𓊉𓊈𓊎𓊕𓊔𓊖𓊗𓋹𓋸𓏲𓌬𓋨"


#Example |  new_list = "WHATERVER YOU WANT HERE"  | This can be named whatever you can think of, doesn't have to be "new_list". It's just what I am using for this example.
#You can add more and make it even more complex. Just make sure to update the rest of the code below.



##-------------- Functions --------------##
def banner():
    return """

            ██████╗ ███████╗███╗   ██╗████████╗███████╗██████╗
           ██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
           ██║  ███╗█████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝
           ██║   ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
           ╚██████╔╝███████╗██║ ╚████║   ██║   ███████╗██║  ██║
            ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝


      Made by Ori#6338 | @therealOri_ | https://github.com/therealOri
    """



#Make master key for encrypting stuff.
def keygen(master):
    salt = os.urandom(16)

    # derive
    print("Generating key...")
    Scr = Scrypt(
        salt=salt,
        length=32,
        n=2**20,
        r=16,
        p=1,
    )
    key = Scr.derive(master)

    clear()
    bkey = b64.b64encode(key) #Base64 encode the bytes. (We decode this before encrypting, using bytes instead of the base64 encoded string.)
    return bkey.decode()




# CLEANING
## ------------------------------------------------------------------------ ##
def clear():
    os.system('cls||clear')


# Cleaning up files.
def cleanup():
    # Remove current pwords{project_ext} db.
    if os.path.isfile(f'pwords{project_ext}'):
        os.remove(f'pwords{project_ext}')
    else:
        pass

    # Rename new database to the name of the original database.
    if os.path.isfile(f'pwords2{project_ext}'):
        os.rename(f'pwords2{project_ext}', f'pwords{project_ext}')
    else:
        pass
## ------------------------------------------------------------------------ ##







# ENCRYPTION STUFF
## ------------------------------------------------------------------------ ##


# Encrypting the passwords with master key and AES encryption.
def stringME(data, key):
    data = bytes(data, 'utf-8')
    cipher = AES.new(key, AES.MODE_GCM)
    cipher.update(header)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
    json_v = [ b64.b64encode(x).decode('utf-8') for x in [cipher.nonce, header, ciphertext, tag ]]
    result = json.dumps(dict(zip(json_k, json_v)))
    result = bytes(result, 'utf-8')
    result = b64.b64encode(result)
    return result.decode()


#Decrypting the passwords with master key and AES encryption.
def stringMD(b64_input, key):
    try:
        json_input = b64.b64decode(b64_input)
        b64j = json.loads(json_input)
        json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
        jv = {k:b64.b64decode(b64j[k]) for k in json_k}

        cipher = AES.new(key, AES.MODE_GCM, nonce=jv['nonce'])
        cipher.update(jv['header'])
        plaintext = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])
        return plaintext.decode()
    except (ValueError, KeyError):
        input("Incorrect data given, or Data has been tampered with. Can't decrypt.\n\nPress 'enter' to continue...")
        clear()
        return None


#Reading a password for selected domain/website
def readMD(web, master_key):
    database = sqlite3.connect(f'pwords{project_ext}')
    c = database.cursor()
    c.execute(f"SELECT passwd FROM pwd_tables WHERE website LIKE '{web}'")

    if b64passwd := c.fetchone():
        gej = b64passwd[0]
        pwdata = stringMD(gej, master_key)
        return pwdata
    else:
        print('Oof..nothing here but us foxos...\n\n')
        input('Press "enter" to continue...')
        return




# Add and remove data from database.
def add_data(website, passwd, notes, key):
    b64_note = b64.b64encode(notes.encode('unicode-escape'))
    database = sqlite3.connect(f'pwords{project_ext}')
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
        c.execute(f"INSERT INTO pwd_tables VALUES ('{website}', '{stringME(passwd, key)}', '{b64_note.decode('unicode-escape')}')")
        database.commit()
        database.close()
        return print(f'"{website}" and your password has been stored/saved to the database!')



def rmv_data(website):
    database = sqlite3.connect(f'pwords{project_ext}')
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
        options = ['Custom key?', 'Generate key?', 'Quit?']
        print(f'{banner()}\n\nHow do you want to make a key for hashing?\n-----------------------------------------------------------\n')
        option = beaupy.select(options, cursor_style="#ffa533")

        if option == None:
            clear()
            return None


        if options[0] in option:
            clear()
            if j_load()[1] == True:
                c_key = beaupy.prompt('Press "q" to go back/quit.\n-----------------------------------------------------------\nEnter/Load key to use for hashing: ', secure=True)
            else:
                c_key = beaupy.prompt('Press "q" to go back/quit.\n-----------------------------------------------------------\nEnter/Load key to use for hashing: ', secure=False)

            if not c_key or c_key.lower() == 'q':
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


        if options[1] in option:
            clear()
            gen_key = ''.join(secrets.choice(alphabet) for _ in range(25))
            salt = bytes(''.join(secrets.choice(alphabet) for _ in range(16)), 'utf-8')

            result2 = blake2b(bytes(password, 'utf-8'), key=bytes(gen_key, 'utf-8'), salt=salt, digest_size=32).hexdigest()
            print(f'Password: {password}  |  Hash: {result2}\nSalt: {salt.decode()}  |  Key: {gen_key}\n')
            return result2

        if options[2] in option:
            clear()
            return None




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
    if os.path.isfile('config.json'):
        with open('config.json') as f:
            data = json.load(f)
            options_flag = data['options_flag']
            secure_prompts = data['secure_prompts']
            wordlst = data['wordlst_update']
        return options_flag, secure_prompts, wordlst

    else:
        print("config.json file not found, downloading it from the repository...")
        wget.download("https://raw.githubusercontent.com/therealOri/Genter/main/config.json")
        clear()
        with open('config.json') as f:
            data = json.load(f)
            options_flag = data['options_flag']
            secure_prompts = data['secure_prompts']
            wordlst = data['wordlst_update']
        return options_flag, secure_prompts, wordlst



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


# Reading passwords functionality.
def domains():
    database = sqlite3.connect(f'pwords{project_ext}')
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
        input('Hmmm...Maybe you should add something to the database first. ^-^\n\nPress "enter" to continue...')
        clear()
    else:
        for d,n in zip(dlist, clean_list):
            with open('.lst', 'a') as f:
                f.writelines(f"{d}  ({n})\n")


def read():
    clear()
    domains()
    try:
        with open(".lst", "r+") as f:
            data = f.read()
            fnlst = data.strip().split('\n')
            f.truncate(0)
            f.close()

        os.remove(".lst")
        print(f'(Press "ctrl+c" to exit)\n-----------------------------------------------------------\n\nWebsite domain/name for password?\n')
        domain = beaupy.select(fnlst, cursor_style="#ffa533")

        clear()
        if domain == None:
            clear()
            return
        else:
            if j_load()[1] == True:
                master_key = beaupy.prompt("Please provide your master key to decrypt the password: ", secure=True)
            else:
                master_key = beaupy.prompt("Please provide your master key to decrypt the password: ", secure=False)
            clear()
            try:
                master_key = b64.b64decode(master_key)
            except Exception as e:
                input(f'Provided key is not base64 encoded...\n\nPress "enter" to continue...')
                clear()
                return

            if not master_key:
                input(f'Key can not be an empty string...\n\nPress "enter" to continue...')
                clear()
                return

            if len(master_key) < 32 or len(master_key) > 32:
                clear()
                input(f'Key needs to be 32 characters/bytes long. Current key length: {len(master_key)}\n\nPress "enter" to continue...')
                clear()
                return
            else:
                domain = domain.split(' ', 1)[0] #get first word in a string.
                pwd = readMD(domain, master_key)
                if pwd == None:
                    clear()
                    return
                else:
                    print(f'Password for "{domain}" is: {pwd}\n\n')
                    input('Press "enter" to continue...')
                    clear()
    except Exception:
        return




# Locking and unlocking files.
def lock(file_path, enc_key, enc_salt):
    oCrypt().file_encrypt(file_path, enc_key, enc_salt)

def unlock(file_path2, enc_key2, enc_salt2):
    oCrypt().file_decrypt(file_path2, enc_key2, enc_salt2)





# Making new DB for the following functions for changing your encryption.
def make_db():
    database = sqlite3.connect(f'pwords2{project_ext}')
    c = database.cursor()
    c.execute('''CREATE TABLE pwd_tables(website text, passwd text, notes text)''')
    database.commit()
    database.close()


def change_creds(old_master_key, new_master_key):
    D_old_key = b64.b64decode(old_master_key)
    E_new_key = b64.b64decode(new_master_key)
    if len(D_old_key) and len(E_new_key) < 32 or len(D_old_key) and len(E_new_key) > 32:
        clear()
        input(f'Keys need to be 32 characters/bytes long.\n\nold_key length: {len(D_old_key)}\nnew_key length: {len(E_new_key)}\n\nPress "enter" to continue...')
        clear()
        return False
    else:
        # Get list of domains/websites from original database.
        database = sqlite3.connect(f'pwords{project_ext}')
        c = database.cursor()
        c.execute(f"SELECT website FROM pwd_tables")
        sites = c.fetchall()
        ldb = str(sites).replace("(", "").replace(",)", "").replace("'", "")
        dlist = ldb.strip('][').split(', ')


        # Get list of passwords from original database.
        database = sqlite3.connect(f'pwords{project_ext}')
        c = database.cursor()
        c.execute(f"SELECT passwd FROM pwd_tables")
        words = c.fetchall()
        lpw = str(words).replace("(", "").replace(",)", "").replace("'", "")
        plist = lpw.strip('][').split(', ')


        # Get list of notes from original database.
        database = sqlite3.connect(f'pwords{project_ext}')
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
                old_pwords = stringMD(y, D_old_key)
                lst.append(old_pwords)


        # Get all of the passwords in lst and encrypt them using the new credentials.
        lst2 = []
        for z in lst:
            if not z:
                pass
            else:
                new_pwords = stringME(z, E_new_key)
                lst2.append(new_pwords)


        # Get all of the websites and all of the newly encrypted passwords and iterate through them both and then write to a new database file.
        for a,b,d in zip(dlist, lst2, nlist):
            database = sqlite3.connect(f'pwords2{project_ext}')
            c = database.cursor()
            c.execute(f"INSERT INTO pwd_tables VALUES ('{a}', '{b}', '{d}')")
            database.commit()
            database.close()

        return True

## ------------------------------------------------------------------------ ##




def main():
    try:
        #You can configure what you want to do in the config.json file.
        if j_load()[0] == True:
            langs = ['uppercase', 'lowercase', 'numbers', 'symbols', 'korean', 'russian', 'chinese', 'GreekUppercase', 'GreekLowercase', 'PortugueseLowercase', 'PortugueseUppercase', 'unicode', 'ascii_boxes', 'ascii_draw_box', 'hindi', 'arabic', 'emojis', 'amharic', 'sinhala', 'hieroglyphs']

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

            if langs[18] in langs_config:
                all += sinhala

            if langs[19] in langs_config:
                all += hieroglyphs

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
            sinha = True
            hiero = True


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
            if sinha:
                all += sinhala
            if hiero:
                all += hieroglyphs

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


    if os.path.isfile('pass.txt'):
        with open('pass.txt', 'w') as f:
            for _ in range(amount):
                password = ''.join(secrets.choice(all) for _ in range(length))
                print(f'Pass: {password}  |  Hash: {d_conv(password)[0]}\nSalt: {d_conv(password)[1].decode()}  |  Key: {d_conv(password)[2]}\n', file=f)
            print('Your newly generated random password(s) and hash info has been saved to "pass.txt".\n\n')
            input('Press "enter" to continue...')
            clear()
    else:
        clear()
        print("Pass.txt not found, downloading file from repository..")
        wget.download("https://raw.githubusercontent.com/therealOri/Genter/main/pass.txt")
        clear()
        with open('pass.txt', 'w') as f:
            for _ in range(amount):
                password = ''.join(secrets.choice(all) for _ in range(length))
                print(f'Pass: {password}  |  Hash: {d_conv(password)[0]}\nSalt: {d_conv(password)[1].decode()}  |  Key: {d_conv(password)[2]}\n', file=f)
            print('Your newly generated random password(s) and hash info has been saved to "pass.txt".\n\n')
            input('Press "enter" to continue...')
            clear()




#Generate Phrases (Like Bitwarden)
def phrzgn():

    #download words.txt from repo
    if os.path.isfile('words.txt'):
        if j_load()[2] == True:
            os.remove('words.txt')
            print("Updating wordlist..")
            wget.download("https://raw.githubusercontent.com/therealOri/Genter/main/words.txt")
            clear()
        else:
            pass #updates set to false
    else:
        print("words.txt doesn't exist...Downloading words.txt from repo.")
        wget.download("https://raw.githubusercontent.com/therealOri/Genter/main/words.txt")
        clear()

    while True:
        try:
            number = beaupy.prompt(f'(Press "ctrl+c" to exit)\n-----------------------------------------------------------\n\nHow many words?: ')
            if number == None:
                clear()
                return
            else:
                number = int(number)
        except ValueError as e:
            print(f'Oops! Something went wrong.\nError: {e}\n\n')
            input('Press "enter" to continue...')
            clear()
            continue

        if number > 20 or number < 3:
            print("20 words is the maximum number of words you can use. And 5 words is the minimum.\n\n")
            input('Press "enter" to continue...')
            clear()
        else:
            break


    cwd = os.getcwd()
    word_path = f"{cwd}/words.txt"
    with open(word_path, 'r') as fh:
        words = fh.read().lower()
    word_list = words.splitlines() #list of words


    sep = beaupy.prompt('(Press "ctrl+c" to exit)\n-----------------------------------------------------------\n\nLine separator? (leave empty for default "-"): ')
    if sep == None:
        clear()
        return
    else:
        if sep == '':
            sep = '-'


    #Returns True or False. Basically Yes or No?
    capital_words = ''
    default_words = ''
    capitalize = beaupy.confirm('(Press "ctrl+c" to exit)\n-----------------------------------------------------------\n\nCapitalize?')
    if capitalize == None:
        clear()
        return
    else:
        if capitalize:
            """Make list of words with the first letter capitalized."""
            c_lst = []
            for i in word_list:
                if len(i) < 3 or len(i) > 9:
                    pass #Ignore and move on to next item
                else:
                    c_lst.append(i.title())

            cap = True
            capital_words = f'{sep}'.join(random.choice(c_lst) for _ in range(number))
        else:
            cap = False
            default_words = f'{sep}'.join(random.choice(word_list) for _ in range(number))


    numbers = beaupy.confirm('(Press "ctrl+c" to exit)\n-----------------------------------------------------------\n\nNumber?')
    if numbers == None:
        clear()
        return
    else:
        if numbers:
            num = True
            rn_num = random.randint(0, 9) # <-- Get a random number to be used with only 1 of the words defined in capital_words or default_words below.
            word_index = random.randint(0, number - 1) # Get random index that is in the word list

            if default_words != '':
                word_with_number = default_words.split(sep)
            else:
                word_with_number = capital_words.split(sep)

            word_with_number[word_index] = word_with_number[word_index] + str(rn_num)
            word_with_number = sep.join(word_with_number)
        else:
            num = False


    if cap == True and num == False:
        return capital_words
    if cap == False and num == False:
        return default_words
    if num == True:
        return word_with_number

##-------------- ^^ Functions End ^^ --------------##




if __name__ == '__main__':
    while True:
        clear()
        options = ['Make a password?', 'Make a phrase?', 'Generate a key?', 'Manage passwords?', 'Get hash for a password?', 'Show pass.txt?', 'Clear pass.txt?', 'Quit?']
        print(f'{banner()}\n\nWhat would you like to do?\n-----------------------------------------------------------\n')
        option = beaupy.select(options, cursor_style="#ffa533")

        if not option:
            clear()
            sys.exit("Keyboard Interuption Detected!\nGoodbye <3")


        if options[0] in option:
            clear()
            main()

        if options[1] in option:
            clear()
            phrase = phrzgn()
            if phrase == None:
                clear()
            else:
                print(phrase)
                input('\n\nPress "enter" to continue...')
                clear()


        if options[2] in option:
            clear()
            m_gen = beaupy.prompt('(It is reccomended to use genter to make the password)\nPress "q" or "ctrl+c" to go back/exit.\n\nPassword to generate master_key - (100+ characters long.): ', secure=True)
            if not m_gen or m_gen.lower() == 'q':
                clear()
            if len(m_gen) < 100:
                clear()
                input('Key must be 100 characters in length or more!\n\nPress "eneter" to continue...')
                clear()
            else:
                m_gen = bytes(m_gen, 'unicode-escape')
                m_key = keygen(m_gen)
                print(f'If you have made this key to encrypt your data...DO NOT LOSE THIS KEY. If you lose this key, you can not recover your passwords or change encrypted data.\nThis key will be used when encrypting & decrypting passwords.\n\n\nKey: {m_key}\n\n')
                input('Press "enter" to continue...')
                clear()


        if options[3] in option:
            clear()
            while True:
                sub_options = ['Add password?', 'Remove password?', 'Show saved websites?', 'Lock database?', 'Unlock database?', 'Change encryption?', 'Back?']
                print(f'{banner()}\n\nWhat would you like to manage?\n-----------------------------------------------------------\n')
                sub_option = beaupy.select(sub_options, cursor_style="#ffa533")


                if sub_option == None:
                    clear()
                    break

                if sub_options[0] in sub_option: # Add passwords
                    if os.path.isfile(f'pwords{project_ext}'):
                        if os.path.isfile(f'pwords{project_ext}.oCrypted'):
                            clear()
                            print("Database file does not exist or is encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            web = beaupy.prompt('Press "q" to go back/quit.\n\nWhat is the website/domain name you would like to store in the Database?: ')
                            if not web or web.lower() == 'q':
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
                            clear()
                            try:
                                master = b64.b64decode(master)
                            except Exception as e:
                                print("Provided key isn't base64 encoded...\n\n")
                                input('Press "enter" to continue...')
                                clear()
                                continue
                            if len(master) < 32 or len(master) > 32:
                                clear()
                                input(f'Key needs to be 32 characters/bytes long. Current key length: {len(master)}\n\nPress "enter" to continue...')
                                clear()
                                continue
                            else:
                                add_data(web.lower(), passwd, notes, master)
                                input('\n\nPress "enter" to continue...')
                                clear()
                    else:
                        print(f"pwords{project_ext} not found, downloading from the repository...")
                        wget.download(f"https://raw.githubusercontent.com/therealOri/Genter/main/pwords{project_ext}")
                        clear()
                        if os.path.isfile(f'pwords{project_ext}.oCrypted'):
                            clear()
                            print("Database file does not exist or is encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            web = beaupy.prompt('Press "q" to go back/quit.\n\nWhat is the website/domain name you would like to store in the Database?: ')
                            if not web or web.lower() == 'q':
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
                            clear()
                            try:
                                master = b64.b64decode(master)
                            except Exception as e:
                                print("Provided key isn't base64 encoded...\n\n")
                                input('Press "enter" to continue...')
                                clear()
                                continue
                            if len(master) < 32 or len(master) > 32:
                                clear()
                                input(f'Key needs to be 32 characters/bytes long. Current key length: {len(master)}\n\nPress "enter" to continue...')
                                clear()
                                continue
                            else:
                                add_data(web.lower(), passwd, notes, master)
                                input('\n\nPress "enter" to continue...')
                                clear()


                if sub_options[1] in sub_option: # Remove passwords
                    if os.path.isfile(f'pwords{project_ext}'):
                        if os.path.isfile(f'pwords{project_ext}.oCrypted'):
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

                                web_to_rmv = beaupy.prompt('-----------------------------------------------------\n(This will remove notes and passwords for the website/domain as well)\nPress "q" to go back/quit.\n\nWhat is the website/domain name you would like to remove from the Database?: ')
                                clear()

                                if not web_to_rmv or web_to_rmv.lower() == 'q':
                                    clear()
                                    continue
                                else:
                                    rmv_data(web_to_rmv.lower())
                                    input('\n\nPress "enter" to continue...')
                                    clear()
                            else:
                                clear()
                                continue
                    else:
                        clear()
                        print(f"pwords{project_ext} not found, downloading from the repository...")
                        wget.download(f"https://raw.githubusercontent.com/therealOri/Genter/main/pwords{project_ext}")
                        input("\n\nDatabse is empty and won't be able to remove any passwords, maybe you should add something to the database first? ^-^.\n\nPress 'enter' to continue...")
                        clear()
                        continue


                #Reading/show passwords
                if sub_options[2] in sub_option:
                    if os.path.isfile(f'pwords{project_ext}'):
                        if os.path.isfile(f'pwords{project_ext}.oCrypted'):
                            clear()
                            print("Database file does not exist or is encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            data = read()
                            if data == None:
                                clear()
                    else:
                        clear()
                        print(f"pwords{project_ext} not found, downloading from the repository...")
                        wget.download(f"https://raw.githubusercontent.com/therealOri/Genter/main/pwords{project_ext}")
                        input("\n\nDatabse is empty and won't be able to show any passwords, maybe you should add something to the database first? ^-^.\n\nPress 'enter' to continue...")
                        clear()
                        continue




                #Lock Database
                if sub_options[3] in sub_option:
                    if os.path.isfile(f'pwords{project_ext}'):
                            if os.path.isfile(f'pwords{project_ext}.oCrypted'):
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
                                if not enc_key or enc_key.lower() == 'q':
                                    clear()
                                    continue

                                if j_load()[1] == True:
                                    enc_salt = beaupy.prompt("Encryption Salt: ", secure=True)
                                else:
                                    enc_salt = beaupy.prompt("Encryption Salt: ", secure=False)
                                if not enc_salt or enc_salt.lower() == 'q':
                                    clear()
                                    continue

                                file_path = input("File path? - (Drag & drop): ").replace('\\ ', ' ').strip()
                                if file_path.lower() == 'q':
                                    clear()
                                    continue

                                try:
                                    enc_key = b64.b64decode(enc_key)
                                except Exception:
                                    clear()
                                    print("Provided ket isn't base64 encoded...\n\n")
                                    input('Press "enter" to continue...')
                                    clear()
                                    continue

                                lock(file_path, enc_key, enc_salt)
                                clear()
                    else:
                        clear()
                        print(f"pwords{project_ext} not found, downloading from the repository...")
                        wget.download(f"https://raw.githubusercontent.com/therealOri/Genter/main/pwords{project_ext}")
                        input("\n\nDatabse is empty, skipping on locking the database.\n\nPress 'enter' to continue...")
                        clear()
                        continue


                #unlock Database
                if sub_options[4] in sub_option:
                    if os.path.isfile(f'pwords{project_ext}'):
                        if os.path.isfile(f'pwords{project_ext}.oCrypted'):
                            clear()
                            print('Please provide the correct credentials to unlock the database. (Do not forget them as you will NOT be able to decrypt without them.)\nPress "q" to go back/quit.\n\n')

                            if j_load()[1] == True:
                                enc_key2 = beaupy.prompt("Encryption Key: ", secure=True)
                            else:
                                enc_key2 = beaupy.prompt("Encryption Key: ", secure=False)
                            if not enc_key2 or enc_key2.lower() == 'q':
                                clear()
                                continue

                            if j_load()[1] == True:
                                enc_salt2 = beaupy.prompt("Encryption Salt: ", secure=True)
                            else:
                                enc_salt2 = beaupy.prompt("Encryption Salt: ", secure=False)
                            if not enc_salt2 or enc_salt2.lower() == 'q':
                                clear()
                                continue

                            file_path2 = input("File path? - (Drag & drop): ").replace('\\ ', ' ').strip()
                            if file_path2.lower() == 'q':
                                clear()
                                continue

                            #if given random string of text, it will try to decode, if it can't, send error.
                            #(Sometimes it likes to decode that random gibberish as it thinks it is valid base64..)
                            try:
                                enc_key2 = b64.b64decode(enc_key2)
                            except Exception:
                                clear()
                                print("Provided key isn't base64 encoded...\n\n")
                                input('Press "enter" to continue...')
                                clear()
                                continue

                            unlock(file_path2, enc_key2, enc_salt2)
                            clear()
                        else:
                            clear()
                            print("Database file is not encrypted/locked...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                    else:
                        clear()
                        print(f"pwords{project_ext} not found, downloading from the repository...")
                        wget.download(f"https://raw.githubusercontent.com/therealOri/Genter/main/pwords{project_ext}")
                        input("\n\nDatabse is empty and not locked, skipping on unlocking the database.\n\nPress 'enter' to continue...")
                        clear()
                        continue


                #change credentials
                if sub_options[5] in sub_option:
                    if os.path.isfile(f'pwords{project_ext}'):
                        if os.path.isfile(f'pwords{project_ext}.oCrypted'):
                            clear()
                            print("Database file does not exist or is encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            print("Making new database for passwords...")
                            if os.path.isfile(f'pwords2{project_ext}'):
                                print("Database already exists, deleting and trying again..")
                                os.remove(f'pwords2{project_ext}')
                                make_db()
                            else:
                                make_db()
                            print("New database created!\nWorking my magic!...\n---------------------------------------------------------------\n\n")

                            if j_load()[1] == True:
                                old_master_key = beaupy.prompt("Old master key: ", secure=True)
                                new_master_key = beaupy.prompt("New master key: ", secure=True)
                            else:
                                old_master_key = beaupy.prompt("Old master key: ", secure=False)
                                new_master_key = beaupy.prompt("New master key: ", secure=False)

                            if not old_master_key or not new_master_key:
                                clear()
                                continue
                            else:
                                crds = change_creds(old_master_key, new_master_key)

                            if crds == False:
                                clear()
                                continue
                            else:
                                clear()
                                input('Credentials have been changed and all data is now using the new encryption & credentials.\n\nPress "enter" to continue...')
                                clear()

                                print("Cleaning up!...")
                                cleanup()
                                input('\n\nFiles have been cleaned up!\nPress "enter" to quit/reload the genter...')
                                clear()
                                sys.exit("Goodbye! <3")
                    else:
                        clear()
                        print(f"pwords{project_ext} not found, downloading from the repository...")
                        wget.download(f"https://raw.githubusercontent.com/therealOri/Genter/main/pwords{project_ext}")
                        input("\n\nDatabse is empty and has no data/credentials to change, skipping on changing credentials.\n\nPress 'enter' to continue...")
                        clear()
                        continue



                if sub_options[6] in sub_option:
                    clear()
                    break


        #hashing
        if options[4] in option:
            clear()
            if j_load()[1] == True:
                pword = beaupy.prompt('Press "q" to go back/quit.\n-----------------------------------------------------------\nWhat would you like to hash?: ', secure=True)
            else:
                pword = beaupy.prompt('Press "q" to go back/quit.\n-----------------------------------------------------------\nWhat would you like to hash?: ', secure=False)


            if not pword or pword.lower() == 'q':
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


        #showing passwords
        if options[5] in option:
            if os.path.isfile('pass.txt'):
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
            else:
                clear()
                print("pass.txt not found, downloading from the repository...")
                wget.download("https://raw.githubusercontent.com/therealOri/Genter/main/pass.txt")
                input("\n\npass.txt is empty, no passwords found.\n\nPress 'enter' to continue...")
                clear()
                continue



        #clear passwords
        if options[6] in option:
            if os.path.isfile('pass.txt'):
                clr_pass()
                print("pass.txt has been wiped clean.\n\n")
                input('Press "enter" to continue...')
                clear()
            else:
                clear()
                print("pass.txt not found, downloading from the repository...")
                wget.download("https://raw.githubusercontent.com/therealOri/Genter/main/pass.txt")
                input("\n\npass.txt is empty already.\n\nPress 'enter' to continue...")
                clear()
                continue


        if options[7] in option:
            clear()
            sys.exit("Goodbye! <3")

