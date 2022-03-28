# Passgen
Passgen will allow you to create a very/crazy strong password that will also be randomized.
You can change up what is used, add more stuff, or remove some things if you wish. You can also change the length of the password and how many you want to generate too.
__ __

<br />

Update | 3/23/2022:
# Menu Overhaul & More features.
If you have an older version of this project, You should update to the current version now!.

- Added some SUS characters to the unicode list.
- Added emoji list.
- Re did the menus and it now flows and acts like a menu. (Instead of just quitting/stopping the script if something breaks.)
- Removed the "Compare Hashes" function. (I didn't see it needing to be a thing and would be more appropriate for files.)
- Added options to the menus to go back and to quit.
- Added a way for you to view the contents of "pass.txt" without having to close the script.
- Changed the generation of keys for hash values. It will now randomly assign a key and salt each time a hash is made. Instead of you having to "change the default key and salt". (If you want, you can just set the "default_key" and "salt" variables to whatever you want if you do not like how it is being done now.)

__ __

<br />

![image](https://user-images.githubusercontent.com/45724082/160468057-cacc5a76-822a-4e9b-a079-d203375f6b11.png)



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
