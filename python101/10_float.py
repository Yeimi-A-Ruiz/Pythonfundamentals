# float numbers

x = 3.3
y = 1.1 + 2.2

print('x=', x)
print('y=', y)
print(x == y)

y_str = format(y, ".2g")
print('y_str =', y_str)

print(y_str == str(x))

print(y, x)

tolerance = 0.00001
print(x - y)
print(y - x)
print(abs(x - y) < tolerance)
print(abs(y - x) < tolerance)