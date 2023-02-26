import requests

sheet_endpoint = 'https://api.sheety.co/b2a45a8ada6395003d80a52420f584f3/copyOfFlightDeals/prices'

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(sheet_endpoint)
        data = response.json()
        self.destination_data = data['prices']

        return self.destination_data

    def update_destination_data(self):

        for city in self.destination_data:

            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(url=f"{sheet_endpoint}/{city['id']}",
                                    json = new_data)
            print(response.text)
