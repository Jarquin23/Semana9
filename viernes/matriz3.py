#MATRIZ
matriz = [["José", "Roger", "Carlos"], ["Ariadna", "Daniela", "Rommel"], ["Chelsea", "Mery", "Winnyver"]]
print("-"*17)
#para imprimir dicha matriz
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6}", end = " ")
    print(" | ")
    print("-"*17)