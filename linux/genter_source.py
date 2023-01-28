#v1.2.14
#Imports
import base64 as b64
import beaupy
import hashlib
import json
import itertools
import os
import sys
import wget
import sqlite3
from string import ascii_lowercase, ascii_uppercase, digits
from alive_progress import alive_bar
import time
from pystyle import Colors, Colorate


#AES stoof
from Crypto.Cipher import AES
from Crypto.Random import random


#To help with brand name changes.
project_name = "Genter"
project_ext = ".gter"

#The header that's used with the aes encryption for the json object is not encrypted, just base64 encoded and I don't really know of its importance.
header = f"Encrypted using {project_name}. DO NOT TAMPER WITH.  |  Made by therealOri  |  {os.urandom(8)}"
header = bytes(header, 'utf-8')


#KeyGen  |  kdf
import argon2


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
sinhala = "්‍රඤචදසමහඒරැඅුටොි්යවනකතගලපබංජඩඉ𐐘𐑀ඞඕ" #SUS
hieroglyphs = "𓀨𓁢𓂀𓂁𓂄𓂉𓃣𓄯𓉢𓊇𓊆𓊉𓊈𓊎𓊕𓊔𓊖𓊗𓋹𓋸𓏲𓌬𓋨"


#Example |  new_list = "WHATERVER YOU WANT HERE"  | This can be named whatever you can think of, doesn't have to be "new_list". It's just what I am using for this example.
#You can add more and make it even more complex. Just make sure to update the rest of the code below.



##-------------- Functions --------------##
def banner():
    banner = """

            ██████╗ ███████╗███╗   ██╗████████╗███████╗██████╗
           ██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
           ██║  ███╗█████╗  ██╔██╗ ██║   ██║   █████╗  ██████╔╝
           ██║   ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
           ╚██████╔╝███████╗██║ ╚████║   ██║   ███████╗██║  ██║
            ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝


      Made by Ori#6338 | @therealOri_ | https://github.com/therealOri
    """
    colored_banner = Colorate.Horizontal(Colors.purple_to_blue, banner, 1)
    return colored_banner



#Make master key for encrypting stuff.
def keygen(master):
    salt = os.urandom(16)

    # derive | DO NOT MESS WITH...unless you know what you are doing and or have more than 8GB of ram to spare and a really good CPU.
    print("Generating key...")
    with alive_bar(0) as bar:
        key = argon2.hash_password_raw(
            time_cost=16,
            memory_cost=2**20,
            parallelism=4,
            hash_len=32,
            password=master,
            salt=salt,
            type=argon2.Type.ID
        )
        bar()
    clear()
    bKey = b64.b64encode(key) #Base64 encode the bytes. (We decode this before encrypting, using bytes instead of the base64 encoded string.)
    return bKey.decode()




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
    except (ValueError, KeyError) as e:
        print(f'Oops, an error has occured: "{e}".\n')
        input("Incorrect data given, or Data has been tampered with. Can't decrypt.\n\nPress 'enter' to continue...")
        clear()
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
    hash_lst = ['Blake2b', 'Sha256', 'Sha512']
    hash_type = beaupy.select(hash_lst, cursor_style="#ffa533")

    if hash_lst[0] in hash_type:
        clear()
        result1 = hashlib.blake2b(bytes(password, 'utf-8')).hexdigest()
        return result1, hash_type

    if hash_lst[1] in hash_type:
        clear()
        result2 = hashlib.sha256(bytes(password, 'utf-8')).hexdigest()
        return result2, hash_type

    if hash_lst[2] in hash_type:
        clear()
        result3 = hashlib.sha512(bytes(password, 'utf-8')).hexdigest()
        return result3, hash_type



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

    login_id = beaupy.prompt("\nLogin ID? - (Example: 1234567890)")

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
def lock(file_path, key):
    with open(file_path, 'rb') as fr:
        data = fr.read()

    b64eData = b64.b64encode(data)
    enc_data = stringME(b64eData, key)

    with open(f'{file_path}', 'w') as fw:
        fw.write(enc_data)
    os.rename(file_path, file_path.replace(file_path, f'{file_path}.locked'))


def unlock(file_path, key):
    with open(file_path, 'r') as fr:
        data = fr.read()

    dcr_data = stringMD(data, key)
    b64dData = b64.b64decode(dcr_data)

    with open(file_path, 'wb') as fw:
        fw.write(b64dData)
    os.rename(file_path, file_path.replace('.locked', ''))



# Making new DB for the following functions for changing your encryption.
def make_db():
    database = sqlite3.connect(f'pwords2{project_ext}')
    c = database.cursor()
    c.execute('''CREATE TABLE logins(id integer, data text)''')
    c.execute('''CREATE TABLE notes(note_name text, note_data text)''')
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
        # Get list of IDs from original database.
        database1 = sqlite3.connect(f'pwords{project_ext}')
        c1 = database1.cursor()
        c1.execute(f"SELECT id FROM logins")
        ids = c1.fetchall()
        ids_lst = list(itertools.chain(*ids))


        # Get list of data from original database.
        c1.execute(f"SELECT data FROM logins")
        enc_data_logins = c1.fetchall()
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
            database2 = sqlite3.connect(f'pwords2{project_ext}')
            c2 = database2.cursor()
            c2.execute(f"INSERT INTO logins VALUES ('{a}', '{b}')")
            database2.commit()


        c1.execute(f"SELECT note_name FROM notes")
        note_names = c1.fetchall()
        nnlist = list(itertools.chain(*note_names))

        c1.execute(f"SELECT note_data FROM notes")
        note_data = c1.fetchall()
        ndlist = list(itertools.chain(*note_data))

        if not note_names or not note_data:
            clear()
            print('Oof..nothing here but us foxos...')
            return False


        # Get all of the note data in ndlist above and decrypt them, then append
        note_data_list=[]
        for d in ndlist:
            if not d:
                pass
            else:
                old_note_data = stringMD(d, D_old_key)
                note_data_list.append(old_note_data)


        # Get all of the decrypted note data in note_data_list above and encrypt them, then append
        enc_note_data_list=[]
        for e in note_data_list:
            if not e:
                pass
            else:
                new_note_data = stringME(bytes(e, 'unicode-escape'), E_new_key)
                enc_note_data_list.append(new_note_data)


        for nn,nd in zip(nnlist, enc_note_data_list):
            database2 = sqlite3.connect(f'pwords2{project_ext}')
            c2 = database2.cursor()
            c2.execute(f"INSERT INTO notes VALUES ('{nn}', '{nd}')")
            database2.commit()

        database1.close()
        database2.close()
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
            c=0
            for _ in range(amount):
                c+=1
                # random.choice() is pycryptodome's "from Crypto.Random import random" and NOT the bad predictable "random" library.
                password = ''.join(random.choice(all) for _ in range(length))
                print(f'Pass {c}: {password}', file=f)
            clear()
            print('Your newly generated random password(s) and hash info has been saved to "pass.txt".\n\n')
            input('Press "enter" to continue...')
            clear()
    else:
        clear()
        print("Pass.txt not found, downloading file from repository..")
        wget.download("https://raw.githubusercontent.com/therealOri/Genter/main/pass.txt")
        clear()
        with open('pass.txt', 'w') as f:
            c=0
            for _ in range(amount):
                c+=1
                password = ''.join(random.choice(all) for _ in range(length))
                print(f'Pass {c}: {password}', file=f)
            clear()
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
        main_options = ['[1] - Passwords?', '[2] - Manage logins?', '[3] - Manage secure notes?', '[4] - Make key?', '[5] - Get Hashes', '[6] - Lock database?', '[7] - Unlock database?', '[8] - Change credentials', '[9] - Exit?']


        print(f'{banner()}\n\nWhat would you like to do?\n-----------------------------------------------------------\n')
        main_option = beaupy.select(main_options, cursor_style="#ffa533")

        if not main_option:
            clear()
            sys.exit("Keyboard Interuption Detected!\nGoodbye <3")


        if main_options[0] in main_option:
            while True:
                clear()
                password_options = ['[1] - Make Password?', '[2] - Make phrase?', '[3] - Show pass.txt', '[4] - Clear pass.txt', '[5] - Back?']
                print(f'{banner()}\n\nWhat would you like to do?\n-----------------------------------------------------------\n')
                pass_option = beaupy.select(password_options, cursor_style="#ffa533")

                if not pass_option:
                    clear()
                    break


                if password_options[0] in pass_option:
                    """Make Passwords"""
                    clear()
                    main()


                if password_options[1] in pass_option:
                    """Make Phrases"""
                    clear()
                    phrase = phrzgn()
                    if phrase == None:
                        clear()
                    else:
                        print(phrase)
                        input('\n\nPress "enter" to continue...')
                        clear()


                if password_options[2] in pass_option:
                    """Show pass.txt"""
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


                if password_options[3] in pass_option:
                    """Clear pass.txt"""
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

                if password_options[4] in pass_option:
                    clear()
                    break



        # Manage Logins
        if main_options[1] in main_option:
            clear()
            while True:
                login_options = ['[1] - Add login?', '[2] - Remove login?', '[3] - Show saved logins?', '[4] - Back?']
                print(f'{banner()}\n\nWhat would you like to manage?\n-----------------------------------------------------------\n')
                login_option = beaupy.select(login_options, cursor_style="#ffa533")


                if login_option == None:
                    clear()
                    break

                # Add passwords
                if login_options[0] in login_option:
                    if os.path.isfile(f'pwords{project_ext}') or os.path.isfile(f'pwords{project_ext}.locked'):
                        if os.path.isfile(f'pwords{project_ext}.locked'):
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
                            if not email or email.lower() == 'q':
                                clear()
                                continue

                            if j_load()[1] == True:
                                passwd = beaupy.prompt(f'Password to save for "{web.lower()}"?: ', secure=True)
                            else:
                                passwd = beaupy.prompt(f'Password to save for "{web.lower()}"?: ', secure=False)
                            if not passwd or passwd.lower() == 'q':
                                clear()
                                continue

                            notes = beaupy.prompt("(Optional) - Additional Information/notes: ")
                            if not notes or notes.lower() == 'q':
                                clear()
                                continue

                            if j_load()[1] == True:
                                master = beaupy.prompt("Master Key for encryption: ", secure=True)
                            else:
                                master = beaupy.prompt("Master Key for encryption: ", secure=False)
                            if not master or master.lower() == 'q':
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
                        if os.path.isfile(f'pwords{project_ext}.locked'):
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
                            if not email or email.lower() == 'q':
                                clear()
                                continue

                            if j_load()[1] == True:
                                passwd = beaupy.prompt(f'Password to save for "{web.lower()}"?: ', secure=True)
                            else:
                                passwd = beaupy.prompt(f'Password to save for "{web.lower()}"?: ', secure=False)
                            if not passwd or passwd.lower() == 'q':
                                clear()
                                continue

                            notes = beaupy.prompt("(Optional) - Additional Information/notes: ")
                            if not notes or notes.lower() == 'q':
                                clear()
                                continue

                            if j_load()[1] == True:
                                master = beaupy.prompt("Master Key for encryption: ", secure=True)
                            else:
                                master = beaupy.prompt("Master Key for encryption: ", secure=False)
                            if not master or master.lower() == 'q':
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
                if login_options[1] in login_option:
                    if os.path.isfile(f'pwords{project_ext}') or os.path.isfile(f'pwords{project_ext}.locked'):
                        if os.path.isfile(f'pwords{project_ext}.locked'):
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

                            if not rmv_key or rmv_key.lower() == 'q':
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
                if login_options[2] in login_option:
                    if os.path.isfile(f'pwords{project_ext}') or os.path.isfile(f'pwords{project_ext}.locked'):
                        if os.path.isfile(f'pwords{project_ext}.locked'):
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

                            if not show_logins_key or show_logins_key.lower() == 'q':
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


                if login_options[3] in login_option:
                    clear()
                    break



        #Manage Notes
        if main_options[2] in main_option:
            clear()
            def get_note_names():
                database = sqlite3.connect('pwords.gter')
                c = database.cursor()
                c.execute("SELECT note_name FROM notes")
                all_note_names = c.fetchall()
                note_names_list = list(itertools.chain(*all_note_names))
                database.commit()
                database.close()
                return note_names_list #will either be an empty list or a list of names.

            while True:
                note_options = ['[1] - Add note?', '[2] - Edit note?', '[3] - Remove note?', '[4] - Show notes?', '[5] - Back?']
                print(f'{banner()}\n\nWhat would you like to do?\n-----------------------------------------------------------\n')
                note_option = beaupy.select(note_options, cursor_style="#ffa533")


                if note_option == None:
                    clear()
                    break


                if note_options[0] in note_option:
                    """Add Notes"""
                    if os.path.isfile(f'pwords{project_ext}') or os.path.isfile(f'pwords{project_ext}.locked'):
                        if os.path.isfile(f'pwords{project_ext}.locked'):
                            clear()
                            print("Database file does not exist or is encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            print(f'{banner()}\n\nPress "ctrl+c" to go back/exit.\n-----------------------------------------------------------\n')
                            note_name = beaupy.prompt("Name of the note you are wanting to make/save?")
                            if not note_name:
                                clear()
                                continue

                            note_data = beaupy.prompt("Message or note you want to save?")
                            if not note_data:
                                clear()
                                continue

                            key = beaupy.prompt("Encryption key")
                            if not key:
                                clear()
                                continue

                            note_data = bytes(note_data, 'unicode-escape')
                            try:
                                key = b64.b64decode(key)
                            except Exception:
                                clear()
                                print("Provided key isn't base64 encoded...\n\n")
                                input('Press "enter" to continue...')
                                clear()
                                continue

                            note_names_list = get_note_names()
                            if note_name in note_names_list:
                                clear()
                                print(f'The name of notes are not allowed to be identical. "{note_name}" already exists in the database. Please try again or feel free to edit this note instead!')
                                input('An error has occured..note has not been saved!\n\nPress "enter" to continue...')
                                clear()
                                continue
                            else:
                                clear()
                                print("Encrypting and saving note!...")
                                enc_note_data = stringME(note_data, key)
                                time.sleep(1)
                                database = sqlite3.connect('pwords.gter')
                                c = database.cursor()
                                c.execute(f"INSERT INTO notes VALUES ('{note_name}', '{enc_note_data}')")
                                database.commit()
                                database.close()
                            clear()
                            input('Note has been saved!\n\nPress "enter" to continue...')
                            clear()
                            continue
                    else:
                        clear()
                        print(f"pwords{project_ext} not found, downloading from the repository...")
                        wget.download(f"https://raw.githubusercontent.com/therealOri/Genter/main/pwords{project_ext}")
                        input(f'\n\n"pwords{project_ext}" has been downloaded. Press "enter" to continue.')
                        clear()
                        pprint(f'{banner()}\n\nPress "ctrl+c" to go back/exit.\n-----------------------------------------------------------\n')
                        note_name = beaupy.prompt("Name of the note you are wanting to make/save?")
                        if not note_name:
                            clear()
                            continue

                        note_data = beaupy.prompt("Message or note you want to save?")
                        if not note_data:
                            clear()
                            continue

                        key = beaupy.prompt("Encryption key")
                        if not key:
                            clear()
                            continue

                        note_data = bytes(note_data, 'unicode-escape')
                        try:
                            key = b64.b64decode(key)
                        except Exception:
                            clear()
                            print("Provided key isn't base64 encoded...\n\n")
                            input('Press "enter" to continue...')
                            clear()
                            continue

                        note_names_list = get_note_names()
                        if note_name in note_names_list:
                            clear()
                            print(f'The name of notes are not allowed to be identical. "{note_name}" already exists in the database. Please try again or feel free to edit this note instead!')
                            input('An error has occured..note has not been saved!\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            print("Encrypting and saving note!...")
                            enc_note_data = stringME(note_data, key)
                            time.sleep(1)
                            database = sqlite3.connect('pwords.gter')
                            c = database.cursor()
                            c.execute(f"INSERT INTO notes VALUES ('{note_name}', '{enc_note_data}')")
                            database.commit()
                            database.close()
                        clear()
                        input('Note has been saved!\n\nPress "enter" to continue...')
                        clear()
                        continue





                if note_options[1] in note_option:
                    """edit notes"""
                    if os.path.isfile(f'pwords{project_ext}') or os.path.isfile(f'pwords{project_ext}.locked'):
                        if os.path.isfile(f'pwords{project_ext}.locked'):
                            clear()
                            print("Database file does not exist or is encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            edit_note_name_list = get_note_names()
                            if not edit_note_name_list:
                                print('Oof..nothing here but us foxos...')
                                input('An error has occured, database is empty.\n\nPress "enter" to continue...')
                                clear()
                                continue

                            edit_options = ['Note name?', 'Note data/message?']
                            print(f'{banner()}\n\nPress "ctrl+c" to go back/exit.\n-----------------------------------------------------------\n')
                            chosen_edit_option = beaupy.select(edit_options, cursor_style="#ffa533")
                            if not chosen_edit_option:
                                clear()
                                continue

                            if edit_options[0] in chosen_edit_option:
                                clear()
                                print(f'{banner()}\n\nPress "ctrl+c" to go back/exit.\n-----------------------------------------------------------\n')
                                note_name = beaupy.select(edit_note_name_list, cursor_style="#ffa533")
                                if not note_name:
                                    clear()
                                    continue
                                updated_note_name = beaupy.prompt(f'What would you like to change the note name "{note_name}" to?')
                                clear()
                                print("Updating note name!...")
                                database = sqlite3.connect('pwords.gter')
                                c = database.cursor()
                                c.execute(f"UPDATE notes SET note_name='{updated_note_name}' WHERE note_name='{note_name}'")
                                database.commit()
                                database.close()
                                time.sleep(1)
                                clear()
                                input('Note name has been updated!\n\nPress "enter" to continue...')
                                clear()
                                continue

                            else:
                                clear()
                                print(f'{banner()}\n\nPress "ctrl+c" to go back/exit.\n-----------------------------------------------------------\n')
                                note_name = beaupy.select(edit_note_name_list, cursor_style="#ffa533")
                                if not note_name:
                                    clear()
                                    continue

                                key = beaupy.prompt("Encryption key")
                                if not key:
                                    clear()
                                    continue
                                try:
                                    key = b64.b64decode(key)
                                except Exception:
                                    clear()
                                    print("Provided key isn't base64 encoded...\n\n")
                                    input('Press "enter" to continue...')
                                    clear()
                                    continue

                                database = sqlite3.connect('pwords.gter')
                                c = database.cursor()
                                c.execute(f"SELECT note_data FROM notes WHERE note_name='{note_name}'")
                                enc_note_data = c.fetchone()
                                database.commit()
                                decrypted_note_data = stringMD(enc_note_data[0], key)

                                print(f'Note for "{note_name}": ({decrypted_note_data})')
                                new_note = beaupy.prompt(f'Editing note/description for "{note_name}"\n\nNote')
                                if not new_note:
                                    clear()
                                    continue
                                clear()
                                print("Updating note!...")
                                new_note = bytes(new_note, 'unicode-escape')
                                new_enc_note = stringME(new_note, key)
                                c.execute(f"UPDATE notes SET note_data = '{new_enc_note}' WHERE note_name='{note_name}'")
                                database.commit()
                                database.close()
                                time.sleep(1)
                                clear()
                                input('Note has been updated!\n\nPress "enter" to continue...')
                                clear()
                                continue
                    else:
                        clear()
                        print(f"pwords{project_ext} not found, downloading from the repository...")
                        wget.download(f"https://raw.githubusercontent.com/therealOri/Genter/main/pwords{project_ext}")
                        input(f'\n\n"pwords{project_ext}" has been downloaded and is currently empty with no notes to edit.\n\nPress "enter" to continue...')
                        clear()
                        continue





                if note_options[2] in note_option:
                    """Remove Notes"""
                    if os.path.isfile(f'pwords{project_ext}') or os.path.isfile(f'pwords{project_ext}.locked'):
                        if os.path.isfile(f'pwords{project_ext}.locked'):
                            clear()
                            print("Database file does not exist or is encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            remove_note_name_list = get_note_names()
                            if not remove_note_name_list:
                                print('Oof..nothing here but us foxos...')
                                input('An error has occured, database is empty.\n\nPress "enter" to continue...')
                                clear()
                                continue

                            print(f'{banner()}\n\nPress "ctrl+c" to go back/exit.\n-----------------------------------------------------------\n')
                            print("What note do you wish to remove?")
                            note_name = beaupy.select(remove_note_name_list, cursor_style="#ffa533")
                            if not note_name:
                                clear()
                                continue

                            database = sqlite3.connect('pwords.gter')
                            c = database.cursor()
                            c.execute(f"DELETE FROM notes WHERE note_name='{note_name}'")
                            database.commit()
                            database.close()
                            input('Note has been removed/deleted!\n\nPress "enter" to continue...')
                            clear()
                            continue
                    else:
                        clear()
                        print(f"pwords{project_ext} not found, downloading from the repository...")
                        wget.download(f"https://raw.githubusercontent.com/therealOri/Genter/main/pwords{project_ext}")
                        input(f'\n\n"pwords{project_ext}" has been downloaded and is currently empty with no notes to remove.\n\nPress "enter" to continue...')
                        clear()
                        continue





                if note_options[3] in note_option:
                    """show notes"""
                    if os.path.isfile(f'pwords{project_ext}') or os.path.isfile(f'pwords{project_ext}.locked'):
                        if os.path.isfile(f'pwords{project_ext}.locked'):
                            clear()
                            print("Database file does not exist or is encrypted...")
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                        else:
                            clear()
                            show_note_name_list = get_note_names()
                            if not show_note_name_list:
                                print('Oof..nothing here but us foxos...')
                                input('An error has occured, database is empty.\n\nPress "enter" to continue...')
                                clear()
                                continue

                            print(f'{banner()}\n\nPress "ctrl+c" to go back/exit.\n-----------------------------------------------------------\n')
                            note_name = beaupy.select(show_note_name_list, cursor_style="#ffa533")
                            if not note_name:
                                clear()
                                continue

                            key = beaupy.prompt("Encryption key")
                            if not key:
                                clear()
                                continue
                            try:
                                key = b64.b64decode(key)
                            except Exception:
                                clear()
                                print("Provided key isn't base64 encoded...\n\n")
                                input('Press "enter" to continue...')
                                clear()
                                continue

                            database = sqlite3.connect('pwords.gter')
                            c = database.cursor()
                            c.execute(f"SELECT note_data FROM notes WHERE note_name='{note_name}'")
                            enc_note_data = c.fetchone()
                            database.commit()
                            database.close()
                            decrypted_note_data = stringMD(enc_note_data[0], key)
                            print(f'Note for "{note_name}" is: ({decrypted_note_data})')
                            input('\n\nPress "enter" to continue...')
                            clear()
                            continue
                    else:
                        clear()
                        print(f"pwords{project_ext} not found, downloading from the repository...")
                        wget.download(f"https://raw.githubusercontent.com/therealOri/Genter/main/pwords{project_ext}")
                        input(f'\n\n"pwords{project_ext}" has been downloaded and is currently empty with no notes to show.\n\nPress "enter" to continue...')
                        clear()
                        continue


                if note_options[4] in note_option:
                    """Leave menu"""
                    clear()
                    break


        #key gen
        if main_options[3] in main_option:
            clear()
            m_gen = beaupy.prompt('(It is reccomended to use genter to make the password)\nPress "q" or "ctrl+c" to go back/exit.\n\nPassword to generate master_key - (100+ characters long.): ', secure=True)
            if not m_gen or m_gen.lower() == 'q':
                clear()
                continue
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




        #hashing
        if main_options[4] in main_option:
            clear()
            if j_load()[1] == True:
                pword = beaupy.prompt('Press "q" to go back/quit.\n-----------------------------------------------------------\nWhat would you like to hash?: ', secure=True)
            else:
                pword = beaupy.prompt('Press "q" to go back/quit.\n-----------------------------------------------------------\nWhat would you like to hash?: ', secure=False)


            if not pword or pword.lower() == 'q':
                clear()
            else:
                clear()
                final_hash = hash(pword)

                # "final_hash[1]" is name of hash that was used. And "[0]" is the actual hash value.
                print(f'{final_hash[1]} hash for "{pword}" - {final_hash[0]}\n\n')
                input('Press "enter" to continue...')
                clear()




        #Lock Database
        if main_options[5] in main_option:
            if os.path.isfile(f'pwords{project_ext}') or os.path.isfile(f'pwords{project_ext}.locked'):
                if os.path.isfile(f'pwords{project_ext}.locked'):
                    clear()
                    print("Database file already encrypted...")
                    input('\n\nPress "enter" to continue...')
                    clear()
                else:
                    clear()
                    print('Please provide credentials to lock the database.\nPress "q" to go back/quit.\n\n')
                    file_path = beaupy.prompt("File path? - (Drag & drop): ")
                    if not file_path or file_path.lower() == 'q':
                        clear()
                        continue
                    file_path = file_path.replace('\\ ', ' ').strip()

                    if j_load()[1] == True:
                        enc_key = beaupy.prompt("Encryption Key: ", secure=True)
                    else:
                        enc_key = beaupy.prompt("Encryption Key: ", secure=False)

                    if not enc_key or enc_key.lower() == 'q':
                        clear()
                        continue

                    try:
                        enc_key = b64.b64decode(enc_key)
                    except Exception:
                        clear()
                        print("Provided key isn't base64 encoded...\n\n")
                        input('Press "enter" to continue...')
                        clear()
                        continue

                    lock(file_path, enc_key)
                    clear()
                    input('Your file has been succesfully locked!\n\nPress "enter" to continue...')
                    clear()
                    continue
            else:
                clear()
                print(f"pwords{project_ext} not found, downloading from the repository...")
                wget.download(f"https://raw.githubusercontent.com/therealOri/Genter/main/pwords{project_ext}")
                input("\n\nDatabse is empty, skipping on locking the database.\n\nPress 'enter' to continue...")
                clear()
                continue


        #unlock Database
        if main_options[6] in main_option:
            if os.path.isfile(f'pwords{project_ext}') or os.path.isfile(f'pwords{project_ext}.locked'):
                if os.path.isfile(f'pwords{project_ext}.locked'):
                    clear()
                    print('Please provide the correct credentials to unlock the database.\nPress "q" to go back/quit.\n\n')
                    file_path2 = beaupy.prompt("File path? - (Drag & drop): ")
                    if not file_path2 or file_path2.lower() == 'q':
                        clear()
                    file_path2 = file_path2.replace('\\ ', ' ').strip()

                    if j_load()[1] == True:
                        enc_key2 = beaupy.prompt("Encryption Key: ", secure=True)
                    else:
                        enc_key2 = beaupy.prompt("Encryption Key: ", secure=False)
                    if not enc_key2 or enc_key2.lower() == 'q':
                        clear()

                    #if given random string of text, it will try to decode, if it can't, send error.
                    #(Sometimes it likes to decode that random gibberish as it thinks it is valid base64..)
                    try:
                        enc_key2 = b64.b64decode(enc_key2)
                    except Exception:
                        clear()
                        print("Provided key isn't base64 encoded...\n\n")
                        input('Press "enter" to continue...')
                        clear()

                    unlock(file_path2, enc_key2)
                    clear()
                    input('Your file has been succesfully unlocked!\n\nPress "enter" to continue...')
                    clear()
                else:
                    clear()
                    print("Database file is not encrypted/locked...")
                    input('\n\nPress "enter" to continue...')
                    clear()
            else:
                clear()
                print(f"pwords{project_ext} not found, downloading from the repository...")
                wget.download(f"https://raw.githubusercontent.com/therealOri/Genter/main/pwords{project_ext}")
                input("\n\nDatabse is empty and not locked, skipping on unlocking the database.\n\nPress 'enter' to continue...")
                clear()


        #change credentials
        if main_options[7] in main_option:
            if os.path.isfile(f'pwords{project_ext}') or os.path.isfile(f'pwords{project_ext}.locked'):
                if os.path.isfile(f'pwords{project_ext}.locked'):
                    clear()
                    print("Database file does not exist or is encrypted...")
                    input('\n\nPress "enter" to continue...')
                    clear()
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
                    else:
                        crds = change_creds(old_master_key, new_master_key)
                        if crds == False:
                            input('Unable to change credentials, No IDs or No Data can be foud in the database..\n\nPress "enter" to continue...')
                            clear()
                            os.remove(f'pwords2{project_ext}')
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



        if main_options[8] in main_option:
            clear()
            sys.exit("Goodbye! <3")

