array_int = [5,4,9,2,1]
print("Array de enteros: ", array_int)
array_int.sort(reverse=True)
print("Array de enters ordenado: ", array_int)
array_int.sort(reverse=True)
print("Array de enteros ordenado inverso: ", array_int)
elemento= 4
if elemento in array_int:
    print("El elemento ", elemento, " se encuentra en el array")
else:
    print("El elemento ", elemento, " no se encuentra en el array")
array_int.append(6)
print("Array de enteros con el elemento 6 agregado: ", array_int)