import requests

sheet_endpoint = 'https://api.sheety.co/b2a45a8ada6395003d80a52420f584f3/copyOfFlightDeals/users'

print('Welcome to the Flight Club!')
First_name = input('What is your first name? ')
Last_name = input('What is your last name? ')
email = input('What is your email id? ')

game_on = True
while game_on:
    check = input('Re-enter your email id: ')

    if email == check:

        new_data = {
            'user':
                {
                    'firstName': First_name,
                    'lastName': Last_name,
                    'email': email,
                }

        }
        response = requests.post(url=f'{sheet_endpoint}'
                                 , json=new_data)
        print('Welcome to the Club :D')
        game_on = False

    else:
        print('Incorrecto!')