import os
import binascii
import argon2
from base64 import b64encode
from Crypto.Protocol.KDF import PBKDF2, scrypt, bcrypt
from Crypto.Hash import SHA512
from alive_progress import alive_bar



def clear():
    os.system("clear||cls")





# Vales of the KDFs can be modified. Just make sure you know what you are doing or can do better than me.
def argon_hash(password: bytes, pass_salt: bytes):
    # derive | DO NOT MESS WITH...unless you know what you are doing and or have more than 8GB of ram to spare and a really good CPU.
    print("Generating key...")
    with alive_bar(0) as bar:
        key = argon2.hash_password_raw(
            time_cost=16,
            memory_cost=2**20,
            parallelism=4,
            hash_len=32,
            password=password,
            salt=pass_salt,
            type=argon2.Type.ID
        )
        bar()
    clear()
    hex_string = binascii.hexlify(key)
    return hex_string.decode(), pass_salt #returns bytes. You will need to base64 encode them yourself if you want a "shareable key"



def pbkdf2_hash(password: bytes, pass_salt: bytes):
    print("Generating key...")
    with alive_bar(0) as bar:
        key = PBKDF2(password=password,
                    salt=pass_salt,
                    dkLen=32,
                    count=7058576,
                    hmac_hash_module=SHA512
        )
        bar()
    clear()
    hex_string = binascii.hexlify(key)
    return hex_string.decode(), pass_salt




def scrypt_hash(password: bytes, pass_salt: bytes):
    print("Generating key...")
    with alive_bar(0) as bar:
        key = scrypt(password=password,
                     salt=pass_salt, key_len=32, N=2**20, r=8, p=4)
        bar()
    clear()
    hex_string = binascii.hexlify(key)
    return hex_string.decode(), pass_salt




def bcrypt_hash(password: bytes, pass_salt: bytes):
    print("Generating key...")
    b64pwd = b64encode(SHA256.new(password).digest())

    with alive_bar(0) as bar:
        key = bcrypt(password=b64pwd, cost=31, salt=pass_salt)
        bar()
    clear()
    hex_string = binascii.hexlify(key)
    return hex_string.decode(), pass_salt
















if __name__ == '__main__':
    print("UwU")
