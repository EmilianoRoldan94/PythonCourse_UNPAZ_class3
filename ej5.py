# Ejercicio 5
print("Escribir un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa no comprobará que las cantidades sean positivas.\n")
a = int(input("Limite de alcancía: "))
b = 0
while b < a:
  b += int(input("Cuanto guardas hoy? "))
  print("El total es: $",b)