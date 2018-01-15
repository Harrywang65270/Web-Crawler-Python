import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=iphone+charger&rh=i%3Aaps%2Ck%3Aiphone+charger")
soup = BeautifulSoup(res.text,'html.parser')

count = 0;

for item in soup.select('.s-item-container'):
    count = count + 1
    print item.select('.sx-price-currency')[0].text + item.select('.sx-price-whole')[0].text + '.' + item.select('.sx-price-fractional')[0].text



print count


