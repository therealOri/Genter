#v3.0.0
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
import atmos
import concurrent.futures
import time
from alive_progress import alive_bar






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



def str_hash(password: str):
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
        prz_spinner = Spinner(ARC, "Picking words for the phrase...")
        prz_spinner.start()
        if capitalize:
            """Make list of words with the first letter capitalized."""
            c_lst = []
            for i in word_list:
                if len(i) < 3 or len(i) > 9:
                    pass #Ignore and move on to next item
                else:
                    c_lst.append(i.title())

            cap = True
            nums = atmos.randint(0, len(c_lst)-1, number)
            stuff = []
            for _ in nums:
                stuff.append(c_lst[_])
            capital_words = f'{sep}'.join(stuff)
            prz_spinner.stop()
        else:
            cap = False
            nums_l = atmos.randint(0, len(word_list)-1, number)
            stuff_l = []
            for _ in nums_l:
                stuff_l.append(word_list[_])
            default_words = f'{sep}'.join(stuff_l)
            prz_spinner.stop()


    numbers = beaupy.confirm('(Press "ctrl+c" to exit)\n-----------------------------------------------------------\n\nNumber?')
    if numbers == None:
        clear()
        return
    else:
        przn_spinner = Spinner(ARC, "Hamsters deployed...Building/Generating Phrase...")
        przn_spinner.start()
        if numbers:
            num = True
            rn_num = atmos.randint(0, 9) # <-- Get a random number to be used with only 1 of the words defined in capital_words or default_words below.
            word_index = atmos.randint(0, number-1) # Get random index that is in the word list

            if default_words != '':
                word_with_number = default_words.split(sep)
            else:
                word_with_number = capital_words.split(sep)

            word_with_number[word_index] = word_with_number[word_index] + str(rn_num)
            word_with_number = sep.join(word_with_number)
            przn_spinner.stop()
        else:
            num = False
            przn_spinner.stop()


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
    print('Note: Please make sure to write your password(s) down or save the password(s) into a new text file before running this script again.\nPress "q" or "ctrl+c" to go back. \n\n')
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



    def generate_password(all_text, length):
        nums = atmos.randint(0, len(all_text)-1, length)
        password = ''.join(all_text[_] for _ in nums)
        return password


    all_text = atmos.shuffle(all)
    batch_size = 5
    print(f"Army of hamsters deployed...generating password(s)...\n{'-'*100}")
    with alive_bar(amount//batch_size) as bar:
        with open('pass.txt', 'w') as wf:
            c=0
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for i in range(0, amount, batch_size):
                    futures = [executor.submit(generate_password, all_text, length) for _ in range(batch_size)]
                    for future in concurrent.futures.as_completed(futures):
                        if c == amount:
                            break
                        else:
                            result = future.result()
                            c+=1
                            print(f'Pass {c}: {result}', file=wf)
                    time.sleep(1)
                    bar()
    clear()
    print('Your newly generated password(s) has been saved to "pass.txt".\n\n')
    input('Press "enter" to continue...')
    clear()


##-------------- ^^ Functions End ^^ --------------##






if __name__ == '__main__':
    while True:
        clear()
        #NOTE - This format will leave room for expansion of features.
        #
        # Passwords - (Make pass, Make phrase, Show pass, Clear pass)
        # Get hash
        # Exit
        main_options = ['[1] - Passwords?', '[2] - Get Hashes', '[3] - Exit?']


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
                        check = clr_pass()
                        if check == 200:
                            input('Success: pass.txt has been wiped clean.\n\nPress "enter" to continue...')
                            clear()
                        else:
                            input('Error: pass.txt file is already empty.\n\nPress "enter" to continue...')
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




        #hashing
        if main_options[1] in main_option:
            clear()
            if j_load()[1] == True:
                pword = beaupy.prompt('Press "q" to go back/quit.\n-----------------------------------------------------------\nWhat would you like to hash?: ', secure=True)
            else:
                pword = beaupy.prompt('Press "q" to go back/quit.\n-----------------------------------------------------------\nWhat would you like to hash?: ', secure=False)


            if not pword or pword.lower() == 'q':
                clear()
            else:
                clear()
                final_hash = str_hash(pword)

                # "final_hash[1]" is name of hash that was used. And "[0]" is the actual hash value.
                print(f'{final_hash[1]} hash for "{pword}" - {final_hash[0]}\n\n')
                input('Press "enter" to continue...')
                clear()



        if main_options[2] in main_option:
            clear()
            sys.exit("Goodbye! <3")


