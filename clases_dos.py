class Usuario:
    
    def inicializar(self, username, password):
        self.username = username 
        self.password= password


user1 = Usuario()
user2 = Usuario()

user1.inicializar('User1', 'password1')
user2.inicializar('user2', 'password2')

print(user1.__dict__)
print(user2.__dict__)

