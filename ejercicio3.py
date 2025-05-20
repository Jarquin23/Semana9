calificaciones = []
for i in range(8):
    while True:
        try:
            calif = float(input(f"Ingrese la calificacion {i + 1}: "))
            if 0 <= calif <= 10:
                calificaciones.append(calif)
                break
            else:
                print("Por favor ingrese una calificacion entre 0 y 10.")
        except ValueError:
            print("Entrada inválida, por favor ingresa un número.")
prom = sum(calificaciones)/len(calificaciones)
print("\nCalificaciones ingresadsa: ", calificaciones)
print(f"El promedio de las calificaciones equivale a: {prom}")