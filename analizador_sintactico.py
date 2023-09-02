import analizador_lexico
import tabla_de_simbolos
import arbol
from tas import *
from componentes_lexicos import *


def analizador_sintactico(ruta_archivo):
    archivo = open(ruta_archivo)
    fuente = archivo.read()
    control = 0
    tabla = []
    tabla_de_simbolos.crear_tabla(tabla)
    pila = [arbol.NodoArbol('$')]
    raiz = arbol.NodoArbol('<Programa>')
    pila.append(raiz)
    exito = False
    error = False
    a = analizador_lexico.obtener_siguiente_componente_lexico(fuente, control, tabla)

    while not exito and not error:
        x = pila.pop()
        if x.valor in terminales:
            if x.valor == a[0]:
                control = a[1]
                a = analizador_lexico.obtener_siguiente_componente_lexico(fuente, control, tabla)
            else:
                error = True
        elif x.valor in variables:
            if a[0] not in tas[x.valor]:
                error = True
            else:
                nueva_lista = []
                for i in tas[x.valor][a[0]]:
                    nuevo_nodo = arbol.NodoArbol(i)
                    x.hijos.append(nuevo_nodo)
                    nueva_lista.append(nuevo_nodo)
                for i in reversed(nueva_lista):
                    nodo = nueva_lista.pop()
                    pila.append(nodo)


            # else:
            #     for i in reversed(tas[x.valor][a[0]]):
            #         nuevo_nodo = arbol.NodoArbol(i)
            #         pila.append(nuevo_nodo)
            #     for i in tas[x.valor][a[0]]:
            #         nuevo_nodo = arbol.NodoArbol(i)
            #         x.hijos.append(nuevo_nodo)

        elif x.valor == '$':
            exito = True

    return [raiz, exito, error]
