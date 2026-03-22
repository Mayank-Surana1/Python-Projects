#This code is regarding the Message Encryption and Decryption
#Firstly Enter the the text to be Encrypted \
#Then Copy the Encrypted message and paste to Decrypt it!

import random
import string

chars = string.ascii_letters + string.punctuation + string.digits + " " 
chars= list(chars)
# print(chars)
# print()
keys = chars.copy()
random.shuffle(keys)
# print(keys)
def encrption(plain_text):
    cipher_text = ""
    for letters in plain_text:
        index = chars.index(letters)
        cipher_text += keys[index]
    return cipher_text

def decryption(cipher_text):
    plain_text = ""
    for letters in cipher_text:
        index = keys.index(letters)
        plain_text += chars[index]
    return plain_text

#MESSAGE ENCRYPTION
plain_text = input("Enter the message to encrypt: ")
cipher_text = encrption(plain_text)
print("Encrypted message: ", cipher_text)

#MESSAGE DECRYPTION

cipher_text = input("Enter the message to be Decrypted: ")
plain_text = decryption(cipher_text)
print("Decrypted message: ", plain_text)
