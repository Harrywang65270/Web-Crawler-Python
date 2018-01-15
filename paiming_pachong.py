import requests
from bs4 import BeautifulSoup
import bs4
import sys

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        return demo
    except:
        return "chan sheng yi chang"
                         


def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string.encode('utf-8'),tds[1].string.encode('utf-8'),tds[3].string.encode('utf-8')])
    return ulist


def printUnivList(ulist,num):
    print "{:^10}\t{:^6}\t{:^10}".format("paiming","mingcheng","zongfen")
    for i in range(num):
        u = ulist[i]
        print "{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2])

     
url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
html = getHTMLText(url)
ulist = []
unew_list = fillUnivList(ulist,html)
printUnivList(unew_list,20)







