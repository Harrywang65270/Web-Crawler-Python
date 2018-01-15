import HTMLParser

import urllib


'''
response = urllib.urlopen('http://www-rohan.sdsu.edu')
html = response.read()
print html[:150]

'''

urlText = []

class parseText(HTMLParser.HTMLParser):


    def handle_data(self,data):

            urlText.append(data)


lParser = parseText()

thisurl = "http://www.rohan.sdsu.edu/~gawron/index.html"

lParser.feed(urllib.urlopen(thisurl).read())
lParser.close

for item in urlText:
    print item
