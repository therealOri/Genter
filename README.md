# Genter
![](https://img.shields.io/badge/Coded%20By%20Human-100%25-brightgreen)

Genter will allow you to create a very crazy & strong randomized password.
You can manually pick and choose what languages and symbols are used. You can also change the length of the password and how many you want to generate. 
> Feel free to contribute! Anything helps more than you'd think!
__ __

<br />
<br>

(Latest) - Update | 09/09/23:
# Features revert
- Reverted "Genter" to be mainly a password generator. It was starting to become to much to handle with all of the password and note manager stuff.
- Passwords and phrases are generated using atmospheric noise instead of math, time, etc. (Thanks to [random.org](https://random.org/))
- If you are going to generate many passwords, it will try to generate in chunks of 5 at a time as to not go over or close to random.org's api limits, while still being pretty fast.
  > Because "`concurrent.futures`" is being used, each chunk of "5" will be generated mostly at the same time.
__ __

<br>

Update | 05/06/2023:

Added:
- [x] Windows executable has been made and can be downloaded now. 
> This is also (for now) the last time I do anything with windows .exe files. Any new updates will just be to genter.py and the linux ELF file/binary. If anyone would like to, they are more than welcome to contribute to the windows version and help keep it maintained.
__ __

<br>

Update | 1/28/2023:

If you have an older version of this project, You should update to the current version now!.
> Older releases are not meant to be used or downloaded, they only exist to showcase progess....and idk how to make them not be downloadable but still viewable.

<br />

Added:
- [x] Replaced Scrypt with Argon2di (kdf).
- [x] Added Secure Notes manager menu and allows you to store secure/encrypted notes in the database. (The note names are not encrypted but the note data is.)
- [x] Updated menus with numbers to look a bit better.
- [x] Changed how the "get hash" function works and allows you to chose from different hashing options and returns the hash of the string of text you have typed.. (using hashlib).
- [x] New colorful banner/logo.
- [x] Squahed some boogs.
- [x] Changed up the menu, hopefully it looks better now and not to crowded.
- [x] Updated lock and unlock functions. They now use AES GCM like everything else. (Use a different key to lock and unlock database)
- [x] The "Change credentials" function now accommodates the new "secure notes" feature.
- [x] Linux and windows executable was compiled using Nuitka instead of pyinstaller. (Size of exe should be smaller now)
- [x] Changed how passwords are shown in pass.txt. (Removed all of the hash, salt, and key information)
- [x] Updated "change credentials" function to reflect changes.

<br />

If you come across ANY issues or bugs, please report it by making an [issue](https://github.com/therealOri/Genter/issues). It helps out a lot!
> I am still fairly new to making and managing an .exe file so I would love any feedback on what could be done better or changed. <3
__ __

<br />
<br />

# ToDo/To-Add
> [] - Make Linux executable binary.
> 
> [] - Make Windoes .exe file.
__ __

<br />
<br />

# Preview
(WiP)
> Note: WiP

__ __




<br />
<br />

# Installation/Links

> If you do not have "virtualenv", you can install it via pip.
```mkd
pip install virtualenv
```

```zsh
git clone https://github.com/therealOri/Genter.git
cd Genter
virtualenv gterENV
source gterENV/bin/activate
pip install -r requirements.txt
python3 genter.py
```

<br />
<br />

- [Git Download](https://git-scm.com/downloads)
- [Blake2 Documentation](https://www.blake2.net)
  > For learning more about the blake2b option in the str_hash() function.
- [Hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
__ __


<br />
<br />


# Extra/Notes
> - If you don't have python3, then you can find, download, and install it from [here](https://www.python.org/downloads/). (Or from your package manager of choice).
> - If you are on windows 10 use this: [download](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe). (Pip3 comes with it)
> - If the "`options_flag`" in the config file is set to "true", Genter will ask you what you want to use in your password. If set to "False", Genter will use the already defined list of options that are all "True" by default found in the code. (Basically will use everything).
> - If the "`secure_prompts`" option in the config file is "true", it will hide what you type for certain prompts, etc. If it is set to "false" it will not hide what you type.
> - If "`wordlst_update`" option is set to true, it will update the wordlist to the current list found here in this repository each time you want to generate phrases. (I don't update the word list frequently enough to have this option be "true" but it's still neat to have just in case someone wants to update all of the time.)
__ __


<br />
<br />
<br />

# Support  |  Buy me a coffee <3
(God knows I need one xD)

Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)
