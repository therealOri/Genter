# PassGen
PassGen will allow you to create a very crazy & strong randomized password.
You can manually pick and choose what languages and symbols are used. You can also change the length of the password and how many you want to generate. Also, In addition to the password generator, PassGen has a built in password manager that you can use! Passwords are encrypted using AES and a "Password Based Key Derivation" master Key.
__ __

<br />

Update | 10/18/2022:
# New Features.
If you have an older version of this project, You should update to the current version now!.

Added:
> - New Passphrase generation feature! Allows you to generate passphrases like Bitwarden! (using the lovely [beaupy](https://github.com/petereon/beaupy) package! <3)
> - Added new languages! Sri Lankin, and Egyptian Hieroglyphs! (Giving us a total of 20! different languages to make passwords from!)
> - Added a new config option. "wordlst_update". This flag (set to false by default) will allow you to always be up to date with the wordlist found here in the repository. You can help contibute valid english (for now) words to the list.
__ __

<br />

# Screenshots

![main_menu](https://user-images.githubusercontent.com/45724082/196574471-e9d58692-087e-4ddc-a45b-1a4d66f5f36e.png)

![password_gen_menu](https://user-images.githubusercontent.com/45724082/196574611-900f8aea-fcf3-4055-bb78-253538855377.png)

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

# Extra/Notes
> - If you don't have python3, then you can find, download, and install it from [here](https://www.python.org/downloads/). (Or from your package manager of choice).
> - If you are on windows 10 use this: [download](https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe). (Pip3 comes with it)
> - The hashing feature of this script can be completly ignorred if you are just making passwords. Hashing is for if you want to store them in a server somewhere, so they aren't just sat around as plaintext.
> - If the "options_flag" in the config file is set to "true", PassGen will ask you what you want to use in your password. If set to "False", PassGen will use the already defined list of options that are all "True" by default found in the code. (Basically will use everything).
> - If the "secure_prompts" option in the config file is "true", it will hide what you type whenever you are asked to provide keys, salts, passwords, etc. If it is set to "false" it will not hide what you type.
__ __

<br />
<br />

# Notice! 💢
It is very important to keep backups of your keys and data as without it you CAN NOT decrypt your passwords or recover anything. It is advised that you keep a backup of your master key and password database file as well on a USB or external SSD. If in the event of anything getting compromized and you need to change your key and encrypted data/your passwords that used your key, you can change your key and encryption automatically using passgen.

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
