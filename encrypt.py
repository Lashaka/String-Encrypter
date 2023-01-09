import constants
import base64
class Encrypt:
    def __init__(
            self,
            value
            ) -> None:
        self.testkey = value
        

    def encrypt(self) -> str:
        self.new_text = ""

        for letter in self.testkey:
            self.new_text += (constants.algorithm[letter.lower()])
        self.new_text = " ".join(format(ord(c), "b") for c in self.new_text)
        self.new_text = base64.standard_b64encode(bytes(self.new_text,"utf-8"))
        return self.new_text
