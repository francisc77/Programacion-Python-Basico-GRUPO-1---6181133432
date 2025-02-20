import json
#puedes acceder a sus elementos usando índices y claves, dependiendo de la estructura del JSON.
#clinica.json

with open('clinica_intermedio.json', encoding='utf-8') as archivo:
    datos_pacientes = json.load(archivo)
    #json.load(archivo)
    print(datos_pacientes) # Muestra el contenido completo
    
# Lista para almacenar las enfermedades y sus cantidades
#["123", 89076541, "Heredia", "Barva", "gripe", "acetaminofen"]

lista_enfermedades = []
lista_cantidades = []
def Enfermedades(Datos):
    lista_enfermedades = []
    for paciente in Datos:    
        #lista_enfermedades.append.paciente[4]
        lista_enfermedades.append(paciente[4])
        #print(f"Enfermedad: {paciente[4]}")
        #print(lista_enfermedades)
        #print(lista_enfermedades)
    return lista_enfermedades
#print(Enfermedades(datos_pacientes))
lista_enfermedades = Enfermedades(datos_pacientes)
print(" La lista de enfermedades son ", lista_enfermedades)

def contarEnfermedad(listaDatos):
    lista_enfermedades = listaDatos
    lista_cantidades = []
    Enfermedad = ""
    conjunto = set(lista_enfermedades) # solo da el conjunto sin repetidos 
    #print(conjunto)
    Contar = 0
    
    for Enfermedad in conjunto:
        Contar = 0   
        if Enfermedad in lista_cantidades:
                pase = 0
        else:
            Contar = lista_enfermedades.count(Enfermedad)
            #print(f'{Enfermedad} si se encuentra en Lista de enfermedades son {Contar}')        
            lista_cantidades.append([Enfermedad , Contar])
    return lista_cantidades
lista_cantidades = contarEnfermedad(lista_enfermedades)        
#listaNueva = contarEnfermedad(lista)
print("La cantidad de enfermedades son ",lista_cantidades)

# Extraemos la enfermedad del paciente
#Puedes imprimir el for para ver los datos que se procesan
#["123", 89076541, "Heredia", "Barva", "gripe", "acetaminofen"],
enfermedad = []
for paciente in datos_pacientes:    
    #lista_enfermedades.append.paciente[4]
    enfermedad.append(paciente[4])
    #print(f"Enfermedad: {paciente[4]}")
    #print(lista_enfermedades)
print(enfermedad)

def VerificarEnfermedadListada(DatosEnfermedades, EnfermedadAverificar):
    lista_enfermedades = DatosEnfermedades
    try:     
        
        if EnfermedadAverificar in lista_enfermedades:            
            return True
        else:
            return False            
    except:
        pass

#print(f' VerificarEnfermedadListada() dicha enfermedad no se encuentra en la lista')    
# Pista: Usa `in` para verificar si la enfermedad ya está en lista_enfermedades.

# Pista: Si la enfermedad no está, agrégala a lista_enfermedades y empieza el conteo en lista_cantidades.
def agregarEnfermedad(DatosEnfermedades,ValorAagregar):
    lista_enfermedades = DatosEnfermedades
    if VerificarEnfermedadListada(lista_enfermedades,ValorAagregar) == False:
        lista_enfermedades.extend(ValorAagregar)
    return lista_enfermedades

print("Digite la enfermedad a buscar")
DigiteEnfermedad = input('Digite enfermedad a buscar')   
ExisteEnfermedad = VerificarEnfermedadListada(lista_enfermedades,DigiteEnfermedad)
print(f'La enfermedad nombrada {DigiteEnfermedad} ¿Se encuentra en Lista de enfermedades? ', ExisteEnfermedad)
if ExisteEnfermedad == False:
    print('Desea agregar enfermedad al listado de enfermedades')
    DeseaAgregar = input("Si desea agregar enfermedad digite 'SI' o 'NO' para no agregarla")
    if DeseaAgregar == "SI":       
        lista_enfermedades.append(DigiteEnfermedad)
else: 
     # si ya esta entonces usa index para encontrar posicion
    posicion = lista_enfermedades.index(DigiteEnfermedad)   
    print(f"La posicion de la enfermedad {DigiteEnfermedad} dentro de la lista es ", posicion)
    lista_enfermedades.append(DigiteEnfermedad)
    

lista_cantidades = contarEnfermedad(lista_enfermedades)


print("La cantidad de enfermedades son ",lista_cantidades)
#print(lista_enfermedades)

print("Reporte de enfermedades tratadas:")
#print(datos_pacientes)
conjunto = set(lista_enfermedades)
#print(conjunto)
contar = 0
for enfermedad in conjunto:
    #print(enfermedad)
    contar = 0
    for pacienteEnfermedad in datos_pacientes:
        
        if enfermedad in pacienteEnfermedad:
            contar += 1
    print(f'Los pacientes tratados para la {enfermedad} son : {contar}')

# Listas para almacenar los medicamentos y sus frecuencias
#[
#["123", 89076541, "Heredia", "Barva", "gripe", "acetaminofen"],
medicamentos = []
frecuencias = []
def MedicamentosCargar(Datos):
    medicamentos = []
    for medicamento in Datos:    
        medicamentos.append(medicamento[5])
    return medicamentos

def MedicamentosContar(MedicamentosLista):
    Medicamentos_lista = MedicamentosLista
    lista_cantidades = []
    Enfermedad = ""
    conjunto = set(Medicamentos_lista) # solo da el conjunto sin repetidos 
    #print(conjunto)
    Contar = 0
    
    for Medicina in conjunto:
        Contar = 0   
        if Medicina in lista_cantidades:
                pase = 0
        else:
            Contar = Medicamentos_lista.count(Medicina)
            #print(f'{Enfermedad} si se encuentra en Lista de enfermedades son {Contar}')        
            lista_cantidades.append([Medicina , Contar])
    return lista_cantidades

def ImprimirFrecuencias(frecuencias):
    print(" La lista de medicamentos son ", medicamentos)
    frecuencias = MedicamentosContar(medicamentos)        

    print("Reporte de medicamentos recetados:")
    for linea in frecuencias:    
        print(f'{linea[0]} : {linea[1]} pacientes')     

def MedicamentoMasrecetados(FrecuentadosLista):    
    Medicamentos = FrecuentadosLista
    ListaMaximo = []
    maximo= 0
    medicina = ""
    #print(Medicamentos)
    for medicamento in Medicamentos:
        #print(medicamento[0],medicamento[1])
        contar = int(medicamento[1])
        if contar > maximo:
            medicina = medicamento[0]
            maximo = contar    
            ListaMaximo = [medicina,maximo]
    print(f'El medicamento mas recetado es : {ListaMaximo}')

medicamentos = MedicamentosCargar(datos_pacientes)
frecuencias = MedicamentosContar(medicamentos)#ImprimirFrecuencias(medicamentos)
ImprimirFrecuencias(frecuencias)
MedicamentoMasrecetados(frecuencias)

# Pedimos las identificaciones de los dos pacientes
#["123", 89076541, "Heredia", "Barva", "migraña", "acetaminofen"],
#["456", 87539856, "San Jose", "Pavas", "dolor", "acetaminofen"],
# pacientes, enfermedad, medicamentos



Pacientes = []
EnfermedadesPaciente1 = []
EnfermedadesPaciente2 = []
MedicamentosPaciente1 = []
MedicamentosPaciente2 = []

EnfermedadesEncomun = []
MedicinasEncomun = []
def PacientesCargar(Datos,Paciente1,Paciente2):
    #print(Datos)
    Paciente1 = str(Paciente1)
    Paciente2 = str(Paciente2)
    for paciente in Datos:
        #print(paciente[1],Paciente1)
        if str(paciente[1]) == str(Paciente1):        
            #print("entro")    
            EnfermedadesPaciente1.append(paciente[4])
            MedicamentosPaciente1.append(paciente[5])        
        if str(paciente[1]) == str(Paciente2):            
            EnfermedadesPaciente2.append(paciente[4])
            MedicamentosPaciente2.append(paciente[5])  
    conjunto = set(EnfermedadesPaciente1)
    for enfermedad in conjunto:
        if enfermedad in EnfermedadesPaciente2:
            EnfermedadesEncomun.append(enfermedad)
    conjunto = set(MedicamentosPaciente1)
    for Medicamento in conjunto:
        if Medicamento in MedicamentosPaciente2:
            MedicinasEncomun.append(Medicamento)  
#87539856 , 45354632 profe tome la segunda columna como cedula
Paciente1 = str(input("digite la cedula del paciente 1"))
Paciente2 = str(input("digite la cedula del paciente 2"))
PacientesCargar(datos_pacientes,Paciente1, Paciente2)
print(f'Las enfermedades en comun del paciente {Paciente1} y el paciente {Paciente2} son',EnfermedadesEncomun)
print(f'Las medicinas en comun del paciente {Paciente1} y el paciente {Paciente2} son ',MedicinasEncomun)

#Prueba con 702370234 - 215487963
#Salida esperada
#Enfermedades en común entre 702370234 y 215487963: ['migraña']
#Medicamentos en común entre 702370234 y 215487963: ['acetaminofen']


