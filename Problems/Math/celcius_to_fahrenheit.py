# celcius = float(input())
# fahrenheit = (celcius * 1.8) + 32
# print(f'The temperature in Fahrenheit is: {fahrenheit:.2f}')

# name = input()
# print(f'Hello, {name}! Nice to meet you.')

numbers = input().split(' ')

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

if a < b and a < c:
    print(a)
elif b < c and b < a:
    print(b)
else:
    print(c)
