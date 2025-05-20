array_str = ["uno", "dos", "tres", "cuatro", "cinco"]
print("Array de cadenas: ", array_str)
#Insertar un elemento al inicio del arreglo
array_str.insert(3, "cero")
print("Array de cadenas con el elemento cero agregado: ", array_str)
#Contar cuantos elementos hay en un arreglo
cantidad = len(array_str)
print("Cantidad de elementos en el arreglo: ", array_str)
#Eliminar un elemento del arreglo
array_str.remove("tres")
print("Array de caenas después de eliminar 'tres': ", array_str)
#Eliminar un elemento del arreglo por posición
array_str.pop(2)
print("Array de cadenas después de eliminar el elemento en la posicion 2:", array_str)