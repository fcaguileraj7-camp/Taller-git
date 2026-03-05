from usuario_a import fibonacci, capicua, numero_perfecto
from usuario_b import primos_rango, es_primo, factorial, mcd

def menu():
    while True:
        print("\nCALCULADORA MATEMATICA")
        print("1. Fibonacci")
        print("2. Capicua")
        print("3. Número Perfecto")
        print("4. Números Primos en un Rango")
        print("5. Es Primo")
        print("6. Factorial")
        print("7. MCD")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            print("Saliendo...")
            break