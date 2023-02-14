"""
se pide un ingreso de numeros separado en comas
se crea un for para que navegue en la entrada de los numeros y los separe 
al mismo tiempo se guarda en lista
despues se crea la variable tupla
y ya solo se imprime 
"""

Entrada = input("Por favor ingrese la lista de números separados por comas: ")

Lista = [int(x) for x in Entrada.split(",")]
Tupla = tuple(Lista)

print(Lista)
print(Tupla)