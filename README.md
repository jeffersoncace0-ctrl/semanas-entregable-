📦 Sistema de Inventario en Python

Aplicación de consola desarrollada en Python que permite gestionar un inventario de productos utilizando estructuras de datos en memoria y persistencia en archivos CSV.

🚀 Funcionalidades
➕ Agregar productos
📋 Mostrar inventario
🔍 Buscar productos
✏️ Actualizar productos
❌ Eliminar productos
📊 Calcular estadísticas
💾 Guardar inventario en CSV
📂 Cargar inventario desde CSV
🧠 Estructura del Proyecto
📁 proyecto/
│
├── app.py          # Archivo principal (menú del sistema)
├── servicios.py    # Lógica de negocio (CRUD + estadísticas)
├── archivos.py     # Manejo de archivos CSV
└── README.md       # Documentación del proyecto
⚙️ Tecnologías usadas
Python 3
Módulos estándar:
csv → manejo de archivos
os → rutas y carpetas
🗂️ Estructura de datos

El sistema utiliza una lista de diccionarios:

{
    "nombre": str,
    "precio": float,
    "cantidad": int
}

Ejemplo:

[
    {"nombre": "lapiz", "precio": 1000, "cantidad": 10},
    {"nombre": "cuaderno", "precio": 5000, "cantidad": 5}
]
▶️ Ejecución
Clonar repositorio:
git clone <url-del-repo>
Entrar a la carpeta:
cd proyecto
Ejecutar:
python app.py
🧪 Validaciones implementadas
Nombres no vacíos
Precios mayores a 0
Cantidades enteras positivas
Control de productos duplicados
Manejo de errores con try/except
📊 Estadísticas generadas
Total de unidades
Valor total del inventario
Producto más caro
Producto con mayor stock
💾 Persistencia
Exportación a archivos .csv
Importación desde archivos .csv
Opción de sobrescribir o fusionar datos
🏗️ Arquitectura
Modular → separación en archivos (servicios, archivos, app)
Capas:
Interfaz → app.py
Lógica → servicios.py
Persistencia → archivos.py
📌 Mejores prácticas aplicadas
Validación de entradas
Reutilización de funciones
Manejo de excepciones
Uso de estructuras simples y eficientes
Código legible y mantenible
💬 Autor

Desarrollado por Jefferson Cacerez
