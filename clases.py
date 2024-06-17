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
#2.- 
print(user1.username)

print(user1.__dict__)