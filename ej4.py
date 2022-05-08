# Ejercicio 4
print("Escribir un programa que pida un número natural N y calcule la suma de todos los números entre 0 y N. Finalmente debe imprimir el resultado de la suma calculada por pantalla.\n")
a = int(input("Dame un num positivo: "))
b = 0
c = 0
if a > 0:
  while b < a:
    b += 1
    c += b
  print("Es toda la suma:",c)
else:
  print("Error master")