# CRUD - Create, Read, Update & Delete

#create
numbers = [1, 2, 3, 4, 5]

#Read
print(numbers[1])

#Update
numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0, 'Hi')
print(numbers)

numbers.insert(3, 'change')
print(numbers)

tasks = ['to do 1', 'to do 2', 'to do 3']

new_list = numbers + tasks
print(new_list)

index = new_list.index('to do 2')
new_list[index] = 'to do changed'
print(new_list)

new_list.reverse()
print(new_list)

number_a = [1, 4, 6,3]
print(number_a)
number_a.sort()
print(number_a)

strings = ['ar', 'ab', 'ds', 'la', 'az', 'zp']
print(strings)
strings.sort()
print(strings)

#Delete

new_list.remove('to do 1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)
