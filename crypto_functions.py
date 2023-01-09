import base64
import random

#Encodes a string to base64

def Add_Trash(string):
  result = ''

  # Iterate through each character in the string
  for char in string:
      # Add the character and two random characters to the result string
      result += char + chr(random.randint(65, 90)) + chr(random.randint(65, 90)) +chr(random.randint(65, 90))

  # Return the modified string
  return result

def Remove_Trash(string):
    result = ''

    # Iterate through every fourth character in the string (skip the added characters)
    for i in range(0, len(string), 4):
        # Add the character to the result string
        result += string[i]

    # Return the modified string
    return result

def EnCode_Base64(string):
  sample_string_bytes = string.encode("utf-8")
  base64_bytes = base64.b64encode(sample_string_bytes)
  return base64_bytes.decode("utf-8")


#Decodes a string from base64
def DeCode_Base64(string):
  base64_bytes = string.encode("utf-8")
  sample_string_bytes = base64.b64decode(base64_bytes)
  return sample_string_bytes.decode("utf-8")

#Decrypt a string using a key 
def decrypt(string, key):
  try:
    decrypted_string = ""
    key = DeCode_Base64(key)
    string =DeCode_Base64(string)
    for i, char in enumerate(string):
      decrypted_char = chr(ord(char) - int(key[i]))
      decrypted_string += decrypted_char

    Remove_Trash(decrypted_string)

    return decrypted_string

#if cannot decrypt with given key return given string.
  except:
    return "Error"

#Encrypt a string in a specific method and give a decryption key
def encrypt(string):
  Add_Trash(string)

  encrypted_string =""
  key=[]
  for char in string:
    randnum=random.randint(0, 9)
    encrypted_char = chr(ord(char) + randnum)
    key.append(randnum)
    encrypted_string += encrypted_char

  key =''.join(map(str,key))
  return EnCode_Base64(encrypted_string), EnCode_Base64(key)
