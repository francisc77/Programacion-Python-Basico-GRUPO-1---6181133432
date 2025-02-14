#Crea una lista llamada numeros que contenga los números del 1 al 10
import numpy as np
#import pandas as pd


ListaDel1Al10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*ListaDel1Al10)

#Código crear un array de ceros de tamaño 5x5
array_ceros = np.zeros((5,5))
print(array_ceros)

#Código crear un array de unos de tamaño 3x3
array_unos = np.ones((5,3))
print(array_unos)

array_numeros = np.array([5,2,4,1,3])
media = np.mean(array_numeros)
print(f'la media aritmetica es {media}')

suma = np.sum(array_numeros)
print(f'la suma de la coleccion es{suma}')

min = np.min(array_numeros)
print(f'el valor minimo es {min}')

maximo = np.max(array_numeros)
print(f'el valor maximo es {maximo}')

#Cambiar la forma de un array "reshape"

array_original = np.array([1, 2, 3, 4, 5, 6])
array_reshapeado = array_original.reshape(3,2)
print(array_reshapeado)


#preferencias peliculas mariana accion comedia drama
mariana =  np.array([7,9,2])

avatar = np.array([10,1,5]) #mas accion y menos comedia
brave_heart = np.array([8,1,7])

#calcular la similitud de cada pelicula con los gustos de mariana

similitud_p1 = np.dot(mariana,avatar)
similitud_p2 = np.dot(mariana,brave_heart)

print(f'similitud de preferencias avatar : {similitud_p1}')
print(f'similitud de preferencias avatar : {similitud_p2}')

if similitud_p1 > similitud_p2:
        print("Recomendamos  avatar")
else:
        print("Recomendamos  brave_heart ")


#***************************
# tipo de cambio de dolar y indice precios al consumidor
tipo_cambio = np.array([506.96,505.00,504.27,505.52,506.23,506.23,506.23,506.58,506.87,507.25])
ipc = np.array([109.46,109.55,109.71,109.57,109.33,108.85,109.36,110.39,110.79,110.79])

#calcular coeficiente de correlación tienen que tener la misma cantidad de elementos
correlacion = np.corrcoef(tipo_cambio,ipc)[0,1] # 0 es q no hay 1 influye un poco 
print(f'Coeficiente de correlacion {correlacion:.2f}') # es de 0.3.2f para poner 2 decimales

# estudio de horas vrs notas
#datos quiero estudiar 2 situaciones las horas de estudio que aplique y las notas que tengo por materia
horas_estudio = np.array([1,2,3,4,5,6,7,8,9,10])
notas = np.array([50,55,60,63,67,72,75,78,81,85])

#calculo del crecimiento del promedio por horas de estudio.
#diferencia entre los puntajes nos va a dar una variacion incremento o decremento

diferencias_Notas = np.diff(notas) # entre la nota mas bajas consecutivas
incremento_notas = np.average(diferencias_Notas) # media ponderada
print(diferencias_Notas)

proyeccion_estudio = 12 
promedio =  np.averange([[(50,75,100)],[4,8,10]])
nota_estimada = (proyeccion_estudio -  max(horas_estudio)) * incremento_notas + max(notas) # este es el incremento que voy a tener en la nota 12 - 10 nota maxima
nota_estimada_Minimo = (min(horas_estudio) - proyeccion_estudio) * incremento_notas + min(notas) # este es el incremento que voy a tener en la nota 12 - 10 nota maxima
print(f'el incremento del promedio por cada hora de estudio es {incremento_notas:.2f}')
print(f'la nota esperada {nota_estimada:.2f}')
print(f'la nota esperada minima es {nota_estimada_Minimo:.2f}')