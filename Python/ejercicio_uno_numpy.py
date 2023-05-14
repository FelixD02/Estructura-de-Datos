import numpy as np

#Creamos un array de tamaño 30 para almacenar los votos de cada uno de los candidatos:
votos = np.zeros(30)

#Repartir los 5000 votos de manera aleatoria:
for i in range(5000):
    voto = np.random.randint(1, 31)
    votos[voto-1]+=1

votos_ordenados = np.argsort(-votos)

print("\nVOTOS OBTENIDOS POR CADA CANDIDATO: ")
for i in votos_ordenados:
    print(f"\nCandidato ({i+1}) : {votos[i]}")
    
#FELIX ADOLFO NIETO RANGEL | 2220093
