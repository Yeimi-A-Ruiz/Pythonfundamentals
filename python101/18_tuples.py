numbers = (1, 2, 3, 5)
strings = ('Andy', 'Natha', 'Dani', 'Chana', 'Andy', 'Natha')

print(numbers)
print('0 = ', numbers[0])
print('-1 = ', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

#CRUD
#numbers.append(10)
#numbers[1] = 'change'
print(numbers)

print(strings.index('Dani'))
print(strings.count('Andy'))

my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'Vale'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))
