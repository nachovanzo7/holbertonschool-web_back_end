# Generadores en Python: Generadores Asincrónicos, Comprensiones Asincrónicas y Generadores con Anotación de Tipos

## Introducción

Los generadores en Python son herramientas poderosas para manejar flujos de datos de forma eficiente. Permiten generar elementos uno a la vez, siendo ideales para trabajar con grandes volúmenes de datos o flujos continuos. Este documento aborda:

1. **Generadores Asincrónicos**: Combinar programación asincrónica con generadores.
2. **Comprensiones Asincrónicas**: Una forma concisa de crear generadores asincrónicos.
3. **Generadores con Anotación de Tipos**: Aumentar la claridad del código y garantizar la seguridad de tipos en funciones generadoras.

---

## 1. Generadores Asincrónicos

### ¿Qué son?

Los generadores asincrónicos combinan la funcionalidad de los generadores tradicionales con la programación asincrónica. Usan `async def` y `yield` para producir valores de forma asincrónica. Son útiles en situaciones como la transmisión de datos a través de una red o cualquier operación que implique esperas no bloqueantes.

### Ejemplo

```python
import asyncio

async def generador_asincrono():
    for i in range(5):
        await asyncio.sleep(1)  # Simula una operación asincrónica
        yield i

# Usando el generador asincrónico
async def main():
    async for valor in generador_asincrono():
        print(valor)

asyncio.run(main())

## Características clave

- Usá `async def` para definir el generador.
- Usá `yield` para producir valores.
- Usá `async for` para iterar sobre los valores generados.

---

## 2. Comprensiones Asincrónicas

### ¿Qué son?

Las comprensiones asincrónicas ofrecen una sintaxis concisa para trabajar con iterables asincrónicos. Permiten generar listas, conjuntos u otras colecciones de manera más legible y eficiente.

### Ejemplo

```python
import asyncio

async def generador_asincrono():
    for i in range(5):
        await asyncio.sleep(1)
        yield i

async def main():
    # Comprensión asincrónica para recolectar valores en una lista
    resultado = [valor async for valor in generador_asincrono()]
    print(resultado)

asyncio.run(main())

## Características clave

- Usá `async for` dentro de corchetes `[]`, llaves `{}` o paréntesis `()` para crear listas, conjuntos o expresiones generadoras, respectivamente.
- Más legibles y concisas que iterar y añadir valores manualmente.

---

## 3. Generadores con Anotación de Tipos

### ¿Qué son?

Las anotaciones de tipos para generadores permiten especificar los tipos de valores que generan, los valores que reciben mediante `send()` y el tipo de valor que retornan al finalizar.

### Sintaxis general para anotar un generador

```python
Generator[TipoYield, TipoSend, TipoReturn]

## Para generadores asincrónicos:

```python
AsyncGenerator[TipoYield, TipoSend]


### Ejemplo

#### Generador Sincrónico con Anotaciones de Tipos

```python
from typing import Generator

def generador_sincronico() -> Generator[int, None, None]:
    for i in range(5):
        yield i


### Generador Asincrónico con Anotaciones de Tipos

```python
from typing import AsyncGenerator

async def generador_asincrono() -> AsyncGenerator[int, None]:
    for i in range(5):
        await asyncio.sleep(1)
        yield i

### Comprensiones Asincrónicas con Anotaciones de Tipos

Podés usar `List`, `Set` u otros tipos de colección para anotar el resultado de comprensiones asincrónicas:

```python
from typing import List

async def recolectar_valores() -> List[int]:
    return [valor async for valor in generador_asincrono()]

## Casos de Uso Práctico

- **Transmisión de Datos**: Obtener datos desde APIs o leer archivos de forma asincrónica.
- **Tareas en Segundo Plano**: Generar eventos periódicos sin bloquear el hilo principal.
- **Evaluación Perezosa**: Manejar grandes volúmenes de datos o datos en tiempo real de manera eficiente.
