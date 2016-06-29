import urllib
from bs4 import BeautifulSoup
 
print "procesing....."
a = 0
data = urllib.urlopen("http://www.cnbeta.com/").read()
soup = BeautifulSoup(data,"lxml")
itemlist = soup.findAll(name='div',attrs={'class':'title'})
 
for item in itemlist:
   name = item.find(name='a').string
   a = a + 1
   print a
   print name
 
