import random

def crearNotas(cantidadDeNotas):
    totalNotas=[]
    for _ in range(cantidadDeNotas):
        nota=random.randint(1,5)
        totalNotas.append(nota)

    return totalNotas

resultado=crearNotas(5)
print(resultado)