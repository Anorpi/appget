import urllib
from bs4 import BeautifulSoup
 
print "procesing....."
a = 0
data = urllib.urlopen("https://www.v2ex.com/?tab=deals").read()
soup = BeautifulSoup(data,"lxml")
itemlist = soup.findAll(name='span',attrs={'class':'item_title'})
 
for item in itemlist:
   name = item.find(name='a').string
   a = a + 1
   print ''
   print a
   print name
 
