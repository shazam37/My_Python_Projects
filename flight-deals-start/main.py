from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager
import smtplib

username = 'shazajmal37@gmail.com'
password = 'jouabiojgvmavpzs'
TEQUILA_API_KEY = "ql_v276SxzS3IGrrANP31Z3GAh6SWiTJ"
sheet_endpoint = 'https://api.sheety.co/b2a45a8ada6395003d80a52420f584f3/copyOfFlightDeals/prices'

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))
notification_man = NotificationManager()

for destination in sheet_data:
    flight = flight_search.check_flights(
        'LON',
        destination['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is None:
        continue

    if flight.price < destination['lowestPrice']:
        if flight.stop_over > 0:
            notification_man.send_email(flight)
