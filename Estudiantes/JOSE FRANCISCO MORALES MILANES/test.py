import re
# para depurar se marca con el punto rojo en alguna linea luego le da terminal depuracion y se va viendo las variables
# # vamos avanzando con F11 PARA Ir paso a paso por el codigo excelente.

#Crear Función Para validar Correo
def validar_correo(correo):
    #patron para validar el email
    #patron = r'[a-zA-Z0-9._%+-]+[._]?[a-zA-Z0-9]+[@]\w+\.\[a-zA-Z0-9]{2,3}$'
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$'
    if re.match(patron,correo):
        return True
    else:
        return False
    
nombre = input("Por favor, ingresa tu nombre: ")
correo = input("Por favor, ingresa tu correo electrónico: ")

if validar_correo(correo):
    print("Hola {}, tu correo electrónico {} es válido.".format(nombre, correo))
else:
    print("Lo siento {}, el correo electrónico {} no es válido.".format(nombre, correo))