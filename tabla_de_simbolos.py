
def crear_tabla(tabla):
    instalar_en_tabla(tabla, 'var', 'var')


def instalar_en_tabla(tabla, componente_lexico, lexema):
    elemento = {'componente_lexico': componente_lexico, 'lexema': lexema}
    if not (elemento in tabla):
        tabla.append(elemento)
