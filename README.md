# Lenguaje de Consultas Ágiles para Logística e Inventario (DSL)

Este repositorio contiene la implementación de un motor léxico y sintáctico para un Lenguaje de Dominio Específico (DSL) diseñado para optimizar y agilizar las consultas en sistemas de logística e inventario. El desarrollo está construido en Python utilizando la librería **PLY (Python Lex-Yacc)**.

---

## 1. Definición Formal de la Gramática

La estructura sintáctica definitiva de este DSL se formaliza mediante una Gramática Libre de Contexto (CFG), compuesta por la tupla G = (N, T, P, S):

### Símbolos No Terminales (N)
* N = { S, ENTIDAD, WHERE, CONDICION, COND_LOGICA, EXPRESION, OPERADOR, VALOR }

### Símbolos Terminales (T)
* T = { BUSCAR, DONDE, Y, O, ES, MAYOR_A, MENOR_A, IDENTIFICADOR, STRING, NUMERO }

### Conjunto de Producciones (P)

* S -> BUSCAR ENTIDAD WHERE
* WHERE -> DONDE CONDICION | lambda
* CONDICION -> EXPRESION COND_LOGICA
* COND_LOGICA -> Y EXPRESION COND_LOGICA | O EXPRESION COND_LOGICA | lambda
* EXPRESION -> IDENTIFICADOR OPERADOR VALOR
* OPERADOR -> ES | MAYOR_A | MENOR_A
* VALOR -> STRING | NUMERO
* ENTIDAD -> IDENTIFICADOR

*(Nota: Las conectivas lógicas aplican recursión por derecha para permitir el encadenamiento de múltiples condiciones de filtrado sin generar conflictos de recursión a la izquierda en el analizador sintáctico descendente).*

### Símbolo Distinguido (S)
* S es el axioma inicial de la gramática, donde S pertenece al conjunto N.

---

## 2. Análisis Arquitectural y Justificación del Motor

El diseño del intérprete sigue un paradigma modular estricto, separando el análisis en dos fases secuenciales:

### Flujo de Procesamiento Léxico (Lexer)
El analizador léxico actúa como la primera barrera del intérprete utilizando una estrategia de punteros dinámicos (posición y lectura anticipada) junto con expresiones regulares:
* **Manejo de Literales Complejos:** Se implementa un algoritmo de emparejamiento por comillas para aislar cadenas de texto que contienen espacios (por ejemplo, categorías de productos o talles con texto compuesto), evitando alterar o normalizar la entrada antes del procesamiento.
* **Clasificación de Palabras Reservadas:** Para evitar ambigüedades, las secuencias alfanuméricas continuas se contrastan primero contra un diccionario de palabras clave (`BUSCAR`, `DONDE`, `Y`, `O`, `ES`). Si no hay coincidencia, el token se cataloga automáticamente como un `IDENTIFICADOR`.

### Estrategia del Parser Descendente Recursivo (Parser)
El motor sintáctico ha sido modelado bajo un enfoque predictivo **LL(1)**. Gracias al diseño de la gramática con recursión por derecha, la transición a funciones nativas es directa:
* **Función de Coincidencia (Match):** Centraliza el control de flujo sintáctico. Si el token provisto por el lexer coincide con el token de anticipación (`lookahead`) esperado por la producción, se consume el elemento; en caso contrario, se interrumpe la ejecución de forma controlada.
* **Resolución de la Ambigüedad:** La regla encargada de procesar las compuertas lógicas (`COND_LOGICA`) se invoca recursivamente a sí misma tras consumir un operador. El ciclo de validación finaliza con éxito mediante una bifurcación que emula la producción vacía (lambda) al alcanzar el fin de archivo (EOF).

---

## 3. Estrategia de Robustez frente a Fallas

El sistema envuelve el proceso de interpretación dentro de un entorno controlado de excepciones para diferenciar con precisión la naturaleza de los errores:
1. **Error Léxico:** Si el usuario ingresa un carácter inválido que no pertenece al alfabeto del lenguaje, el sistema aborta inmediatamente en la fase léxica.
2. **Error Sintáctico:** Si los componentes son válidos pero alteran el orden jerárquico establecido por las producciones, el parser captura la anomalía y dispara un reporte detallado que especifica el token esperado y la ubicación exacta del fallo.

---

## 4. Instalación y Uso

### Requisitos previos
Es necesario contar con Python y la librería `ply` instalada:
```bash
pip install ply
```

### Ejecución
Para iniciar el entorno y evaluar las consultas del DSL, ejecute el archivo principal:
```bash
python main.py
```

---

## Colaboradores
* Priscila Rodríguez
* Facundo Nicolás Fernández
* Ignacio Roch
* Ade Díaz
* Wilson Alexis Cabrera 