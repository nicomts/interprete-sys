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
        transicion = caracter_a_simbolo(cadena[control])
        estado_actual = delta[estado_actual][transicion]
        control += 1
    if estado_actual in estados_finales:
        cadena_aceptada = True
        return cadena_aceptada


def es_identificador(fuente, control, lexema):

    # rules: identificador always starts with a letter, the rest can be letters or digits, no special symbols (not even _)
    def caracter_a_simbolo(caracter):
        es_digito = re.search('[0-9]', caracter)
        es_letra = re.search('[a-zA-Z]', caracter)

        if es_letra:
            return 'letra'
        elif es_digito:
            return 'digito'
        else:
            return 'otro'

    estado_inicial = 0
    estados_finales = [2]
    estado_salida = 3

    control_local = control
    estado_actual = estado_inicial

    # State 3 is the exit state, it marks the end of the identifier recognized
    delta = {0: {'letra': 2, 'digito': 1, 'otro': 1},
             1: {'letra': 1, 'digito': 1, 'otro': 1},
             2: {'letra': 2, 'digito': 2, 'otro': 3},
             3: {'letra': 3, 'digito': 3, 'otro': 3}
             }

    while not (estado_actual == estado_salida):
        try:
            caracter_automata = fuente[control_local]
            transicion = caracter_a_simbolo(caracter_automata)
            estado_actual = delta[estado_actual][transicion]
            if estado_actual in estados_finales:
                lexema = lexema + caracter_automata
        except IndexError:
            print('End of file in automaton')
            break

        control_local += 1
    if (estado_actual in estados_finales or estado_actual == estado_salida):
        cadena_aceptada = True
        control = control + control_local
        return [cadena_aceptada, control, lexema]


def obtener_siguiente_componente_lexico (fuente, control):
    fin_de_archivo = False
    lexema = ''
    try:
        caracter = fuente[control]
        while ord(caracter) in range(33): # this will skip control characters (blank spaces)
            control += 1
            caracter = fuente[control]


    except IndexError: # This will return end of file if the index of the array is out of range
        fin_de_archivo = True

    if fin_de_archivo == True:
        print('Fin de archivo')
    else:
        es_id = es_identificador(fuente, control, lexema)
        if es_id[0] == True:
            print('Identificador reconocido')
            componente_lexico = 'Identificador'
            control = es_id[1]
            lexema = es_id[2]
            print(componente_lexico + ': ' + lexema)

            # instalar_en_ts(lexema, tabla_de_simbolos, componente_lexico)
        else:
            print('No reconocio nada mas')
        # elif not es_simbolo_especial(fuente, control, lexema, componente_lexico):
        #     componente_lexico = 'error lexico'

    return control







ruta_archivo = 'test.txt'
archivo = open(ruta_archivo)
fuente = archivo.read()
control = 0
control = obtener_siguiente_componente_lexico(fuente, control)
control = obtener_siguiente_componente_lexico(fuente, control)