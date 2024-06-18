
class Animal():
    pass


class Mascota: #clase padre

    def comer(self):
        print('la mascota come')
    def dormir(self):
        print('la mascota duerme')

class Perro(Mascota): #clase hijo
    pass


class Felino():
    def cazar(self):
        print('el felino caza')


class Gato(Mascota,Felino): #herencia multiple
    pass




duke = Perro()

duke.comer()
duke.dormir()


patricio = Gato()

patricio.comer()#atributo de clase padre Mascota
patricio.cazar()#atributo de clase padre Felino
