tas = {
    '<Programa>': {
        'var': ['<Declaraciones>', '<Cuerpo>'],
        '{': ['<Declaraciones>', '<Cuerpo>']
    },
    '<Declaraciones>': {
        'var': ['var', '<ListaVariables>'],
        '{': ['epsilon']
    },
    '<ListaVariables>': {
        'id': ['id', '<FinListaVariables>']
    },
    '<FinListaVariables>': {
        ',': [',', 'id', '<FinListaVariables>'],
        '{': ['epsilon']
    },
    '<Cuerpo>': {
        '{': ['{', '<ListaSentencias>', '}']
    },
    '<ListaSentencias>': {
        'id': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        'write': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        'read': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        'if': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        'while': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
    },
    '<ListaSentenciasFin>': {
        'id': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        'write': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        'read': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        'if': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        'while': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        '}': ['epsilon']
    },
    '<Sentencia>': {
        'id': ['<Asignacion>'],
        'write': ['<Escritura>'],
        'read': ['<Lectura>'],
        'if': ['<Condicional>'],
        'while': ['<CicloMientras>']
    },
    '<Asignacion>': {
        'id': ['id', 'operadorAsignacion', '<ExpresionAritmetica>']
    },
    '<ExpresionAritmetica>': {
        'id': ['<OperandoSumaResta>', '<OperacionSumaResta>'],
        'constanteReal': ['<OperandoSumaResta>', '<OperacionSumaResta>'],
        '-': ['<OperandoSumaResta>', '<OperacionSumaResta>'],
        '(': ['<OperandoSumaResta>', '<OperacionSumaResta>']
    },
    '<OperacionSumaResta>': {
        '{': ['epsilon'],
        ';': ['epsilon'],
        '+': ['+', '<OperandoSumaResta>', '<OperacionSumaResta>'],
        '-': ['-', '<OperandoSumaResta>', '<OperacionSumaResta>'],
        ')': ['epsilon'],
        'operadorRelacional': ['epsilon'],
        'and': ['epsilon'],
        'or': ['epsilon'],
        ']': ['epsilon']
    },
    '<OperandoSumaResta>': {
        'id': ['<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        'constanteReal': ['<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        '-': ['<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        '(': ['<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>']
    },
    '<OperacionMultiplicacionDivision>': {
        '{': ['epsilon'],
        ';': ['epsilon'],
        '+': ['epsilon'],
        '-': ['epsilon'],
        '*': ['*', '<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        '/': ['/', '<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        ')': ['epsilon'],
        'operadorRelacional': ['epsilon'],
        'and': ['epsilon'],
        'or': ['epsilon'],
        ']': ['epsilon']
    },
    '<OperandoMultiplicacionDivision>': {
        'id': ['<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        'constanteReal': ['<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        '-': ['<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        '(': ['<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>']
    },
    '<OperacionPotenciaRaiz>': {
        '{': ['epsilon'],
        ';': ['epsilon'],
        '+': ['epsilon'],
        '-': ['epsilon'],
        '*': ['epsilon'],
        '/': ['epsilon'],
        '**': ['**', '<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        '*/': ['*/', '<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        ')': ['epsilon'],
        'operadorRelacional': ['epsilon'],
        'and': ['epsilon'],
        'or': ['epsilon'],
        ']': ['epsilon']
    },
    '<OperandoPotenciaRaiz>': {
        'id': ['id'],
        'constanteReal': ['constanteReal'],
        '-': ['-', '<OperandoPotenciaRaiz>'],
        '(': ['(', '<ExpresionAritmetica>', ')']
    },
    '<Lectura>': {
        'read': ['read', '(', 'Cadena', ',', 'id', ')']
    },
    '<Escritura>': {
        'write': ['write', '(', 'Cadena', ',', '<ExpresionAritmetica>', ')']
    },
    '<Condicional>': {
        'if': ['if', '<Condicion>', '<Cuerpo>', '<FinCondicional>']
    },
    '<FinCondicional>': {
        ';': ['epsilon'],
        'else': ['else', '<Cuerpo>'],
    },
    '<Condicion>': {
        'id': ['<OperandoAndOr>', '<OperacionAndOr>'],
        'constanteReal': ['<OperandoAndOr>', '<OperacionAndOr>'],
        '-': ['<OperandoAndOr>', '<OperacionAndOr>'],
        '(': ['<OperandoAndOr>', '<OperacionAndOr>'],
        'not': ['<OperandoAndOr>', '<OperacionAndOr>'],
        '[': ['<OperandoAndOr>', '<OperacionAndOr>']
    },
    '<OperacionAndOr>': {
        '{': ['epsilon'],
        'and': ['and', '<OperandoAndOr>', '<OperacionAndOr>'],
        'or': ['or', '<OperandoAndOr>', '<OperacionAndOr>'],
        ']': ['epsilon']
    },
    '<OperandoAndOr>': {
        'id': ['<ExpresionAritmetica>', 'operadorRelacional', '<ExpresionAritmetica>'],
        'constanteReal': ['<ExpresionAritmetica>', 'operadorRelacional', '<ExpresionAritmetica>'],
        '-': ['<ExpresionAritmetica>', 'operadorRelacional', '<ExpresionAritmetica>'],
        '(': ['<ExpresionAritmetica>', 'operadorRelacional', '<ExpresionAritmetica>'],
        'not': ['not', '<OperandoAndOr>'],
        '[': ['[', '<Condicion>', ']']
    },
    '<CicloMientras>': {
        'while': ['while', '<Condicion>', '<Cuerpo>']
    }

}
