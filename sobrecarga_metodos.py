class SerVivo:
    def dormir(self):
        print('El ser duerme')


class Animal(): #clase padre

    def comer(self):
        print('el animal come')
    
    def dormir(self):
        print('el animal duerme')

class Mascota(Animal): #clase padre
    
    def comer(self):
        print('la mascota come')


class Felino: #clase hija

    def cazar(self):
        print('El felino caza')


class Gato(SerVivo, Mascota, Felino): #clase hija
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer(self):
        super().comer()
        print(f'{self.nombre} come')



patricio = Gato('Patricio')
patricio.comer()
patricio.dormir()
patricio.cazar()


