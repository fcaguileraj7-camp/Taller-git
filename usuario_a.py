def fibonacci():
    n = int(input("Ingrese la cantidad de términos: "))
    
    a = 0
    b = 1

    print("Serie Fibonacci:")

    for i in range(n):
        print(a)
        a, b = b, a + b