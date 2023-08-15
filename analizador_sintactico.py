import analizador_lexico
import tabla_de_simbolos
import arbol
import tas

ruta_archivo = 'test.txt'
archivo = open(ruta_archivo)
fuente = archivo.read()
control = 0
tabla = []
tabla_de_simbolos.crear_tabla(tabla)


pila = ['$']
raiz = arbol.NodoArbol('<Programa>')
pila.append(raiz)
exito = False
error = False
a = analizador_lexico.obtener_siguiente_componente_lexico(fuente, control, tabla)

terminal = False
variable = False

def analizador_sintactico():
    while not exito and not error:
        x = pila.pop()
        if terminal:
            if x == a:
                a = analizador_lexico.obtener_siguiente_componente_lexico(fuente, control, tabla)
            else:
                error = True
        elif variable:
            if tas.tas[x,a] == None:
                error = True
            else:
                for i in reversed(tas.tas[x,a]):
                    pila.append(i)
                    nuevo_nodo = arbol.NodoArbol(i)
                    x.hijos.append(nuevo_nodo)

        elif x==a=='$':
            exito = True


