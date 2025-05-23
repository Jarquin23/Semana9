#MATRIZ
matriz = [["José", "Roger", "Carlos"],
          ["Ariadna", "Daniela", "Rommel"],
          ["Chelsea", "Mery", "Winnyver"]]
cant_letras = []
for fila in matriz:
    for columna in fila:
        print(f"|{columna}", end = " ")
    print(" | ")
    print("-"*17)

for fila in matriz:
    new_row = []
    for nombre in fila:
        new_row.append(len(nombre))
        print(f"|{nombre:>6}", end = " ")
    print("|")
    print("-"*17)
    cant_letras.append(new_row)

for fila in cant_letras:
    for cantidad in fila:
        print(f"| {cantidad:>6}", end = " ")
    print("|")
    print("-"*17)