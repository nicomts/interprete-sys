import re
import tabla_de_simbolos

# re is the regular expression module
# ord() function returns the value of the character in the ascii table


def es_real(fuente, control, lexema):
    cadena_aceptada = False
    def caracter_a_simbolo(caracter):
        es_digito = re.search('[0-9]', caracter)  # this regular expression returns true if the character is a digit

        if caracter == '.':
            return 'punto'
        elif caracter == '-' or caracter == '+':
            return 'signo'
        elif es_digito:
            return 'digito'
        else:
            return 'otro'

    estado_inicial = 0
    estados_finales = [1, 4]
    estado_salida = 5

    control_local = control
    estado_actual = estado_inicial

    # This is the definition of the delta function(transitions) as a matrix of python dictionaries:
    delta = {0: {'digito': 1, 'otro': 2, 'punto': 2, 'signo': 6},  # from state 0 through digito you go to state 1
             1: {'digito': 1, 'otro': 5, 'punto': 3, 'signo': 5},
             2: {'digito': 2, 'otro': 2, 'punto': 2, 'signo': 2},
             3: {'digito': 4, 'otro': 2, 'punto': 2, 'signo': 2},
             4: {'digito': 4, 'otro': 5, 'punto': 5, 'signo': 5},
             5: {'digito': 5, 'otro': 5, 'punto': 5, 'signo': 5},
             6: {'digito': 1, 'otro': 2, 'punto': 2, 'signo': 2}}

    while not estado_actual == estado_salida:
        try:
            caracter_automata = fuente[control_local]
            transicion = caracter_a_simbolo(caracter_automata)
            estado_actual = delta[estado_actual][transicion]

            # if i don't add 'estado_actual == 3' it won't add . to lexema
            if (estado_actual in estados_finales or estado_actual == 3 or estado_actual == 6):
                lexema = lexema + caracter_automata
            control_local += 1
        except IndexError:
            break

    if (estado_actual in estados_finales or estado_actual == estado_salida):
        cadena_aceptada = True
        control = control_local
    return [cadena_aceptada, control, lexema]



def es_identificador(fuente, control, lexema):
    cadena_aceptada = False
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
            break

        control_local += 1
    if (estado_actual in estados_finales or estado_actual == estado_salida):
        cadena_aceptada = True
        control = control_local
    return [cadena_aceptada, control, lexema]

def es_operador_relacional(fuente, control, lexema):
    cadena_aceptada = False
    def caracter_a_simbolo(caracter):
        if caracter == '<':
            return 'menor'
        elif caracter == '>':
            return 'mayor'
        elif caracter == '=':
            return 'igual'
        else:
            return 'otro'

    estado_inicial = 0
    estados_finales = [1, 2]
    estado_salida = 6

    control_local = control
    estado_actual = estado_inicial

    delta = {0: {'menor': 1, 'mayor': 4, 'igual': 3, 'otro': 5},
             1: {'menor': 6, 'mayor': 2, 'igual': 2, 'otro': 6},
             2: {'menor': 6, 'mayor': 6, 'igual': 6, 'otro': 6},
             3: {'menor': 5, 'mayor': 5, 'igual': 2, 'otro': 5},
             4: {'menor': 5, 'mayor': 5, 'igual': 2, 'otro': 5},
             5: {'menor': 5, 'mayor': 5, 'igual': 5, 'otro': 5},
             6: {'menor': 6, 'mayor': 6, 'igual': 6, 'otro': 6}}

    while not estado_actual == estado_salida:
        try:
            caracter_automata = fuente[control_local]
            transicion = caracter_a_simbolo(caracter_automata)
            estado_actual = delta[estado_actual][transicion]
            if estado_actual in estados_finales:
                lexema = lexema + caracter_automata
            control_local += 1
        except IndexError:
            break

    if (estado_actual in estados_finales or estado_actual == estado_salida):
        cadena_aceptada = True
        control = control_local
    return [cadena_aceptada, control, lexema]

def es_operador_aritmetico(fuente, control, lexema):
    cadena_aceptada = False
    def caracter_a_simbolo(caracter):
        if caracter == '+':
            return 'suma'
        elif caracter == '-':
            return 'resta'
        elif caracter == '*':
            return 'multiplicacion'
        elif caracter == '/':
            return 'division'
        else:
            return 'otro'

    estado_inicial = 0
    estados_finales = [1, 2, 4]
    estado_salida = 5

    control_local = control
    estado_actual = estado_inicial

    delta = {0: {'suma': 1, 'resta': 1, 'multiplicacion': 2, 'division': 1, 'otro': 3},
             1: {'suma': 5, 'resta': 5, 'multiplicacion': 5, 'division': 5, 'otro': 5},
             2: {'suma': 5, 'resta': 5, 'multiplicacion': 4, 'division': 4, 'otro': 5},
             3: {'suma': 3, 'resta': 3, 'multiplicacion': 3, 'division': 3, 'otro': 3},
             4: {'suma': 5, 'resta': 5, 'multiplicacion': 5, 'division': 5, 'otro': 5},
             5: {'suma': 5, 'resta': 5, 'multiplicacion': 5, 'division': 5, 'otro': 5}}

    while not estado_actual == estado_salida:
        try:
            caracter_automata = fuente[control_local]
            transicion = caracter_a_simbolo(caracter_automata)
            estado_actual = delta[estado_actual][transicion]
            if estado_actual in estados_finales:
                lexema = lexema + caracter_automata
            control_local += 1
        except IndexError:
            break

    if (estado_actual in estados_finales or estado_actual == estado_salida):
        cadena_aceptada = True
        control = control_local
    return [cadena_aceptada, control, lexema]

def es_cadena(fuente, control, lexema):
    cadena_aceptada = False
    def caracter_a_simbolo(caracter):
        if caracter == '"':
            return 'comilla'
        else:
            return 'caracter'

    estado_inicial = 0
    estados_finales = [2]
    estado_salida = 4

    control_local = control
    estado_actual = estado_inicial

    delta = {0: {'comilla': 1, 'caracter': 3, 'otro': 3},
             1: {'comilla': 2, 'caracter': 1, 'otro': 3},
             2: {'comilla': 4, 'caracter': 4, 'otro': 4},
             3: {'comilla': 3, 'caracter': 3, 'otro': 3},
             4: {'comilla': 4, 'caracter': 4, 'otro': 4}}

    while not estado_actual == estado_salida:
        try:
            caracter_automata = fuente[control_local]
            transicion = caracter_a_simbolo(caracter_automata)
            estado_actual = delta[estado_actual][transicion]
            if (estado_actual in estados_finales or estado_actual == 1):
                lexema = lexema + caracter_automata
            control_local += 1
        except IndexError:
            break

    if (estado_actual in estados_finales or estado_actual == estado_salida):
        cadena_aceptada = True
        control = control_local
    return [cadena_aceptada, control, lexema]

def es_simbolo_gramatical(fuente, control, lexema):
    aceptado = False
    control_local = control
    caracter = fuente[control_local]
    match caracter:
        case '+':
            componente_lexico = 'mas'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '-':
            componente_lexico = 'menos'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '*':
            componente_lexico = 'por'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '/':
            componente_lexico = 'dividido'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '^':
            componente_lexico = 'elevado'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '=':
            componente_lexico = 'igual'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '(':
            componente_lexico = 'parentesis_izquierdo'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case ')':
            componente_lexico = 'parentesis_derecho'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '[':
            componente_lexico = 'corchete_izquierdo'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case ']':
            componente_lexico = 'corchete_derecho'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '{':
            componente_lexico = 'llave_izquierda'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '}':
            componente_lexico = 'llave_derecha'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case ',':
            componente_lexico = 'coma'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case ';':
            componente_lexico = 'punto_coma'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local

        case _: # Default action if it doesn't match the others
            componente_lexico = 'Error léxico'
            aceptado = False

    return [aceptado, control, lexema, componente_lexico]



def obtener_siguiente_componente_lexico (fuente, control, tabla):
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
        real = es_real(fuente, control, lexema)
        operador_relacional = es_operador_relacional(fuente, control, lexema)
        operador_aritmetico = es_operador_aritmetico(fuente, control, lexema)
        cadena = es_cadena(fuente, control, lexema)
        simbolo_gramatical = es_simbolo_gramatical(fuente, control, lexema)

        if es_id[0] == True:
            componente_lexico = 'Identificador'
            control = es_id[1]
            lexema = es_id[2]
            tabla_de_simbolos.instalar_en_tabla(tabla, componente_lexico, lexema)
            print(componente_lexico + ': ' + lexema)

        elif real[0] == True:
            componente_lexico = 'Constante Real'
            control = real[1]
            lexema = real[2]
            print(componente_lexico + ': ' + lexema)

        elif operador_relacional[0] == True:
            componente_lexico = 'Operador relacional'
            control = operador_relacional[1]
            lexema = operador_relacional[2]
            print(componente_lexico + ': ' + lexema)

        elif operador_aritmetico[0] == True:
            componente_lexico = 'Operador aritmetico'
            control = operador_aritmetico[1]
            lexema = operador_aritmetico[2]
            print(componente_lexico + ': ' + lexema)

        elif cadena[0] == True:
            componente_lexico = 'Cadena'
            control = cadena[1]
            lexema = cadena[2]
            print(componente_lexico + ': ' + lexema)

        elif simbolo_gramatical[0]:
            componente_lexico = simbolo_gramatical[3]
            control = simbolo_gramatical[1]
            lexema = simbolo_gramatical[2]
            print(componente_lexico)
        else:
            componente_lexico = 'Error léxico'


    return control



