from Cola import *

class ListaEstatica(Cola):
    """
    Hereda de la clase Cola para reutilizar self.vector, self.capacidad y self.fin.
    Le agregamos las operaciones específicas de una Lista que pide el documento.
    """
    def __init__(self, capacidad):
        super().__init__(capacidad)  # Llama al __init__ de tu Cola original

    # 1. Agregar una medición (Usamos la lógica de tu encolar)
    def agregar(self, elemento):
        # En tu clase Cola original esto es encolar()
        self.encolar(elemento)

    # 2. Consultar una medición mediante su posición
    def consultar(self, posicion):
        if 0 <= posicion <= self.fin:
            return self.vector[posicion]
        else:
            print("Error: Posición inválida.")
            return None

    # 3. Buscar una medición determinada
    def buscar(self, elemento):
        for i in range(self.fin + 1):
            if self.vector[i] == elemento:
                return i  # Retorna la posición
        return -1  # No encontrado

    # 4. Modificar una medición existente
    def modificar(self, posicion, nuevo_elemento):
        if 0 <= posicion <= self.fin:
            self.vector[posicion] = nuevo_elemento
            return True
        print("Error: Posición inválida.")
        return False

    # 5. Eliminar una medición (Rompe la regla FIFO de la cola, pero es necesario para la Lista)
    def eliminar(self, posicion):
        if self.esVacio():
            print("Error: La lista está vacía.")
            return False
        if 0 <= posicion <= self.fin:
            # Desplazamos a la izquierda para tapar el hueco
            for i in range(posicion, self.fin):
                self.vector[i] = self.vector[i + 1]
            self.vector[self.fin] = None
            self.fin -= 1
            return True
        print("Error: Posición inválida.")
        return False

    def obtener_elementos_validos(self):
        # Devuelve solo el fragmento del vector que tiene datos
        if self.esVacio():
            return []
        return self.vector[:self.fin + 1]


class Persona:
    """Clase para identificar a la persona y almacenar su lista de mediciones."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_mediciones = ListaEstatica(7) # Capacidad 7 días

    def registrar_medicion(self, valor):
        self.lista_mediciones.agregar(valor)

    def calcular_maxima(self):
        elementos = self.lista_mediciones.obtener_elementos_validos()
        if not elementos: return None
        maxima = elementos[0]
        for val in elementos:
            if val > maxima: maxima = val
        return maxima

    def calcular_minima(self):
        elementos = self.lista_mediciones.obtener_elementos_validos()
        if not elementos: return None
        minima = elementos[0]
        for val in elementos:
            if val < minima: minima = val
        return minima

    def determinar_estatus(self):
        elementos = self.lista_mediciones.obtener_elementos_validos()
        if not elementos: return "SIN DATOS"
        for val in elementos:
            if val < 70 or val > 140:
                return "DESCONTROLADO"
        return "CONTROLADO"

    def mostrar_analisis(self):
        print(f"\n--- Análisis de Glucosa: {self.nombre} ---")
        print(f"Mediciones (Lun-Dom): {self.lista_mediciones.obtener_elementos_validos()}")
        if not self.lista_mediciones.esVacio():
            print(f"Medición Mínima: {self.calcular_minima()}")
            print(f"Medición Máxima: {self.calcular_maxima()}")
            print(f"Estatus actual: {self.determinar_estatus()}")


def main():
    print("=== SISTEMA DE CONTROL DE GLUCOSA SEMANAL ===")

    # Carga de datos
    ana = Persona("Ana")
    for med in [92, 105, 110, 98, 115, 108, 100]: ana.registrar_medicion(med)

    carlos = Persona("Carlos")
    for med in [180, 175, 190, 165, 185, 172, 195]: carlos.registrar_medicion(med)

    luis = Persona("Luis")
    for med in [130, 145, 138, 150, 142, 135, 128]: luis.registrar_medicion(med)

    # Casos de prueba requeridos en el PDF
    print("\n[ CASO 1: Persona controlada (Ana) ]")
    ana.mostrar_analisis()

    print("\n[ CASO 2: Persona descontrolada (Carlos) ]")
    carlos.mostrar_analisis()

    print("\n[ CASO 3: Modificación (Luis: Jueves 150 -> 135) ]")
    luis.mostrar_analisis()
    luis.lista_mediciones.modificar(3, 135)
    print("-> Después de modificar:")
    luis.mostrar_analisis()

    print("\n[ CASO 4: Eliminación (Carlos: Domingo) ]")
    carlos.mostrar_analisis()
    carlos.lista_mediciones.eliminar(6)
    print("-> Después de eliminar (Domingo):")
    carlos.mostrar_analisis()

    print("\n[ CASO 5: Búsqueda ]")
    print(f"Ana - Posición del valor 110: {ana.lista_mediciones.buscar(110)}")
    print(f"Ana - Posición del valor 200: {ana.lista_mediciones.buscar(200)}")

    print("\n[ CASO 6: Operaciones con Lista Vacía ]")
    paciente_vacio = Persona("Prueba Vacía")
    paciente_vacio.lista_mediciones.consultar(0)
    paciente_vacio.lista_mediciones.eliminar(0)
    paciente_vacio.mostrar_analisis()

if __name__ == "__main__":
    main()