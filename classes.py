class Tuna:
    def __init__(self):
        print("dsmrpl")

    def swim(self):
        print("3")

flipper = Tuna()
flipper.swim()

class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
jason.get_energy()
sandy = Enemy(11)
sandy.get_energy()