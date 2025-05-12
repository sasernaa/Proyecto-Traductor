"""
Esta es la primera versión del programa traductor de texto a morse:

    En esta versión se pueden traducir caracteres desde la A hasta la Z, 
    no permite dejar espacio entre las letras y en caso de que el usuario
    desee traducir un caracter que no se encuentra en la lista de letras,
    el programa no le permitirá continuar con la traducción del texto.
"""

#Se le pregunta al usuario que texto desea traducir:

texto = input("Ingrese el texto que desea traducir a código morse:\n")

#Las siguientes dos listas permiten conocer la respectiva traducción a morse de cada letra:

caracteres_morse = [".- .-.-./ ","-... .-.-./ ","-.-. .-.-./ ","-.. .-.-./ ",". .-.-./ ","..-. .-.-./ ","--. .-.-./ ",
                        ".... .-.-./ ",".. .-.-./ ",".--- .-.-./ ","-.- .-.-./ ",".-.. .-.-./ ","-- .-.-./ ","-. .-.-./ ",
                        "--- .-.-./ ",".--. .-.-./ ","--.- .-.-./ ",".-. .-.-./ ","... .-.-./ ","- .-.-./ ","..- .-.-./ ",
                        "...- .-.-./ ",".-- .-.-./ ","-..- .-.-./ ","-.-- .-.-./ ","--.. .-.-./ "]
letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#La variable traduccion almacena la traducción del texto

traduccion = ""

"""El búcle for realiza una búsqueda dentro de la lista letras,
comparando cada caracter dentro del texto del usuario con los caracteres de la lista letras,
almacenando su respectiva traducción en caracteres_morse dentro de traduccion"""

for i in range(len(texto)):
    if(texto[i].upper() in letras):
        w = 0
        while(texto[i].upper() != letras[w]):
            w += 1
        else:
            traduccion += caracteres_morse[w]
    else:
        traduccion = "Lo sentimos realizar la traducción :("

#Se imprime el resultado final de la traducción del texto ingresado por el usuario

print(traduccion)