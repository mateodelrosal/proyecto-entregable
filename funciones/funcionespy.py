def producto(n, k):
    resultado = 1
    for i in range(k + 1):  # Iteramos desde 0 hasta k
        resultado *= (n - i + 1)
    return resultado

n = 5
k = 3
print(producto(n, k))

def producto_secuencia_geometrica(a1, r, k):
    resultado = 1
    for n in range(k):
        an = a1 * (r ** n)  # Calcular el término a_n
        resultado *= an     # Multiplicar en el producto
    return resultado

# Ejemplo de uso
a1 = 2  # Primer término
r = 3   # Razón
k = 2   # Número de términos
print(producto_secuencia_geometrica(a1, r, k))

def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def combinatorio(n, k):
    if n < k:
        raise ValueError("n debe ser mayor o igual a k")
    return factorial(n) // (factorial(k) * factorial(n - k))

# Ejemplo de uso
n = 5
k = 2
print(f"C({n}, {k}) = {combinatorio(n, k)}")

import math

def combinatorio(n, k):
    """Calcula el número combinatorio C(n, k)."""
    if k > n:
        return 0
    return math.comb(n, k)

def S(n, k):
    """Calcula S(n, k) según la fórmula dada."""
    suma = 0
    for i in range(k + 1):
        # Calculamos el término (-1)^i * C(k + 1, i + 1) * (k - i)^n
        termino = (-1) ** i * combinatorio(k + 1, i + 1) * (k - i) ** n
        suma += termino
        
    resultado = suma / math.factorial(k)  # Dividimos por k!
    return resultado

# Ejemplo de uso
n = 5
k = 2
print(f"S({n}, {k}) = {S(n, k)}")

def newton_method(f, df, a, epsilon):
    """
    Aplica el método de Newton para encontrar una raíz de f(x).
    
    :param f: La función objetivo.
    :param df: La derivada de la función objetivo.
    :param a: Valor inicial.
    :param epsilon: Tolerancia del error.
    :return: Aproximación de la raíz.
    """
    x_n = a
    iteration = 0  # Contador de iteraciones
    while abs(f(x_n)) > epsilon:
        if df(x_n) == 0:
            raise ValueError("La derivada es cero. No se puede continuar.")
        
        # Actualiza x_n usando la fórmula de Newton
        x_n = x_n - f(x_n) / df(x_n)
        iteration += 1
        
        print(f"Iteración {iteration}: x_n = {x_n}, f(x_n) = {f(x_n)}")  # Muestra el progreso
        
    return x_n

# Ejemplo de uso
def f(x):
    return x**2 - 2  # Ejemplo: f(x) = x^2 - 2 (raíz en sqrt(2))

def df(x):
    return 2 * x  # Derivada: f'(x) = 2x

a = 1.0  # Valor inicial
epsilon = 1e-6  # Error tolerable

raiz = newton_method(f, df, a, epsilon)
print(f"La raíz aproximada es: {raiz}")