from main import MENU
from main import resources

def resource_sufficient():
    entry = MENU[a]['ingredients']

    if resources['water'] - entry['water'] > 0:
        resources['water'] = resources['water'] - entry['water']
    else:
        print('Sorry! not enough water')
        return 0

    if a != 'espresso':
        if resources['milk'] - entry['milk'] > 0:
            resources['milk'] = resources['milk'] - entry['milk']
        else:
            print('Sorry! not enough milk')
            return 0

    if resources['coffee'] - entry['coffee'] > 0:
        resources['coffee'] = resources['coffee'] - entry['coffee']
    else:
        print('Sorry! not enough coffee')
        return 0


def process_coins():
    quarters = 0.25
    dimes = 0.1
    nickles = 0.05
    pennies = 0.01
    print('Please insert coins')
    w = int(input('insert quarters: '))
    x = int(input('insert dimes: '))
    y = int(input('insert nickel: '))
    z = int(input('insert pennies: '))

    total_coins = 0.25*w + 0.1*x + 0.05*y + 0.01*z

    return total_coins

def transaction_successful():
    global x
    global money
    global total_money
    if x - money > 0:
        x = x - money
        print(f'Your transaction is successful. Here is your change: ${round(x,2)}')
        total_money = total_money + money
        return 1

    elif x - money == 0:
        x = x - money
        print(f'Your transaction is successful')
        total_money = total_money + money
        return 1

    elif x - money < 0:
        print('Sorry thats not enough money. Money refunded')
        return 0


def report():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f'amount: ${total_money}')

machine_on = True
total_money = 0

while machine_on:

    report_track = True
    while report_track:
        a = input('What would you like? espresso,latte,cappuccino ')
        if a.lower() == 'report':
            report()
            report_track = True
        else:
            report_track = False

    if a.lower() == 'off':
        break

    # entry = MENU[a]['ingredients']
    money = MENU[a]['cost']

    x = process_coins()
    z = transaction_successful()
    if z == 0:
        continue

    y = resource_sufficient()
    if y != 0:

        z = transaction_successful()
        if z == 1:
            print(f'here is your {a}. Enjoy!')

print('Thanks for using the machine')











