import requests
import smtplib
from bs4 import BeautifulSoup

#Price history website: https://camelcamelcamel.com/

#--------------------------------------------------- Amazon Product Tracker ---------------------------------------------------#
AMAZON_PRODUCT_URL = 'https://www.amazon.com/gp/product/B08PCKYHR4/ref=ox_sc_act_title_4?smid=A2G697YVFPFSPH&psc=1'
HEADERS = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7'
}

response = requests.get(AMAZON_PRODUCT_URL,headers = HEADERS)
amazon_web = response.text

soup = BeautifulSoup(amazon_web,'lxml')

div_price_tag = soup.select('.a-section span.a-offscreen')
product_price = float(div_price_tag[0].text.split('$')[1])

span_product_tag = soup.select('.a-size-large span.product-title-word-break')
product_name = span_product_tag[0].getText().strip()

#--------------------------------------------------- Sending Email if product price is lower ---------------------------------------------------#

MY_EMAIL = 'MYEMAIL'
MY_PASSWORD = 'MYPASSWORD'
DST_EMAIL = 'DSTEMAIL'

if product_price < 60:
    with smtplib.SMTP('smtp.gmail.com',port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=DST_EMAIL,
            msg=f"Subject:Amazon Price Alert: {product_name}\n\n The price of the product have being reduce, the new price is: \n\n{product_price}")

