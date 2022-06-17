#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []
keysf = "keys.key"

# Collecting the files in the current directory
if os.path.exists(keysf):
    print("Files are already encrypted!")

else:
    open(keysf, "w").close

    for file in os.listdir():
        if file == "encryptor.py" or file == "decryptor.py" or file == "keys.key" or file == "LICENSE" or file == "README.md":
            continue
        if os.path.isfile(file):
            files.append(file)

    pwd = input("Enter a password: ")

    # Generating Password Encryption Key
    pKey = Fernet.generate_key()

    with open(keysf, "wb") as keys:
        keys.write(pKey)

    with open(keysf, "a") as keys:
        keys.write("\n")

    # Encrypting the Password
    pwd = Fernet(pKey).encrypt(pwd.encode())

    with open(keysf, "ab") as keys:
        keys.write(pwd)

    with open(keysf, "a") as keys:
        keys.write("\n")

    # Generating File Encryption Key
    key = Fernet.generate_key()

    with open(keysf, "ab") as keys:
        keys.write(key)

    with open(keysf, "a") as keys:
        keys.write("\n")

    # Encrypting the files
    for file in files:
        with open(file, "rb") as f:
            contents = f.read()
        encrypted_contents = Fernet(key).encrypt(contents)
        with open(file, "wb") as f:
            f.write(encrypted_contents)
        with open(file, "a") as f:
            f.write("\n")

    print("The following files have been encrypted: ")

    for file in files:
        print(f"\t-{file}")

    while(True):
        sf = input("Self-destruct? (y/n) ")
        if sf == 'y':
            os.remove("encryptor.py")
            os.remove("decryptor.py")
            os.remove("keys.key")
            exit()
        elif sf == 'n':
            exit()
        else:
            print("Incorrect input. Try again.\n")
            continue   
