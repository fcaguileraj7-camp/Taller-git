def primos_en_rango():
    inicio = int(input("Ingresa el número inicial: "))
    fin = int(input("Ingresa el número final: "))

    if inicio > fin:
        print("El número inicial debe ser menor o igual al número final.")
        return

    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primos = [num for num in range(inicio, fin + 1) if es_primo(num)]

    print("Números primos:", primos)


def es_primo():
    numero = int(input("Ingrese un número: "))

    if numero <= 1:
        print("El número NO es primo")
        return

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print("El número NO es primo")
            return

    print("El número es primo")


def factorial():
    n = int(input("Ingrese un número: "))

    if n < 0:
        print("El factorial no está definido para números negativos.")
        return

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    print("El factorial es:", resultado)


def mcd():
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    while b != 0:
        a, b = b, a % b

    print("El MCD es:", a)



