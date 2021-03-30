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
            while aux.siguiente != None:
                if nuevo.id < aux.siguiente.id:
                    nuevo.siguiente = aux.siguiente
                    aux.siguiente.anterior = nuevo
                    nuevo.anterior = aux
                    aux.siguiente = nuevo
                    break
                aux = aux.siguiente

            if aux.siguiente == None:
                aux.siguiente = nuevo
                nuevo.anterior = aux
    
    def devolver_encabezado(self, id):
        aux = self.primero
        while aux != None:
            if aux.id == id:
                return aux
            aux = aux.siguiente
        return None