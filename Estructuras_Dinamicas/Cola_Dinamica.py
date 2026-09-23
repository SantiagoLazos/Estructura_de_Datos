#cola dinamica


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    def __init__(self):
        self.frente = None
        self.ultimo = None

    # Insertar al final
    def encolar(self, dato):
        nuevo = Nodo(dato)

        if self.ultimo is None:
            self.frente = nuevo
        else:
            self.ultimo.siguiente = nuevo

        self.ultimo = nuevo

    # Eliminar del frente
    def desencolar(self):
        if self.frente is None:
            print("La cola está vacía")
        else:
            valor = self.frente.dato
            self.frente = self.frente.siguiente

            if self.frente is None:
                self.ultimo = None

            return valor

    # Mostrar la cola
    def mostrar(self):
        actual = self.frente

        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente

    def mostrar_frente(self):
        if self.frente is None:
            print("La cola está vacía")
        else:
            print("Frente de la cola:", self.frente.dato)

    def mostrar_ultimo(self):
        if self.ultimo is None:
            print("La cola está vacía")
        else:
            print("Último de la cola:", self.ultimo.dato)
