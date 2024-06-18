class Animal(): #clase padre

    def comer(self):
        print('el animal come')
    
    def dormir(self):
        print('el animal duerme')

class Mascota(Animal): #clase padre
    pass


class Felino: #clase hija

    def cazar(self):
        print('El felino caza')


class Gato(Mascota, Felino): #clase hija
    def __init__(self, nombre):
        self.nombre = nombre



patricio


