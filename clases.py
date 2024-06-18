"""
class Usuario:
    pass

cody = Usuario()
print (cody)

"""

#atributos de clase

class Usuario:
    username =" Username por default" #atributos dentro de la clase 
    email =""

print(Usuario.username)
#     clase.atributo

Usuario.username = "User 1"
print(Usuario.username)


#atributos de instancia 

class User:
    username = "Usuario por default"
    email = ""

#__dict__ 
user1 = User()
#1.- verifica si el atributo existe denro del objeto
#2.- verifica si el atibuto existe dentro de la clase -> lectura 
#3.- lanzara un error 
user1.username="Cody" #añadir atributo al objeto
print(user1.username) # de instancia 

print(id(user1.username))
print(id(User.username))
print(user1.__dict__)