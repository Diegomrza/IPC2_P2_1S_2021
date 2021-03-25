class nodo:
    def __init__(self,fila,columna,contenido):
        self.fila = fila
        self.columna = columna
        self.contenido = contenido
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None

class nodo_encabezado:
    def __init__(self, id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None