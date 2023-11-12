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
        estado = eval_lectura(arbol.hijos[0], estado)
    elif arbol.hijos[0].valor == '<Escritura>':
        estado = eval_escritura(arbol.hijos[0], estado)
    elif arbol.hijos[0].valor == '<Condicional>':
        estado = eval_condicional(arbol.hijos[0], estado)
    elif arbol.hijos[0].valor == '<CicloMientras>':
        estado = eval_ciclo_mientras(arbol.hijos[0], estado)
    return estado



# <Asignacion> ::= "id" "operadorAsignacion" <ExpresionAritmetica>
def eval_asignacion(arbol, estado):

    estado, resultado = eval_expresion_aritmetica(arbol.hijos[2], estado)
    estado[arbol.hijos[0].lexema] = resultado
    return estado

# <ExpresionAritmetica> ::= <OperandoSumaResta> <OperacionSumaResta>
def eval_expresion_aritmetica(arbol, estado):
    estado, operando1 = eval_operando_suma_resta(arbol.hijos[0], estado)
    estado, resultado = eval_operacion_suma_resta(arbol.hijos[1], estado, operando1)
    return estado, resultado

# <OperacionSumaResta> ::= "+" <OperandoSumaResta> <OperacionSumaResta> | "-" <OperandoSumaResta> <OperacionSumaResta> | epsilon
def eval_operacion_suma_resta(arbol, estado, operando1):
    if len(arbol.hijos) > 0:
        estado, operando2 = eval_operando_suma_resta(arbol.hijos[1], estado)
        if arbol.hijos[0].valor == '+':
            suma_parcial = operando1 + operando2
        elif arbol.hijos[0].valor == '-':
            suma_parcial = operando1 - operando2
        estado, resultado = eval_operacion_suma_resta(arbol.hijos[2], estado, suma_parcial)
        return estado, resultado
    else:
        return estado, operando1

# <OperandoSumaResta> ::= <OperandoMultiplicacionDivision> <OperacionMultiplicacionDivision>
def eval_operando_suma_resta(arbol, estado):
    estado, operando1 = eval_operando_multiplicacion_division(arbol.hijos[0], estado)
    estado, resultado = eval_operacion_multiplicacion_division(arbol.hijos[1], estado, operando1)
    return estado, resultado


# <OperacionMultiplicacionDivision> ::= "*" <OperandoMultiplicacionDivision> <OperacionMultiplicacionDivision> | "/" <OperandoMultiplicacionDivision> <OperacionMultiplicacionDivision> | epsilon
def eval_operacion_multiplicacion_division(arbol, estado, operando1):
    if len(arbol.hijos) > 0:
        estado, operando2 = eval_operando_multiplicacion_division(arbol.hijos[1], estado)
        if arbol.hijos[0].valor == '*':
            operacion_parcial = operando1 * operando2
        elif arbol.hijos[0].valor == '/':
            operacion_parcial = operando1 / operando2
        estado, resultado = eval_operacion_multiplicacion_division(arbol.hijos[2], estado, operacion_parcial)
        return estado, resultado
    else:
        return estado, operando1


# <OperandoMultiplicacionDivision> ::= <OperandoPotenciaRaiz> <OperacionPotenciaRaiz>
def eval_operando_multiplicacion_division(arbol, estado):
    estado, operando1 = eval_operando_potencia_raiz(arbol.hijos[0], estado)
    estado, resultado = eval_operacion_potencia_raiz(arbol.hijos[1], estado, operando1)
    return estado, resultado


# <OperacionPotenciaRaiz> ::= "**" <OperandoPotenciaRaiz> <OperacionPotenciaRaiz> | "*/" <OperandoPotenciaRaiz> <OperacionPotenciaRaiz> | epsilon
def eval_operacion_potencia_raiz(arbol, estado, operando1):
    if len(arbol.hijos) > 0:
        estado, operando2 = eval_operando_potencia_raiz(arbol.hijos[1], estado)
        if arbol.hijos[0].valor == '**':
            operacion_parcial = pow(operando1, operando2)
        elif arbol.hijos[0].valor == '*/':
            operacion_parcial = pow(operando1, (1/operando2))
        estado, resultado = eval_operacion_potencia_raiz(arbol.hijos[2], estado, operacion_parcial)
        return estado, resultado
    else:
        return estado, operando1

# <OperandoPotenciaRaiz> ::= "(" <ExpresionAritmetica> ")" | "id" | "constanteReal" | "-" <OperandoPotenciaRaiz>
def eval_operando_potencia_raiz(arbol, estado):
    if arbol.hijos[0].valor == '(':
        estado, resultado = eval_expresion_aritmetica(arbol.hijos[1], estado)
    elif arbol.hijos[0].valor == 'id':
        resultado = float(estado[arbol.hijos[0].lexema])
    elif arbol.hijos[0].valor == 'constanteReal':
        resultado = float(arbol.hijos[0].lexema)
    elif arbol.hijos[0].valor == '-':
        estado, resultado_potencia_raiz = eval_operando_potencia_raiz(arbol.hijos[1], estado)
        resultado = -1 * resultado_potencia_raiz
    return estado, resultado



# <Lectura> ::= "read" "(" "Cadena" "," "id" ")"
def eval_lectura(arbol, estado):
    estado[arbol.hijos[4].lexema] = input(arbol.hijos[2].lexema)
    return estado

# <Escritura> ::= "write" "(" "Cadena" "," <ExpresionAritmetica> ")"
def eval_escritura(arbol, estado):
    estado, resultado = eval_expresion_aritmetica(arbol.hijos[4], estado)
    print(arbol.hijos[2].lexema + str(resultado))
    return estado



# <Condicional> ::= "if" <Condicion> <Cuerpo> <FinCondicional>
def eval_condicional(arbol, estado):
    estado, condicion = eval_condicion(arbol.hijos[1], estado)
    if condicion:
        estado = eval_cuerpo(arbol.hijos[2], estado)
    else:
        estado = eval_fin_condicional(arbol.hijos[3], estado)
    return estado

# <FinCondicional> ::= "else" <Cuerpo> | epsilon
def eval_fin_condicional(arbol, estado):
    if len(arbol.hijos) > 0:
        estado = eval_cuerpo(arbol.hijos[1], estado)
    return estado

# <Condicion> ::= <OperandoAndOr> <OperacionAndOr>
def eval_condicion(arbol, estado):
    estado, operando1 = eval_operando_and_or(arbol.hijos[0], estado)
    estado, condicion = eval_operacion_and_or(arbol.hijos[1], estado, operando1)
    return estado, condicion

# <OperacionAndOr> ::= "or" <OperandoAndOr> <OperacionAndOr> | "and" <OperandoAndOr> <OperacionAndOr> | epsilon
def eval_operacion_and_or(arbol, estado, operando1):
    if len(arbol.hijos) > 0:
        estado, operando2 = eval_operando_and_or(arbol.hijos[1], estado)
        if arbol.hijos[0].valor == 'or':
            operacion_parcial = operando1 or operando2
        elif arbol.hijos[0].valor == 'and':
            operacion_parcial = operando1 and operando2
        estado, resultado = eval_operacion_and_or(arbol.hijos[2], estado, operacion_parcial)
        return estado, resultado
    else:
        return estado, operando1


# <OperandoAndOr> ::= <ExpresionAritmetica> "operadorRelacional" <ExpresionAritmetica> | "not" <OperandoAndOr> | "[" <Condicion> "]"
def eval_operando_and_or(arbol, estado):
    if arbol.hijos[0].valor == '<ExpresionAritmetica>': # controlar esto
        estado, exp1 = eval_expresion_aritmetica(arbol.hijos[0], estado)
        estado, exp2 = eval_expresion_aritmetica(arbol.hijos[2], estado)
        if arbol.hijos[1].lexema == '>':
            condicion = exp1 > exp2
        elif arbol.hijos[1].lexema == '<':
            condicion = exp1 < exp2
        elif arbol.hijos[1].lexema == '==':
            condicion = exp1 == exp2
        elif arbol.hijos[1].lexema == '<=':
            condicion = exp1 <= exp2
        elif arbol.hijos[1].lexema == '>=':
            condicion = exp1 >= exp2
        elif arbol.hijos[1].lexema == '<>':
            condicion = exp1 != exp2

    elif arbol.hijos[0].valor == 'not':
        estado, condicion = eval_operando_and_or(arbol.hijos[1], estado)
        condicion = not condicion

    elif arbol.hijos[0].valor == '[':
        estado, condicion = eval_condicion(arbol.hijos[1], estado)
    return estado, condicion


# <CicloMientras> ::= "while" <Condicion> <Cuerpo>
def eval_ciclo_mientras(arbol, estado):
    estado, condicion = eval_condicion(arbol.hijos[1], estado)
    while condicion:
        estado = eval_cuerpo(arbol.hijos[2], estado)
        estado, condicion = eval_condicion(arbol.hijos[1], estado)
    return estado






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

interprete('programas/mcm.txt')