from NodoSimple import nodo_simple

class ListaSimple:
    def __init__(self):
        self.primero = None
        self.tamanio = 0
        
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
            aux.matriz.recorrerFilas()    
            aux = aux.siguiente

    def verificar_nombre(self,nombre):
        aux = self.primero
        while aux != None:
            if aux.nombre == nombre:
                return True
            aux = aux.siguiente
        return False

    def mostrar_elemento(self, id):
        aux = self.primero
        while aux != None:
            if aux.nombre == id:
                return aux
            aux = aux.siguiente

    def obtener_tamanio(self):
        aux = self.primero
        while aux != None:
            self.tamanio += 1
            aux = aux.siguiente
        return self.tamanio
    
    