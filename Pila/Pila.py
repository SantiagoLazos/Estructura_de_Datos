

class Pila:#Con esta Clase voy a crear una Pila de x tamaño y realizar sus metodos
    
    def __init__(self,capacidad):#Esta parte es el constructor
        self.capacidad = capacidad
        self.cima = -1
        self.arreglo = [None] * self.capacidad
    
    def esVacio(self):#Compara la cima de la pila con -1 para decir si esta vacia o no 
        if self.cima == -1:
            return True
        else:
            return False
        
    def esLleno(self):#Compara la cima con la capacidad para checar si esta llena
        if self.cima == (self.capacidad-1):
            return True
        else:
            return False
    
    def mostrarPila(self):
        if self.esVacio():
            print(f"Esta Pila Esta Vacia")
        else: 
            print("========Pila======")
            for i in range(self.cima, -1, -1):#Empieza en la cima, luego nos dice el final es -1, y va de -1 en -1
                print(self.arreglo[i])
            print("========Fin_Pila==")

    def apilar(self, elemento):
        if self.esLleno() == True:
            print(f"Esta Pila esra llena, No se pueden agregar elementos")
        
        else:
            self.cima += 1
            self.arreglo[self.cima] = elemento

    def desapilar(self):
        if self.esVacio() == True:
            print(f"Esta Pila Esta Vacia, No se pueden eliminar elementos")
        else:
            self.cima -= 1
            return self.arreglo[self.cima + 1]
        
    def verCIMA(self):
        if self.esVacio():
            print(f"Esta Pila esra Vacia")
        else:
            print(self.arreglo[self.cima])

    def ObtenerCima(self):
        if self.esVacio():
            return False
        else:
            return self.arreglo[self.cima]

