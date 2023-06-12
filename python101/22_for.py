for element in range(1,21):
    print(element)

my_list = [23, 45, 67, 89, 43]

for element in my_list:
    print(element)

my_tuple = ('Andy', 'Natha', 'Dani', 'Chana')

for element in my_tuple:
    print(element)

inventory = {
    'name': 't-shirt',
    'price': 100,
    'stock': 89
}

for i in inventory:
    print(i, ': ', inventory[i])

for key, value in inventory.items():
    print(key, ': ', value)

leads = [
    {
        'name': 'Chana',
        'age': 10
    },
    {
        'name': 'Dani',
        'age': 8
    },
    {
        'name': 'Natha',
        'age': 31
    }
]

for person in leads:
    print(person)
    print('name: ', person['name'])

