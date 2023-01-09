import random
import PySimpleGUI as sg
from Scripts.Algorithm_Functions.Base64_Functions import DeCode_Base64,EnCode_Base64
from Scripts.Algorithm_Functions.Trash_Functions import Add_Trash,Remove_Trash


#Decrypt a string using a key 
def decrypt(string, key):
  try:
    key = DeCode_Base64(key)
    string =DeCode_Base64(string)

    string_length=len(string)
    decrypted_string = ""

    counter=0
    for i in range(string_length):
      decrypted_char = chr(ord(string[i]) - int(key[counter]))
      decrypted_string += decrypted_char

      counter=counter+1
      if(counter+1==len(key)):
        counter=0


    decrypted_string = Remove_Trash(decrypted_string)

    return decrypted_string

#if cannot decrypt with given key return given string.
  except:
    sg.popup_ok('Error')

#Encrypt a string in a specific method and give a decryption key
def encrypt(string):
  try:
    string = Add_Trash(string)

    encrypted_string =""
    key=[]
    for char in string:
      randnum=random.randint(0, 9)
      encrypted_char = chr(ord(char) + randnum)
      key.append(randnum)
      encrypted_string += encrypted_char

    key =''.join(map(str,key))
    return EnCode_Base64(encrypted_string), EnCode_Base64(key)
  except:
    sg.popup_ok('Error')

def encrypt_with_key(string,key):
  try:
    string = Add_Trash(string)

    key = DeCode_Base64(key)

    string_length=len(string)

    encrypted_string =""

    counter=0
    for i in range(string_length):
      encrypted_char = chr(ord(string[i]) + int(key[counter]))
      encrypted_string += encrypted_char

      counter=counter+1
      if(counter+1==len(key)):
        counter=0

      

    return EnCode_Base64(encrypted_string), EnCode_Base64(key)
  except:
    sg.popup_ok('Error')

