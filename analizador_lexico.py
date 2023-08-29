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
        elif es_digito:
            return 'digito'
        else:
            return 'otro'

    estado_inicial = 0
    estado_final = 5
    estado_muerto = 7

    control_local = control
    estado_actual = estado_inicial

    # This is the definition of the delta function(transitions) as a matrix of python dictionaries:
    delta = {0: {'digito': 1, 'otro': 2, 'punto': 2},  # from state 0 through digito you go to state 1
             1: {'digito': 1, 'otro': 5, 'punto': 3},
             2: {'digito': 2, 'otro': 2, 'punto': 2},
             3: {'digito': 4, 'otro': 2, 'punto': 2},
             4: {'digito': 4, 'otro': 5, 'punto': 5},
             5: {'digito': 5, 'otro': 5, 'punto': 5},
             6: {'digito': 1, 'otro': 2, 'punto': 2}}

    while not estado_actual == estado_final and not estado_actual == estado_muerto and control_local < len(fuente):
        caracter_automata = fuente[control_local]
        transicion = caracter_a_simbolo(caracter_automata)
        estado_actual = delta[estado_actual][transicion]
        lexema = lexema + caracter_automata
        control_local += 1
    if estado_actual == estado_final:
        lexema = lexema[:-1]  # This removes the last character
        cadena_aceptada = True
        control = control_local - 1
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
    estado_final = 3
    estado_muerto = 1
    control_local = control
    estado_actual = estado_inicial

    # State 3 is the exit state, it marks the end of the identifier recognized
    delta = {0: {'letra': 2, 'digito': 1, 'otro': 1},
             1: {'letra': 1, 'digito': 1, 'otro': 1},
             2: {'letra': 2, 'digito': 2, 'otro': 3},
             3: {'letra': 3, 'digito': 3, 'otro': 3}
             }

    while not estado_actual == estado_final and not estado_actual == estado_muerto and control_local < len(fuente):
        caracter_automata = fuente[control_local]
        transicion = caracter_a_simbolo(caracter_automata)
        estado_actual = delta[estado_actual][transicion]
        lexema = lexema + caracter_automata
        control_local += 1
    if estado_actual == estado_final:
        lexema = lexema[:-1]  # This removes the last character
        cadena_aceptada = True
        control = control_local - 1

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
    estado_muerto = 5
    estado_final = 6

    control_local = control
    estado_actual = estado_inicial

    delta = {0: {'menor': 1, 'mayor': 4, 'igual': 3, 'otro': 5},
             1: {'menor': 6, 'mayor': 2, 'igual': 2, 'otro': 6},
             2: {'menor': 6, 'mayor': 6, 'igual': 6, 'otro': 6},
             3: {'menor': 5, 'mayor': 5, 'igual': 2, 'otro': 5},
             4: {'menor': 6, 'mayor': 6, 'igual': 2, 'otro': 6},
             5: {'menor': 5, 'mayor': 5, 'igual': 5, 'otro': 5},
             6: {'menor': 6, 'mayor': 6, 'igual': 6, 'otro': 6}}

    while not estado_actual == estado_final and not estado_actual == estado_muerto and control_local < len(fuente):
        caracter_automata = fuente[control_local]
        transicion = caracter_a_simbolo(caracter_automata)
        estado_actual = delta[estado_actual][transicion]
        lexema = lexema + caracter_automata
        control_local += 1
    if estado_actual == estado_final:
        lexema = lexema[:-1]  # This removes the last character
        cadena_aceptada = True
        control = control_local - 1
    return [cadena_aceptada, control, lexema]


def es_potencia(fuente, control, lexema):
    cadena_aceptada = False

    def caracter_a_simbolo(caracter):
        if caracter == '*':
            return 'asterisco'
        else:
            return 'otro'

    estado_inicial = 0
    estado_muerto = 4
    estado_final = 3

    control_local = control
    estado_actual = estado_inicial

    delta = {0: {'asterisco': 1, 'otro': 4},
             1: {'asterisco': 2, 'otro': 4},
             2: {'asterisco': 3, 'otro': 3},
             3: {'asterisco': 3, 'otro': 3},
             4: {'asterisco': 4, 'otro': 4}}

    while not estado_actual == estado_final and not estado_actual == estado_muerto and control_local < len(fuente):
        caracter_automata = fuente[control_local]
        transicion = caracter_a_simbolo(caracter_automata)
        estado_actual = delta[estado_actual][transicion]
        lexema = lexema + caracter_automata
        control_local += 1
    if estado_actual == estado_final:
        lexema = lexema[:-1]  # This removes the last character
        cadena_aceptada = True
        control = control_local - 1
    return [cadena_aceptada, control, lexema]


def es_raiz(fuente, control, lexema):
    cadena_aceptada = False

    def caracter_a_simbolo(caracter):
        if caracter == '*':
            return 'asterisco'
        elif caracter == '/':
            return 'barra'
        else:
            return 'otro'

    estado_inicial = 0
    estado_muerto = 4
    estado_final = 3

    control_local = control
    estado_actual = estado_inicial

    delta = {0: {'asterisco': 1, 'barra': 4, 'otro': 4},
             1: {'asterisco': 4, 'barra': 2, 'otro': 4},
             2: {'asterisco': 3, 'barra': 3, 'otro': 3},
             3: {'asterisco': 3, 'barra': 3, 'otro': 3},
             4: {'asterisco': 4, 'barra': 4, 'otro': 4}}

    while not estado_actual == estado_final and not estado_actual == estado_muerto and control_local < len(fuente):
        caracter_automata = fuente[control_local]
        transicion = caracter_a_simbolo(caracter_automata)
        estado_actual = delta[estado_actual][transicion]
        lexema = lexema + caracter_automata
        control_local += 1
    if estado_actual == estado_final:
        lexema = lexema[:-1]  # This removes the last character
        cadena_aceptada = True
        control = control_local - 1
    return [cadena_aceptada, control, lexema]


def es_cadena(fuente, control, lexema):
    cadena_aceptada = False

    def caracter_a_simbolo(caracter):
        if caracter == '"':
            return 'comilla'
        else:
            return 'otro'

    estado_inicial = 0
    estado_muerto = 3
    estado_final = 4

    control_local = control
    estado_actual = estado_inicial

    delta = {0: {'comilla': 1, 'otro': 3},
             1: {'comilla': 2, 'otro': 1},
             2: {'comilla': 4, 'otro': 4},
             3: {'comilla': 3, 'otro': 3},
             4: {'comilla': 4, 'otro': 4}}

    while not estado_actual == estado_final and not estado_actual == estado_muerto and control_local < len(fuente):
        caracter_automata = fuente[control_local]
        transicion = caracter_a_simbolo(caracter_automata)
        estado_actual = delta[estado_actual][transicion]
        lexema = lexema + caracter_automata
        control_local += 1
    if estado_actual == estado_final:
        lexema = lexema[:-1]  # This removes the last character
        cadena_aceptada = True
        control = control_local - 1
    return [cadena_aceptada, control, lexema]


def es_simbolo_gramatical(fuente, control, lexema):
    aceptado = False
    control_local = control
    caracter = fuente[control_local]
    match caracter:
        case '+':
            componente_lexico = '+'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '-':
            componente_lexico = '-'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '*':
            componente_lexico = '*'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '/':
            componente_lexico = '/'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '(':
            componente_lexico = '('
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case ')':
            componente_lexico = ')'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '[':
            componente_lexico = '['
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case ']':
            componente_lexico = ']'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '{':
            componente_lexico = '{'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '}':
            componente_lexico = '}'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case ',':
            componente_lexico = ','
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case ';':
            componente_lexico = ';'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case '=':
            componente_lexico = 'operadorAsignacion'
            lexema = caracter
            aceptado = True
            control_local += 1
            control = control_local
        case _:  # Default action if it doesn't match the others
            componente_lexico = 'Error léxico'
            aceptado = False

    return [aceptado, control, lexema, componente_lexico]


def obtener_siguiente_componente_lexico(fuente, control, tabla):
    fin_de_archivo = False
    lexema = ''
    componente_lexico = ''
    try:
        caracter = fuente[control]
        while ord(caracter) in range(33):  # this will skip control characters (blank spaces)
            control += 1
            caracter = fuente[control]
    except IndexError:  # This will return end of file if the index of the array is out of range
        fin_de_archivo = True

    if fin_de_archivo is True:
        componente_lexico = 'Fin de archivo'
    else:

        es_id = es_identificador(fuente, control, lexema)
        real = es_real(fuente, control, lexema)
        operador_relacional = es_operador_relacional(fuente, control, lexema)
        cadena = es_cadena(fuente, control, lexema)
        potencia = es_potencia(fuente, control, lexema)
        raiz = es_raiz(fuente, control, lexema)
        simbolo_gramatical = es_simbolo_gramatical(fuente, control, lexema)

        if es_id[0] is True:
            componente_lexico = 'id'
            control = es_id[1]
            lexema = es_id[2]

            for i in tabla:
                if i['lexema'] == lexema:
                    componente_lexico = i['componente_lexico']

            tabla_de_simbolos.instalar_en_tabla(tabla, componente_lexico, lexema)

        elif real[0] is True:
            componente_lexico = 'constanteReal'
            control = real[1]
            lexema = real[2]

        elif operador_relacional[0] is True:
            componente_lexico = 'operadorRelacional'
            control = operador_relacional[1]
            lexema = operador_relacional[2]

        elif potencia[0] is True:
            componente_lexico = '**'
            control = potencia[1]
            lexema = potencia[2]

        elif raiz[0] is True:
            componente_lexico = '*/'
            control = raiz[1]
            lexema = raiz[2]

        elif cadena[0] is True:
            componente_lexico = 'Cadena'
            control = cadena[1]
            lexema = cadena[2]

        elif simbolo_gramatical[0]:
            componente_lexico = simbolo_gramatical[3]
            control = simbolo_gramatical[1]
            lexema = simbolo_gramatical[2]

        else:
            componente_lexico = 'Error léxico'

    return [componente_lexico, control, lexema]
