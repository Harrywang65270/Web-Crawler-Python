import requests
from bs4 import BeautifulSoup

payload = {
    'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490',
    'EndStation':'3301e395-46b8-47aa-aa37-139e15708779',
    'SearchDate':'2017/05/02',
    'SearchTime':'16:00',
    'SearchWay':'DepartureInMandarin'
    }

res = requests.post('https://www.thsrc.com.tw/tw/TimeTable/SearchResult',data = payload)

soup = BeautifulSoup(res.text,'html.parser')

for item in soup.select('ul'):
    print item.select('.column3')
