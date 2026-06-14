# Lenguaje de Consultas Ágiles para Productos e Inventario

Este repositorio contiene la implementación de un motor léxico y sintáctico para un Lenguaje de Dominio Específico (DSL) diseñado para optimizar y agilizar las consultas en sistemas de logística e inventario. El desarrollo está construido en Python utilizando la librería **PLY (Python Lex-Yacc)**.

---

## 1. Definición Formal de la Gramática

La gramática definida permite realizar búsquedas de productos, consultas de stock y filtrado mediante distintas condiciones.

### Símbolos No Terminales (N)
* N = {S, CONSULTA, BUSQUEDA, STOCK, CONDICION, RESTO_CONDICION, FILTRO, COMPARADOR, NOMBRE, RESTO_NOMBRE}

### Símbolos Terminales (T)
* T = {buscar, producto, mostrar, productos, ver, stock, sin, con, de, categoria, precio, >, <, y, o, IDENTIFICADOR, NUMERO}

### Conjunto de Producciones (P)

```text
S -> CONSULTA
CONSULTA -> BUSQUEDA | STOCK
BUSQUEDA -> buscar producto NOMBRE | mostrar productos CONDICION
STOCK -> ver stock NOMBRE
CONDICION -> FILTRO RESTO_CONDICION
RESTO_CONDICION -> y FILTRO RESTO_CONDICION | o FILTRO RESTO_CONDICION | λ
FILTRO -> sin stock | con stock | de categoria NOMBRE | con precio COMPARADOR NUMERO
COMPARADOR -> > | <
NOMBRE -> IDENTIFICADOR RESTO_NOMBRE
RESTO_NOMBRE -> IDENTIFICADOR RESTO_NOMBRE | λ
```
### Símbolo Distinguido (S)
* S es el axioma inicial de la gramática, donde S pertenece al conjunto N.

---

## 2. Análisis Arquitectural y Justificación del Motor

El diseño del intérprete sigue un paradigma modular estricto, separando el análisis en dos fases secuenciales:

### Flujo de Procesamiento Léxico (Lexer)
El analizador léxico actúa como la primera etapa del procesamiento utilizando expresiones regulares para identificar y clasificar los componentes básicos del lenguaje.
* **Reconocimiento de Palabras Reservadas:** Las secuencias alfanuméricas son comparadas contra un diccionario de palabras clave (BUSCAR, PRODUCTO, MOSTRAR, PRODUCTOS, VER, STOCK, SIN, CON, DE, CATEGORIA, PRECIO, Y, O). Si existe coincidencia, se genera el token correspondiente.
* **Identificación de Tokens Generales:** Cuando una secuencia no corresponde a una palabra reservada, se clasifica automáticamente como un IDENTIFICADOR. Además, el lexer reconoce valores numéricos (NUMERO) y operadores relacionales (> y <) utilizados en los filtros de búsqueda.

### Estrategia del Parser LALR(1) (Parser)
El motor sintáctico se implementa utilizando la estrategia **LALR(1)** proporcionada por la biblioteca PLY (Python Lex-Yacc).
La elección de este enfoque se debe a que la gramática presenta producciones con prefijos comunes, particularmente en el no terminal *FILTRO*, lo que impide una resolución determinística mediante un parser LL(1).
* **Validación Sintáctica:** El parser recibe la secuencia de tokens generada por el lexer y verifica que cumpla con las producciones definidas en la gramática.
* **Manejo de Producciones Recursivas:** Las reglas RESTO_CONDICION y RESTO_NOMBRE permiten reconocer consultas con múltiples filtros y nombres compuestos, manteniendo una estructura flexible y cercana al lenguaje natural.

---

## 3. Estrategia de Robustez frente a Fallas

El sistema incorpora mecanismos de detección de errores tanto en la fase léxica como en la fase sintáctica, permitiendo informar al usuario cuando la consulta ingresada no cumple con las reglas del lenguaje.

1. **Error Léxico:** Si se detecta un carácter que no pertenece al lenguaje definido, el analizador léxico informa el error y continúa con el procesamiento del resto de la entrada.

2. **Error Sintáctico:** Si la secuencia de tokens generada por el lexer no respeta la estructura definida por la gramática, el parser informa el token inesperado y la línea donde se produjo el error.

---

## 4. Instalación y Uso

### Requisitos previos
Es necesario contar con Python y la librería `ply` instalada:
```bash
pip install ply
```

### Ejecución
Para probar el analizador léxico:
```bash
python lexer.py
```
Para probar el analizador sintáctico:
```bash
python parser.py
```

---

## Colaboradores
* Priscila Rodríguez
* Facundo Nicolás Fernández
* Ignacio Roch
* Adela Díaz
* Wilson Alexis Cabrera 
