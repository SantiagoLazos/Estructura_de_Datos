class Cola:
    def __init__(self,capacidad):
        self.capacidad=capacidad
        self.vector=[None]*capacidad
        self.fin=-1

    def esVacio(self):
        if self.fin==-1:
            return True
        else:
            return False
        
    def esLleno(self):
        if self.fin==self.capacidad-1:
            return True
        else:
            return False

    def encolar(self,elemento):
        if self.esLleno()==False:
            self.fin=self.fin+1
            self.vector[self.fin]=elemento
        else:
            print(f"La Cola esta llena")

    def desencolar(self):
        if self.esVacio()==False:
            print(f"La cola esta vacia, no se puede vaciar")
        else:
            print("")
            elemento_saliente = self.vector[0]
            for i in range(self.fin):
                self.vector[i] = self.vector[i + 1]
            self.vector[self.fin] = None
            self.fin = self.fin - 1

    def obtenerFrente(self):
        if self.esVacio():
            print("La Cola Esta Vacia")
        else:
            print(f"El elemento del frente es: {self.vector[0]}")
            return self.vector[0]

    def mostrar(self):
        if self.esVacio():
            print("Cola Vacia")
        else:
            print("=====Cola=====")
            print(self.vector[:self.fin + 1])


if __name__ == "__main__":
    
    print("Bienvenido al programa de Colas")
    print("Ingrese la capacidad de la Cola")
    capacidad=int(input())
    cola=Cola(capacidad)

    print("seleccione una opcion:")
    print("1. Encolar")
    print("2. Desencolar")
    print("3. Mostrar frente")
    print("4. Mostrar")
    print("5. Salir")




    while True:
        opcion=int(input("Ingrese una opcion: "))
        if opcion==1:
            elemento=input("Ingrese el elemento a encolar: ")
            cola.encolar(elemento)
        elif opcion==2:
            cola.desencolar()
        elif opcion==3:
            cola.obtenerFrente()
        elif opcion==4:
            cola.mostrar()
        elif opcion==5:
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida, intente de nuevo")