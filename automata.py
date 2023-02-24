import re


def es_real(cadena):
    def caracter_a_simbolo(caracter):
        es_digito = re.search('[0-9]', caracter)  # this regular expresion returns true if the character is a digit

        if caracter == '.':
            return 'punto'
        elif es_digito:
            return 'digito'
        else:
            return 'otro'

    estado_inicial = 0
    estados_finales = [1, 4]

    control = 0
    estado_actual = estado_inicial

    # This is the definition of the delta function(transitions) as a matrix of python dictionaries:
    delta = {0: {'digito': 1, 'otro': 2, 'punto': 2},  # from state 0 through digito you go to state 1
             1: {'digito': 1, 'otro': 2, 'punto': 3},
             2: {'digito': 2, 'otro': 2, 'punto': 2},
             3: {'digito': 4, 'otro': 2, 'punto': 2},
             4: {'digito': 4, 'otro': 2, 'punto': 2}}

    for i in range(len(cadena)):
        aux = caracter_a_simbolo(cadena[control])
        estado_actual = delta[estado_actual][aux]
        control += 1
    if estado_actual in estados_finales:
        cadena_aceptada = True
        return cadena_aceptada

