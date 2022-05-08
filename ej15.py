# Ejercicio 15
print("Escribir un programa que calcule el promedio de un/una estudiante. Primero debe preguntar cuantas notas quiere ingresar. Luego pide las notas (comprendidas entre 0 y 10) por teclado y las almacena en una lista. A continuación debe mostrar todas las notas y el promedio. Nota: El promedio se calcula sumando todas las notas y dividiendo por la cantidad.\n")
a = int(input("Ingrese cantidad de notas a promediar:"))
n = [int(input("Primera nota: "))]
b = 0
prom = 0
for i in range((a-1)):
  b = int(input("Dame otro numero: "))
  while b < 0 or b > 10:
    b = int(input("Tiene que ser entre 0 y 10: "))
  n.append(b)
b = 0
for i in range(len(n)):
  prom += n[b]
  b += 1
print("El promedio es de:",prom/a)