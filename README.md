# Genter
![](https://img.shields.io/badge/Coded%20By%20Human-100%25-brightgreen)

Genter will allow you to create a very crazy & strong randomized password.
You can manually pick and choose what languages and symbols are used. You can also change the length of the password and how many you want to generate. 
> Feel free to contribute! Anything helps more than you'd think!
__ __

<br>
<br>

(Latest) - Update | 11/06/23:
# Kernel RNG Updates
- Changed randomness from using atmos to genter's own local libs "rnd" library.
- Hashing now uses KDF's instead of normal hashing. The KDFs being used are [Argon2id, PBKdf2,  Scrypt]
- Instead of downloading files from the github repo, genter will now make them locally instead of downloading them if they aren't found. The only exception is the "words.txt" file. As that is to large and has to many words and stuff to just create if not found. So that will still be downloaded, but it now has a new way of checking to see if a new version of words.txt exists/if there is a new update.

<br>
<br>

If you come across ANY issues or bugs, please report it by making an [issue](https://github.com/therealOri/Genter/issues). It helps out a lot! And if you happen to like what I have made, make sure to leave a :star:.
__ __

<br>
<br>

# ToDo/To-Add
> 
> [] - Make Windoes .exe file.
__ __

<br />
<br />

# Preview
[![asciicast](https://asciinema.org/a/619800.svg)](https://asciinema.org/a/619800)
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
- [Python](https://www.python.org/downloads/)
- [Python3 - [Windows]](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe)
__ __


<br />
<br />


# Extra/Notes
> - If the "`options_flag`" in the config file is set to "true", Genter will ask you what you want to use in your password. If set to "False", Genter will use the already defined list of options that are all "True" by default found in the code. (Basically will use everything).
> - If the "`secure_prompts`" option in the config file is "true", it will hide what you type for certain prompts, etc. If it is set to "false" it will not hide what you type. (Will allow for expansion or more features If I want to add more to genter.
> - If "`wordlst_update`" option is set to true, It will do a check to see if there is an update for words.txt and if an update is found, it will download the new words.txt file in this repo.


<br />
<br />
<br />

# Support  |  Buy me a coffee <3
(God knows I need one xD)

Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)
