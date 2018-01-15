imports requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        ""


def getStockList(lst,stockURL):

    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a',target="_blank")
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href))[0]
        except:
            continue
        
        

def getStockInfo(lst,stockURL,fpath):
    for stock in lst:
        url = stockURL + i.encode('utf-8') + ".html"
        html = requests.get(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html,'html.parser',fromEncoding = 'utf-8')
            stockInfo = soup.find('div',attrs={"class":"stock-info"})
                
            name = stockInfo.find_all('a',attrs={"class":"bets-name"})[0]
            infoDict.update({"ming cheng": name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key]  = val
            
def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'http://gupiao.baidu.com/stock/'
    output_file = '/Users/wanghaigang/Documents/Python_Script/gupiao.txt'
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)

main()
