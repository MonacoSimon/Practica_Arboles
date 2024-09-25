"""
es hoja, eliminar derecho e izquierdo y agregar idem,
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)
    
    def vacio(self):
        if self.raiz == None:
            return "esta vacio"
    def es_hoja(self, nodo):
        # pila = []
        # a = 0
        # a = ArbolBinario()
        # a.recorrido_inorden(a.raiz)
        if nodo is not None:
            self.recorrido_inorden(nodo.izquierdo)
            # print(nodo.valor, end=" ")
            # self.recorrido_inorden(nodo.derecho)

    def obtener_hijo_izquierdo(self, nodo):
        if nodo is not None:
            self.recorrido_inorden(nodo.izquierdo)
    
    def obtener_hijo_derecho(self, nodo):
        if nodo is not None:
            self.recorrido_inorden(nodo.derecho)
    
    def agregar_hijo_izquierdo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)  
        
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, valor)

    def agregar_hijo_derecho(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)  
        
        if valor > nodo.valor:
            nodo.izquierdo = self._insertar_recursivo(nodo.derecho, valor)

    def eliminar_hijo_izquierdo(self, nodo, valor):
        pila = []
        pila.append(a.obtener_hijo_izquierdo(a.raiz))
        for i in pila:
            print(pila())
        
    def _insertar_recursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)  
        
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, valor)
        
        return nodo
    
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
    

    
    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        
        if nodo.valor == valor:
            return True
        
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo.derecho, valor)
    
    def recorrido_inorden(self, nodo):
        if nodo is not None:
            self.recorrido_inorden(nodo.izquierdo)
            print(nodo.valor, end=" ")
            self.recorrido_inorden(nodo.derecho)

    def recorrido_postorden(self, nodo):
        if nodo is not None:
            self.recorrido_postorden(nodo.izquierdo)
            self.recorrido_postorden(nodo.derecho)
            print(nodo.valor, end=" ")


a = ArbolBinario()
a.insertar(5)
a.insertar(3)
a.insertar(7)
a.insertar(2)
a.insertar(4)
a.insertar(6)
a.insertar(8)

# print(a.buscar(4))  
# print(a.buscar(9))  

# a.recorrido_inorden(a.raiz)
# a.recorrido_postorden(a.raiz)
# print("es hoja")
# a.es_hoja(a.raiz)
# a.obtener_hijo_derecho(a.raiz)
# print("derecho")
# a.obtener_hijo_izquierdo(a.raiz)

a.agregar_hijo_izquierdo(a.raiz, 9)
# a.recorrido_inorden(a.raiz)
a.obtener_hijo_izquierdo(a.raiz)
a.eliminar_hijo_izquierdo(a.raiz, 3)
a.obtener_hijo_izquierdo(a.raiz)
# a.agregar_hijo_derecho(a.raiz, 9)
# a.obtener_hijo_derecho(a.raiz)
a.eliminar_hijo_izquierdo(a.raiz)