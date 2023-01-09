import constants
import base64
class Decrypt:
    def __init__(
            self,
            value
            ) -> None:
        self.regular_text = bytes(value,"utf-8")
        
    def decrypt(self) -> str:
        self.text = ""
        self.regular_text = base64.standard_b64decode(self.regular_text)
        self.regular_text =  "".join(chr(int(c,2)) for c in self.regular_text.decode().split(" "))
        self.regular_text = self.regular_text.split(",")[1:]
        result = ["," + direction for direction in self.regular_text]
        for num in result:
            self.text += constants.amgorith[num]
        return self.text

