from nodo import Nodo

class Arbol:
    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.dato, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)
    
    def obtener_hijo_izquierdo(self, nodo):
        pila = []
        while nodo.izquierda is not None:
            pila.append(nodo.izquierda)
            nodo = nodo.izquierda
        for i in pila:
            print(i.dato)
            
    def obtener_hijo_derecho(self, nodo):
        if nodo is None:
            print("El nodo es None.")
            return

    print(nodo.dato)  # Muestra el dato del nodo actual
    while nodo.derecha is not None:  # Mientras haya un hijo derecho
        nodo = nodo.derecha  # Mueve al hijo derecho
        print(nodo.dato)
    def obtener_raiz(self):
        return self.raiz.dato

    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)

    def inorden(self):
        self.__inorden_recursivo(self.raiz)

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
    

a = Arbol(8)
a.agregar(3)
a.agregar(1)
a.agregar(6)
a.agregar(4)
# a.obtener_hijo_izquierdo(a.raiz) 
a.obtener_hijo_derecho(a.raiz)
# a.obtener_raiz()
# a.inorden()
