notas = []

for i in range(3):
    nota_valida = False #controlar si la nota es valida
    while not nota_valida: #se repite el bucle hasta que la nota sea valida
        entrada = input(f"Ingrese la nota {i+1}: ") #se pide la nota
        if entrada.replace(".", "", 1).isdigit(): #se verifica si la nota es un numero
            nota = float(entrada) #se convierte la nota a un numero
            if 0 <= nota <= 10: #se verifica si la nota es valida
                notas.append(nota) #se agrega la nota a la lista
                nota_valida = True #se sale del bucle
            else:
                print("La nota debe estar entre 0 y 10") #se muestra un mensaje de error
        else:
            print("La nota debe ser un numero") #se muestra un mensaje de error
    

suma = sum(notas)
promedio = suma / len(notas)

print(f"El promedio de las notas es: {promedio:.2f}")

#alumnos segun el promedio desaprobado, aprobado, excelente, sobresaliente

if promedio >= 9:
    print("El alumno está sobresaliente")
elif promedio >= 8:
    print("El alumno está excelente")
elif promedio >= 6:
    print("El alumno está aprobado")
else:
    print("El alumno está desaprobado")