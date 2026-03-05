from usuario_a import fibonacci, capicua, numero_perfecto
from usuario_b import primos_en_rango, es_primo, factorial, mcd

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

        opciones_validas = ['0','1','2','3','4','5','6','7']

        if opcion not in opciones_validas:
            print("Opción inválida")
            continue

        elif opcion == '1':
            fibonacci()
            input("\nPresione Enter para continuar...")

        elif opcion == '2':
            capicua()
            input("\nPresione Enter para continuar...")
        
        elif opcion == '3':
            numero_perfecto()
            input("\nPresione Enter para continuar...")
        
        elif opcion == '4':
            primos_en_rango()
            input("\nPresione Enter para continuar...")
        
        elif opcion == '5':
            es_primo()
            input("\nPresione Enter para continuar...")  

        elif opcion == '6':
            factorial()
            input("\nPresione Enter para continuar...") 

        elif opcion == '7':
            mcd()   
            input("\nPresione Enter para continuar...")

        elif opcion == '0':
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()