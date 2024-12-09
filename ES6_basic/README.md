# Fundamentos de ES6

Este README es una introducción a los conceptos básicos de ES6 (ECMAScript 2015), una versión importante de JavaScript que introdujo numerosas características nuevas. Estas herramientas hacen que el código sea más legible, eficiente y moderno.

## Tabla de Contenidos

1. [Introducción](#introducción)
2. [Nuevas Declaraciones de Variables](#nuevas-declaraciones-de-variables)
    - [`let`](#let)
    - [`const`](#const)
3. [Strings y Literales de Plantilla](#strings-y-literales-de-plantilla)
4. [Funciones Flecha](#funciones-flecha)
5. [Parámetros por Defecto](#parámetros-por-defecto)
6. [Destructuración](#destructuración)
7. [Operador Spread y Rest](#operador-spread-y-rest)
8. [Módulos](#módulos)
9. [Referencias](#referencias)

---

## Introducción

ES6 (ECMAScript 2015) es una de las mayores actualizaciones de JavaScript. Introduce características como nuevos tipos de variables, funciones más concisas y herramientas para manejar datos más fácilmente. Estos fundamentos te ayudarán a escribir código más moderno y eficiente.

---

## Nuevas Declaraciones de Variables

### `let`

`let` se utiliza para declarar variables cuyo valor puede cambiar:

```javascript
let contador = 0;
contador += 1;
console.log(contador); // Output: 1
```

### `const`

`const` se usa para declarar constantes, cuyo valor no puede reasignarse:

```javascript
const PI = 3.14159;
console.log(PI); // Output: 3.14159
// PI = 3.2; // Error: Assignment to constant variable.
```

---

## Strings y Literales de Plantilla

Los literales de plantilla (`template literals`) permiten incluir expresiones dentro de cadenas de texto usando backticks (`` ` ``):

```javascript
const nombre = "Juan";
const saludo = `Hola, ${nombre}!`;
console.log(saludo); // Output: Hola, Juan!
```

---

## Funciones Flecha

Las funciones flecha (`arrow functions`) son una forma más concisa de escribir funciones y manejan el contexto (`this`) de forma predecible:

```javascript
const sumar = (a, b) => a + b;
console.log(sumar(3, 5)); // Output: 8
```

---

## Parámetros por Defecto

Puedes asignar valores por defecto a los parámetros de una función:

```javascript
const saludar = (nombre = "invitado") => `Hola, ${nombre}!`;
console.log(saludar()); // Output: Hola, invitado!
console.log(saludar("Ana")); // Output: Hola, Ana!
```

---

## Destructuración

La destructuración permite extraer valores de arrays u objetos de forma más sencilla:

### Arrays

```javascript
const colores = ["rojo", "verde", "azul"];
const [primero, segundo] = colores;
console.log(primero); // Output: rojo
console.log(segundo); // Output: verde
```

### Objetos

```javascript
const persona = { nombre: "Luis", edad: 25 };
const { nombre, edad } = persona;
console.log(nombre); // Output: Luis
console.log(edad); // Output: 25
```

---

## Operador Spread y Rest

### Spread (`...`)

El operador spread permite expandir arrays u objetos:

```javascript
const numeros = [1, 2, 3];
const nuevosNumeros = [...numeros, 4, 5];
console.log(nuevosNumeros); // Output: [1, 2, 3, 4, 5]
```

### Rest (`...`)

El operador rest permite agrupar múltiples argumentos en un solo parámetro:

```javascript
const sumarTodo = (...numeros) => numeros.reduce((acc, num) => acc + num, 0);
console.log(sumarTodo(1, 2, 3, 4)); // Output: 10
```

---

## Módulos

Los módulos permiten dividir el código en archivos reutilizables. Usa `export` para exponer funciones o variables y `import` para utilizarlas:

### Exportar

```javascript
// archivo.js
export const saludar = () => "Hola!";
```

### Importar

```javascript
// main.js
import { saludar } from "./archivo.js";
console.log(saludar()); // Output: Hola!
```

---

## Referencias

- [MDN Web Docs - ECMAScript 6](https://developer.mozilla.org/en-US/docs/Web/JavaScript/New_in_JavaScript/ECMAScript_2015)
- [JavaScript.info - ES6 Basics](https://javascript.info/es6)
- [ES6 Features](https://github.com/lukehoban/es6features)

---

¡Aprende y domina los fundamentos de ES6 para llevar tu código al siguiente nivel! 🚀
