
import PySimpleGUI as SG
import pyperclip
import constants
import threading
from encrypt import Encrypt
from decrypt import Decrypt
class Gui:
    def __init__(self) -> None:
        self.window = self.create_window()
    

    def create_window(self) -> SG.Window:
        SG.theme("DarkBlue")
        layout = [
    [
        SG.Text(constants.SET_DEF_TEXT[0],
      font=(
        "Helvetica",
      10
        )
      )],
    [
        SG.Text
        (constants.SET_DEF_TEXT[1],
          font=(
            "Helvetica", 14
            )
          )],
    [
        SG.Input(
        key="string_input",
        font=(
        "Helvetica",
        14
            )
        )],
    [
        SG.Text(constants.SET_DEF_TEXT[2],
            font=(
            "Helvetica",
            14
                )
            )],
    [
        SG.Input(
            key="key_input",
            font=(
            "Helvetica",
            14
                )
            )],
    [
        SG.Button(constants.SET_DEF_TEXT[3],
            button_color=("mint cream",
            "slate blue"), 
            font=("Helvetica", 14)), 
            SG.Button("Decrypt",button_color=("slate blue", 
            "mint cream"), 
            font=("Helvetica", 
            14
                )
                )],
    [
        SG.Text(constants.SET_DEF_TEXT[4], 
        font=("Helvetica", 
        14
            )
        )],
    [
        SG.Output(
        key="result_output", 
        font=("Helvetica", 
        14),
        size=(100,
        10  )
        )],
    [
        SG.Button(constants.SET_DEF_TEXT[5],
        button_color=("mint cream", 
        "slate blue"), 
        font=("Helvetica", 
        14  )
        ), 
        SG.Button(
        "Copy Key",
        button_color=(
        "slate blue", 
        "mint cream"), 
        font=(
        "Helvetica", 
        14
            )
        )]
        ]
        window = SG.Window(
            constants.WINDOW_TEXT, 
            layout, 
            size=(
            800,
            600
            )
            )
        return window

    def copy_string(self) -> None:
        if self.Copy_String =="":
            SG.popup_ok(constants.NO_COPY_TEXT)
        else:    
            pyperclip.copy(self.Copy_String)
            SG.popup_ok(constants.COPY_TEXT)
    

    def copy_key(self) -> None:
        if self.Copy_Key =="":
            SG.popup_ok(constants.NO_KEY_COPY_TEXT)
        else:    
            pyperclip.copy(self.Copy_Key)
            SG.popup_ok(constants.KEY_COPY_TEXT)

    def get_events(self) -> None:
            match self.event:
                    case "Encrypt":
                        self.result = Encrypt(
                                value=self.string_input
                                ).encrypt()
                        self.Copy_String = self.result
                        self.Copy_Key = self.result
                        self.window["result_output"].update(f"Encrypted string:{self.result}")
                    case "Decrypt":
                        self.result = Decrypt(
                            value=self.key_input
                           ).decrypt()
                        self.Copy_String=self.result
                        self.Copy_Key = ""
                        self.window["result_output"].update(f"Decrypted string:{self.result}")
                    case "Copy String":
                        self.copy_string()

                    case "Copy Key":
                        self.copy_key()
                

    def show_window(self) -> None:
        singa = 1
        self.Copy_String =""
        self.Copy_Key =""
        while 1:
            self.event, self.values = self.window.read()
            self.string_input = self.values["string_input"]
            self.key_input = self.values["key_input"]
            if singa == 1:
                threading.Thread(target=self.get_events()).start()





if __name__ == "__main__":
    Gui().show_window()