#ESTE ES UN PROGRMA PARA REGISTRAR PRODUCTOS EN EL INVENTARIO

#SOLICITAR EL NOMBRE DEL PRODUCTO 
nombre = input("Ingrese el nombre del producto: ")

#VALIDAR PRECIOS 
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("El precio no puede ser negativo. Intente de nuevo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número para el precio.")

#VALIDAR CANTIDAD 
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa. Intente de nuevo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero para la cantidad.")

#CALCULAR COSTO TOTAL DEL PRODUCTO 
costo_total = precio * cantidad

#MOSTRAR LOS RESULTADO EN CONSOLA 
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

# Este programa solicita el nombre, precio y cantidad de un producto.
# Luego valida que los datos numéricos sean correctos, no se permiten numeros en negativos.
# Finalmente calcula el costo total multiplicando el precio por la cantidad
# y muestra toda la información en pantalla mediante un resumen de la compra.
