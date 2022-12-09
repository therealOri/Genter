# Genter
Genter will allow you to create a very crazy & strong randomized password.
You can manually pick and choose what languages and symbols are used. You can also change the length of the password and how many you want to generate. Also, In addition to the password generator, Genter has a built in password manager that you can use! Passwords are encrypted using AES and a "Password Based Key Derivation" master Key.
> Feel free to contribute! 

> Also, If you are good at auditing code and password encryption then please feel free to do so here and let me know what could be fixed and improved!
__ __

<br />

Update | 12/8/2022:
# New Features.
If you have an older version of this project, You should update to the current version now!.

Added:
- New way of handling database data. It will now be based off of IDs when picking a login. (which you can copy and paste) "Passwords" will now be referred to as "logins", as the website, email, password, and notes will all be in one encrypted data package. This also means you can have a login for the same website many times.
- General fixes and function updates.
- "domains()" function is now "fetch_logins()".
- How data is stored and read is now changed.
- Removed "secrets" library for the use of pycryptodom's Crypto.Random().
- Added itertools for turning the .fetchall() for sqlite3 output into useable lists.


<br />

If you come across ANY issues or bugs, please report it by making an [issue](https://github.com/therealOri/Genter/issues). It helps out a lot!
> This is my first time making and managing an .exe file so I would love any feedback on what could be done better or changed. <3
__ __

<br />
<br />

# ToDo
- [] Change how the databse is locked and unlocked. Maybe using gpg/pgp. (RSA encryption)? idk yet.
- [] Add a new table in the database and new feature for just normal/unrelated notes that you'd write down on a notepad.
__ __

<br />
<br />

# Screenshots
![main_menu](https://user-images.githubusercontent.com/45724082/206585491-c3174aa2-ca54-4f32-adb6-65c23129a6eb.png)

![password_options](https://user-images.githubusercontent.com/45724082/198920472-73b5f648-1584-4df0-b05c-4210c45b7115.png)

![sub_menu](https://user-images.githubusercontent.com/45724082/206585506-e2d14dab-28a2-45ac-a0af-fc6e634ff11b.png)

__ __




<br />
<br />

# Installation/Links

> If you do not have "virtualenv", you can install it via pip.
```mkd
pip install virtualenv
```

```zsh
git clone https://github.com/therealOri/PassGen.git
cd Genter
virtualenv gterENV
source gterENV/bin/activate
pip install -r requirements.txt
python3 genter.py
```
> The first thing you should do is make a 100+ character password, generate a key, and then keep it safe for when you want to use the password manager.

<br />
<br />

- [Git Download](https://git-scm.com/downloads)
- [Database Browser for pwords.pgen](https://sqlitebrowser.org/dl/)
- [Blake2 Documentation](https://www.blake2.net)
- [Hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
__ __

<br />
<br />

# Notice! 💢
- It is very important to keep backups of your keys and data as without it you CAN NOT decrypt your passwords or recover anything. It is advised that you keep a backup of your master key and password database file as well on a USB or external SSD. If in the event of anything getting compromized and you need to change your key and encrypted data/your passwords that used your key, you can change your key and encryption automatically using genter.

> By using Genter you understand the risk of data encryption and the always possible risk of losing data. I am hereby not liable or responisble for any loss of data and or if you lose your key and are unable to decrypt your passwords/data. Everything lies in your hands in terms of how well you keep your master key safe and your data backed up. (It is reccomended that you make keys using genter).

- Because Genter is only being worked on by me currently, security may not be the best it could be and I may not be aware of better methods. I am still learning more everyday. If you know of better methods of password encryption or of better ways of doing anything, PLEASE!! bring it to my attention and or make a pull request and fix the issue! Don't be like the people on r/Python and just tell me there's an issue and not provide any ways of fixing the problem or providing no resources to look into to help make genter better and or fix the issue. Help out if you find any issues, I will always be very appreciative of any help! <3

> By using the genter password manager feature, you ackowledge that you are aware of the above information and accpet what has been said and are using it at your own risk.
__ __

<br />
<br />


# Extra/Notes
> - If you don't have python3, then you can find, download, and install it from [here](https://www.python.org/downloads/). (Or from your package manager of choice).
> - If you are on windows 10 use this: [download](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe). (Pip3 comes with it)
> - The hashing feature of this script can be completly ignorred if you are just making passwords. Hashing is for if you want to store them in a server somewhere, so they aren't just sat around as plaintext.
> - If the "options_flag" in the config file is set to "true", PassGen will ask you what you want to use in your password. If set to "False", PassGen will use the already defined list of options that are all "True" by default found in the code. (Basically will use everything).
> - If the "secure_prompts" option in the config file is "true", it will hide what you type whenever you are asked to provide keys, salts, passwords, etc. If it is set to "false" it will not hide what you type.
__ __


<br />
<br />
<br />

# Support  |  Buy me a coffee <3
(God knows I need one xD)

Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)
