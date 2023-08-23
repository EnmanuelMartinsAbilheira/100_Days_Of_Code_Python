class User:
    
    def __init__(self, user_id, username, follower):
        self.id = user_id
        self.username = username
        self.follower = 0

user_1 = User("001", "enmanuel")
user_2 = User("001", "angela")



# es lo mismo que arriba para eso el __init__ para inicializar
#class User:
#    pass
#user_1 = User()
#user_1.id = "001"
#user_1.username = "enmanuel"
#
#print(user_1)
#
#user_2 = User()
#user_2.id = "001"
#user_2.username = "enmanuel"
