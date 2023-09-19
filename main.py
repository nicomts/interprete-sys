from tests import *

# test_analizador_lexico('test.txt')
# test_analizador_lexico('test2.txt')
# test_analizador_sintactico('test2.txt')

# test_analizador_sintactico('suma.txt')

# <Declaraciones> ::= "var" <ListaVariables> | ε
def eval_declaraciones(arbol, estado):
    if len(arbol.hijos) > 0:
        estado = eval_lista_variables(arbol.hijos[1], estado)

    return estado

# <ListaVariables> ::= "id" <FinListaVariables>
def eval_lista_variables(arbol, estado):
    estado[arbol.hijos[0].lexema] = 0.0
    estado = eval_fin_lista_variables(arbol.hijos[1], estado)
    return estado

# <FinListaVariables> ::= "," "id" <FinListaVariables> | epsilon
def eval_fin_lista_variables(arbol, estado):
    if len(arbol.hijos) > 0:
        estado[arbol.hijos[1].lexema] = 0.0
        estado = eval_fin_lista_variables(arbol.hijos[2], estado)
    return estado

# <Cuerpo> ::= "{" <ListaSentencias> "}"

# <Programa> ::= <Declaraciones> <Cuerpo>
def eval_programa(arbol, estado):
    estado = eval_declaraciones(arbol.hijos[0], estado)
    estado = eval_cuerpo(arbol.hijos[1], estado)

def evaluador_semantico(arbol):
    estado = {}
    eval_programa(arbol, estado)

def interprete(ruta_archivo):
    a = analizador_sintactico(ruta_archivo)
    arbol_derivacion = a[0]
    exito = a[1]
    error = a[2]
    arbol_derivacion.imprimir()
    if exito:
        print('Éxito')
        evaluador_semantico(arbol_derivacion)
    if error:
        print('Error')