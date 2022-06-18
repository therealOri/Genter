# Passgen
Passgen will allow you to create a very/crazy strong password that will also be randomized.
You can change up what is used, add more stuff, or remove some things if you wish. You can also change the length of the password and how many you want to generate too.
__ __

<br />

Update | 6/12/2022:
# New Features.
If you have an older version of this project, You should update to the current version now!.

Added:
> - Amharic (Ethopian) alphabet.

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
__ __

<br />
<br />

- [Git Download](https://git-scm.com/downloads)
- [Database Browser for pwords.pgen](https://sqlitebrowser.org/dl/)
- [Blake2 Documentation](https://www.blake2.net)
- [Hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
__ __

<br />
<br />

# Obfuscation & Cythonize instructions.
!! IMPORTANT !!: 
- Do not change the env.py file contents or name of the file unless you know what you are doing. The passgen.py code/file uses and IMPORTS `env.py` for things and if you change env.py to anything else, you MUST do the same for `import env` and also for wherever `env.py`, `env.FLAG`, & `env.SALT` is/are located at in passgen.py. Or else you'll likely get errors. You'll be better off not changing the name of the `env.py` file is all. You will also need to update the `setup.py` file later on when in the "Cythonize" part of the process to reflect the name change if you change the name of `env.py`.

> We are going to use [oriscate](https://github.com/therealOri/oriscate) for our obfuscation and stuff. This should be done **after** running passgen.py **once** and setting up the env.py file.
```
# Install oriscate
Command: git clone https://github.com/therealOri/oriscate.git
Command: cd oriscate
Command: pip install -r requirements.txt


# Obfuscate code.
# Move the env.py file into the oriscate folder/directory.
Command: python main.py -i env.py -o env.py -s 100 -r


# Cythonize Code
# env.py is what is being used in the setup.py file
# You can remove the "build" folder/directory, the "env.c" file and "env.py" file AFTER running & completing the following command.
Command: python setup.py build_ext --inplace


# Final
Rename the newly made .so/.pyd file to "env.so" OR "env.pyd" and move it back into the same directory as passgen.py. 
That way when we "import env", it'll know what file to use. (that contains your SALT and PASS).
Then change directory back to the PassGen folder/directory, and run passgen.py again.
Command: cd ..
Command: python passgen.py
```
> If you did everything correctly, you should now have an `env.pyd` or `env.so` file in the PassGen folder/directory and when you run `passgen.py`, it should run with no errors.
> If you do Have ANY issues, by all means, make an issue/report about it if you belive it to be a bug, etc. and or get in touch with me over in the [Discussions](https://github.com/therealOri/PassGen/discussions/10) page if you have questions or need help/guidence with troubleshooting stuff! <3
__ __

<br />
<br />

# Extra/Notes
> - If you don't have python3, then you can find, download, and install it from [here](https://www.python.org/downloads/). (Or from your package manager of choice).
> - If you are on windows 10 use this: [download](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe). (Pip3 comes with it)
> - The hashing feature of this script can be completly ignorred if you are just making passwords. Hashing is for if you want to store them in a server somewhere, so they aren't just sat around as plaintext.
__ __

<br />
<br />

# Notice! 💢
It is very important to keep backups of your so/pyd file as without it you CAN NOT decrypt your passwords. It is advised that you keep a backup of your password database and your so/pyd file as well on a USB or external SSD. If in the event of your so/pyd file getting compromized and you need to change it and your passwords that used it. For now you will just have to manually decrypt the passwords using your current so/pyd file, save it with the email associated with it, delete the existing saved password record, then once you have everything decrypted..you can use the new so/pyd file you have made for encryption and start adding the passwords back into the database. At least until I can make a way to do this automatically...
__ __


<br />
<br />
<br />

# Support  |  Buy me a coffee <3
(God knows I need one xD)

Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)
