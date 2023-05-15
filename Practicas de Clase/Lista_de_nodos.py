class Nodo:
    
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
    def devolver_valor(self):
        print(self.valor)
        
    def asignar_siguiente(self, nodo):
        self.siguiente = nodo
        
    def cambiar_valor(self, nuevo_valor):
        self.valor = nuevo_valor
        

#primera_lista = [1, 2, 3, 4, 5]

#for numero in primera_lista:
    #print(numero)
    
lista_nodos = []

nodo1 = Nodo("A")
nodo2 = Nodo("B")
nodo3 = Nodo("C")
nodo4 = Nodo("D")

lista_nodos.append(nodo1)
lista_nodos.append(nodo2)
lista_nodos.append(nodo3)
lista_nodos.append(nodo4)


for nodo in lista_nodos:
    print(nodo.valor)




