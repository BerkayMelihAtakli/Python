class Player:
    def __init__(self):
        self.__health = 5

    def show(self):
        print(self.__health)


p = Player()
p.show( )
p.__health = -50
p.show()
q = Player()
print(q.__health)

# In taak 1 was _health met één underscore alleen een afspraak