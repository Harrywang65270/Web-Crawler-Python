import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return "chan sheng yi chang"

if __name__ == "__main__":
    url = "http://item.jd.com/2967929.html"
    print getHTMLText(url)
