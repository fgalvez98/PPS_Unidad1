class Error(Exception):
    pass

class NotInRange(Error):
    pass

class NotInList(Error):
    pass

def estaEnRango(valor, minimo, maximo):
    if valor < minimo or valor > maximo:
        return False
    return True

def estaEnLista(valor, lista):
    if valor in lista:
        return True
    return False

minimo = 0
maximo = 20
lista = [6, 14, 11, 3, 2, 1, 15, 19]

try:
    numero = int(input(f"Introduce un número entre {minimo} y {maximo}: "))

    if not estaEnRango(numero, minimo, maximo):
        raise NotInRange
    else:
        print(f"El número está entre {minimo} y {maximo}")

    if not estaEnLista(numero, lista):
        raise NotInList
    else:
        print("El valor introducido está en la lista.")

except NotInRange:
    print("El número no está entre 1 y 20.")
except NotInList:
    print("El número no está en la lista.")