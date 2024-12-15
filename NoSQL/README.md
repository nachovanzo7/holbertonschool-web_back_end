# MongoDB Basics Guide 📚

Este documento es una guía práctica para aprender los conceptos básicos de MongoDB, su sintaxis y comandos principales. ¡Perfecto para aprender y enseñar como un godeano! 😏

---

## 📖 **¿Qué es MongoDB?**
MongoDB es una base de datos NoSQL orientada a documentos. Guarda datos en formato **JSON/BSON**, permitiendo estructuras flexibles y escalables.

### Características clave:
- **NoSQL**: No usa tablas como bases SQL tradicionales.
- **Documentos**: Guarda datos en estructuras tipo JSON.
- **Escalable**: Perfecta para grandes volúmenes de datos.
- **Flexible**: No necesita esquemas rígidos.

---

## 🚀 **Instalación**
1. Descargá MongoDB desde [mongodb.com](https://www.mongodb.com/try/download/community).
2. Instalá y verificá que esté funcionando:
   ```bash
   mongo --version

# 🛠️ Comandos Básicos

## Selección y Manejo de Bases de Datos
```bash
show dbs                      # Mostrar bases de datos
use nombreBaseDeDatos         # Crear/Seleccionar base de datos
db.dropDatabase()             # Eliminar la base actual

# Manejo de Colecciones
```bash
show collections              # Mostrar colecciones
db.createCollection("nombre") # Crear colección
db.nombre.drop()              # Eliminar colección

# Insertar Datos
```javascript
db.coleccion.insertOne({ nombre: "Ana", edad: 25 })
db.coleccion.insertMany([{ nombre: "Juan", edad: 30 }, { nombre: "Sofía", edad: 22 }])

# Consultar Datos
```javascript
db.coleccion.find()           // Traer todos los documentos
db.coleccion.find({ edad: { $gt: 25 } }) // Filtro: edad > 25
db.coleccion.find().pretty()  // Formato legible

# Actualizar Datos
```javascript
db.coleccion.updateOne(
  { nombre: "Ana" }, 
  { $set: { edad: 26 } }
)
db.coleccion.updateMany(
  { edad: { $lt: 30 } }, 
  { $set: { joven: true } }
)

# Eliminar Datos
```javascript
db.coleccion.deleteOne({ nombre: "Juan" })
db.coleccion.deleteMany({ edad: { $lt: 25 } })

# 📂 Tipos de Datos en MongoDB
- **String**: Cadenas de texto.
- **Number**: Enteros o decimales.
- **Boolean**: Verdadero/Falso.
- **Array**: Listas de valores.
- **Object**: Documentos anidados.

### Ejemplo:
```json
{
  "nombre": "Luis",
  "edad": 28,
  "hobbies": ["fútbol", "cocina"],
  "contacto": { "email": "luis@gmail.com", "tel": "12345678" }
}
