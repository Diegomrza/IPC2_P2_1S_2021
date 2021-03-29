from Matriz import matriz_ortogonal

class nodo_simple:
    def __init__(self,x,y,nombre):
        self.siguiente = None
        self.x = x
        self.y = y
        self.nombre = nombre
        self.matriz = matriz_ortogonal()