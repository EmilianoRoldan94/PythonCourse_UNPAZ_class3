# Ejercicio 8
print("Escriba un programa que cree una lista de números enteros que contenga los siguientes números: 2 , 3 , 5 , 9 , 12 , 15 , 3 , 6 , 7. Luego debe mostrar por pantalla el contenido de la la lista y su tamaño. Finalmente debe eliminar los últimos dos elementos de la lista y volver a mostrar su contenido y longitud por pantalla, para ver como quedó luego de eliminarlos.\n")
a = [2 ,3 , 5 , 9 , 12 , 15 , 3 , 6 , 7]
print(a,"\nLongitud de lista:",len(a))
a.remove(7)
a.remove(6)
print(a,"\nLongitud de lista:",len(a))