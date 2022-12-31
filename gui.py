import PySimpleGUI as sg
from crypto_functions import encrypt, decrypt


layout = [
    [sg.Text("Enter a string to encrypt or decrypt:", font=("Helvetica", 14))],
    [sg.Input(key="string_input", font=("Helvetica", 14))],
    [sg.Text("Enter a key (leave blank for encryption):", font=("Helvetica", 14))],
    [sg.Input(key="key_input", font=("Helvetica", 14))],
    [sg.Button("Encrypt",button_color=("white", "slate blue"), font=("Helvetica", 14)), sg.Button("Decrypt",button_color=("white", "medium slate blue"), font=("Helvetica", 14))],
    [sg.Text("Result:", font=("Helvetica", 14))],
    [sg.Output(key="result_output", font=("Helvetica", 14),size=(100,10))]
]

sg.theme("DarkBlue")

window = sg.Window("Encrypt/Decrypt", layout, size=(800,600))

while True:
    event, values = window.read()
    
    string_input = values["string_input"]
    key_input = values["key_input"]
    
    if event == "Encrypt":
        result, key = encrypt(string_input)
        window["result_output"].update(f"Encrypted string: {result}\nKey: {key}")
    elif event == "Decrypt":
        result = decrypt(string_input, key_input)
        window["result_output"].update(f"Decrypted string: {result}")

window.close()