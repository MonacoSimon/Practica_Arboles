# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.root = None
    
#     def insert(self, value):
#         self.root = self._insert_recursive(self.root, value)
        
#     def _insert_recursive(self, node, value):
#         if node is None:
#             return Node(value)
        
#         if value < node.value:
#             node.left = self._insert_recursive(node.left, value)
#         else:
#             node.right = self._insert_recursive(node.right, value)
        
#         return node
    
#     def search(self, value):
#         return self._search_recursive(self.root, value)
    
#     def _search_recursive(self, node, value):
#         if node is None:
#             return False
        
#         if node.value == value:
#             return True
        
#         if value < node.value:
#             return self._search_recursive(node.left, value)
#         else:
#             return self._search_recursive(node.right, value)
    
#     def inorder_traversal(self, node):
#         if node is not None:
#             self.inorder_traversal(node.left)
#             print(node.value, end=" ")
#             self.inorder_traversal(node.right)

# tree = BinaryTree()
# tree.insert(5)
# tree.insert(3)
# tree.insert(7)
# tree.insert(2)
# tree.insert(4)
# tree.insert(6)
# tree.insert(8)
# print(tree.search(4))  # True
# print(tree.search(9))  # False


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
        
    def _insertar_recursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)  # Corregido aquí
        
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

print(a.buscar(4))  
print(a.buscar(9))  

a.recorrido_inorden(a.raiz)
a.recorrido_postorden(a.raiz)

