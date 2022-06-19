#uso del context manager

class Manejo_Archivos:
    def __init__(self,nombre):
        self._nombre = nombre

    def __enter__(self):
        print("obtenemos el recurso".center(50,"*"))
        self.nombre = open(self._nombre,"r",encoding="utf8")
        return self._nombre

    def __exit__(self,tipo_exepcion, valor_exepcion, traza_error):
        print("cerramos el recurso".center(50,"*"),)
        if self.nombre:
            self.nombre.close()