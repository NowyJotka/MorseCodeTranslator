# Define the Morse code dictionary
morse_code = {
    'a': ".-", 
    'b': "-...", 
    'c': "-.-.", 
    'd': "-..", 
    'e': ".", 
    'f': "..-.", 
    'g': "--.", 
    'h': "....", 
    'i': "..", 
    'j': ".---", 
    'k': "-.-", 
    'l': ".-..", 
    'm': "--", 
    'n': "-.", 
    'o': "---", 
    'p': ".--.", 
    'q': "--.-", 
    'r': ".-.", 
    's': "...", 
    't': "-", 
    'u': "..-", 
    'v': "...-", 
    'w': ".--", 
    'x': "-..-", 
    'y': "-.--", 
    'z': "--.."
}

traducir = input("What do you want to translate?: ").lower()

translation = ""
for char in traducir:
    if char == " ":
        translation += "/"  
    elif char in morse_code:
        translation += morse_code[char] + " "  

print(translation.strip())
print(input("Press enter to escape the terminal"))