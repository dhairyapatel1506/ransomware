#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#Collecting the files in the current directory

files = []
save_path = './keys'

if len(os.listdir(save_path)) != 0:
    print("Files are already encrypted!")

else:
    for file in os.listdir():
        if file == "encryptor.py" or file == "key.key" or file == "decryptor.py" or file == "pkey.key" or file == "password.key":
            continue
        if os.path.isfile(file):
            files.append(file)

    pwd = input("Enter a password: ")

    pKey = Fernet.generate_key()

    with open(os.path.join(save_path, "pkey.key"), "wb") as pkf:
        pkf.write(pKey)

    pwd = Fernet(pKey).encrypt(pwd.encode())

    with open(os.path.join(save_path, "password.key"), "wb") as pf:
        pf.write(pwd)

    #Generating the key

    key = Fernet.generate_key()

    with open(os.path.join(save_path, "key.key"), "wb") as kf:
        kf.write(key)

    #Encrypting the files

    for file in files:
        with open(file, "rb") as f:
            contents = f.read()
        encrypted_contents = Fernet(key).encrypt(contents)
        with open(file, "wb") as f:
            f.write(encrypted_contents)

    print("The following files have been encrypted: ")

    for file in files:
        print(f"\t-{file}")
