import os
import random
import time
participantes = list()
while True:
    os.system("cls")
    os.system("color 0a")
    nombre = input("Ingrese el nombre del participante (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    participantes.append(nombre.upper())
os.system("cls")
print("participante agregado...")
print(participantes)
x = input("Presiona una tecla")
cont = 10
while cont > 0:
    os.system("cls || clear")
    print(cont)
    time.sleep(1)
    cont -=1
os.system("cls || clear")
fin = len(participantes) -1
ganador = random.randint(0, len(participantes))
print(f"Ganador: {participantes[ganador]}")