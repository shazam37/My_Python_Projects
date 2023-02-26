##################### Normal Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

my_email = 'shazajmal37@gmail.com'
my_password = 'jouabiojgvmavpzs'
now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv('birthdays.csv')

birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    person_birthday = birthday_dict[today]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path, mode='r') as file:
        contents = file.read()
        x = contents.replace("[NAME]", person_birthday["name"])
        print(x)

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=person_birthday['email'], msg=f'Subject:Happy Birthday!!\n\n'
                                                                                       f'{x}')




