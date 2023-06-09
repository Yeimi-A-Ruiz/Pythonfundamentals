my_dict = {}
print(type(my_dict))

my_dict = {
    'name': 'Yeimi',
    'last_name': 'Ruiz',
    'age': 32
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
#print(my_dict('cellphone'))
print(my_dict.get('cellphone'))

print('name' in my_dict)
print('cellphone' in my_dict)