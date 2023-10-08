from tests import *

# test_analizador_lexico('test.txt')
# test_analizador_lexico('test2.txt')
# test_analizador_sintactico('test2.txt')

test_analizador_sintactico('suma.txt')

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
def eval_cuerpo(arbol, estado):
    estado = eval_lista_sentencias(arbol.hijos[1], estado)
    return estado

# <ListaSentencias> ::= <Sentencia> ";" <ListaSentenciasFin>
def eval_lista_sentencias(arbol, estado):
    estado = eval_sentencia(arbol.hijos[0], estado)
    estado = eval_lista_sentencias_fin(arbol.hijos[2], estado)
    return estado

# <ListaSentenciasFin> ::= <Sentencia> ";" <ListaSentenciasFin> | epsilon
def eval_lista_sentencias_fin(arbol, estado):
    if len(arbol.hijos) > 0:
        estado = eval_sentencia(arbol.hijos[0], estado)
        estado = eval_lista_sentencias_fin(arbol.hijos[2], estado)
    return estado

# <Sentencia> ::= <Asignacion> | <Lectura> | <Escritura> | <Condicional> | <CicloMientras>
def eval_sentencia(arbol, estado):
    if arbol.hijos[0].valor == '<Asignacion>':
        estado = eval_asignacion(arbol.hijos[0], estado)
    elif arbol.hijos[0].valor == '<Lectura>':
        estado = eval_asignacion(arbol.hijos[0], estado)
    elif arbol.hijos[0].valor == '<Escritura>':
        estado = eval_asignacion(arbol.hijos[0], estado)
    elif arbol.hijos[0].valor == '<Condicional>':
        estado = eval_asignacion(arbol.hijos[0], estado)
    elif arbol.hijos[0].valor == '<CicloMientras>':
        estado = eval_asignacion(arbol.hijos[0], estado)
    return estado



# <Asignacion> ::= "id" "operadorAsignacion" <ExpresionAritmetica>
def eval_asignacion(arbol, estado):
    estado, resultado = eval_expresion_aritmetica(arbol.hijos[2], estado)
    estado[arbol.hijos[0].lexema] = resultado
    return estado

# <ExpresionAritmetica> ::= <OperandoSumaResta> <OperacionSumaResta>
def eval_expresion_aritmetica(arbol, estado):
    estado = eval_operando_suma_resta(arbol.hijos[0], estado)
    estado = eval_operacion_suma_resta(arbol.hijos[1], estado)
    return estado, resultado

# <OperacionSumaResta> ::= "+" <OperandoSumaResta> <OperacionSumaResta> | "-" <OperandoSumaResta> <OperacionSumaResta> | epsilon


# <OperandoSumaResta> ::= <OperandoMultiplicacionDivision> <OperacionMultiplicacionDivision>
def eval_operando_suma_resta(arbol, estado):
    estado = eval_operando_multiplicacion_division(arbol.hijos[0], estado)
    estado = eval_operacion_multiplicacion_division(arbol.hijos[1], estado)
    return estado


# <OperacionMultiplicacionDivision> ::= "*" <OperandoMultiplicacionDivision> <OperacionMultiplicacionDivision> | "/" <OperandoMultiplicacionDivision> <OperacionMultiplicacionDivision> | epsilon


# <OperandoMultiplicacionDivision> ::= <OperandoPotenciaRaiz> <OperacionPotenciaRaiz>
def eval_operando_multiplicacion_division(arbol, estado):
    estado = eval_operando_potencia_raiz(arbol.hijos[0], estado)
    estado = eval_operacion_potencia_raiz(arbol.hijos[1], estado)
    return estado


# <OperacionPotenciaRaiz> ::= "**" <OperandoPotenciaRaiz> <OperacionPotenciaRaiz> | "*/" <OperandoPotenciaRaiz> <OperacionPotenciaRaiz> | epsilon
def eval_operacion_potencia_raiz(arbol, estado, resultado):
    while len(arbol.hijos) > 0:
        if arbol.hijos[0].valor == '**':
            # placeholder
        elif arbol.hijos[0].valor == '*/':
            # placeholder

# <OperandoPotenciaRaiz> ::= "(" <ExpresionAritmetica> ")" | "id" | "constanteReal" | "-" <OperandoPotenciaRaiz>
def eval_operando_potencia_raiz(arbol, estado, resultado):
    if arbol.hijos[0].valor == '(':
        estado, resultado = eval_expresion_aritmetica(arbol.hijos[1], estado)
    elif arbol.hijos[0].valor == 'id':
        resultado = estado[arbol.hijos[0].lexema]
    elif arbol.hijos[0].valor == 'constanteReal':
        resultado = estado[arbol.hijos[0].lexema]
    elif arbol.hijos[0].valor == '-':
        estado, resultado_potencia_raiz = eval_expresion_aritmetica(arbol.hijos[1], estado, resultado)
        resultado = resultado - resultado_potencia_raiz
    return estado, resultado



# <Lectura> ::= "read" "(" "Cadena" "," "id" ")"
# <Escritura> ::= "write" "(" "Cadena" "," <ExpresionAritmetica> ")"
# <Condicional> ::= "if" <Condicion> <Cuerpo> <FinCondicional>
# <FinCondicional> ::= "else" <Cuerpo> | epsilon
# <Condicion> ::= <OperandoAndOr> <OperacionAndOr>
# <OperacionAndOr> ::= "or" <OperandoAndOr> <OperacionAndOr> | "and" <OperandoAndOr> <OperacionAndOr> | epsilon
# <OperandoAndOr> ::= <ExpresionAritmetica> "operadorRelacional" <ExpresionAritmetica> | "not" <OperandoAndOr> | "[" <Condicion> "]"
# <CicloMientras> ::= "while" <Condicion> <Cuerpo>






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