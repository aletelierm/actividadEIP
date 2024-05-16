class AireAcondicionado:
    def __init__(self, mensaje,temp, intencidad):
        self.mensaje = mensaje
        self.temp = temp
        self.intencidad = intencidad

    def encenderAire(self):
        if self.mensaje == "Tengo Frio":
            print (f"""Se ha encendido el aire {self.temp} grados y con una intencidad
                    {self.intencidad}""")
        elif self.mensaje == "Tengo Calor":
            print (f"""" Se ha encendido el aire {self.temp} grados y con una intencidad
                   {self.intencidad}""")
        else:
            print("No te entendi ctm !")

Aire = AireAcondicionado("Tengo Frio",23,"alta")
Aire2 = AireAcondicionado("Tengo Calor", 21,"baja")
Aire3 = AireAcondicionado("Nada",0,"nada")
Aire.encenderAire()
Aire2.encenderAire()
Aire3.encenderAire()