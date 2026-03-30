# =============================================================================
#  GUÍA PYTHON - MÓDULO 1 | Fundamentos de programación
#  Be a Coder - RIWI
# =============================================================================
#  Ejecuta cada sección comentando/descomentando el código que quieras probar.
#  Puedes correr este archivo completo o sección por sección en tu editor.
# =============================================================================


# =============================================================================
# 1. VARIABLES Y TIPOS DE DATOS
# =============================================================================

# --- Declaración de variables ---
nombre = "Ana García"       # str  → cadena de texto
edad = 25                   # int  → número entero
altura = 1.68               # float → número decimal
activo = True               # bool → True o False
sin_valor = None            # NoneType → ausencia de valor

# --- Ver el tipo de una variable ---
print(type(nombre))         # <class 'str'>
print(type(edad))           # <class 'int'>

# --- Conversión de tipos (casting) ---
num_texto = "42"
num_entero = int(num_texto)         # "42"  → 42
num_decimal = float("3.14")         # str   → 3.14
texto = str(100)                    # 100   → "100"
booleano = bool(0)                  # 0     → False  (0, "", None → False)
booleano2 = bool("hola")            # str   → True   (cualquier otro valor → True)

# --- f-strings (formateo de texto) ---
print(f"Hola, me llamo {nombre} y tengo {edad} años.")
print(f"Mi altura es {altura:.2f} metros.")  # :.2f → 2 decimales


# =============================================================================
# 2. OPERADORES ARITMÉTICOS Y LÓGICOS
# =============================================================================

a, b = 10, 3

# --- Aritméticos ---
print(a + b)    # 13  → suma
print(a - b)    # 7   → resta
print(a * b)    # 30  → multiplicación
print(a / b)    # 3.33 → división real (siempre da float)
print(a // b)   # 3   → división entera (descarta decimales)
print(a % b)    # 1   → módulo (resto de la división)
print(a ** b)   # 1000 → potencia

# Truco útil con módulo:
print(10 % 2 == 0)  # True  → es par
print(9 % 2 == 0)   # False → es impar

# --- Comparación ---
print(5 == 5)   # True  → igual
print(5 != 3)   # True  → diferente
print(5 > 3)    # True  → mayor
print(5 < 3)    # False → menor
print(5 >= 5)   # True  → mayor o igual
print(5 <= 4)   # False → menor o igual

# --- Lógicos ---
print(True and False)   # False → ambos deben ser True
print(True or False)    # True  → al menos uno debe ser True
print(not True)         # False → invierte el valor


# =============================================================================
# 3. ESTRUCTURAS DE CONTROL
# =============================================================================

# --- if / elif / else ---
nota = 75

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bueno")
elif nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")

# --- Condicional en una línea (ternario) ---
estado = "Mayor" if edad >= 18 else "Menor"
print(estado)

# --- for con range ---
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8  (de 2 en 2)
    print(i)

# --- for sobre una lista ---
frutas = ["manzana", "pera", "uva", "mango"]
for fruta in frutas:
    print(fruta)

# --- break y continue ---
for numero in range(10):
    if numero == 3:
        continue    # salta el 3, sigue con el 4
    if numero == 7:
        break       # para el bucle al llegar a 7
    print(numero)   # imprime: 0, 1, 2, 4, 5, 6

# --- while ---
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1   # equivale a: contador = contador + 1

# --- while con break (útil para menús) ---
while True:
    opcion = input("Escribe 'salir' para terminar: ")
    if opcion == "salir":
        break
    print(f"Escribiste: {opcion}")


# =============================================================================
# 4. FUNCIONES
# =============================================================================

# --- Función básica con parámetros y retorno ---
def calcular_descuento(precio, porcentaje):
    """Calcula el precio final después de aplicar un descuento."""
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

resultado = calcular_descuento(100, 20)
print(f"Precio con descuento: ${resultado}")    # $80.0

# --- Parámetros con valor por defecto ---
def saludar(nombre, mensaje="Hola"):
    """Saluda a una persona con un mensaje opcional."""
    return f"{mensaje}, {nombre}!"

print(saludar("Luis"))              # Hola, Luis!
print(saludar("Luis", "Buenas"))    # Buenas, Luis!

# --- Función con múltiples retornos ---
def dividir(a, b):
    """Divide dos números y retorna cociente y resto."""
    cociente = a // b
    resto = a % b
    return cociente, resto          # retorna una tupla

coc, res = dividir(17, 5)
print(f"Cociente: {coc}, Resto: {res}")

# --- Lambda (función anónima) ---
doble = lambda x: x * 2
cuadrado = lambda x: x ** 2
suma = lambda a, b: a + b

print(doble(5))         # 10
print(cuadrado(4))      # 16
print(suma(3, 7))       # 10

# Lambda con sorted (ejemplo típico de prueba):
personas = [{"nombre": "Carlos", "edad": 30}, {"nombre": "Ana", "edad": 25}]
ordenadas = sorted(personas, key=lambda p: p["edad"])
print(ordenadas)        # Ana primero (25), luego Carlos (30)


# =============================================================================
# 5. ESTRUCTURAS DE DATOS
# =============================================================================

# ----- LISTAS -----
# Ordenadas, modificables, permiten duplicados

productos = ["leche", "pan", "huevos"]

productos.append("café")        # agrega al final
productos.insert(1, "mantequilla")  # inserta en posición 1
productos.remove("pan")         # elimina la primera ocurrencia
eliminado = productos.pop()     # elimina y retorna el último
productos[0] = "yogur"          # modifica por índice

print(len(productos))           # cantidad de elementos
print(productos[0])             # primer elemento
print(productos[-1])            # último elemento
print(productos[1:3])           # slice: elementos del índice 1 al 2

# Recorrer con índice y valor:
for i, producto in enumerate(productos):
    print(f"{i}: {producto}")

# Verificar si existe:
if "café" in productos:
    print("El café está en la lista")

# ----- TUPLAS -----
# Ordenadas, NO modificables, más rápidas que las listas

coordenadas = (4.7110, -74.0721)    # latitud, longitud
colores_semaforo = ("rojo", "amarillo", "verde")

print(coordenadas[0])           # 4.711
print(len(colores_semaforo))    # 3

# Desempaquetado:
lat, lon = coordenadas
print(f"Latitud: {lat}, Longitud: {lon}")

# ----- DICCIONARIOS -----
# Pares clave:valor, no ordenados (en Python 3.7+ mantienen orden de inserción)

usuario = {
    "nombre": "Ana",
    "edad": 25,
    "email": "ana@email.com",
    "activo": True
}

# Acceder:
print(usuario["nombre"])            # Ana
print(usuario.get("telefono", "No registrado"))  # valor por defecto si no existe

# Agregar / modificar:
usuario["ciudad"] = "Barranquilla"  # agrega nueva clave
usuario["edad"] = 26                # modifica valor existente

# Eliminar:
del usuario["activo"]
email = usuario.pop("email")        # elimina y retorna el valor

# Recorrer:
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# Solo claves o solo valores:
print(list(usuario.keys()))
print(list(usuario.values()))

# Verificar si existe una clave:
if "nombre" in usuario:
    print("El usuario tiene nombre")

# Lista de diccionarios (muy común en casos de estudio):
inventario = [
    {"producto": "laptop",  "precio": 1500, "stock": 10},
    {"producto": "mouse",   "precio": 25,   "stock": 50},
    {"producto": "teclado", "precio": 45,   "stock": 30},
]

for item in inventario:
    print(f"{item['producto']}: ${item['precio']} ({item['stock']} unidades)")


# =============================================================================
# 6. MANEJO DE ERRORES
# =============================================================================

# --- try / except básico ---
def dividir_seguro(a, b):
    """Divide dos números manejando posibles errores."""
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: no se puede dividir entre 0")
        return None
    except TypeError:
        print("Error: los valores deben ser números")
        return None

print(dividir_seguro(10, 2))    # 5.0
print(dividir_seguro(10, 0))    # Error: no se puede dividir entre 0
print(dividir_seguro(10, "a"))  # Error: los valores deben ser números

# --- try / except / else / finally ---
def leer_archivo_simulado(nombre):
    try:
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío")
        # aquí iría código que puede fallar
        contenido = f"Contenido de {nombre}"
    except ValueError as e:
        print(f"Error de valor: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    else:
        print("Lectura exitosa")    # se ejecuta si NO hubo error
        return contenido
    finally:
        print("Operación finalizada")  # se ejecuta SIEMPRE

# --- Patrón de validación de entrada (muy común en pruebas) ---
def pedir_entero(mensaje, minimo=None, maximo=None):
    """Pide un número entero al usuario con validación robusta."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}")
                continue
            return valor
        except ValueError:
            print("Por favor ingresa solo números enteros.")

# Uso:
# edad = pedir_entero("Ingresa tu edad: ", minimo=0, maximo=120)


# =============================================================================
# 7. BUENAS PRÁCTICAS Y MODULARIZACIÓN
# =============================================================================
# Cada función hace UNA sola cosa.
# Nombres descriptivos, comentarios donde sea necesario.
# Un main() que orquesta todo el flujo.

def mostrar_menu():
    """Muestra el menú principal del programa."""
    print("\n===== GESTIÓN DE PRODUCTOS =====")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Buscar producto")
    print("4. Salir")
    print("================================")

def agregar_producto(inventario, nombre, precio, stock):
    """Agrega un nuevo producto al inventario."""
    producto = {"nombre": nombre, "precio": precio, "stock": stock}
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado exitosamente.")

def mostrar_inventario(inventario):
    """Imprime todos los productos del inventario."""
    if not inventario:
        print("El inventario está vacío.")
        return
    print(f"\n{'Producto':<15} {'Precio':>10} {'Stock':>8}")
    print("-" * 35)
    for p in inventario:
        print(f"{p['nombre']:<15} ${p['precio']:>9.2f} {p['stock']:>8}")

def buscar_producto(inventario, nombre_buscar):
    """Busca un producto por nombre (sin distinción de mayúsculas)."""
    resultados = [p for p in inventario if nombre_buscar.lower() in p["nombre"].lower()]
    return resultados

def main():
    """Función principal: controla el flujo del programa."""
    inventario = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            try:
                precio = float(input("Precio: "))
                stock = int(input("Stock disponible: "))
                agregar_producto(inventario, nombre, precio, stock)
            except ValueError:
                print("Error: precio y stock deben ser números.")

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            termino = input("¿Qué producto buscas? ").strip()
            encontrados = buscar_producto(inventario, termino)
            if encontrados:
                mostrar_inventario(encontrados)
            else:
                print(f"No se encontró ningún producto con '{termino}'.")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Ingresa un número del 1 al 4.")

# --- Punto de entrada del programa ---
# Esta condición asegura que main() solo se ejecute si corres este archivo
# directamente, no si lo importas desde otro archivo.
if __name__ == "__main__":
    main()


# =============================================================================
# RESUMEN RÁPIDO - MÉTODOS MÁS USADOS
# =============================================================================

# STRINGS
# s.upper()         → "hola" → "HOLA"
# s.lower()         → "HOLA" → "hola"
# s.strip()         → elimina espacios al inicio y final
# s.split(",")      → divide en lista por separador
# s.replace("a","b")→ reemplaza caracteres
# s.startswith("h") → True/False
# len(s)            → longitud

# LISTAS
# lista.append(x)   → agrega al final
# lista.insert(i,x) → inserta en posición i
# lista.remove(x)   → elimina primera ocurrencia de x
# lista.pop()       → elimina y retorna el último
# lista.sort()      → ordena (modifica la lista original)
# sorted(lista)     → retorna lista ordenada (no modifica original)
# lista.index(x)    → retorna el índice de x
# x in lista        → True/False

# DICCIONARIOS
# d.get(k, default) → valor de k o default si no existe
# d.keys()          → todas las claves
# d.values()        → todos los valores
# d.items()         → pares (clave, valor)
# d.pop(k)          → elimina y retorna valor de k
# k in d            → True/False

# =============================================================================
#  ¡Éxitos en tu prueba! - Be a Coder RIWI
# =============================================================================
