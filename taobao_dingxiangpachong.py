import requests
import re

# try except can ignore some bugs which are caused by me!!! it will be difficult for me to debug

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        print r.status_code
    
        return r.text
    except:
        return ""
    

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html) # not fully understood re
        
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print ""
    

def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print tplt.format("1","2","3")
    count = 0
    for g in ilt:
        count = count + 1
        print tplt.format(count, g[0],g[1])
    
def main():

    inital_url = "https://s.taobao.com/search?q="
    keyword = "%E4%B9%A6%E5%8C%85"   # the url Encode of shubao, python 3.0 should be better
    start_url = inital_url + keyword
    depth = 3
    info_list = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(i*44)
            print url
            html = getHTMLText(url)
           
            parsePage(info_list,html)
            
        except:
            continue
    printGoodList(info_list)
        
 
     


main()
