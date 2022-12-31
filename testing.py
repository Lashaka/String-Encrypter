import random
import base64
import PySimpleGUI as sg

def EnCodeBase64(string):
  sample_string_bytes = string.encode("ascii")
  base64_bytes = base64.b64encode(sample_string_bytes)
  return base64_bytes.decode("ascii")

def DeCodeBase64(string):
  base64_bytes = string.encode("ascii")
  sample_string_bytes = base64.b64decode(base64_bytes)
  return sample_string_bytes.decode("ascii")

def decrypt(string, key):
  decrypted_string = ""
  key = DeCodeBase64(key)
  string =DeCodeBase64(string)
  for i, char in enumerate(string):
    decrypted_char = chr(ord(char) - int(key[i]))
    decrypted_string += decrypted_char

  return decrypted_string

def encrypt(string):
  encrypted_string =""
  key=[]
  for char in string:
    randnum=random.randint(0, 10)
    encrypted_char = chr(ord(char) + randnum)
    key.append(randnum)
    encrypted_string += encrypted_char

  key =''.join(map(str,key))
  return EnCodeBase64(encrypted_string), EnCodeBase64(key)


Encrypted_string,key = encrypt("hello")

print(Encrypted_string)

Decrypted_string = decrypt(Encrypted_string,key)
print(Decrypted_string)

layout = [
    [sg.Text("Enter a string to encrypt or decrypt:")],
    [sg.Input(key="string_input")],
    [sg.Text("Enter a key (leave blank for encryption):")],
    [sg.Input(key="key_input")],
    [sg.Button("Encrypt"), sg.Button("Decrypt")],
    [sg.Text("Result:")],
    [sg.Output(key="result_output")]
]

window = sg.Window("Encrypt/Decrypt", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Encrypt", "Decrypt"):
        break
    
    string_input = values["string_input"]
    key_input = values["key_input"]
    
    if event == "Encrypt":
        result, key = encrypt(string_input)
        window["result_output"].update(f"Encrypted string: {result}\nKey: {key}")
    elif event == "Decrypt":
        result = decrypt(string_input, key_input)
        window["result_output"].update(f"Decrypted string: {result}")

window.close()



