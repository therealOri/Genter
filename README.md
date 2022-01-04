# Passgen
A strong password generator made with python3!


This will create a very strong password that is pretty long and randomized.
You can change up what is used, add more stuff, or remove some things if you wish. You can also change the length of the password and how many you want to generate too.
__ __

<br />

Update | 1/3/2022:
> - Added salting for hashes! Makin them even more secure!
> - Updated the way in which passwords and info gets printed to pass,txt.
> 
> Note: Hashing library being used is blake2b instead of sha256. I'd use blake3 but hashlib only has blake2 right now..

- [blake2 documentation](https://www.blake2.net)
- [hashlib documentation](https://docs.python.org/3/library/hashlib.html)
__ __

<br />

![passterminal](https://user-images.githubusercontent.com/45724082/147999295-ea668365-dc40-4c16-8df3-442148c898a9.png)

<br />
<br />

# Installation

```bash
git clone https://github.com/therealOri/PassGen.git
cd PassGen
python3 passgen.py
```

You may need to type `pip3 install secrets` if it gives you a module not found error.
__ __

<br />
<br />

# Extra/Notes
> - If you don't have python3, then you can find, download, and install it from [here](https://www.python.org/downloads/). (Or from your package manager of choice).
> - If you are on windows 10 use this: [download](https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe). (Pip3 comes with it)
> - The hashing feature of this script can be completly ignorred if you are just making passwords. Hashing is for if you want to store them in a server somewhere, so they aren't just sat around as plaintext.
