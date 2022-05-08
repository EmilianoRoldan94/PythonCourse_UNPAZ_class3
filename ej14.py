# Ejercicio 14
print("Escribir un programa que pida palabras y las almacene en una lista, hasta que el usuario ingrese la palabra “fin”. Luego debe mostrar en pantalla cada palabra almacenada en la lista pero repetida 5 veces. Por ejemplo, si la palabra es “hola”, se debe mostrar “holaholaholaholahola”. Nota: Recuerden como funciona el operador producto “*” entre un string y un entero.\n")
a = [input("Ingrese la primer palabra: ")]
b = 0
while a[-1] != "fin":
  a.append(input("Ingrese otra palabra(fin para terminar):"))
for i in range(len(a)):
  print(a[b] * 5)
  b += 1