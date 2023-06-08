# Prove that a number is even

# testing stage

'''
print(100%2)
print(51%2)
print(13%2)
print(0%2)
print(7%2)
print(2%2)
'''

# logical approach

var = int(input('PLease type a number: '))

testing = var % 2

if testing == 0:
    print('This number is even')
else:
    print('This number is odd')
