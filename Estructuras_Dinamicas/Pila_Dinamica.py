class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    def __init__(self):
        self.raiz = None

    # Insertar al inicio
    def apilar(self, dato):
        nuevo = Nodo(dato)

        nuevo.siguiente = self.raiz
        self.raiz = nuevo

    # Eliminar al inicio
    def desapilar(self):
        if self.raiz is None:
            print("La pila está vacía")
        else:
            valor = self.raiz.dato
            self.raiz = self.raiz.siguiente
            return valor

    # Mostrar la pila
    def mostrar(self):
        actual = self.raiz

        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente

    def mostrar_cima(self):
        if self.raiz is None:
            print("La pila está vacía")
        else:
            print("Cima de la pila:", self.raiz.dato)



