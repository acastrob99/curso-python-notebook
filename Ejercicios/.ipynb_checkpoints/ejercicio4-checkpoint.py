# 1. Insertar aulmno --> En que aula quieres meter al alumno (1,2,3) --> DNI, Nombre, Apellidos 
# 2. Mostrar alumnos colegio --> Todos los alumnos del colegio por aula
# 3. Mostrar alumnos aula --> Pregunta de que aula quiere mostrar los alumnos (1,2,3)
# 4. Buscar alumno --> Pregunta por el DNI --> Muestra en el aula que esta el alumno con ese DNI, si existe
# 5. Salir

#HACERLO CON DICCIONARIOS {} Y CON LISTAS []                 
# Tenemos un colegio en el que hay aulas a las que estan asignadas unos alumos con DNI, NOMBRE Y APELLIDOS


aulas = [1,2,3]                 #Tenemos 3 clases 1,2 y 3
colegio = {'Aulas':aulas}       #Como ya sabemos las clases que metemos la lista de clases dentro del colegio asigando la clave "Aulas" y acontinuacion la lista de aulas
alumnos = []                    #Creamos la lista de alumnos que iremos añadiendo

def menu():                     #Pintamos menu
    opcion = 0
    while opcion != 5:
        print("1. Insertar aulmno")
        print("2. Mostrar alumnos colegio")
        print("3. Mostrar alumnos aula")
        print("4. Busvar alumnos")
        print("5. Salir")
        opcion = int(input("Elige una opcion: "))
        if opcion == 1:
            insertar_alumno()
        if opcion == 2:
            print(mostrar_alumnos())
        if opcion == 3:
            print(mostrar_alumnos_aula(int(input("Elige la aula para mostrar alumnos"))))
        if opcion == 4:
            print(buscar_alumno(str(input("Escribe Dni para buscar alumno"))))
        if opcion == 5:
            print("Adios!!!")

def insertar_alumno():
    dni = str(input("Inserta Dni alumno: "))
    nombre = str(input("Inserta nombre alumno: "))
    apellidos = str(input("Inserta apellidos alumno: "))
    aula = int(input("Inserta aula alumno: ")) 
    alumno = {'Dni': dni, 'Nombre': nombre,'Apellidos': apellidos, "Aula": aula}    #Creamos un diccionario llamado alumno 
    alumnos.append(alumno)                                                          #Añadimos a la lista de alumnos el diccionario creado alumno en el paso anterior
    colegio['Alumno'] = alumnos                                                     #Añadimos al diccionario colegio la lista de alumnos despues de haber añadido el ultimo


def mostrar_alumnos():    
    aula1 = ""
    aula2 = ""
    aula3 = ""
    for alumno in alumnos:                  #Recorremos los diccionarios de alumnos de la lista de alumnos
        if alumno['Aula'] == 1:             #Buscamos alumnos para mostrarlos por aula añadiendo a un string los alumnos que cuya clase sea la 1 en este caso
            aula1 += str(alumno)+", "       #alumno es un diccionario lo pasamos a string para meterlo en la variable string
        if alumno['Aula'] == 2:
            aula2 += str(alumno)+", " 
        if alumno['Aula'] == 3:
            aula3 += str(alumno)+", " 

    return "Alumnos aula 1: "+aula1+"\n"+"Alumnos aula 2: "+aula2+"\n"+"Alumnos aula 3: "+aula3+"\n"    #Retornamos un string final 


def mostrar_alumnos_aula(aula):                 #Retornar solo los alumnos de un aula en concreto
    alumnos_aula = ""                           #String para ir concatenando los alumnos en la clase pasada en la llamada de la funcion
    for alumno in alumnos:                      #Recorremos los diccionarios de alumnos de la lista de alumnos
        if alumno['Aula'] == aula:              #Comparamos los alumnos para ver si son del aula que nos interesa
            alumnos_aula += str(alumno)+", "    #Añadimos dentro al alumno pasando el diccionario a string
        if aula >= 4:
            return "Aula no existente"
    if alumnos_aula != "":                      #Comrprobamos si el aula esta vacia para devolver aula vacia o o los alumnos del aula
        return alumnos_aula
    else:
        return "Aula vacia"
        

def buscar_alumno(dni):                         #Buscamos alumno por dni
    alumno_dni = ""                             #string del alumno para luego retornar
    for alumno in alumnos:                      #Recorremos la lista de alumnos
        if alumno['Dni'] == dni:                #Comparamos DNI 
            alumno_dni = str(alumno)            #Encontrado lo asociamos al string para retornar
    
    if alumno_dni != "":        
        return alumno_dni       
    else:
        return "Alumno no encontrado"


menu()
