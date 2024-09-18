"""
metodos obtener hijo derecho e izquierdo
agregar hijo izquierdo y derecho
eliminar hijo izquierdo y derecho
esta vacio
es hoja
tiene hijo derecho e izquierdo
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolB:
    def __init__(self):
        self.raiz = None


    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.raiz == None:
            self.raiz = nuevo_nodo
            return
        else:
            actual = self.raiz
            while True:
                if dato < actual.dato:
                    if actual.izquierda == None:
                        actual.izquierda = nuevo_nodo
                        break
                    actual = actual.izquierda
                else:
                    if dato > actual.dato:
                        if actual.derecha is None:
                            actual.derecha = nuevo_nodo
                            break
                        actual = actual.derecha
    def obtener_hijo_derecho (self):
        actual = self.raiz
        a = actual.derecha
        pila = []
        while a.dato > actual.dato:
            pila.append(actual)
            print(actual.dato)


    def mostrar(self):
        actual = self.raiz
        pila = []
        while pila or actual is not None:
            if actual != None:    
                pila.append(actual)
                actual = actual.izquierda
            else:
                actual = pila.pop()
                print(actual.dato)
                actual = actual.derecha
    
    def esta_vacio(self):
        if self.raiz == None:
            return False 
        else:
            return True


    def tiene_hijo_derecho (self):
        print("A")
        if self.raiz:
            return self.raiz.derecha.dato
        return None



a = ArbolB()
a.esta_vacio()
print(a.tiene_hijo_derecho())
a.insertar(54)
a.insertar(32)
a.insertar(98)
a.insertar(67)
a.insertar(1)
# a.tiene_hijo_derecho()


a.mostrar()
print(a.tiene_hijo_derecho())
# a.obtener_hijo_derecho()
