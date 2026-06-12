import ply.yacc as yacc

# Importamos los tokens que definimos en el analizador léxico
from lexer import tokens 


# analizador sintatico (PARSER) y generacion del AST


def p_consulta(p):
    '''consulta : busqueda
                | stock'''
    # Nodo raíz del árbol sintáctico 
    p[0] = {'tipo': 'CONSULTA', 'valor': p[1]}

def p_busqueda(p):
    '''busqueda : BUSCAR PRODUCTO IDENTIFICADOR
                | MOSTRAR PRODUCTOS condicion'''
    # Usamos la palabra clave para distinguir qué tipo de búsqueda es.
    # Con lower() nos aseguramos de que funcione sin importar si el usuario usó mayúsculas.
    if p[1].lower() == 'buscar':
        p[0] = {'tipo': 'BUSQUEDA_SIMPLE', 'entidad': p[3]}
    else:
        # Si es "mostrar productos", enlazamos el sub-árbol de la condición
        p[0] = {'tipo': 'BUSQUEDA_FILTRADA', 'condicion': p[3]}

def p_stock(p):
    '''stock : VER STOCK IDENTIFICADOR'''
    # Nodo simple para la consulta directa de stock de un producto
    p[0] = {'tipo': 'CONSULTA_STOCK', 'entidad': p[3]}

def p_condicion(p):
    '''condicion : filtro resto_condicion'''
    # Armamos el nodo de condición uniendo el primer filtro con el resto de la recursividad
    p[0] = {'tipo': 'CONDICION', 'filtro': p[1], 'resto': p[2]}

def p_resto_condicion(p):
    '''resto_condicion : Y filtro resto_condicion
                       | empty'''
    # Si la longitud es 4, significa que entró por la primera regla (tiene operador 'Y')
    if len(p) == 4:
        p[0] = {'tipo': 'OPERADOR_LOGICO', 'operador': 'Y', 'filtro': p[2], 'resto': p[3]}
    else:
        # Derivación nula (lambda / epsilon). Corta la recursividad.
        p[0] = None

def p_filtro(p):
    '''filtro : SIN STOCK
              | CON STOCK
              | DE CATEGORIA IDENTIFICADOR
              | CON PRECIO comparador NUMERO'''
    
    # Clasificamos el tipo de filtro dependiendo de las palabras clave que se leyeron
    if p[1].lower() == 'sin' or (p[1].lower() == 'con' and p[2].lower() == 'stock'):
        p[0] = {'tipo': 'FILTRO_STOCK', 'valor': f'{p[1]} {p[2]}'}
    elif p[1].lower() == 'de':
        p[0] = {'tipo': 'FILTRO_CATEGORIA', 'valor': p[3]}
    else:
        # Si no es stock ni categoría, por descarte es el filtro de precio
        p[0] = {'tipo': 'FILTRO_PRECIO', 'comparador': p[3], 'valor': p[4]}

def p_comparador(p):
    '''comparador : MAYOR_QUE
                  | MENOR_QUE'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    # Función de ayuda para representar a lambda (cadena vacía) en PLY
    pass


#manejo de errores

def p_error(p):
    if p:
        print(f"Error Sintáctico: Token inesperado '{p.value}' en la línea {p.lineno}")
    else:
        print("Error Sintáctico: Fin de archivo inesperado. Faltan tokens por analizar.")

# Instanciamos el parser
parser = yacc.yacc()

#pruebas

if __name__ == '__main__':
    from lexer import lexer
    
    # Cadena de entrada de prueba con recursividad
    data = "mostrar productos con precio < 15000 y de categoria oversize"
    
    print(f"Analizando cadena: '{data}'\n")
    # Le pasamos el lexer a mi parser para que trabaje sobre los tokens
    ast = parser.parse(data, lexer=lexer)
    
    # Si la validación es exitosa, formateamos e imprimimos el AST como un JSON
    if ast:
        import json
        print("Sintaxis válida. Árbol Sintáctico Abstracto (AST) generado:")
        print(json.dumps(ast, indent=2, ensure_ascii=False))