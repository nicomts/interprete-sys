tas = {
    '<Programa>': {
        'var': ['<Declaraciones>', '<Cuerpo>']
    },
    '<Declaraciones>': {
        'var': ['var', '<ListaVariables>'],
        'Cadena': ['epsilon']
    },
    '<ListaVariables>': {
        'id': ['id', '<FinListaVariables>']
    },
    '<FinListaVariables>': {
        ',': [',', 'id', '<FinListaVariables>'],
        ';': ['epsilon']
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
        'Cadena': ['<Sentencia>', ';', '<ListaSentenciasFin>']
    },
    '<ListaSentenciasFin>': {
        'id': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        'write': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        'read': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        'if': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        'while': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        'Cadena': ['<Sentencia>', ';', '<ListaSentenciasFin>'],
        '}': ['epsilon']
    },
    '<Sentencia>': {
        'id': ['<Asignacion>'],
        'write': ['<Escritura>'],
        'read': ['<Lectura>'],
        'if': ['<Condicional>'],
        'while': ['<CicloMientras>'],
        'Cadena': ['<Escritura>']
    },
    '<Asignacion>': {
        'id': ['id', 'operadorAsignacion', '<ExpresionAritmetica>']
    },
    '<ExpresionAritmetica>': {
        'id': ['<OperandoSumaResta>', '<OperacionSumaResta>'],
        'constanteReal': ['<OperandoSumaResta>', '<OperacionSumaResta>'],
        '(': ['<OperandoSumaResta>', '<OperacionSumaResta>']
    },
    '<OperacionSumaResta>': {
        '+': ['+', '<OperandoSumaResta>', '<OperacionSumaResta>'],
        '-': ['-', '<OperandoSumaResta>', '<OperacionSumaResta>'],
        ')': ['epsilon'],
        ';': ['epsilon'],
        'operadorRelacional': ['epsilon'],
        'and': ['epsilon'],
        'or': ['epsilon']
    },
    '<OperandoSumaResta>': {
        'id': ['<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        'constanteReal': ['<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        '(': ['<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>']
    },
    '<OperacionMultiplicacionDivision>': {
        '*': ['*', '<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        '/': ['/', '<OperandoMultiplicacionDivision>', '<OperacionMultiplicacionDivision>'],
        '+': ['epsilon'],
        '-': ['epsilon'],
        ')': ['epsilon'],
        ';': ['epsilon'],
        'operadorRelacional': ['epsilon'],
        'and': ['epsilon'],
        'or': ['epsilon']
    },
    '<OperandoMultiplicacionDivision>': {
        'id': ['<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        'constanteReal': ['<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        '(': ['<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>']
    },
    '<OperacionPotenciaRaiz>': {
        '**': ['**', '<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        '*/': ['*/', '<OperandoPotenciaRaiz>', '<OperacionPotenciaRaiz>'],
        '*': ['epsilon'],
        '/': ['epsilon'],
        '+': ['epsilon'],
        '-': ['epsilon'],
        ')': ['epsilon'],
        ';': ['epsilon'],
        'operadorRelacional': ['epsilon'],
        'and': ['epsilon'],
        'or': ['epsilon']
    },
    '<OperandoPotenciaRaiz>': {
        'id': ['id', '<SiguientePorenciaRaiz>'],
        'constanteReal': ['constanteReal'],
        '-': ['-', '<OperandoPotenciaRaiz>'],
        '(': ['(', '<ExpresionAritmetica>', ')']
    },
    '<SiguientePorenciaRaiz>': {
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
        'else': ['else', '<Cuerpo>'],
        '}': ['epsilon']
    },
    '<Condicion>': {
        'id': ['<OperandoAndOr>', '<OperacionAndOr>'],
        'constanteReal': ['<OperandoAndOr>', '<OperacionAndOr>'],
        '(': ['<OperandoAndOr>', '<OperacionAndOr>'],
        'not': ['not', '<OperandoAndOr>'],
        '[': ['[', '<Condicion>', ']']
    },
    '<OperandoAndOr>': {
        'id': ['<ExpresionAritmetica>', 'operadorRelacional', '<ExpresionAritmetica>'],
        'constanteReal': ['<ExpresionAritmetica>', 'operadorRelacional', '<ExpresionAritmetica>'],
        '(': ['<ExpresionAritmetica>', 'operadorRelacional', '<ExpresionAritmetica>']
    },
    '<OperacionAndOr>': {
        'and': ['and', '<OperandoAndOr>'],
        'or': ['or', '<OperandoAndOr>'],
        ')': ['epsilon']
    },
    '<CicloMientras>': {
        'while': ['while', '<Condicion>', '<Cuerpo>']
    }

}
