
class Ampolleta:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def encenderLuz(self):
        if self.mensaje == "Encender":
            print("Luz encendida")
        else:
            print("Luz Apagada")



Ampolleta1 = Ampolleta("Apagado")
Ampolleta1.encenderLuz()
print("Listo")
