def primos_en_rango(inicio, fin):
    def es_primo(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    return [num for num in range(inicio, fin + 1) if es_primo(num)]


# Pedir datos al usuario
inicio = int(input("Ingresa el número inicial: "))
fin = int(input("Ingresa el número final: "))

# Validación básica
if inicio > fin:
    print("El número inicial debe ser menor o igual al número final.")
else:
    primos = primos_en_rango(inicio, fin)
    print(f"Números primos entre {inicio} y {fin}:")
    print(primos)

def es_primo(numero):
    # Validar que sea mayor que 1
    if numero <= 1:
        return False
    
    # Verificar divisores desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    
    return True
# Programa principal
num = int(input("Ingrese un número: "))

if es_primo(num):
    print("El número es primo.")
else:
    print("El número NO es primo.")

def factorial(n):
    # Validar que no sea negativo
    if n < 0:
        return None
    
    resultado = 1
    
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado
# Programa principal
num = int(input("Ingrese un número: "))

resultado = factorial(num)

if resultado is None:
    print("El factorial no está definido para números negativos.")
else:
    print(f"El factorial de {num} es: {resultado}")

def mcd(a, b):


