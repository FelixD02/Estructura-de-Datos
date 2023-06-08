class Paciente:
    def __init__(self,nombre,edad,motivo,gravedad):
        self.nombre = nombre
        self.edad = edad
        self.motivo = motivo
        self.gravedad = gravedad
        self.next = None
        self.previous = None

    def mostrar_datos(self):
        print(self.nombre, self.edad, self.motivo, self.gravedad) 
        
class ColaPrioridad:
    def __init__(self):
        self.ultimo = None
        self.primero = None
        
    def is_empty(self):
        return self.primero is None
    
    def enqueue(self, nombre, edad, motivo, gravedad):
        nuevo_paciente = Paciente(nombre, edad, motivo, gravedad)
        if self.is_empty():
            self.primero = nuevo_paciente
            self.ultimo = nuevo_paciente
        else:
            actual = self.primero
            x = False
            while x is False:
                if nuevo_paciente.gravedad > actual.gravedad:
                    if actual == self.primero:
                        nuevo_paciente.next = actual
                        actual.previous = nuevo_paciente
                        self.primero = nuevo_paciente
                        x = True
                        break
                    else:
                        nuevo_paciente.previous = actual.previous
                        nuevo_paciente.next = actual
                        actual.previous = nuevo_paciente
                        x = True
                        break

                if nuevo_paciente.gravedad == actual.gravedad:
                    if actual.edad <= 12:
                        if nuevo_paciente.edad < actual.edad:
                            if actual == self.primero:
                                nuevo_paciente.next = actual
                                actual.previous = nuevo_paciente
                                self.primero = nuevo_paciente
                                x = True
                                break
                            else:
                                nuevo_paciente.previous = actual.previous
                                nuevo_paciente.next = actual
                                actual.previous = nuevo_paciente
                                x = True
                                break

                    if actual.edad >= 65:
                        if nuevo_paciente.edad > actual.edad:
                            if actual == self.primero:
                                nuevo_paciente.next = actual
                                actual.previous = nuevo_paciente
                                self.primero = nuevo_paciente
                                x = True
                                break
                            else:
                                nuevo_paciente.previous = actual.previous
                                nuevo_paciente.next = actual
                                actual.previous = nuevo_paciente
                                x = True
                                break

                if actual == self.ultimo:
                    nuevo_paciente.previous = self.ultimo
                    self.ultimo.next = nuevo_paciente
                    self.ultimo = nuevo_paciente
                    
                else:
                    actual = actual.next
    
    def imprimir(self):
        actual = self.primero
        while actual.next is not None:
            actual.mostrar_datos()
            actual = actual.next


urgencias = ColaPrioridad()

urgencias.enqueue("felix", 10, "gripe", 1)
urgencias.enqueue("brayan", 10, "gripe", 5)
urgencias.enqueue("matheo", 10, "gripe", 2)
urgencias.imprimir()