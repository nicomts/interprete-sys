class NodoArbol:
    def __init__(self, valor, hijos=None):
        self.valor = valor
        self.hijos = hijos if hijos is not None else []

'''

# Crear un árbol
nodo1 = NodoArbol(1)
nodo2 = NodoArbol(2)
nodo3 = NodoArbol(3)
nodo4 = NodoArbol(4)
nodo5 = NodoArbol(5)

nodo1.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4, nodo5]

# Recorrer el árbol utilizando un enfoque de recorrido en profundidad (DFS)
def dfs(nodo):
    print(nodo.valor)
    for hijo in nodo.hijos:
        dfs(hijo)

dfs(nodo1)

'''