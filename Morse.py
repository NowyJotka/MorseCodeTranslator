seleccion = input("""Bienvenido al traductor de morse
      Welcome to the Morse translator
      
      Select '1' to text to morse
      Selecciona '1' para texto a morse
      
      And '2' to morse to text
      Y '2' para morse a texto:
       """)

if seleccion == "1":
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

    traducir = input("""What do you want to translate?: 
Que quieres traducir?""").lower()

    translation = ""
    for char in traducir:
        if char == " ":
            translation += "/"  
        elif char in morse_code:
            translation += morse_code[char] + " "  

    print(translation.strip())
    print(input("""Press enter to escape the terminal
 Dale a enter para salir de la terminal""")) 

elif seleccion == "2":
    code_morse = {
        '.-': 'a',
        '-...': 'b',
        '-.-.': 'c',
        '-..': 'd',
        '.': 'e',
        '..-.': 'f',
        '--.': 'g',
        '....': 'h',
        '..': 'i',
        '.---': 'j',
        '-.-': 'k',
        '.-..': 'l',
        '--': 'm',
        '-.': 'n',
        '---': 'o',
        '.--.': 'p',
        '--.-': 'q',
        '.-.': 'r',
        '...': 's',
        '-': 't',
        '..-': 'u',
        '...-': 'v',
        '.--': 'w',
        '-..-': 'x',
        '-.--': 'y',
        '--..': 'z'
    }

    revertir = input("""What do you want to convert?
Que quieres convertir?""")
    reverticion = ""
    for char in revertir.split():
        if char == "/":
            reverticion += " "  
        elif char in code_morse:
            reverticion += code_morse[char]  

    print(reverticion.strip())
    print(input("""Press enter to exit
Dale a enter para salir"""))
