import requests
import smtplib

sheet_endpoint = 'https://api.sheety.co/b2a45a8ada6395003d80a52420f584f3/copyOfFlightDeals/users'
username = 'shazajmal37@gmail.com'
password = 'jouabiojgvmavpzs'



class NotificationManager:

    def dict_func(self):

        response = requests.get(sheet_endpoint)
        data = response.json()['prices']

        my_dict = {}
        for i in range(1, len(data)):
            my_dict[data[i]['iataCode']] = data[i]['lowestPrice']

        return my_dict

    def send_email(self, flight):

        response = requests.get(url=sheet_endpoint)
        data = response.json()['users']


        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=username, password=password)
            for elements in data:

                connection.sendmail(from_addr=username,
                                    to_addrs=elements['email'],
                                    msg=f'Subject: Giddy Up! Cheapest flight deals on offer\n\n'
                                        f' Only {flight.price} pounds to fly '
                                        f'from {flight.origin_city}-{flight.origin_airport} '
                                        f'to {flight.destination_city}-{flight.destination_airport}\n'
                                        f'Flight has {flight.stop_over} stop over, via {flight.via_city}\n'
                                        f'https://www.google.co.uk/flights?hl=en'
                                        f'#flt={flight.origin_city}.{flight.destination_city}'
                                        f'.2020-08-25*SXF.STN.2020-09-08')







