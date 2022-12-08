#Imports
import base64 as b64
import beaupy
from hashlib import blake2b
import json
import itertools
from ocryptor import oCrypt
import os
import sys
import wget
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
    with alive_bar(0) as bar:
        Scr = Scrypt(
            salt=salt,
            length=32,
            n=2**20,
            r=16,
            p=1,
        )
        key = Scr.derive(master)
        bar()
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
        print("Incorrect data given, or Data has been tampered with. Can't decrypt.")
        return None



# get's data at row xyz and retruns the data
def readMD(db_row):
    database = sqlite3.connect('pwords.gter')
    c = database.cursor()

    c.execute("SELECT id FROM logins")
    all_ids = c.fetchall()
    lst_output = list(itertools.chain(*all_ids))

    if not all_ids:
        input('Oof..nothing here but us foxos...\n\nPress "enter" to cotinue...')
        clear()
        database.commit()
        database.close()
        return None
    else:
        for x in lst_output:
            if x == db_row:
                c.execute(f"SELECT data FROM logins WHERE id LIKE '{db_row}'")
                enc_data = c.fetchone()
                database.commit()
                database.close()
                return enc_data[0]
            else:
                pass



def add_data(encrypted_data):
    nums_lst = [random.randint(0, 9) for i in range(10)]
    ID = int("".join(list(map(str, nums_lst))))
    database = sqlite3.connect('pwords.gter')
    c = database.cursor()
    c.execute("SELECT id FROM logins")
    all_ids = c.fetchall()
    db_IDs = list(itertools.chain(*all_ids))
    if len(db_IDs) == 9999999999: # I don't want to get to the point where I have ran out of unique 10 digit numbers to use as an ID.
        print('Max amount of entries/IDs reached! "9999999999" logins!')
        flag = '#wtf... O-O;'
        return flag

    if ID in db_IDs:
        nums_lst = [random.randint(0, 9) for i in range(10)]
        ID = int("".join(list(map(str, nums_lst))))
    else:
        c.execute(f"INSERT INTO logins VALUES ('{ID}', '{encrypted_data}')")
        database.commit()
        database.close()




def rmv_data(db_row):
    database = sqlite3.connect('pwords.gter')
    c = database.cursor()
    c.execute("SELECT id FROM logins")
    all_ids = c.fetchall()
    id_lst = list(itertools.chain(*all_ids))
    if db_row in id_lst:
        c.execute(f"DELETE FROM logins WHERE id LIKE '{db_row}'")
        database.commit()
        database.close()
        return print(f'Login with ID: "{db_row}" has been removed from the database!')
    else:
        database.commit()
        database.close()
        return print(f'Login with ID: "{db_row}" is not a valid option or does not exist.')
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
            gen_key = ''.join(random.choice(alphabet) for _ in range(25))
            salt = bytes(''.join(random.choice(alphabet) for _ in range(16)), 'utf-8')

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

    default_key = ''.join(random.choice(alphabet) for _ in range(25)) #Can be as long as you want.
    salt = bytes(''.join(random.choice(alphabet) for _ in range(16)), 'utf-8') #MUST be 16 or less.

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




#This is for getting login options and the ID for the login.
def fetch_logins(dKey):
    database = sqlite3.connect('pwords.gter')
    c = database.cursor()
    c.execute("SELECT data FROM logins")
    websites = c.fetchall()
    enc_output = list(itertools.chain(*websites))

    c.execute("SELECT id FROM logins")
    ids = c.fetchall()
    all_ids = list(itertools.chain(*ids))

    if not websites or not ids:
        clear()
        print('Oof..nothing here but us foxos...')
        return None


    web_lst = []
    note_lst = []
    for x in enc_output:
        result = stringMD(x, dKey) #decrypt encrypted json string.
        if result == None:
            return None
        else:
            obj_result = json.loads(result) #turns back into json object
            website = obj_result['Domain']
            notes = obj_result['Notes']
            web_lst.append(website)
            note_lst.append(notes)


    for i,w,n in zip(all_ids, web_lst, note_lst):
        with open('.lst', 'a') as fa:
            fa.writelines(f"[{i}] {w}   ({n})\n")
            fa.close()


    with open(".lst", "r+") as fr:
        data = fr.read()
        fnlst = data.strip().split('\n')
        fr.truncate(0)
        fr.close()


    os.remove(".lst")
    print(f'(Press "ctrl+c" to exit)\n-----------------------------------------------------------\n\n')
    for _ in fnlst:
        print(_)

    login_id = beaupy.prompt("\nLogin ID? - (Example: 1)")

    if login_id == '':
        clear()
        print("Option selected can't be nothing...")
        return None

    if not login_id:
        clear()
        print('Keyboard Interuption detected. Stopping login removal...')
        return None

    if int(login_id) not in all_ids:
        clear()
        print('The option picked is not a valid ID or the option is not in the current list of IDs...')
        return None
    else:
        clear()
        login_id = int(login_id)
        return login_id


# Locking and unlocking files.
def lock(file_path, enc_key, enc_salt):
    oCrypt().file_encrypt(file_path, enc_key, enc_salt)

def unlock(file_path2, enc_key2, enc_salt2):
    oCrypt().file_decrypt(file_path2, enc_key2, enc_salt2)





# Making new DB for the following functions for changing your encryption.
def make_db():
    database = sqlite3.connect(f'pwords2{project_ext}')
    c = database.cursor()
    c.execute('''CREATE TABLE logins(id integer, data text)''')
    database.commit()
    database.close()




#update to reflect new database
def change_creds(old_master_key, new_master_key):
    D_old_key = b64.b64decode(old_master_key)
    E_new_key = b64.b64decode(new_master_key)
    if len(D_old_key) and len(E_new_key) < 32 or len(D_old_key) and len(E_new_key) > 32:
        clear()
        input(f'Keys need to be 32 characters/bytes long.\n\nold_key length: {len(D_old_key)}\nnew_key length: {len(E_new_key)}\n\nPress "enter" to continue...')
        clear()
        return False
    else:
        # Get list of IDs from original database.
        database = sqlite3.connect(f'pwords{project_ext}')
        c = database.cursor()
        c.execute(f"SELECT id FROM logins")
        ids = c.fetchall()
        ids_lst = list(itertools.chain(*ids))


        # Get list of data from original database.
        database = sqlite3.connect(f'pwords{project_ext}')
        c = database.cursor()
        c.execute(f"SELECT data FROM logins")
        enc_data_logins = c.fetchall()
        plist = list(itertools.chain(*enc_data_logins))

        if not enc_data_logins or not ids:
            clear()
            print('Oof..nothing here but us foxos...')
            return False


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
                load_z = json.loads(z)
                z = json.dumps(load_z, ensure_ascii=False).encode('utf-8')
                new_pwords = stringME(z, E_new_key)
                lst2.append(new_pwords)


        # Get all of the websites and all of the newly encrypted passwords and iterate through them both and then write to a new database file.
        for a,b in zip(ids_lst, lst2):
            database = sqlite3.connect(f'pwords2{project_ext}')
            c = database.cursor()
            c.execute(f"INSERT INTO logins VALUES ('{a}', '{b}')")
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
                # random.choice() is pycryptodome's "from Crypto.Random import random" and NOT the bad predictable "random" library.
                password = ''.join(random.choice(all) for _ in range(length))
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
                password = ''.join(random.choice(all) for _ in range(length))
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
        options = ['Make a password?', 'Make a phrase?', 'Generate a key?', 'Manage logins?', 'Get hash for a password?', 'Show pass.txt?', 'Clear pass.txt?', 'Quit?']
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
                sub_options = ['Add login?', 'Remove login?', 'Show saved logins?', 'Lock database?', 'Unlock database?', 'Change encryption?', 'Back?']
                print(f'{banner()}\n\nWhat would you like to manage?\n-----------------------------------------------------------\n')
                sub_option = beaupy.select(sub_options, cursor_style="#ffa533")


                if sub_option == None:
                    clear()
                    break

                # Add passwords
                if sub_options[0] in sub_option:
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
                                email = beaupy.prompt(f'Email/Login to save for "{web.lower()}"?: ', secure=True)
                            else:
                                email = beaupy.prompt(f'Email/Login to save for "{web.lower()}"?: ', secure=False)
                            if email.lower() == 'q':
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
                                json_data = {
                                    'Domain': web,
                                    'Email': email,
                                    'Password': passwd,
                                    'Notes': notes
                                    }

                                json_data = json.dumps(json_data, ensure_ascii=False).encode('utf-8')
                                enc_json_data = stringME(json_data, master)
                                max_limit_check = add_data(enc_json_data)
                                if max_limit_check == '#wtf... O-O;':
                                    input('You have reached the limit of logins available.\n\nPress "enter" to continue...')
                                    clear()
                                    continue
                                clear()
                                input('Login saved!\n\nPress "enter" to continue...')
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
                                email = beaupy.prompt(f'Email/Login to save for "{web.lower()}"?: ', secure=True)
                            else:
                                email = beaupy.prompt(f'Email/Login to save for "{web.lower()}"?: ', secure=False)
                            if email.lower() == 'q':
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
                                json_data = {
                                    'Domain': web,
                                    'Email': email,
                                    'Password': passwd,
                                    'Notes': notes
                                    }

                                json_data = json.dumps(json_data, ensure_ascii=False).encode('utf-8')
                                enc_json_data = stringME(json_data, master)
                                add_data(enc_json_data)
                                clear()
                                input('Login saved!\n\nPress "enter" to continue...')
                                clear()


                # Remove passwords
                if sub_options[1] in sub_option:
                    if os.path.isfile(f'pwords{project_ext}'):
                        if os.path.isfile(f'pwords{project_ext}.oCrypted'):
                            clear()
                            print("Database file does not exist or is encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            if j_load()[1] == True:
                                rmv_key = beaupy.prompt("Encryption key: ", secure=True)
                            else:
                                rmv_key = beaupy.prompt("Encryption key: ", secure=False)

                            if rmv_key.lower() == 'q' or not rmv_key:
                                clear()
                                continue

                            try:
                                rmv_dKey = b64.b64decode(rmv_key)
                            except:
                                clear()
                                input('Could not base64 decode given key...\n\nPress "enter" to continue...')
                                clear()
                                continue

                            clear()
                            id_to_remove = fetch_logins(rmv_dKey)
                            if not id_to_remove:
                                input('Unable to get login ID, an error has occured..\n\nPress "enter" to continue...')
                                clear()
                                continue
                            else:
                                rmv_data(id_to_remove)
                                input('\nPress "enter" to continue...')
                                clear()
                    else:
                        clear()
                        print(f"pwords{project_ext} not found, downloading from the repository...")
                        wget.download(f"https://raw.githubusercontent.com/therealOri/Genter/main/pwords{project_ext}")
                        input("\n\nDatabse is empty and won't be able to remove any passwords, maybe you should add something to the database first? ^-^.\n\nPress 'enter' to continue...")
                        clear()
                        continue


                #Reading/show logins
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
                            if j_load()[1] == True:
                                show_logins_key = beaupy.prompt("Encryption key: ", secure=True)
                            else:
                                show_logins_key = beaupy.prompt("Encryption key: ", secure=False)

                            if show_logins_key.lower() == 'q' or not show_logins_key:
                                clear()
                                continue

                            try:
                                show_logins_dKey = b64.b64decode(show_logins_key)
                            except:
                                clear()
                                input('Could not base64 decode given key...\n\nPress "enter" to continue...')
                                clear()
                                continue

                            clear()
                            login_id = fetch_logins(show_logins_dKey)
                            if login_id == None:
                                input('Unable to get login ID, an error has occured..\n\nPress "enter" to continue...')
                                clear()
                                continue
                            else:
                                pwd = readMD(login_id)
                                if pwd == None:
                                    clear()
                                    input('Had an error while reading logins..\n\nPress "enter" to continue...')
                                    clear()
                                    continue

                                result = stringMD(pwd, show_logins_dKey)
                                obj_result = json.loads(result)

                                website = obj_result['Domain']
                                email = obj_result['Email']
                                password = obj_result['Password']
                                notes = obj_result['Notes']
                                clear()
                                print(f'Login for "{website}" is: \n\nEmail: {email}\nPass: {password}\nNotes: {notes}')
                                input('\n\nPress "enter" to continue..')
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
                                os.remove(f'pwords2{project_ext}')
                                continue
                            else:
                                crds = change_creds(old_master_key, new_master_key)

                            if crds == False:
                                input('Unable to change credentials, No IDs or No Data can be foud in the database..\n\nPress "enter" to continue...')
                                clear()
                                os.remove(f'pwords2{project_ext}')
                                continue
                            else:
                                clear()
                                input('Credentials have been changed and all data is now using the new encryption & credentials.\n\nPress "enter" to continue...')
                                clear()

                                print("Cleaning up!...")
                                cleanup()
                                input('\n\nFiles have been cleaned up!\nPress "enter" to quit/reload genter...')
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

