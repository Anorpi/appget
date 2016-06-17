from bs4 import BeautifulSoup
import urllib
import re
python_web =urllib.urlopen("https://www.python.org/downloads/")
python_soup = BeautifulSoup(python_web.read(),"lxml")
tags_a =python_soup.findAll(name="a",attrs={'href':re.compile("^https?://.*python\-2.*(exe|msi|zip|rar)$")})
for tag_a in tags_a:
	print tag_a["href"]
