import requests
from bs4 import BeautifulSoup
import smtplib
import time 

#URL for product I want
URL = 'https://www.amazon.de/Lenovo-Convertible-Notebook-i7-8550U-champagner-Silber/dp/B07KT4JKXG/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=lenovo&qid=1562093581&refinements=p_n_feature_thirteen_browse-bin%3A11470324031&rnid=8321961031&s=computers&sr=1-1'

#Pass User agent into header to give info on browser
headers = {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    #return all data from the website
    page = requests.get(URL, headers=headers)

    #Parsing BeautifulSoup allows to pull individual items from the site
    soup = BeautifulSoup(page.content, 'html.parser')

    #Pulls product title info(search by id).get_text returns text only(optional).strip removes spaces
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    #convert price to a float and return only first five characters
    converted_price = float(price[0:5])

    print(title.strip())
    print(converted_price)

    if (converted_price < 1.400):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #command sent by an email server to identify itself when connecting to another email server to start the process of sending an email
    server.ehlo()
    #encrypt connection
    server.starttls()
    #call ehlo again
    server.ehlo()

    server.login('boy416920@gmail.com', 'uxogqdzyvncypcmn')
    #set up email
    subject = 'Price fell down!'
    body = 'check the amazon link https://www.amazon.de/Lenovo-Convertible-Notebook-i7-8550U-champagner-Silber/dp/B07KT4JKXG/ref=sr_1_1?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=lenovo&qid=1562093581&refinements=p_n_feature_thirteen_browse-bin%3A11470324031&rnid=8321961031&s=computers&sr=1-1'
    #set up message(interpolate subject)
    msg = f"Subject: {subject}\n\n{body}"
    #send email
    server.sendmail(
        #from
        'boy416920@gmail.com',
        #to
        'sammymbevi@gmail.com',
        msg
    )
    print('Email Sent')
    #close up the connection
    server,quit()

#call check_price function and set a while loop to check every 24 hours(86400seconds)
while(True):   
    check_price()    
    time.sleep(86400)