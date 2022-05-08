# Ejercicio 3
print("Escribir un programa pida al usuario dos números enteros e imprima por pantalla todos los números pares entre ellos.\n")
a = int(input("Dame un numero entero: "))
b = int(input("Dame otro numero entero: "))
c = 0
if a < b:
  c = a
  while c < b:
    if c % 2 == 0:
      print(c)
    c += 1
elif b < a:
  c = b
  while c < a:
    if c % 2 == 0:
      print(c)    
    c += 1
else:
  print("No se puede si son iguales")