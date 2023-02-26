import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 23.344101
MY_LONG = 85.309563
my_email = 'shazajmal37@gmail.com'
my_password = 'jouabiojgvmavpzs'

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) < iss_latitude < (MY_LAT + 5) and (MY_LONG - 5) < iss_longitude < (MY_LONG + 5):
        return True

def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night_time():
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg='Subject: Look Up\n\nOii mate. Time to see the ISS.')
