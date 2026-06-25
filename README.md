# Lenguaje de Consultas para Productos e Inventario

Este proyecto implementa un **analizador léxico y sintáctico** junto con la generación de un **Árbol Sintáctico Abstracto (AST)** utilizando la librería **PLY (Python Lex-Yacc)**.

Forma parte de la asignatura *Teoría de la Computación*.

---

## 1. Estructura del proyecto

- `lexer.py` → Analizador léxico (tokens)  
- `parser.py` → Analizador sintáctico + generación de AST  
- `main.py` → Ejecución automática de casos de prueba
- `TC-FRCCRD-LenguajeConsultasInventario.pdf` → Informe técnico

---

## 2. Instalación y Uso

### Requisitos previos
Es necesario contar con Python y la librería `ply` instalada:
```bash
pip install ply
```

### Ejecución del proyecto
Para ejecutar el sistema completo con pruebas automáticas:
```bash
python main.py
```

Para probar el analizador léxico:
```bash
python lexer.py
```

Para probar el analizador sintáctico:
```bash
python parser.py
```

---

## Integrantes
* Priscila Rodríguez
* Facundo Nicolás Fernández
* Ignacio Roch
* Adela Díaz
* Wilson Alexis Cabrera 
* Claudio Castillo
