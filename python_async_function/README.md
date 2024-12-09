# Async Functions en Python

Las funciones asíncronas son una característica poderosa de Python que permite manejar operaciones concurrentes de manera eficiente. Este README explica cómo funcionan, cómo usarlas y sus principales beneficios en Python.

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Definición de Async Functions](#definición-de-async-functions)
3. [Usando `await`](#usando-await)
4. [Ejecutando Funciones Asíncronas](#ejecutando-funciones-asíncronas)
5. [Manejo de Errores](#manejo-de-errores)
6. [Ejemplos Prácticos](#ejemplos-prácticos)
    - [Esperar Tareas Simultáneamente](#esperar-tareas-simultáneamente)
    - [Integración con APIs](#integración-con-apis)
    - [Uso del Módulo Random](#uso-del-módulo-random)
7. [Limitaciones](#limitaciones)
8. [Referencias](#referencias)

---

## Introducción

En Python, las funciones asíncronas (async functions) facilitan la escritura de código concurrente. Usando el módulo `asyncio`, se pueden realizar tareas como solicitudes de red, operaciones de E/S, o procesos intensivos sin bloquear la ejecución de otras tareas.

---

## Definición de Async Functions

Para definir una función asíncrona, se usa la palabra clave `async` antes de `def`:

```python
import asyncio

async def mi_funcion():
    print("Hola, mundo!")
    await asyncio.sleep(1)  # Simula una operación asíncrona
    print("Adiós, mundo!")
```

---

## Usando `await`

Dentro de una función asíncrona, se usa la palabra clave `await` para pausar la ejecución hasta que una operación asíncrona se complete. Esto es especialmente útil para llamadas de red o tareas largas:

```python
async def saludar():
    print("Hola!")
    await asyncio.sleep(2)  # Simula espera
    print("Después de 2 segundos")
```

---

## Ejecutando Funciones Asíncronas

Para ejecutar una función asíncrona, se debe utilizar un event loop. Esto se logra con `asyncio.run` o creando un loop manualmente:

```python
asyncio.run(saludar())
```

Si tienes múltiples funciones, puedes ejecutarlas concurrentemente con `asyncio.gather`:

```python
async def tarea1():
    await asyncio.sleep(1)
    print("Tarea 1 completada")

async def tarea2():
    await asyncio.sleep(2)
    print("Tarea 2 completada")

asyncio.run(asyncio.gather(tarea1(), tarea2()))
```

---

## Manejo de Errores

El manejo de errores en funciones asíncronas es similar al de funciones normales. Puedes usar bloques `try` y `except`:

```python
async def puede_fallar():
    try:
        raise ValueError("Error simulado")
    except ValueError as e:
        print(f"Capturado un error: {e}")

asyncio.run(puede_fallar())
```

---

## Ejemplos Prácticos

### Esperar Tareas Simultáneamente

```python
async def contar(segundos):
    print(f"Esperando {segundos} segundos...")
    await asyncio.sleep(segundos)
    print(f"Hecho esperando {segundos} segundos.")

asyncio.run(asyncio.gather(contar(1), contar(2), contar(3)))
```

### Integración con APIs

```python
import aiohttp

async def obtener_datos(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(data)

asyncio.run(obtener_datos("https://jsonplaceholder.typicode.com/posts/1"))
```

### Uso del Módulo Random

El módulo `random` puede integrarse con funciones asíncronas para generar valores aleatorios en operaciones concurrentes:

```python
import random

async def generar_aleatorio():
    await asyncio.sleep(1)  # Simula una tarea asíncrona
    numero = random.randint(1, 100)
    print(f"Número aleatorio generado: {numero}")

asyncio.run(asyncio.gather(generar_aleatorio(), generar_aleatorio()))
```

---

## Limitaciones

1. **No bloquea completamente:** Aunque async es eficiente para operaciones de E/S, no optimiza tareas intensivas de CPU.
2. **Complejidad:** El uso de async puede complicar el flujo lógico del programa.
3. **Compatibilidad:** Algunas bibliotecas no soportan funciones asíncronas directamente.

---

## Referencias

- [Documentación de asyncio](https://docs.python.org/3/library/asyncio.html)
- [Guía de aiohttp](https://docs.aiohttp.org/)
- [PEP 492: Coroutines with async and await syntax](https://peps.python.org/pep-0492/)

---

¡Explora las async functions y lleva tus aplicaciones Python al próximo nivel! 🚀
