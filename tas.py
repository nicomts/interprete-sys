tas = {
    '<Programa>': {
        'var': ['<Declaraciones>', '<Cuerpo>'],
        '{': ['<Declaraciones>', '<Cuerpo>']
    },
    '<Declaraciones>': {
        'var': ['var', '<ListaVariables>'],
        '{': []
    },
    '<ListaVariables>': {
        'id': ['id', '<FinListaVariables>']
    },
    '<FinListaVariables>': {
        ',': [',', 'id', '<FinListaVariables>'],
        '{': []
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
        '}': []
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
        '{': [],
        ';': [],
        '+': ['+', '<OperandoSumaResta>', '<OperacionSumaResta>'],
        '-': ['-', '<OperandoSumaResta>', '<OperacionSumaResta>'],
        ')': [],
        'operadorRelacional': [],
        'and': [],
        'or': [],
        ']': []
    },
    '<OperandoSumaResta>': {
        'id': ['<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        'constanteReal': ['<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        '-': ['<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        '(': ['<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>']
    },
    '<OperacionMultiplicacionDivision>': {
        '{': [],
        ';': [],
        '+': [],
        '-': [],
        '*': ['*', '<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        '/': ['/', '<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        ')': [],
        'operadorRelacional': [],
        'and': [],
        'or': [],
        ']': []
    },
    '<OperandoMultiplicacionDivision>': {
        'id': ['<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        'constanteReal': ['<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        '-': ['<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        '(': ['<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>']
    },
    '<OperacionPotenciaRaiz>': {
        '{': [],
        ';': [],
        '+': [],
        '-': [],
        '*': [],
        '/': [],
        '**': ['**', '<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        '*/': ['*/', '<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        ')': [],
        'operadorRelacional': [],
        'and': [],
        'or': [],
        ']': []
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
        ';': [],
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
        '{': [],
        'and': ['and', '<OperandoAndOr>', '<OperacionAndOr>'],
        'or': ['or', '<OperandoAndOr>', '<OperacionAndOr>'],
        ']': []
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
