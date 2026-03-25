# 📦 Sistema de Inventario en Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Activo-success)
![License](https://img.shields.io/badge/License-MIT-green)

Aplicación de consola desarrollada en **Python** para la gestión de inventario de productos, utilizando estructuras en memoria y persistencia en archivos CSV.

---

## 🚀 Funcionalidades

- ➕ Agregar productos  
- 📋 Mostrar inventario  
- 🔍 Buscar productos  
- ✏️ Actualizar productos  
- ❌ Eliminar productos  
- 📊 Generar estadísticas  
- 💾 Guardar en CSV  
- 📂 Cargar desde CSV  

---

## 🧠 Estructura del Proyecto
📁 proyecto/
│
├── app.py # Menú principal (interfaz)
├── servicios.py # Lógica de negocio
├── archivos.py # Manejo de archivos CSV
└── README.md # Documentación

---

## ⚙️ Tecnologías

- Python 3  
- Librerías estándar:
  - `csv`
  - `os`

---

## 🗂️ Modelo de Datos

Estructura usada para cada producto:

```python
{
    "nombre": str,
    "precio": float,
    "cantidad": int
}
Ejemplo :
[
    {"nombre": "lapiz", "precio": 1000, "cantidad": 10},
    {"nombre": "cuaderno", "precio": 5000, "cantidad": 5}
]
🧪 Validaciones
Nombre obligatorio
Precio > 0
Cantidad entera positiva
Control de duplicados
Manejo de errores (try/except)
📊 Estadísticas
Total de unidades
Valor total del inventario
Producto más caro
Producto con mayor stock
💾 Persistencia
Exportación a .csv
Importación desde .csv
Opción de sobrescribir o fusionar datos
🏗️ Arquitectura
Modular (separación por archivos)
Basado en capas:
Interfaz → app.py
Lógica → servicios.py
Persistencia → archivos.py
📌 Buenas prácticas
Código limpio y estructurado
Validación de datos
Reutilización de funciones
Manejo de excepciones
Separación de responsabilidades
AUTOR :
Jefferson Cacerez
