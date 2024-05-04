day = 'sunny'

if day == 'hot':
    print("It's a hot day.")
    print('Drink more water.')
elif day == 'cold':
    print("It's a cold day.")
    print('Wear warm cloths.')
else:
    print('Enjoy your day.')

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2

print(f'Your down payment is {down_payment:.2f}$')
