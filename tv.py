
class Television:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def encenderTV(self):
        if self.mensaje == "Encender":
            print("TV encendida")
        else:
            print("TV Apagada")



Tv1 = Television("Apagado")
Tv1.encenderTV()
print("Listo")
