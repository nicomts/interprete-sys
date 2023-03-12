
def crear_tabla(tabla):
    instalar_en_tabla(tabla, 'var', 'var')
    instalar_en_tabla(tabla, 'read', 'read')
    instalar_en_tabla(tabla, 'write', 'write')
    instalar_en_tabla(tabla, 'if', 'if')
    instalar_en_tabla(tabla, 'else', 'else')
    instalar_en_tabla(tabla, 'while', 'while')
    instalar_en_tabla(tabla, 'not', 'not')
    instalar_en_tabla(tabla, 'and', 'and')
    instalar_en_tabla(tabla, 'or', 'or')


def instalar_en_tabla(tabla, componente_lexico, lexema):
    elemento = {'componente_lexico': componente_lexico, 'lexema': lexema}
    if not (elemento in tabla):
        tabla.append(elemento)
