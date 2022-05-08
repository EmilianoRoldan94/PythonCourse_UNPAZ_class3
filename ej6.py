# Ejercicio 6
print("Escribir un programa que vaya pidiendo números positivos y mostrando si el número ingresado es par o impar, el programa debe dejar de pedir números cuando el usuario ingresa un número negativo.\n")
a = int(input("Dame un positivo: "))
if a > 0:
  while a > 0:
    if a % 2 == 0:
      print("es par\n")
    else:
      print("no es par\n")
    a = int(input("\nDame un positivo: "))
else:
  print("Error, solo positivos")