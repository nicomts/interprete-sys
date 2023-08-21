from analizador_sintactico import *


def test_analizador_sintactico():
    ruta_archivo = 'test2.txt'
    a = analizador_sintactico(ruta_archivo)
    arbol_derivacion = a[0]
    exito = a[1]
    error = a[2]

    def dfs(nodo):
        print(nodo.valor)
        for hijo in nodo.hijos:
            dfs(hijo)

    dfs(arbol_derivacion)

    if exito:
        print('Exito')
    if error:
        print('Error')


test_analizador_sintactico()


# import analizador_lexico, tabla_de_simbolos
#
# ruta_archivo = 'test.txt'
# archivo = open(ruta_archivo)
# fuente = archivo.read()
# control_global = 0
# tabla = []
# tabla_de_simbolos.crear_tabla(tabla)
# for i in range(14):
#     aux = analizador_lexico.obtener_siguiente_componente_lexico(fuente, control_global, tabla)
#     control_global = aux[1]
#     print(aux[0] + ': ' + aux[2])
#

# tabla = []
# componente_lexico = 'identificador'
# lexema = 'variable1'
#
# tabla_de_simbolos.crear_tabla(tabla)
# tabla_de_simbolos.instalar_en_tabla(tabla, componente_lexico, lexema)
