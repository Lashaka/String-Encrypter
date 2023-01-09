import base64
import random

#Encodes a string to base64


def EnCodeBase64(string):
  sample_string_bytes = string.encode("ascii")
  base64_bytes = base64.b64encode(sample_string_bytes)
  return base64_bytes.decode("ascii")


#Decodes a string from base64
def DeCodeBase64(string):
  base64_bytes = string.encode("ascii")
  sample_string_bytes = base64.b64decode(base64_bytes)
  return sample_string_bytes.decode("ascii")

#Decrypt a string using a key 
def decrypt(string, key):
  try:
    decrypted_string = ""
    key = DeCodeBase64(key)
    string =DeCodeBase64(string)
    for i, char in enumerate(string):
      decrypted_char = chr(ord(char) - int(key[i]))
      decrypted_string += decrypted_char
    return decrypted_string

#if cannot decrypt with given key return given string.
  except: 
    return string

#Encrypt a string in a specific method and give a decryption key
def encrypt(string):
  encrypted_string =""
  key=[]
  for char in string:
    randnum=random.randint(0, 9)
    encrypted_char = chr(ord(char) + randnum)
    key.append(randnum)
    encrypted_string += encrypted_char

  key =''.join(map(str,key))
  return EnCodeBase64(encrypted_string), EnCodeBase64(key)
