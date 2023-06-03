# strings

name = 'Yeimi'
last_name = 'Ruiz'

print(name)
print(last_name)

Full_name = name + " " + last_name

print(Full_name)
type(Full_name)

quote = "I'm Yeimi"

print(quote)

quote2 = 'She said "Hello"'

print(quote2)

# format

template = "Hi, my name is " + name + " and my last name is " + last_name

print('V1', template)

template = "Hi, my name is {} and my last name is {}".format(name, last_name)

print('V2', template)

template = f"Hi, my name is {name} and my last name is {last_name}"

print('V3', template)