# Sistema de Registro de Estudiantes y Notas

estudiantes = []

# -------------------------
# Registrar estudiantes
# -------------------------

cantidad = int(input("¿Cuántos estudiantes desea registrar?: "))

for i in range(cantidad):
    nombre = input("Ingrese el nombre del estudiante: ")

    estudiante = {
        "nombre": nombre,
        "materias": {}
    }

    estudiantes.append(estudiante)

# -------------------------
# Registrar materias y notas
# -------------------------

for estudiante in estudiantes:

    print("\nRegistro de materias para:", estudiante["nombre"])

    cantidad_materias = int(input("¿Cuántas materias desea registrar?: "))

    for i in range(cantidad_materias):

        materia = input("Nombre de la materia: ")
        nota = float(input("Nota: "))

        estudiante["materias"][materia] = nota

# -------------------------
# Mostrar información
# -------------------------

print("\n----- INFORMACIÓN DE ESTUDIANTES -----")

for estudiante in estudiantes:

    print("\nEstudiante:", estudiante["nombre"])

    for materia, nota in estudiante["materias"].items():
        print(materia, ":", nota)

# -------------------------
# Calcular promedios
# -------------------------

print("\n----- PROMEDIOS -----")

mejor_estudiante = ""
mejor_promedio = 0

for estudiante in estudiantes:

    suma = 0
    cantidad_notas = 0

    for nota in estudiante["materias"].values():
        suma += nota
        cantidad_notas += 1

    promedio = suma / cantidad_notas

    print("Promedio de", estudiante["nombre"], ":", round(promedio,2))

    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = estudiante["nombre"]

# -------------------------
# Mejor estudiante
# -------------------------

print("\n----- MEJOR ESTUDIANTE -----")
print("Estudiante:", mejor_estudiante)
print("Promedio:", round(mejor_promedio,2))
