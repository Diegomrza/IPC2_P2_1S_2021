from NodoSimple import nodo_simple

class ListaSimple:
    def __init__(self):
        self.primero = None
        
    def insertar_simple(self, nombre, x, y, matriz):
        nuevo = nodo_simple(x, y, nombre)
        nuevo.matriz = matriz

        if self.primero == None:
            self.primero = nuevo
        else:
            auxiliar = self.primero
            while auxiliar.siguiente != None:
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente = nuevo


    def mostrar_simple(self):
        aux = self.primero
        while aux != None:
            print(aux.nombre)
            aux = aux.siguiente


