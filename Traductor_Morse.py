from colorama import Fore

#Se define la función que traduce de texto a morse

def texto_a_morse(msg):
    caracteres_morse = [".- ","-... ","-.-. ","-.. ",". ","..-. ","--. ",
                        ".... ",".. ",".--- ","-.- ",".-.. ","-- ","-. ",
                        "--- ",".--. ","--.- ",".-. ","... ","- ","..- ",
                        "...- ",".-- ","-..- ","-.-- ","--.. ","/ ","..--.. ",  
                        "--...- ","-.-.-- ","--..-- ",".-.-.- ","---... ","-.--. ",
                        "-.--.- ","----- ",".---- ","..--- ","...-- ","....- ","..... ",
                        "-.... ","--... ","---.. ","----. "]
    
    letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
              "S","T","U","V","W","X","Y","Z"," ","?","¡","!",",",".",":","(",")","0",
              "1","2","3","4","5","6","7","8","9"]
    traduccion = ""
    for i in range(len(msg)):
        if(msg[i].upper() in letras):
            w = 0
            while(msg[i].upper() != letras[w]):
                w += 1
            else:
                traduccion += caracteres_morse[w]
        else:
            traduccion = "Lo sentimos no se pudo realizar la traducción :("
            break
    return traduccion

#Se define la función que traduce de morse a texto

def morse_a_texto(msg):
    caracteres_morse = [".- ","-... ","-.-. ","-.. ",". ","..-. ","--. ",
                        ".... ",".. ",".--- ","-.- ",".-.. ","-- ","-. ",
                        "--- ",".--. ","--.- ",".-. ","... ","- ","..- ",
                        "...- ",".-- ","-..- ","-.-- ","--.. ","/ ","..--.. ",
                        "--...- ","-.-.-- ","--..-- ",".-.-.- ","---... ","-.--. ",
                        "-.--.- ","----- ",".---- ","..--- ","...-- ","....- ","..... ",
                        "-.... ","--... ","---.. ","----. "]
    
    letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
              "S","T","U","V","W","X","Y","Z"," ","?","¡","!",",",".",":","(",")","0",
              "1","2","3","4","5","6","7","8","9"]
    traduccion = ""
    morse = []
    temp = ""
    for i in range(len(msg)):
        temp += msg[i]
        if(temp in caracteres_morse):
            morse.append(temp)
            temp = "" 
    for i in range(len(morse)):
        if(morse[i] in caracteres_morse):
            w = 0
            while(morse[i] != caracteres_morse[w]):
                w +=1
            else:
                traduccion += letras[w]
    return traduccion

#Se crea un bucle para que el usuario decida cuando quiere dejar de traducir

repetir = "SI"
while(repetir == "SI"):
    pregunta = input(Fore.GREEN + "Seleccione:\nPara traducir de texto a morse, ingrese 1\nPara traducir de morse a texto, ingrese 2\n")
    if(pregunta == "1"):
        texto = input(Fore.CYAN + "Ingrese el texto que desea traducir a código morse:\n")
        print(texto_a_morse(texto))
    elif(pregunta == "2"):
        texto = input(Fore.CYAN + "Ingrese el código morse que desea traducir a texto:\n")
        print(morse_a_texto(texto))
    repetir = input(Fore.LIGHTYELLOW_EX + "¿Desea volver a traducir? (Responda con si o no)\n").upper()
    if(repetir == "NO"):
        print(Fore.WHITE + "¡Vueva pronto! :)")
        break