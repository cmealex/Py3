from operator import attrgetter

class User:

    def __init__(self, x, y):
        self.user_id = y
        self.name = x

    def __repr__(self):
        return self.name + " ; " + str(self.user_id)

users = [
    User('Bucke', 43),
    User('Aucke', 41),
    User('Cucke', 42),
    User('Eucke', 46),
    User('Ducke', 45),
    ]

for user in sorted(users, key=attrgetter('name')):
    print(user)
for user in sorted(users, key=attrgetter('user_id')):
    print(user)

