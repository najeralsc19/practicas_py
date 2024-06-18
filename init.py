#__init__

class Usuario:
    def __init__(self, username = '', password= ''):
       self.username = username
       self.password = password


user1 = Usuario('user1','password1')
user2 = Usuario()


print(user1.__dict__)
print(user2.__dict__)