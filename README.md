# Passgen
Passgen will allow you to create a very/crazy strong password that will also be randomized.
You can change up what is used, add more stuff, or remove some things if you wish. You can also change the length of the password and how many you want to generate too.
__ __

<br />

Update | 1/5/2022:
> - Added a password manager for your passwords! (All stored locally).
> - AES salted encryption is what is being used to store the passwords.
> - The AES encryption is also being encoded before storrage.
> - Storing certain variables in a .env file for you to make things more secure. (Both salt and password need to be changed)
> 

__ __

<br />

![passterminal](https://user-images.githubusercontent.com/45724082/148269910-184c510b-18c8-4832-b951-0296f4c11840.png)


<br />
<br />

# Installation/Links

```bash
git clone https://github.com/therealOri/PassGen.git
cd PassGen
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
