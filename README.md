# Passgen
Passgen will allow you to create a very/crazy strong password that will also be randomized.
You can change up what is used, add more stuff, or remove some things if you wish. You can also change the length of the password and how many you want to generate too.
__ __

<br />

Update | 4/6/2022:
# New Features.
If you have an older version of this project, You should update to the current version now!.

Added:
> - Functions to lock and unlock the database file and added a way to do that in the menu.
> - New way to encrypt the passwords. No longer needs an IV. (Also means less being stored in the database)
> - New way to show saved domains in the database.

Changed:
> - The names a of a few functions. cipherE >to> stringE and read_data() >to> stringD()

__ __

<br />

![image](https://user-images.githubusercontent.com/45724082/162041412-537d797a-0fa4-4d9e-8e9f-f3635b19e160.png)





<br />
<br />

# Installation/Links

```zsh
pip3 install virtualenv
git clone https://github.com/therealOri/PassGen.git
cd PassGen
virtualenv pgenENV
source pgenENV/bin/activate
pip3 install -r requirements.txt
python3 passgen.py
```

<br />
<br />

- [Git Download](https://git-scm.com/downloads)
- [Database Browser for pwords.pgen](https://sqlitebrowser.org/dl/)
- [Blake2 Documentation](https://www.blake2.net)
- [Hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
__ __

<br />
<br />

# Extra/Notes
> - If you don't have python3, then you can find, download, and install it from [here](https://www.python.org/downloads/). (Or from your package manager of choice).
> - If you are on windows 10 use this: [download](https://www.python.org/ftp/python/3.10.3/python-3.10.3-amd64.exe). (Pip3 comes with it)
> - The hashing feature of this script can be completly ignorred if you are just making passwords. Hashing is for if you want to store them in a server somewhere, so they aren't just sat around as plaintext.

<br />
<br />
<br />

# Support  |  Buy me a coffee <3
Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)
