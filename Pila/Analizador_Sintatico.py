from Pila import *

expresion = input("Ingresa la expresion a evaluar: ")
z=len(expresion)
Pilaespecial= Pila(z)
Error_de_sintaxis=False

if z==0:
    print(f"Error no hay expresion")

else:        

    for caracter in expresion:

        if caracter == "{" or caracter == "[" or caracter== "(":
            Pilaespecial.apilar(caracter)

        elif caracter == "}" or caracter == "]" or caracter== ")":
        
            if Pilaespecial.esVacio():
                print("Error Revisa (Cierre sin apertura): ",caracter)
                Error_de_sintaxis=True
                break

        cima=Pilaespecial.ObtenerCima()

        if caracter == ")" and cima == "(" or caracter == "}" and cima == "{" or caracter == "]" and cima == "[":
            Pilaespecial.desapilar()

        else:

            if caracter == ")" or caracter == "}" or caracter == "]":
                print("Error Revisa (Apertura sin cierre): ",caracter)
                Error_de_sintaxis=True
                break

    if Pilaespecial.esVacio() and Error_de_sintaxis==False:
        print("La expresion es correcta")

    else:
        print("La expresion es incorrecta")