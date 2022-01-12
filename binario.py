# Presento dos formas de realizar este ejercicio

def esBinario(numero):
    for i in numero:
        if int(i) != 1 and int(i) != 0:
            return False
    return True

# Esta primera forma es más óptima desde el punto de vista del programador 
try:
    decimal = int(input("Introduce un número en binario: "), 2)
    print(f"El número introducido en decimal es {decimal}")
except ValueError:
    print("Debes introducir un número binario")

# En esta segunda forma se calcula el número con las divisiones sucesivas
# try:
#     binario = input("Introduce un número binario: ")

#     if not esBinario(binario):
#        raise ValueError
            
#     digitos = [int(i) for i in str(binario)]
#     digitos.reverse()

#     decimal = 0

#     for idx, value in enumerate(digitos):
#         decimal += value*(2**(idx))
        
#     print(f"El número {binario} en decimal es {decimal}")
# except:
#     print("Debes introducir un número binario.")
