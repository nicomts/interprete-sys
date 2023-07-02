import analizador_lexico, tabla_de_simbolos

ruta_archivo = 'test.txt'
archivo = open(ruta_archivo)
fuente = archivo.read()
control_global = 0
tabla = []
tabla_de_simbolos.crear_tabla(tabla)
for i in range(14):
    control_global = analizador_lexico.obtener_siguiente_componente_lexico(fuente, control_global, tabla)


# tabla = []
# componente_lexico = 'identificador'
# lexema = 'variable1'
#
# tabla_de_simbolos.crear_tabla(tabla)
# tabla_de_simbolos.instalar_en_tabla(tabla, componente_lexico, lexema)
