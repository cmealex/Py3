# myd = {1:"one",2:"two", 3:"three"} #dictionary
# for k,v in myd.items():
#     print(k,v)
# print(min(zip(myd.keys(), myd.values())))
# print(max(zip(myd.keys(), myd.values())))
# print(sorted(zip(myd.values(), myd.keys())))

##MultipleKeySort

from operator import itemgetter

users = [
    {'fname':'Bucky', 'lname':'Roberts'},
    {'fname':'Aucky', 'lname':'Roberts'},
    {'fname':'Cucky', 'lname':'Roberts'},
    {'fname':'Ducky', 'lname':'Doberts'},
    {'fname':'Ducky', 'lname':'Boberts'},
    {'fname':'Ducky', 'lname':'Aoberts'},
]

for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)

