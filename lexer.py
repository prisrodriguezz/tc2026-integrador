import ply.lex as lex

# Lista de Tokens
tokens = (
    'BUSCAR',
    'PRODUCTO',
    'MOSTRAR',
    'PRODUCTOS',
    'VER',
    'STOCK',
    'SIN',
    'CON',
    'DE',
    'CATEGORIA',
    'PRECIO',
    'Y',
    'MAYOR_QUE',
    'MENOR_QUE',
    'IDENTIFICADOR',
    'NUMERO'
)

# Palabras reservadas
reservadas = {
    'buscar': 'BUSCAR',
    'producto': 'PRODUCTO',
    'mostrar': 'MOSTRAR',
    'productos': 'PRODUCTOS',
    'ver': 'VER',
    'stock': 'STOCK',
    'sin': 'SIN',
    'con': 'CON',
    'de': 'DE',
    'categoria': 'CATEGORIA',
    'precio': 'PRECIO',
    'y': 'Y',
    'mayor': 'MAYOR',
    'menor': 'MENOR',
    'a': 'A'
}
# Operadores
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'

t_ignore = ' \t'

# Manejo de errores


# Logica de tokens

# Construccion del lexer
lexer = lex.lex()
