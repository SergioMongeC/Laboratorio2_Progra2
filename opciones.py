def calculoPaga(**Kargs):
    try:
        pagaPendiente = str(int(Kargs["horasTrabajadas"]) * int(Kargs["costoHora"]))
        pagaPendiente += " es tu paga." 
    except BaseException:
        pagaPendiente = "No se pudo realizar la operación, ingrese números enteros."
        
    return pagaPendiente

def mensajeBienvenida(nombre):
    try:
        bienvenida = "Bienvenido a la UIA {0}"
        bienvenida = bienvenida.format(nombre)
        mensaje =  bienvenida.upper() + "\n" + bienvenida.lower()
    except BaseException:
        mensaje = "No se pudo realizar la operación."
        
    return mensaje

def checkNumeroEntero(numeroStr): 
    try:
        numero = int(numeroStr)
        if (numero > 0 and numero < 11):
            numero = numero**2
        elif(numero > 10 and numero < 21):
            numero = numero**4
        elif(numero > 20 and numero < 31):
            numero = numero**6
        elif(numero > 30 and numero < 41):
            numero = numero**8
        elif(numero > 40 and numero < 51):
            numero = numero**10        
        else:
            numero = 0
            
        mensaje = "El nuevo número es " + str(numero)

    except BaseException:
        mensaje = "No se pudo realizar la operación, ingrese números enteros."
    
    return mensaje
        
def numeroPrimos(numeroStr): 
    try:
        numero = int(numeroStr)
        mensaje = "El número "+ str(numero) + " ES PRIMO."
        
        for i in range(2, numero):
            if (numero % i) == 0:
                mensaje = "El número "+ str(numero) + " NO ES PRIMO."
                break
                
    except BaseException:
        mensaje = "No se pudo realizar la operación."
        
    return mensaje

def cantidadDeA(texto):
    try:
        numOcurrencias = texto.lower().count("a")   
        mensaje = "La letra 'a' aparece en el texto brindado "+str(numOcurrencias)
        if (numOcurrencias == 1):
            mensaje += " vez."
        else:
            mensaje += " veces."
        
    except BaseException:
        mensaje = "No se pudo realizar la operación."
        
    return mensaje