import requests
from bs4 import BeautifulSoup
import smtplib
import re

my_email = 'shazajmal37@gmail.com'
password = 'jouabiojgvmavpzs'

def remove(string):
    return string.replace(' ', '')

url = 'https://www.amazon.in/Fastrack-reflex-Rectangle-activity-tracker/dp/B09QKLM2VK/' \
      '?_encoding=UTF8&pd_rd_w=9B2mQ&content-id=amzn1.sym.720b5979-f50b-4492-bd1b-bccb0403950f&' \
      'pf_rd_p=720b5979-f50b-4492-bd1b-bccb0403950f&pf_rd_r=TZB4SPK3NX84HYG1QVXC&pd_rd_wg=YDJGw&' \
      'pd_rd_r=95a61d04-53b2-466f-8cbb-7ee5c1ac62cc&ref_=pd_gw_unk'

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
        'Accept-Language': 'en-US,en;q=0.9',
}

data = requests.get(url,
                    headers=HEADERS)

soup = BeautifulSoup(data.text, 'lxml')

price = soup.find(name='span',class_='a-offscreen')

new_price = price.getText().split('₹')[1]
new_price_convert = new_price.split(',')
attach = new_price_convert[0]+new_price_convert[1]
# test_price = new_price.split('.')[0]
float_price = float(attach)

name = soup.find(name='span', class_='a-size-large product-title-word-break')
pdt_name = name.getText().split(',')[0]
new_name = remove(pdt_name.strip(''))

if float_price < 3000:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f'Subject:Price alert on your item\n\nYour item {new_name} is now rupees {float_price}\n'
                                f'{url}'.encode('utf-8'))


