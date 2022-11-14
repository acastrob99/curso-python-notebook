# 1. Insertar aulmno --> En que aula quieres meter al alumno (1,2,3) --> DNI, Nombre, Apellidos 
# 2. Mostrar alumnos colegio --> Todos los alumnos del colegio por aula
# 3. Mostrar alumnos aula --> Pregunta de que aula quiere mostrar los alumnos (1,2,3)
# 4. Buscar alumno --> Pregunta por el DNI --> Muestra en el aula que esta el alumno con ese DNI, si existe
# 5. Salir


aulas = [1,2,3]
alumnos = []
colegio = {'Alumno': alumnos, 'Aula': aulas }


opcion = 0
while opcion != 5:
    print("1. Insertar alumno")
    print("2. Mostrar alumno colegio") 
    print("3. Mostrar alumno aula")
    print("4. Buscar alumno")
    print("5. Salir")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        dni = str(input("Escriba Dni alumno: "))
        nombre = str(input("Escriba Nombre alumno: "))
        apellidos = str(input("Escriba Apellidos alumno: "))
        aula = int(input("En que aula quieres meter al alumno 1,2 o 3: "))
        alum = {'DNI':dni,'Nombre':nombre,'Apellidos':apellidos,'Aula': aula}
        alumnos.append(alum)
        colegio['Alumno','Aula'] = alumnos[alum],alum['Aula']

    if opcion == 2:
       for alumno in alumnos:
        if alumno["Aula"] == 1:
            print(alumno['Nombre'])
    
    if opcion == 3:
        aul = int(input("Elige aula para mostrar alumnos 1, 2 o 3: "))

    if opcion == 4:
         buscar_dni = int(input("Escribe DNI a buscar: "))

