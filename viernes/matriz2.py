#MATRIZ
matriz = [[10.8, 2.3], [30.85, 4.16]]
print("-"*17)
#para imprimir dicha matriz
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6.1f}", end = " ")
    print("|")
    print("-"*17)