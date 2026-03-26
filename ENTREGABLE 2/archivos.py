import csv
import os

def guardar_csv(inventario):
    # Verifica si el inventario está vacío antes de guardarlo
    if not inventario:
        print("Error: El inventario está vacío.")
        return
    # Solicita al usuario el nombre de la carpeta donde se guardará el archivo.
    carpeta = ""
    while len(carpeta.strip()) == 0:
        carpeta = input("Ingrese el nombre de la carpeta: ").strip()
        if len(carpeta) == 0:
            print("Error: no puede estar vacío.")

    # Solicita al usuario el nombre del archivo asegurándose que sea válido.
    archivo = ""
    valido = False

    while not valido:
        archivo = input("Ingrese el nombre del archivo (ej: jheffer.csv): ").strip()

        # Validación  para evita entradas vacías.
        if len(archivo) == 0:
            print("Error: no puede estar vacío.")

        # Validación para asegura que el archivo tenga extensión .csv.
        elif not archivo.endswith(".csv"):
            print("Error: solo se permiten archivos .csv")

        # Validación evita nombres de archivo inválidos.
        elif "." in archivo[:-4]:
            print("Error: nombre inválido.")

        else:
            #Al pasar por todas las  validaciones, se habilita la salida del bucle.
            valido = True

    # Crea la carpeta si no existe.
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # Construye la ruta del archivo de manera segura.
    ruta = os.path.join(carpeta, archivo)

    try:
        # Abre el archivo en modo escritura y crea un escritor de CSV que manjea diccionarios
        with open(ruta, "w", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["nombre", "precio", "cantidad"])
            
            # Escribe la cabecera del archivo CSV.
            writer.writeheader()
            
            # Escribe todos los registros del inventario.
            writer.writerows(inventario)

        print(f"Inventario guardado en: {ruta}")

    except Exception as e:
        # Captura errores durante la escritura (ej. permisos).
        print(f"Error de escritura: {e}")

def cargar_csv():
    # Solicita al usuario la carpeta donde se encuentra el archivo CSV.
    carpeta = input("Ingrese la carpeta: ").strip()

    archivo = ""
    valido = False

    while not valido:
        archivo = input("Ingrese el archivo (ej: jheffer.csv): ").strip()

        if len(archivo) == 0:
            print("Error: no puede estar vacío.")

        elif not archivo.endswith(".csv"):
            print("Error: solo se permiten archivos .csv")

        else:
            valido = True

    # Construye la ruta completa del archivo.
    ruta = os.path.join(carpeta, archivo)

    nuevos_productos = []
    errores = 0

    try:
        # Abre el archivo en modo lectura, lee el archivo y conviertefilas en un diccionario
        with open(ruta, "r") as f:
            reader = csv.DictReader(f)
            
            for fila in reader:
                try:
                    # Convierte los tipos de datos de las columnas.
                    p = {
                        "nombre": fila["nombre"],
                        "precio": float(fila["precio"]),
                        "cantidad": int(fila["cantidad"])
                    }

                    # Valida que los datos sean correctos (no negativos).
                    if p["precio"] < 0 or p["cantidad"] < 0:
                        raise ValueError

                    nuevos_productos.append(p)

                except:
                    # Cuenta errores para permitir continuar leyendo.
                    errores += 1

        # Retorna los nuevos productos y el número de errores encontrados.
        return nuevos_productos, errores

    except FileNotFoundError:
        # Maneja el error si el archivo no se encuentra.
        print("Archivo no encontrado.")
        return [], 0
