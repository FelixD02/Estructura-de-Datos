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
                
lista = Lista() 

while True:
    
    print("\nMenú de opciones: ")
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")
    
    opcion = int(input("Ingrese el número de opción que desea ejecutar: "))

    if opcion == 1:
        print("\n*Ha seleccionado [Añadir número a la lista]")
        numero = int(input("Ingrese el número que desea añadir a la lista: "))
        lista.agregar_cola(numero)
        limpiar_pantalla()
        
    elif opcion == 2:
        print("\n*Ha seleccionado [Añadir número de la lista en una posición]")
        numero = int(input("Ingrese el número que desea añadir a la lista: "))
        posicion = int(input("Ingrese la posición en la que desea agregar el número: "))
        lista.agregar_posicion(numero,posicion)
        limpiar_pantalla()

    elif opcion == 3:
        print("\n*Ha seleccionado [Longitud de la lista]")
        print(f"La longitud de la lista es: {lista.tamaño()}")
    
    elif opcion == 4:
        print("\n*Ha seleccionado [Eliminar el último número]")
        lista.eliminar_ultimo()
        limpiar_pantalla()
        
    elif opcion == 5:
        print("\n*Ha seleccionado [Eliminar un número]")
        posicion = int(input("Ingrese la posicion del número que desea borrar: "))
        lista.eliminar_posicion(posicion)
        limpiar_pantalla()
    
    elif opcion == 6:
        print("\n*Ha seleccionado [Contar números]")
        numero = int(input("Ingrese el número que desea buscar: "))
        print(f"El número {numero} aparece {lista.contar_apariciones(numero)} veces en la lista.")
        
    elif opcion == 7:
        print("\n*Ha seleccionado [Posiciones de un número]")
        numero = int(input("Ingrese el número que desea buscar: "))
        apariciones = lista.buscar_posiciones(numero)
        print(f"El numero {numero} aparece en la posiciones: {apariciones}")
    
    elif opcion == 8:
        print("\n*Ha seleccionado [Mostrar números]")
        lista.imprimir_lista()
    
    elif opcion == 9:
        print("Menú Cerrado")
        break 
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")