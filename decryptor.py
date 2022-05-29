#!/usr/bin/env python3

import os
import shutil
from cryptography.fernet import Fernet

#Collecting the files in the current directory

files = []
save_path = './keys'

if not os.path.isdir(save_path):
    print("Files are not encrypted!")
    
else:
    for file in os.listdir():
        if file == "encryptor.py" or file == "key.key" or file == "decryptor.py" or file == "pkey.key" or file == "password.key":
            continue
        if os.path.isfile(file):
            files.append(file)

    with open (os.path.join(save_path, "key.key"), "rb") as kf:
        key = kf.read()

    with open (os.path.join(save_path, "pkey.key"), "rb") as pkf:
        pKey = pkf.read()

    with open (os.path.join(save_path, "password.key"), "rb") as pf:
        pwd = pf.read()

    pwd = Fernet(pKey).decrypt(pwd).decode()

    pwd2 = input("Enter the password: ")

    #Decrypting the files

    if pwd2 == pwd:
        for file in files:
            with open(file, "rb") as f:
                contents = f.read()
                decrypted_contents = Fernet(key).decrypt(contents)
            with open(file, "wb") as f:
                f.write(decrypted_contents)

        print("The following files have been decrypted: ")
        for file in files:
            print(f"\t-{file}")

        shutil.rmtree(save_path)
    else:
        print("Incorrect password.")
