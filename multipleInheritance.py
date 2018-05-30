class Mario():
    def move(self):
        print("i move")

class Shroom():
    def eat_shroom(self):
        print("i big")

class BigMario(Mario, Shroom):
    pass

m = BigMario()
m.move()
m.eat_shroom()