# PassGen
PassGen will allow you to create a very crazy & strong randomized password.
You can manually pick and choose what languages and symbols are used. You can also change the length of the password and how many you want to generate. Also, In addition to the password generator, PassGen has a built in password manager that you can use! Passwords are encrypted using AES and a "Password Based Key Derivation" master Key.
__ __

<br />

Update | 9/9/2022:
# New Features.
If you have an older version of this project, You should update to the current version now!.

Added:
> - Overhauled how you will encrypt your passwords. It now uses "Password Based Key Derivation" to make a key. That key will allow you to encrypt and decrypt your passwords. (Don't lose the key and store it somewhere safe). You can use keys generated to encrypt whatever..like Locking the database for example.
> - Removed the need for the env.py file.
> - Updated the password gen option names to refect what languages you are using. (More understandable now)
__ __

<br />

# Screenshots
![2022-09-09_11-34](https://user-images.githubusercontent.com/45724082/189410810-976e6db6-3a96-4946-bff9-5316f738aaec.png)

![2022-09-09_11-36](https://user-images.githubusercontent.com/45724082/189411174-b514b651-122c-4ae6-8fa9-ac9cbf2c578b.png)

![2022-09-09_11-38](https://user-images.githubusercontent.com/45724082/189411567-48bda427-b0f7-4935-948f-5a72c19f8f95.png)
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
cd PassGen
virtualenv pgenENV
source pgenENV/bin/activate
pip install -r requirements.txt
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
> - If you are on windows 10 use this: [download](https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe). (Pip3 comes with it)
> - The hashing feature of this script can be completly ignorred if you are just making passwords. Hashing is for if you want to store them in a server somewhere, so they aren't just sat around as plaintext.
> - If the "options_flag" in the config file is set to "true", PassGen will ask you what you want to use in your password. If set to "False", PassGen will use the already defined list of options that are all "True" found in the code. (Basically will use everything).
__ __

<br />
<br />

# Notice! 💢
It is very important to keep backups of your keys and data as without it you CAN NOT decrypt your passwords or recover anything. It is advised that you keep a backup of your master key and password database file as well on a USB or external SSD. If in the event of anythong getting compromized and you need to change your key and encrypted data/your passwords that used your key, you can change your key and encryption automatically using passgen.

By using PassGen you understand the risk of data encryption and the always possible risk of losing data. I am hereby not liable or responisble for any loss of data and or if you lose your key and are unable to decrypt your passwords/data. Everything lies in your hands in terms of how well you keep your master key safe and your data backed up.
__ __


<br />
<br />
<br />

# Support  |  Buy me a coffee <3
(God knows I need one xD)

Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)
