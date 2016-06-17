from bs4 import BeautifulSoup
import urllib,requests
import re
python_web =urllib.urlopen("https://www.python.org/downloads/")
resp = requests.get("https://www.python.org/downloads/")
if python_web == resp:
	print "same"
else:
	print "not same"

python_soup = BeautifulSoup(python_web.read(),"lxml")
tags_a =python_soup.findAll(name="a",attrs={'href':re.compile("^https?://.*python\-2.*(exe|msi|zip|rar)$")})
for tag_a in tags_a:
	print tag_a["href"]


Everything_web =urllib.urlopen("https://www.voidtools.com/downloads/")
Everything_soup = BeautifulSoup(Everything_web.read(),"lxml")
tags_a =Everything_soup.findAll(name="a",attrs={'href':re.compile("^\/Everything\-.*[0-9]\.x64.Multilingual-Setup.exe$")})
for tag_a in tags_a:
	print "https://www.voidtools.com%s" % tag_a["href"]

nmap_web =urllib.urlopen("https://nmap.org/download.html")
nmap_soup = BeautifulSoup(nmap_web.read(),"lxml")
tags_a =nmap_soup.findAll(name="a",attrs={'href':re.compile("^.*setup\.(exe|msi|zip|rar)$")})
for tag_a in tags_a:
	print tag_a["href"]


winscp_web =urllib.urlopen("https://winscp.net/eng/download.php")
winscp_soup = BeautifulSoup(winscp_web.read(),"lxml")
tags_a =winscp_soup.findAll(name="a",attrs={'href':re.compile("^.*setup\.(exe|msi|zip|rar)$")})
for tag_a in tags_a:
	print "https://winscp.net%s" % tag_a["href"][2:]
	#https://winscp.net/ ../download/winscp577setup.exe



#https://www.jetbrains.com/pycharm/download/#section=windows
#https://download.jetbrains.com/python/pycharm-community-2016.1.4.exe
#nmap_web =urllib.urlopen("https://nmap.org/download.html")
#nmap_soup = BeautifulSoup(nmap_web.read(),"lxml")
#tags_a =nmap_soup.findAll(name="a",attrs={'href':re.compile("^.*(exe|msi|zip|rar)$")})
#for tag_a in tags_a:
#	print "https://www.voidtools.com%s" % tag_a["href"]
