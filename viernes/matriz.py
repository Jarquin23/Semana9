#MATRIZ
matriz = [[10, 2], [300, 4]]
print("-"*17)
#para imprimir dicha matriz
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6}", end = " ")
    print("|")
    print("-"*17)