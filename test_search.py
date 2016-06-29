from bs4 import BeautifulSoup

soup = BeautifulSoup(open("E:\index.html"),"lxml")
#print soup.get_text()
for tag in soup.find_all("h1"):
    print "##### %s" % tag.string
