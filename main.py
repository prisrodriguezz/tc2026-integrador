from lexer import lexer
from parser import parser
import json

# Casos de prueba
casos_prueba = [

    # Casos validos
    ("buscar producto mate imperial", "Valida", "Nombre compuesto"),
    ("ver stock yerba mate", "Valida", "Consulta de stock"),
    ("mostrar productos sin stock", "Valida", "Filtro simple"),
    ("mostrar productos con stock", "Valida", "Filtro simple"),
    ("mostrar productos con precio > 5000", "Valida", "Comparador mayor"),
    ("mostrar productos con precio < 20000", "Valida", "Comparador menor"),
    ("mostrar productos de categoria mates y con stock", "Valida", "Conector Y"),
    ("mostrar productos sin stock o con precio < 1000", "Valida", "Conector O"),

    # Casos invalidos
    ("mostrar productos con precio 5000", "Invalida", "Falta comparador"),
    ("ver producto mate", "Invalida", "Comando no definido"),
    ("mostrar productos de categoria", "Invalida", "Falta nombre")
]

print("=" * 80)
print("EJECUCION AUTOMATICA DE CASOS DE PRUEBA")
print("=" * 80)

for i, (entrada, esperado, cobertura) in enumerate(casos_prueba, start=1):

    print(f"\nCaso {i}")
    print(f"Entrada: {entrada}")
    print(f"Esperado: {esperado}")
    print(f"Cobertura: {cobertura}")

    try:
        resultado = parser.parse(entrada, lexer=lexer)

        if resultado:
            obtenido = "Valida"
            print("Resultado: ✓ Consulta valida")

            print("AST:")
            print(json.dumps(resultado, indent=2, ensure_ascii=False))

        else:
            obtenido = "Invalida"
            print("Resultado: ✗ Consulta invalida")

        if obtenido == esperado:
            print("Estado: ✓")
        else:
            print("Estado: ✗")

    except Exception as e:
        print(f"Error durante el analisis: {e}")

        if esperado == "Invalida":
            print("Estado: ✓")
        else:
            print("Estado: ✗")

print("\n" + "=" * 80)
print("FIN DE LAS PRUEBAS")
print("=" * 80)