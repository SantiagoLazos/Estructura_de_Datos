#Lista simple

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class lista_simple:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            actual = self.raiz
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.raiz
        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente

    def mostrar_primero(self):
        if self.raiz is None:
            print("La lista está vacía")
        else:
            print("Primer elemento de la lista:", self.raiz.dato)

    def quitar_elemento(self, dato):
        if self.raiz is None:
            print("La lista está vacía")
            return

        if self.raiz.dato == dato:
            self.raiz = self.raiz.siguiente
            return

        actual = self.raiz
        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

        print("Elemento no encontrado en la lista")

        

