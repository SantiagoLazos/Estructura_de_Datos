from Pila_Dinamica import Pila
from Cola_Dinamica import Cola
from Lista_simple import lista_simple

print("Bienvenido al menú de estructuras de datos")

a = int(input("Ingresa opcion: \n 1. Pila Dinámica \n 2. Cola Dinámica \n 3. Lista Simple \n"))

if a == 1:
    pila = Pila()
    while True:
        print("\nOpciones de Pila Dinámica:")
        print("1. Apilar")
        print("2. Desapilar")
        print("3. Mostrar Pila")
        print("4. Mostrar Cima")
        print("5. Salir")

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            dato = input("Ingresa el dato a apilar: ")
            pila.apilar(dato)
        elif opcion == 2:
            pila.desapilar()
        elif opcion == 3:
            pila.mostrar()
        elif opcion == 4:
            pila.mostrar_cima()
        elif opcion == 5:
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
elif a == 2:
    cola = Cola()
    while True:
        print("\nOpciones de Cola Dinámica:")
        print("1. Encolar")
        print("2. Desencolar")
        print("3. Mostrar Cola")
        print("4. Mostrar Frente")
        print("5. Mostrar Último")
        print("6. Salir")

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            dato = input("Ingresa el dato a encolar: ")
            cola.encolar(dato)
        elif opcion == 2:
            cola.desencolar()
        elif opcion == 3:
            cola.mostrar()
        elif opcion == 4:
            cola.mostrar_frente()
        elif opcion == 5:
            cola.mostrar_ultimo()
        elif opcion == 6:
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

elif a == 3:
    lista = lista_simple()
    while True:
        print("\nOpciones de Lista Simple:")
        print("1. Insertar")
        print("2. Mostrar Lista")
        print("3. Mostrar Primer Elemento")
        print("4. Quitar Elemento")
        print("5. Salir")

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            dato = input("Ingresa el dato a insertar: ")
            lista.insertar(dato)
        elif opcion == 2:
            lista.mostrar()
        elif opcion == 3:
            lista.mostrar_primero()
        elif opcion == 4:
            dato = input("Ingresa el dato a quitar: ")
            lista.quitar_elemento(dato)
        elif opcion == 5:
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
else:
    print("Opción inválida. Intenta de nuevo.")

    



