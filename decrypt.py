#Code for decrypting the data

import os

from cryptography.fernet import Fernet

files = []

path = "pathname" #Enter the path of the directory or file which was encrypted

for file in os.listdir(path):
	if file == 'voldemort.py' or file == "decrypt.py" or file == 'thekey.key':
		continue
	if os.path.isfile(file):
		files.append(file)

with open("thekey.key", "rb") as thekey:
	super_key = thekey.read()  #The key to decrypt the data

phrase = "Football"   #Keeping a secret phase for fun
userInput = input("Enter the secret phrase: ")

if userInput == phrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()

		contents_decrypted =  Fernet(super_key).decrypt(contents)
		with open(file,'wb') as thefile:
			thefile.write(contents_decrypted)
	print("Your files have been decrypted!!")
else:
	print("Wrongg!!!")
