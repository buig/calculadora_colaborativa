# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

# Otras funciones serán añadidas por colaboradores

def multiplica(a,b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "No se puede dividir por cero"

def maximo(a, b):
    if a > b:
        return a
    return b

def minimo (a, b):
    return maximo(b, a)