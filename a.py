class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo is not None
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        return self._buscar_recursivo(nodo.derecha, valor)

    def inorden(self):
        self._inorden_recursivo(self.raiz)
        print()

    def _inorden_recursivo(self, nodo):
        if nodo:
            self._inorden_recursivo(nodo.izquierda)
            print(nodo.valor, end=" ")
            self._inorden_recursivo(nodo.derecha)

    def preorden(self):
        self._preorden_recursivo(self.raiz)
        print()

    def _preorden_recursivo(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self._preorden_recursivo(nodo.izquierda)
            self._preorden_recursivo(nodo.derecha)

    def postorden(self):
        self._postorden_recursivo(self.raiz)
        print()

    def _postorden_recursivo(self, nodo):
        if nodo:
            self._postorden_recursivo(nodo.izquierda)
            self._postorden_recursivo(nodo.derecha)
            print(nodo.valor, end=" ")

# Ejemplo de uso
if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    valores = [50, 30, 70, 20, 40, 60, 80]
    for v in valores:
        arbol.insertar(v)
    
    print("Recorrido inorden:")
    arbol.inorden()
    
    print("Recorrido preorden:")
    arbol.preorden()
    
    print("Recorrido postorden:")
    arbol.postorden()
    
    print("Buscar 40 en el árbol:", arbol.buscar(40))
    print("Buscar 90 en el árbol:", arbol.buscar(90))
