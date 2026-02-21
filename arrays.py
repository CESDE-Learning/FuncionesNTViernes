import random

notas=[]

# For para llenar el array
for i in range(5):
    notasSimulada = random.randint(1,5)
    notas.append(notasSimulada)

notas.insert(0,80) # Meter un dato, selecionado un lugar
notas.remove(80) # Quitar un especifico
notas.pop(0) # Eliminar un elemnto
notas.sort(reverse=False) # False: Menor a Mayor | True: Mayor a Menor
notas.clear() # Limpiar los datos

print(notas)