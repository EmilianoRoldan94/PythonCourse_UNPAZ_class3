import os

def ejercicio(numero):
  n = b + repr(a) + c
  exec(open(n).read())
  
a = int(input("Dame el numero de ejercicio que necesites probar: "))
b = "ej"
c = ".py"
n = b + repr(a) + c

while a != 0:
  if a > 0 and a < 16:
    print("\nEjercicio",a,"\n")
    ejercicio(0)
    a = int(input("\nProbas otro ejercicio? poné 0 para terminar: "))
    os.system('clear')
  else:
    a = int(input("No es un numero de ejercicio válido, debe ser entre 1 y 15: "))
    os.system('clear')

print("\n\n\n   **** Finalizado ****")