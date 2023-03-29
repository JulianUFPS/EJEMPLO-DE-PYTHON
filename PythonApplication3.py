
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b


num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
operacion = input("Ingresa la operacion deseada (+, -, *, /): ")


if operacion == "+":
    resultado = suma(num1, num2)
elif operacion == "-":
    resultado = resta(num1, num2)
elif operacion == "*":
    resultado = multiplicacion(num1, num2)
elif operacion == "/":
    resultado = division(num1, num2)
else:
    resultado = "Error: Operacion no valida"


print("El resultado de la operacion es: ", resultado)