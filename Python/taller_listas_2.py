def limpiar_pantalla():
    print('\033c', end='')

class Nodo:
    
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    
class Lista:
    
    def __init__(self):
        self.cabeza = None
    
    def lista_vacia(self):
        return self.cabeza is None
    
    def imprimir_lista(self):
        if self.lista_vacia():
            print("La lista está vacia")
        else:
            nodo_actual = self.cabeza
            while nodo_actual:
                print(nodo_actual.valor)
                nodo_actual = nodo_actual.siguiente
        
    
    #AGREGA UN NODO AL FINAL:
    def agregar_cola(self,valor):
        nuevo_nodo = Nodo(valor)
        if self.lista_vacia():
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            
    #AGREGA UN NODO EN UN POSICIÓN EN ESPECIFICO:
    def agregar_posicion(self,valor,posicion):
        posicion = posicion - 1
        nuevo_nodo = Nodo(valor)
        
        if self.lista_vacia():
            if posicion == 0:
                self.cabeza = nuevo_nodo
            else:
                print("**La lista está vacia**")
                return 
        
        if posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return
        
        nodo_actual = self.cabeza
        indice = 0
        while nodo_actual:
            
            if indice == posicion - 1:
                nuevo_nodo.siguiente = nodo_actual.siguiente
                nodo_actual.siguiente = nuevo_nodo
                return
            nodo_actual = nodo_actual.siguiente
            indice += 1
        print("**La posición no está en el rango de la lista** ")
        return
    
    #MUESTRA EL TAMAÑO:
    def tamaño(self):
        tamaño = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            tamaño += 1
            nodo_actual = nodo_actual.siguiente
        return tamaño
    
    #ELIMINA EL ULTIMO NODO:
    def eliminar_ultimo(self):
        if self.lista_vacia():
            print("**La lista está vacía**")
            return
        
        if self.cabeza.siguiente is None:
            print(f"El número borrado es: {self.cabeza.valor}")
            self.cabeza = None 
            return
        
        nodo_actual = self.cabeza
        while nodo_actual.siguiente.siguiente:
            nodo_actual = nodo_actual.siguiente
        print(f"El número borrado es: {nodo_actual.siguiente.valor}")
        nodo_actual.siguiente = None
        
    #ELIMINA UN NODO EN ESPECIFICO:
    def eliminar_posicion(self, posicion):
        if self.lista_vacia():
            print("**La lista está vacia**")
            return

        if posicion == 1:
            valor_eliminado = self.cabeza.valor
            self.cabeza = self.cabeza.siguiente
            print("Número eliminado:", valor_eliminado)
            return

        nodo_actual = self.cabeza
        indice = 1
        while nodo_actual:
            if indice == posicion - 1:
                if nodo_actual.siguiente is None:
                    print("Error: la posición está fuera de rango.")
                    return
                valor_eliminado = nodo_actual.siguiente.valor
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                print("Número eliminado:", valor_eliminado)
                return
            nodo_actual = nodo_actual.siguiente
            indice += 1

        print("Error: la posición está fuera de rango.")
        
    def contar_apariciones(self, numero):
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.valor == numero:
                contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador
    
    def buscar_posiciones(self, numero):
        posiciones = []
        nodo_actual = self.cabeza
        indice = 1
        while nodo_actual:
            if nodo_actual.valor == numero:
                posiciones.append(indice)
            nodo_actual = nodo_actual.siguiente
            indice += 1
        return posiciones
    
    