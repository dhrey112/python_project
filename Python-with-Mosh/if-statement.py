is_hot = True
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes.")
else:
    print("It's a lovely day")


price_house = 1000000
is_good = False

if is_good:
    print("They need to put down 10%")
    print("Down payment: $", price_house*10/100)
else:
    print("Down payment: $", price_house*20/100)

# print(f'Down payment: ${down_payment}')


