# numbers
# int

lives = 3
print(type(lives))

age = 32
buget = 100

#float

temp = 12.9
print(type(temp))

# increases

lives = 12 + 15
print(lives)

lives = lives-1
print(lives)

lives -= 1
print(lives)

lives += 3
print(lives)

# scientific note for numbers

number_a = 45000000000000000000.1
print(number_a)

number_b = 0.000000000000000000016548
print(number_b)

# exercise

text_a = "PLease write your espenses for each applicable month:"
print(text_a)

january_fee = int(input('January: '))
february_fee = int(input('February: '))
march_fee = int(input('March: '))
april_fee = int(input('April: '))
may_fee = int(input('May: '))
june_fee = int(input('June: '))

average = (january_fee + february_fee + march_fee + april_fee + may_fee + june_fee) / 6
print('The average for this semester is ', average)