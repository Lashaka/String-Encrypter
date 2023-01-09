import random

def Add_Trash(string):
  result = ''

  # Iterate through each character in the string
  for char in string:
      # Add the character and 2 random characters to the result string
      result += char + chr(random.randint(65, 122)) + chr(random.randint(65, 122))

  # Return the modified string
  return result

def Remove_Trash(string):
    result = ''

    # Iterate through every third character in the string (skip the added characters)
    for i in range(0, len(string), 3):
        # Add the character to the result string
        result += string[i]

    # Return the modified string
    return result