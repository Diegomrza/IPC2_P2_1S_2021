from Nodos import nodo, nodo_encabezado

class lista_encabezado:

    def __init__(self, primero = None):
        self.primero = primero
    
    def insertar(self, nuevo):
        if self.primero == None:
            self.primero = nuevo
        elif nuevo.id < self.primero.id:
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        else:
            aux = self.primero
            while aux.siquiente != None:
                if nuevo.id < aux.siquiente.id:
                    nuevo.siguiente = aux.siquiente
                    aux.siquiente.anterior = nuevo
                    nuevo.anterior = aux
                    aux.siquiente = nuevo
                    break
                aux = aux.siquiente

            if aux.siquiente == None:
                aux.siquiente = nuevo
                nuevo.anterior = aux
    
    def devolver_encabezado(self,id):
        aux = self.primero
        while aux != None:
            if aux.id == id:
                return aux
            aux = aux.siquiente
        return None