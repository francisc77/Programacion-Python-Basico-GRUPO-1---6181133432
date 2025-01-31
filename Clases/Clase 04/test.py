#Respuesta
# Ejemplo mejorado: Clasificación de calificaciones de un estudiante
while True: 
    try:
    #calificacion = input('Ingrese la calificación del estudiante (0 a 100): ') ERRROR DSE TIPADO
        calificacion = float(input('Ingrese la calificación del estudiante (0 a 100): '))
        if calificacion >= 90:
            print(f"La calificacón : {calificacion} corresponde 'A'.Excelente Trabajo!")
        elif calificacion >= 80:
            print(f"La calificacón : {calificacion} corresponde 'A'. Excelente Trabajo!")
        elif calificacion >= 70:
            print(f"La calificacón : {calificacion} corresponde 'C'. Puedes mejorar!")
    except ValueError:
        print('Error: Por favor ingresa un valor válido para la calificación.')