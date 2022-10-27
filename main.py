import opciones as op
from os import system

salir = False
resultado = ""

system("cls")

while (not salir):
    try:
        opUsuario = input("¡Hola!, Ingrese el número de alguna de las siguientes opciones: \n" +
                        "   1) Calculo de Paga según horas trabajadas\n"+
                        "   2) Mensaje de Bienvenida\n"+
                        "   3) Operaciones con números enteros\n"+
                        "   4) ¿Número Primo?\n"+
                        "   5) ¿Cuantás 'a' tiene tu cadena de texto?\n"+
                        "   6) Terminar el programa\n")     
        if (not opUsuario.isdigit()):
            system("cls")
            print("* Las opciones digitadas deben ser númeroso.\n\n")
            continue
        elif (opUsuario == '1'):
            system("cls")
            print("|| Cálculo de Paga según horas trabajadas ||\n")
            horasTrabajadas = input("Ingrese la cantidad de horas trabajadas: ")
            costoHora = input("Ingrese su paga por cada hora laborada: ")
            resultado = op.calculoPaga(horasTrabajadas = horasTrabajadas, costoHora = costoHora)           
        elif (opUsuario == '2'):
            system("cls")
            print("|| Mensaje de Bienvenida ||\n")
            nombre = input("Ingrese su nombre: ")
            resultado = op.mensajeBienvenida(nombre)                
        elif (opUsuario == '3'):
            system("cls")
            print("|| Operaciones con números enteros ||\n")
            numero = input("Ingrese un número entero: ")
            resultado = op.checkNumeroEntero(numero)      
        elif (opUsuario == '4'):
            system("cls")
            print("|| ¿Número Primo? ||\n")
            numero = input("Ingrese un número entero: ")
            resultado = op.numeroPrimos(numero)  
        elif (opUsuario == '5'):
            system("cls")
            print("|| ¿Cuantás 'a' tiene tu cadena de texto? ||\n")
            texto = input("Ingrese el texto a verificar: ")
            resultado = op.cantidadDeA(texto)     
        elif (opUsuario == '6'):
            system("cls")
            print ("Programa Finalizado.\n\n")
            break
        else:
            system("cls")
            print ("No existe una opción con ese número.\n\n")
            
        print("\n" + resultado + "\n")
        continue
    except BaseException:
        system("cls")
        print ("* Usted no digito una opción numerica válida.\n\n")
            
input()