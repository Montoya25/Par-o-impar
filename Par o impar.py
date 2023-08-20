# 1- Primero se solicita el número
num_str = input("Ingresa un número: ")
num = int(num_str)  # Convertir el valor ingresado a un número entero

# 2- Comprobar si es par o impar
if num % 2 == 0:
    print("Genial, tu número es par.")
else:
    print("Ups, tu número es impar.")