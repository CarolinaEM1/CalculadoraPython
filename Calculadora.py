#Construir un programa que simule el funcionamiento de una calculadora que puede realizar las 4 operaciones aritmeticas básicas.
#El usuario debe especificar la operación con el primer caracter del nombre de la operación.

print("Hola, esta es una simulación de calculadora, por favor digita con un caracter dependiendo la operación que deseas realizar")
print("S-> suma, R-> resta, M-> multiplicación, D-> División")

letra = input("Digita la letra según la operación: ").lower()
num1 = int(input("Digita el número 1: "))
num2 = int(input("Digita el número 2: "))

if letra=='s':
    print(f"La suma de los números es {num1+num2}")
elif letra=='r':
    print(f"La resta de los números es {num1-num2}")
elif letra=='m':
    print(f"La multiplicación de los números es {num1*num2}")
elif letra=='d':
    print(f"La división de los números es {num1/num2}")
else:
    print("Se equivcó de operación")

#Carolina EM
