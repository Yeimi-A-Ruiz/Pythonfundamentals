user = {
    'name': 'Andres',
    'last_name': 'Ruiz',
    'langs': ['python', 'javascript'],
    'age': 99
}

print(user)

user['age'] = 40
user['name'] = 'Yeimi'
user['age'] -= 8
user['langs'].append('C#')

print(user)

del user['last_name']
user.pop('age')

print(user)

print('items')
print(user.items())

print('keys')
print(user.keys())

print('values')
print(user.values())