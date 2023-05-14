import numpy as np
from faker import Faker 

fake = Faker()

estudiantes = np.empty((6500, 5), dtype=object)

for i in range(6500):
    estudiantes[i, 0] = nombre = fake.name() #Genera un nombre aleatorio
    estudiantes[i, 1] = np.random.randint(1000000, 10000000) #Genera un código aleatorio de 7 digitos
    estudiantes[i, 2] = round(np.random.rand()*5, 2) #Genera un promedio entre 0.0 y 5.0
    estudiantes[i, 3] = np.random.randint(1, 100) #Genera un codigo para los 99 diferentes pregrados.
    estudiantes[i, 4] = np.random.randint(1944, 2024) #Genera un año de ingreso entre el año 1994 y el año 2023
    
print("Ingrese el código de la carrera que desea consultar (1-99): ", end="") #Pide el codigo de la carrera en especifico que desea consultar
codigo_carrera = int(input())

while codigo_carrera < 1 or codigo_carrera > 99:
    print("*CÓDIGO NO VALIDO*")
    print("Ingrese el código de la carrera que desea consultar (1-99): ", end="")
    codigo_carrera = int(input())
    

print(f"\nESTUDIANTES CON PROMEDIO MAYOR O IGUAL A 4.0 DE LA CARRERA #{codigo_carrera}: ") #Imprime los datos de los estudiantes de una carrera X con promedio mayor a 4.2
total_estudiantes = 0
for x in range(6500):
    if estudiantes[x, 3] == codigo_carrera and estudiantes[x, 2] >= 4.0:
        total_estudiantes += 1
        print(f"Nombre: {estudiantes[x, 0]} | Código: {estudiantes[x, 1]} | Promedio: {estudiantes[x, 2]}")
print(f"->Total de Estudiantes: {total_estudiantes}")


print("\nESTUDIANTES QUE INGRESARON ANTES DE 1990 Y ESTÁN CONDICIONALES: ")
for x in range(6500):
    if estudiantes[x, 4] < 1990 and estudiantes[x, 2] > 2.7 and estudiantes[x, 2] < 3.2: #Imprime los datos de los estudiantes que entraron antes de 1990 y su promedio está entre 2.7 y 3.2
        print(f"Nombre: {estudiantes[x, 0]} | Código: {estudiantes[x, 1]} | Promedio: {estudiantes[x, 2]} | Año: {estudiantes[x, 4]}")

#FELIX ADOLFO NIETO RANGEL | 2220093        
        