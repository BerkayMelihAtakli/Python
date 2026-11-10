class Thermostat:
    def __init__(self):
        self.__target = 20

    def show(self):
        print(self.__target)

t = Thermostat()
t.show()

t.__target = 25
t.show()

u = Thermostat()
print(u.__target + 2)



# De class mist twee soorten methodes: een getter (om de waarde te
# lezen en terug te krijgen) en een setter (om de waarde veilig te
# veranderen).