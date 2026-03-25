# 📦 Sistema de Inventario en Python

Sistema de gestión de inventario por consola desarrollado en Python, con soporte para operaciones CRUD, estadísticas y persistencia de datos en formato CSV.

---

## 📁 Estructura del Proyecto

```
inventario/
│
├── app.py          # Menú principal e interfaz de usuario
├── servicios.py     # Lógica de negocio (CRUD y estadísticas)
└── archivos.py      # Persistencia de datos (guardar/cargar CSV)
```

---

## 🚀 Funcionalidades

| Opción | Función |
|--------|---------|
| 1 | Agregar producto |
| 2 | Mostrar inventario |
| 3 | Buscar producto |
| 4 | Actualizar producto |
| 5 | Eliminar producto |
| 6 | Ver estadísticas |
| 7 | Guardar inventario en CSV |
| 8 | Cargar inventario desde CSV |
| 9 | Salir |

---

## 🗂️ Descripción de Módulos

### `app.py` — Interfaz de Usuario
Punto de entrada del programa. Controla el flujo del menú principal y gestiona las interacciones con el usuario.

- Validación de entradas (nombre, precio, cantidad) antes de delegar a `servicios.py`
- Uso de bucles de control para garantizar datos correctos
- Separación clara entre lógica de interfaz y lógica de negocio

**Ejecución:**
```bash
python app.py
```

---

### `servicios.py` — Lógica de Negocio
Contiene todas las operaciones sobre el inventario en memoria.

**Funciones:**

| Función | Descripción |
|---------|-------------|
| `agregar_producto(inventario, nombre, precio, cantidad)` | Agrega un nuevo producto. Valida duplicados y formato del nombre. |
| `buscar_producto(inventario, nombre)` | Búsqueda lineal insensible a mayúsculas. Retorna el diccionario del producto o `None`. |
| `eliminar_producto(inventario, nombre)` | Elimina un producto por nombre. Retorna `True` si fue exitoso. |
| `calcular_estadisticas(inventario)` | Retorna unidades totales, valor total, producto más caro y de mayor stock. |

**Estructura de un producto:**
```python
{
    "nombre": str,
    "precio": float,
    "cantidad": int
}
```

---

### `archivos.py` — Persistencia de Datos
Maneja la lectura y escritura del inventario en archivos `.csv`.

**Funciones:**

| Función | Descripción |
|---------|-------------|
| `guardar_csv(inventario)` | Solicita carpeta y nombre de archivo. Crea la carpeta si no existe y guarda el inventario. |
| `cargar_csv()` | Lee un archivo CSV y retorna una lista de productos válidos junto con el conteo de errores. |

**Formato del CSV:**
```
nombre,precio,cantidad
producto1,15000.0,10
producto2,8500.5,25
```

**Notas:**
- Solo se permiten archivos con extensión `.csv`
- Las filas con datos inválidos o negativos son descartadas y contadas como errores
- Al cargar, el usuario puede elegir **sobrescribir** el inventario actual o **fusionarlo** (suma cantidades si el producto ya existe)

---

## ✅ Validaciones Implementadas

- **Nombre:** No puede estar vacío ni contener espacios
- **Precio:** Debe ser un número decimal mayor a 0
- **Cantidad:** Debe ser un número entero mayor a 0
- **Archivo CSV:** Solo acepta formato `.csv` con nombre simple (sin múltiples extensiones)
- **Duplicados:** No se permite agregar dos productos con el mismo nombre

---

## 🔧 Requisitos

- Python 3.x
- No requiere librerías externas (solo módulos estándar: `csv`, `os`)

---

## 📌 Ejemplo de Uso

```
--- SISTEMA DE INVENTARIO ---
1. Agregar | 2. Mostrar | 3. Buscar | 4. Actualizar producto | 5. Eliminar | 6. Estadísticas
7. Guardar CSV | 8. Cargar CSV | 9. Salir

Seleccione opción: 1
Nombre: Laptop
Precio: 2500000
Cantidad: 5
Producto agregado con éxito.
```

---

## 👤 Autor

Jefferson Cacerez
