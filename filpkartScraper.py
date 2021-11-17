import time 
from bs4 import BeautifulSoup 
import requests 
import datetime
import csv
import smtplib
import os
import re
source = requests.get('https://www.flipkart.com/croma-20-l-solo-microwave-oven/p/itm124b6bdfa702c?pid=MRCFPCJDJSYFHH5J&lid=LSTMRCFPCJDJSYFHH5JHWPMAH&marketplace=FLIPKART&q=microwave+oven&store=j9e%2Fm38%2Fo49&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=en_QasrMw8sec27a1kOWmhWPgOEZSamZaw4n7YqOV1MVufSFAxK6FNnra1Pw3AH2BZhnxo022u3kcTDPbobe0EcRw%3D%3D&ppt=hp&ppn=homepage&ssid=s5ggphb09s0000001636987647200&qH=473b4abe03a500c3').text
soup = BeautifulSoup(source, 'lxml')
product = soup.find('h1', class_ = 'yhB1nd').span.text
print(product)
price = soup.find('div', class_ = '_30jeq3 _16Jk6d').text
price = price.strip()[1: ]
a =re.sub("[^\d\.]","", price)
a = int(a)
print(price)
today = datetime.date.today()
print(today)
header = ['Product', 'Price', 'Date']
data = [product, price, today]

with open('data.csv', 'w', newline = '', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

def get_mail():
    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('APP_PASS')

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = "The Oven you want is below 59990! Now is your chance to buy!"
        body = '''This is the moment we have been waiting for.Now is your chance to pick up the OVEN of your dreams.'''
        lines = "\n\n"
        msg = subject + lines+ body
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

    

def check_price():
    
    source = requests.get('https://www.flipkart.com/croma-20-l-solo-microwave-oven/p/itm124b6bdfa702c?pid=MRCFPCJDJSYFHH5J&lid=LSTMRCFPCJDJSYFHH5JHWPMAH&marketplace=FLIPKART&q=microwave+oven&store=j9e%2Fm38%2Fo49&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=en_QasrMw8sec27a1kOWmhWPgOEZSamZaw4n7YqOV1MVufSFAxK6FNnra1Pw3AH2BZhnxo022u3kcTDPbobe0EcRw%3D%3D&ppt=hp&ppn=homepage&ssid=s5ggphb09s0000001636987647200&qH=473b4abe03a500c3').text
    soup = BeautifulSoup(source, 'lxml')
    product = soup.find('h1', class_ = 'yhB1nd').span.text
    print(product)
    price = soup.find('div', class_ = '_30jeq3 _16Jk6d').text
    price = price.strip()[1: ]
    print(price)
    today = datetime.date.today()
    print(today)
    header = ['Product', 'Price', 'Date']
    data = [product, price, today]
    if(a<=5990):
        get_mail()


    #appending

    with open('data.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)    
while(True):
    check_price()

    time.sleep(86400)
    

