import json

lt = [
    {'name': '李蒙', 'age': 19},
    {'name': 'WRB', 'age': 19},
    {'name': 'Ning', 'age': 19},
    {'name': '宋甜甜', 'age': 18},
    {'name': '贤贤', 'age': 20},
]

# Sting = json.dumps(lt)
# obj = json.loads(Sting)
# print(type(Sting))

json.dump(lt, open('new.txt', 'w', encoding='utf8'))
obj = json.load(open('new.txt', 'r', encoding='utf8'))
print(obj)