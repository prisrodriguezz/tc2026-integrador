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

# -------------------------
# LOGICA DE TOKENS
# -------------------------
# Números
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t
    
# Identificadores y palabras reservadas
def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value.lower(), 'IDENTIFICADOR')
    return t
    
# Saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Carácter no valido '{t.value[0]}'")
    t.lexer.skip(1)
    
# Construccion del lexer
lexer = lex.lex()
