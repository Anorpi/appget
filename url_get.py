from bs4 import BeautifulSoup
import urllib
import re
python_web =urllib.urlopen("https://www.python.org/downloads/")
python_soup = BeautifulSoup(python_web.read(),"lxml")
tags_a =python_soup.findAll(name="a",attrs={'href':re.compile("^https?://.*python\-2.*(exe|msi|zip|rar)$")})
for tag_a in tags_a:
	print tag_a["href"]


Everything_web =urllib.urlopen("https://www.voidtools.com/downloads/")
Everything_soup = BeautifulSoup(Everything_web.read(),"lxml")
tags_a =Everything_soup.findAll(name="a",attrs={'href':re.compile("^\/Everything\-.*[0-9]\.x64.Multilingual-Setup.exe$")})
for tag_a in tags_a:
	print "https://www.voidtools.com%s" % tag_a["href"]
