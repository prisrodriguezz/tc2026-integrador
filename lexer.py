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

# Operadores
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'

t_ignore = ' \t'

# Manejo de errores


# Logica de tokens

# Construccion del lexer
lexer = lex.lex()