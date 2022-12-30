
# def encrypt(string, shift):
#   Encrypted_string = ""
#   for char in string:
#     encrypted_char = chr(ord(char) + shift)
#     Encrypted_string += encrypted_char
#   return Encrypted_string


# Encrypted_string = encrypt("hello", 2)

# print(Encrypted_string)

# Decrypted_string = encrypt(Encrypted_string, -2)
# print(Decrypted_string)

import base64
import random

def subtract_lists(list1, list2):
  return [x - y for x, y in zip(list1, list2)]

def add_lists(list1, list2):
  return [x + y for x, y in zip(list1, list2)]

def encrypt(string):
  # Convert string to keyboard values
  keyboard_values = [ord(c) for c in string]

  # Add a random number between 0 and 100 to each keyboard value
  encrypted_values = [val + random.randint(0, 10) for val in keyboard_values]
  key = subtract_lists(encrypted_values, keyboard_values)

  # Convert encrypted values to base64 encoded string
  encrypted_string = base64.b64encode(bytes(encrypted_values))

  # Return encrypted string and decryption key
  return encrypted_string,key

def decrypt(encrypted_string, key):
  # Decode base64 encoded string to list of encrypted values
  base64_Decrypt = base64.b64decode(bytes(encrypted_string)).decode("utf-8")

  # Subtract the decryption key from each encrypted value
  decrypted_values = add_lists(base64_Decrypt, key)

  # Convert decrypted values to string
  decrypted_string = "".join(chr(val) for val in decrypted_values)
  return decrypted_string


# Encrypt the string "hello"
encrypted_string, key = encrypt("hello")

# Print the encrypted string and decryption key
print(encrypted_string)
print(key)

# Decrypt the encrypted string using the key
decrypted_string = decrypt(encrypted_string, key)

# Print the decrypted string
print(decrypted_string)