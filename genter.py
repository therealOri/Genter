#v4.0.0
#Imports
import beaupy
from beaupy.spinners import *
import hashlib
import json
import os
import sys
import wget
from string import ascii_lowercase, ascii_uppercase, digits
from pystyle import Colors, Colorate
import time
from alive_progress import alive_bar
from libs import rnd, kdf
import requests





#Languages
uppercase_letters = ascii_uppercase
lowercase_letters = ascii_lowercase
symbols = "!=<>'@#$%^&*()[\],.;:-_/+?{|}`~"
unicode = "¡¢£¤¥¦§¨©ª«¬®™️¯°±²³´µ¶·¸¹º»¼½¾¿×Ø÷øÞßƒðÐıæᔕ€≡‗"
emojis = "⚔☣️⚛️〰️🗝️🔒⛓️✨🫠🫧🫥💢🪬"
uni_boxes = "░▒▓█▄▀■"
uni_pipes = "╣╗╝┴┬╩╦═╬"
numbers = "012345678901234567890"
korean = "ㅂㅋㅎㅭㅱㅶㅹㅺㅿㆁㆄㆅ"
russian = "БГДЁЖИЙЛПФфЦЧШЩЪЫЬЭЮЯ"
chinese = "诶比西迪伊尺杰大水开勒哦屁吉吾儿诶比西迪伊弗吉尺艾弗吉杰屁吉吾儿八九十开勒马娜哦月人马娜口"
greek = "ΓΔΘΛΞΠΣΦΨΩαβγδεζηθικλμνξπρστυφχψω"
portu = "ãáàâçéêíõóôúüÃÁÀÂÇÉÊÍÕÓÔÚÜ"
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



def clear():
    os.system('cls||clear')







def str_hash(password, salt):
    print(f'Press "ctrl+c" to go back/quit.\n{"-"*60}\n')
    hash_lst = ['Argon2id - (recommended)', 'PBkdf2', 'Scrypt']
    hash_type = beaupy.select(hash_lst, cursor_style="#ffa533")

    if not hash_type:
        return None


    if hash_lst[0] in hash_type:
        clear()
        password = bytes(password, 'utf-8')
        try:
            salt = bytes(salt, 'utf-8')
        except:
            salt = os.urandom(64)

        result1 = kdf.argon_hash(password, salt)
        return result1[0], result1[1], hash_type



    if hash_lst[1] in hash_type:
        clear()
        password = bytes(password, 'utf-8')
        try:
            salt = bytes(salt, 'utf-8')
        except:
            salt = os.urandom(64)

        result1 = kdf.pbkdf2_hash(password, salt)
        return result1[0], result1[1], hash_type



    if hash_lst[2] in hash_type:
        clear()
        password = bytes(password, 'utf-8')
        try:
            salt = bytes(salt, 'utf-8')
        except:
            salt = os.urandom(64)

        result1 = kdf.scrypt_hash(password, salt)
        return result1[0], result1[1], hash_type




# config.json file loading.
def j_load():
    if os.path.isfile('config.json'):
        with open('config.json') as f:
            data = json.load(f)
            options_flag = data['password_options_flag']
            secure_prompts = data['secure_prompts']
            wordlst = data['wordlst_update']
        return options_flag, secure_prompts, wordlst

    else:
        input('config.json file not found, press "enter" to create default config and continue...')
        json_config = {
            "password_options_flag": True,
            "secure_prompts": False,
            "wordlst_update": False
        }
        with open('config.json', 'w') as jwf:
            json.dump(json_config, jwf, ensure_ascii=False, indent=4)

        clear()
        with open('config.json') as f:
            data = json.load(f)
            options_flag = data['password_options_flag']
            secure_prompts = data['secure_prompts']
            wordlst = data['wordlst_update']
        return options_flag, secure_prompts, wordlst



# Showing contents of pass.txt and clearing it.
def show_pass():
    with open('pass.txt', 'r') as f:
        result = f.read()
        if not result:
            return None
        else:
            return result


def clr_pass():
  if os.path.getsize('pass.txt') > 0:
    with open('pass.txt', 'r+') as f:
      f.truncate(0)
    return 200
  else:
    return 404








def update_words():
    github_url = "https://raw.githubusercontent.com/therealOri/Genter/main/words.txt"
    hash_url = "https://raw.githubusercontent.com/therealOri/Genter/main/words_hash.txt"

    local_file = "words.txt"

    response = requests.get(hash_url)
    remote_hash = response.content.decode().strip()

    with open(local_file, "rb") as f:
        local_hash = hashlib.sha256(f.read()).hexdigest()

    if remote_hash == local_hash:
        clear()
        print(f"Note: {local_file} is up-to-date.")
        return
    else:
        clear()
        print(f"Note: There is an update for {local_file}. Updating words...")
        response = requests.get(github_url)
        if response.status_code == 200:
            with open(local_file, "wb") as f:
                f.write(response.content)
            input(f'{local_file} has been successfully updated!\n\nPress "enter" to continue...')
            clear()
            return 200
        else:
            clear()
            input(f'Error: could not get {local_file} contents from GitHub. Please contact therealOri:https://github.com/therealOri/ on github if this continues...\n\nPress "enter" to continue..."')
            clear()
            return 404




#Generate Phrases (Like Bitwarden)
def phrzgn():
    dash=60
    if os.path.isfile('words.txt'):
        if j_load()[2] == True:
            check = update_words()
            if check == 404:
                return
        else:
            pass #updates set to false. Continue.
    else:
        print("words.txt doesn't exist and is to big to create...Downloading words.txt from repo.")
        wget.download("https://raw.githubusercontent.com/therealOri/Genter/main/words.txt")
        clear()

    while True:
        try:
            number = beaupy.prompt(f'(Press "ctrl+c" to exit)\n{"-"*dash}\n\nHow many words?: ')
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


    sep = beaupy.prompt(f'(Press "ctrl+c" to exit)\n{"-"*dash}\n\nLine separator? (leave empty for default "-"): ')
    if sep == None:
        clear()
        return
    else:
        if sep == '':
            sep = '-'



    #Returns True or False. Basically Yes or No?
    capital_words = ''
    default_words = ''
    capitalize = beaupy.confirm(f'(Press "ctrl+c" to exit)\n{"-"*dash}\n\nCapitalize?')
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
            capital_words = f'{sep}'.join(rnd.choice(c_lst) for _ in range(number))
        else:
            cap = False
            default_words = f'{sep}'.join(rnd.choice(word_list) for _ in range(number))


    numbers = beaupy.confirm(f'(Press "ctrl+c" to exit)\n{"-"*dash}\n\nNumber?')
    if numbers == None:
        clear()
        return
    else:
        if numbers:
            num = True
            rn_num = rnd.randint(0, 9) # <-- Get a random number to be used with only 1 of the words defined in capital_words or default_words below.
            word_index = rnd.randint(0, number-1) # Get random index that is in the word list

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




def main():
    try:
        #You can configure what you want to do in the config.json file.
        if j_load()[0] == True:
            langs = ['uppercase', 'lowercase', 'numbers', 'symbols', 'korean', 'russian', 'chinese', 'greek', 'portu', 'unicode', 'uni_boxes', 'uni_pipes', 'hindi', 'arabic', 'emojis', 'amharic', 'sinhala', 'hieroglyphs']

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
                all += greek

            if langs[8] in langs_config:
                all += portu

            if langs[9] in langs_config:
                all += unicode

            if langs[10] in langs_config:
                all += uni_boxes

            if langs[11] in langs_config:
                all += uni_pipes

            if langs[12] in langs_config:
                all += hindi

            if langs[13] in langs_config:
                all += arabic

            if langs[14] in langs_config:
                all += emojis

            if langs[15] in langs_config:
                all += amharic

            if langs[16] in langs_config:
                all += sinhala

            if langs[17] in langs_config:
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
            grk = True
            port = True
            spec = True
            block = True
            pipes = True
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
            if grk:
                all += greek
            if port:
                all += portu
            if spec:
                all += unicode
            if block:
                all += uni_boxes
            if a_box:
                all += uni_pipes
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
    print('WARNING!!: Password(s) WILL be overwritten when generating passwords again.\nPress "q" or "ctrl+c" to go back. \n\n')
    try:
        length = beaupy.prompt('How long do you want your password(s)?: ')
        if not length:
            clear()
            return None
        elif length.lower() == 'q':
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
        amount = beaupy.prompt('How many do you want generated?: ')
        if not amount:
            clear()
            return None
        elif amount.lower() == 'q':
            clear()
            return None
        else:
            amount = int(amount)
    except Exception as e:
        clear()
        print(f'Oops..The value you gave me is not a number/integer.\n[Error]: {e}')
        input('\nPress "enter" to continue...')
        return None



    all_text = rnd.shuffle(all)
    print(f"Army of hamsters deployed...generating password(s)...\n{'-'*100}")
    with alive_bar(amount) as bar:
        with open('pass.txt', 'w') as wf:
            c=0
            for _ in range(amount):
                c+=1
                password = ''.join(rnd.choice(all) for _ in range(length))
                passwprd = rnd.shuffle(password)
                print(f'Pass {c}: {password}', file=wf)
                bar()
    clear()
    print('Your newly generated password(s) has been saved to "pass.txt".\n\n')
    input('Press "enter" to continue...')
    clear()


##-------------- ^^ Functions End ^^ --------------##






if __name__ == '__main__':
    dash=60
    while True:
        clear()
        #NOTE - This format will leave room for expansion of features.
        #
        # Passwords - (Make pass, Make phrase, Show pass, Clear pass)
        # Get hash
        # Exit
        main_options = ['[1] - Passwords?', '[2] - Get Hashes', '[3] - Exit?']


        print(f'{banner()}\n\nWhat would you like to do?\n{"-"*dash}\n')
        main_option = beaupy.select(main_options, cursor_style="#ffa533")

        if not main_option:
            clear()
            sys.exit("Keyboard Interuption Detected!\nGoodbye <3")


        if main_options[0] in main_option:
            while True:
                clear()
                password_options = ['[1] - Make Password?', '[2] - Make phrase?', '[3] - Show pass.txt', '[4] - Clear pass.txt', '[5] - Back?']
                print(f'{banner()}\n\nWhat would you like to do?\n{"-"*dash}\n')
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
                        clear()
                        passwords = show_pass()
                        if not passwords:
                            print('No passwords found in "pass.txt"\n\n')
                            input('Press "enter" to continue...')
                            clear()
                        else:
                            print(passwords)
                            input('Press "enter" to continue...')
                            clear()
                    else:
                        clear()
                        with open('pass.txt', 'w') as fm:
                            fm.write('\n')
                        clr_pass()
                        input("pass.txt was not found and has been created successfully!.\n\nPress 'enter' to continue...")
                        clear()
                        continue


                if password_options[3] in pass_option:
                    """Clear pass.txt"""
                    if os.path.isfile('pass.txt'):
                        check = clr_pass()
                        if check == 200:
                            input('Success: pass.txt has been wiped clean.\n\nPress "enter" to continue...')
                            clear()
                        else:
                            input('Error: pass.txt file is already empty.\n\nPress "enter" to continue...')
                            clear()
                    else:
                        clear()
                        with open('pass.txt', 'w') as fm:
                            fm.write('\n')
                        clr_pass()
                        input("pass.txt was not found and has been created successfully!.\n\nPress 'enter' to continue...")
                        clear()
                        continue

                if password_options[4] in pass_option:
                    clear()
                    break




        #hashing
        if main_options[1] in main_option:
            clear()
            if j_load()[1] == True:
                pword = beaupy.prompt(f'Press "q" to go back/quit.\n{"-"*dash}\nWhat would you like to hash?: ', secure=True)
                if not pword or pword.lower() == 'q':
                    clear()
                    continue

                salt = beaupy.prompt(f'Press "q" to go back/quit.\n{"-"*dash}\nWhat would you like to have as the salt?', secure=True)
                if not salt or salt.lower() == 'q':
                    clear()
                    continue
            else:
                pword = beaupy.prompt(f'Press "q" to go back/quit.\n{"-"*dash}\nWhat would you like to hash?: ', secure=False)
                if not pword or pword.lower() == 'q':
                    clear()
                    continue

                salt = beaupy.prompt(f'Press "q" to go back/quit.\n{"-"*dash}\nWhat would you like to have as the salt?', secure=False)
                if not salt or salt.lower() == 'q':
                    clear()
                    continue



            clear()
            final_hash = str_hash(pword, salt)
            if not final_hash:
                clear()
                continue

            # "final_hash[2]" is name of hash that was used. "[1]" is the salt and "[0]" is the actual hash value.
            print(f'{final_hash[2]} hash & salt for "{pword}"  |  Hash: {final_hash[0]}  |  Salt - {final_hash[1]}\n\n')
            input('Press "enter" to continue...')
            clear()



        if main_options[2] in main_option:
            clear()
            sys.exit("Goodbye! <3")


