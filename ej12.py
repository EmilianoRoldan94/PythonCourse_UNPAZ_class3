# Ejercicio 12
print("Escribir un programa que almacene las asignaturas de un curso, por ejemplo Matemática, Física,Química, Historia y Lengua, en una lista y luego muestre por pantalla los mensajes (en diferenteslíneas) “Yo estudio <asignatura>”, donde <asignatura> es cada una de las asignaturas de la lista.\n")
a = ["Matematicas","Lenguas","Ingles","Naturales","Humanidades","Filosofia","MySQL","C#","Kali Linux"]
b = 0
for i in range(len(a)):
  print("Yo estudio",a[b])
  b += 1