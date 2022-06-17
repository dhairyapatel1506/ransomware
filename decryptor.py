#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []
keysf = 'keys.key'

# Collecting the files in the current directory
if not os.path.exists(keysf):
    print("Files are not encrypted!")
    
else:
    for file in os.listdir():
        if file == "encryptor.py" or file == "keys.key" or file == "decryptor.py" or file == "LICENSE" or file == "README.md":
            continue
        if os.path.isfile(file):
            files.append(file)

    with open(keysf, "rb") as keys:
        pKey, pwd, key = keys.readlines()

    # Decrypting the Password
    pwd = Fernet(pKey).decrypt(pwd).decode()

    pwd2 = input("Enter the password: ")

    # Decrypting the files
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

        os.remove(keysf)
    else:
        print("Incorrect password.")
