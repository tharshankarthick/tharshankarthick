import random
import string

char = list(" " + string.punctuation + string.digits + string.ascii_letters)
key = char.copy()

random.shuffle(key)

plain_text = input("Enter a message to encrypt: ")
encrypt_text = ""

for letter in plain_text:
    index = char.index(letter)
    encrypt_text += key[index]

print(f"original message : {plain_text}")
print(f"encrypted message: {encrypt_text}")

encrypt_text = input("Enter a message to Decrypt: ")
plain_text = ""

for letter in encrypt_text:
    index = key.index(letter)
    plain_text += char[index]

print(f"original message : {encrypt_text}")
print(f"encrypted message: {plain_text}")
