class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class Arbol:
    def __init__(self):
        self.raiz = None

    def agregar_nodo(self, valor, padre=None):
        nuevo_nodo = Nodo(valor)
        if padre is None:
            if self.raiz is None:
                self.raiz = nuevo_nodo
            else:
                raise ValueError("El árbol ya tiene una raíz")
        else:
            padre.hijos.append(nuevo_nodo)

    def peso(self):
        if self.raiz is None:
            return 0
        return self.calcular_peso(self.raiz)

    def calcular_peso(self, nodo):
        peso = 1
        for hijo in nodo.hijos:
            peso += self.calcular_peso(hijo)
        return peso

    def orden(self):
        if self.raiz is None:
            return 0
        return self.calcular_orden(self.raiz)

    def calcular_orden(self, nodo):
        orden_max = 0
        for hijo in nodo.hijos:
            orden_hijo = self.calcular_orden(hijo)
            if orden_hijo > orden_max:
                orden_max = orden_hijo
        return 1 + orden_max

    def altura(self):
        if self.raiz is None:
            return 0
        return self.calcular_altura(self.raiz)

    def calcular_altura(self, nodo):
        altura_max = 0
        for hijo in nodo.hijos:
            altura_hijo = self.calcular_altura(hijo)
            if altura_hijo > altura_max:
                altura_max = altura_hijo
        return 1 + altura_max


arbol = Arbol()

arbol.agregar_nodo(1)
arbol.agregar_nodo(2, arbol.raiz)
arbol.agregar_nodo(3, arbol.raiz)
arbol.agregar_nodo(4, arbol.raiz.hijos[0])
arbol.agregar_nodo(5, arbol.raiz.hijos[0])
arbol.agregar_nodo(6, arbol.raiz.hijos[1])

peso_arbol = arbol.peso()
print("Peso:", peso_arbol)

orden_arbol = arbol.orden()
print("Orden:", orden_arbol)

altura_arbol = arbol.altura()
print("Altura:", altura_arbol)