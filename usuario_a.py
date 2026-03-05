def fibonacci():
    n = int(input("Ingrese la cantidad de términos: "))

    if n <= 0:
        print("Debe ingresar un número positivo")
        return

    a = 0
    b = 1

    print("Serie Fibonacci:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()