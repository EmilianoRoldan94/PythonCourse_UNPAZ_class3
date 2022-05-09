# Ejercicio 13
print("Escribir un programa que pida 10 números enteros y los almacene en una lista. Luego debe recorrer la lista y contar cuantos números pares se ingresaron. Finalmente debe imprimir el contenido de la lista y la cantidad de números pares encontrados. Nota: Para ver si un número es par o impar deben usar un “if”.\n")

''' ver 0.1
a = [int(input("Dame el primer numero: "))]
pares = 0
b = 0
for i in range(9):
  a.append(int(input("Dame otro numero: ")))
for i in range(len(a)):
  if a[b] % 2 == 0:
    pares += 1
  b += 1
print(a,"\nCant. numeros pares:",pares,)
'''
# ver 0.2 (1 linea menos)
a = [int(input("Dame el primer numero: "))]
par = 0
for i in range(9):
  if a[-1] % 2 == 0:
    par += 1
  a.append(int(input("Dame otro numero: ")))
if a[-1] % 2 == 0:
  par += 1
print("Total de pares:",par)


