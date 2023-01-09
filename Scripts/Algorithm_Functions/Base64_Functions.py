import base64

#Encodes a string to base64
def EnCode_Base64(string):
  sample_string_bytes = string.encode("utf-8")
  base64_bytes = base64.b64encode(sample_string_bytes)
  return base64_bytes.decode("utf-8")


#Decodes a string from base64
def DeCode_Base64(string):
  base64_bytes = string.encode("utf-8")
  sample_string_bytes = base64.b64decode(base64_bytes)
  return sample_string_bytes.decode("utf-8")
