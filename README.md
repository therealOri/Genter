# Passgen
Passgen will allow you to create a very/crazy strong password that will also be randomized.
You can change up what is used, add more stuff, or remove some things if you wish. You can also change the length of the password and how many you want to generate too.
__ __

<br />

Update | 2/18/2022:
# Auto .env setup update
If you have an older version of this project, You should update to the current version now!.

> - On passgen.py's first time being ran, it'll check the .env file for "FLAG=#src". If it is found, it'll automatically set up the file for you with a SALT and PASS credentials. (removing the FLAG variable as well). And On passgen.py's 2nd run and any after, it'll check the .env file and find that "FLAG=#src" isn't there and skip to the normal functions and code like usual.

In the very odd chance that you would like new .env credentials, all you will need to do is add FLAG=#src back to the .env file and then run passgen.py again.

__ __

<br />

![passterminal](https://user-images.githubusercontent.com/45724082/148269910-184c510b-18c8-4832-b951-0296f4c11840.png)


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
> - If you are on windows 10 use this: [download](https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe). (Pip3 comes with it)
> - The hashing feature of this script can be completly ignorred if you are just making passwords. Hashing is for if you want to store them in a server somewhere, so they aren't just sat around as plaintext.
