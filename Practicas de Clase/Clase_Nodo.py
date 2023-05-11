class Nodo: 

    #Constructor Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    #Método Ver el valor:
    def devolver_valor(self):
        print(self.valor)

    #Método Asignar siguiente:
    def asignar_siguiente(self,nodo):
        self.siguiente = nodo

    #Método cambiar valor siguiente:
    def cambiar_valor(self,nuevo_valor):
        self.valor = nuevo_valor

    
Nodo1 = Nodo("A")
Nodo2 = Nodo("C")
print(Nodo2)

#print(Nodo1.siguiente)

# Primera Forma:
#Nodo1.devolver_valor()

# Segunda Forma:
#Nodo.devolver_valor(Nodo1)


Nodo1.cambiar_valor("B")

Nodo1.devolver_valor()

Nodo1.asignar_siguiente(Nodo2)

print(Nodo1.siguiente)


