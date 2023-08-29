from analizador_sintactico import *
import analizador_lexico
import tabla_de_simbolos


def test_analizador_sintactico(ruta_archivo):
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


def test_analizador_lexico(ruta_archivo):
    archivo = open(ruta_archivo)
    fuente = archivo.read()
    control_global = 0
    tabla = []
    tabla_de_simbolos.crear_tabla(tabla)
    for i in range(100):
        aux = analizador_lexico.obtener_siguiente_componente_lexico(fuente, control_global, tabla)
        control_global = aux[1]
        print(aux[0] + ': ' + aux[2])


test_analizador_lexico('test.txt')
test_analizador_lexico('test2.txt')

test_analizador_sintactico('test2.txt')
