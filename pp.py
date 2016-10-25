from bs4 import BeautifulSoup
import requests
import re
python_web =requests.get("https://www.python.org/downloads/")
#same as `python_web =requests.get("https://www.python.org/downloads/")`

python_soup = BeautifulSoup(python_web.text,"lxml")
#same as `python_soup = BeautifulSoup(python_web.text,"lxml")`
tags_a =python_soup.findAll(name="a",attrs={'href':re.compile("^https?://.*python\-2.*(exe|msi|zip|rar)$")})
for tag_a in tags_a:
	print tag_a["href"]


everything_web =requests.get("https://www.voidtools.com/downloads/")
everything_soup = BeautifulSoup(everything_web.text,"lxml")
tags_a =everything_soup.findAll(name="a",attrs={'href':re.compile("^\/Everything\-.*[0-9]\.x64.Multilingual-Setup.exe$")})
for tag_a in tags_a:
	print "https://www.voidtools.com%s" % tag_a["href"]

nmap_web =requests.get("https://nmap.org/download.html")
nmap_soup = BeautifulSoup(nmap_web.text,"lxml")
tags_a =nmap_soup.findAll(name="a",attrs={'href':re.compile("^.*setup\.(exe|msi|zip|rar)$")})
for tag_a in tags_a:
	print tag_a["href"]


winscp_web =requests.get("https://winscp.net/eng/download.php")
winscp_soup = BeautifulSoup(winscp_web.text,"lxml")
tags_a =winscp_soup.findAll(name="a",attrs={'href':re.compile("^.*setup\.(exe|msi|zip|rar)$")})
for tag_a in tags_a:
	print "https://winscp.net%s" % tag_a["href"][2:]
	#https://winscp.net/ ../download/winscp577setup.exe


print "https://live.sysinternals.com/autoruns.exe"
print "https://live.sysinternals.com/Tcpview.exe"
teamviewer_web =requests.get("https://www.teamviewer.com/zhcn/download/windows/")
teamviewer_soup = BeautifulSoup(teamviewer_web.text,"lxml")
tags_a =teamviewer_soup.findAll(name="a",attrs={'href':re.compile("^.*Setup.zhcn.exe$")})
for tag_a in tags_a:
	print  tag_a["href"]

#https://notepad-plus-plus.org/download/v6.9.2.html
#https://notepad-plus-plus.org/zh/download/
notepadplus_web =requests.get("https://notepad-plus-plus.org/zh/download/")
notepadplus_soup = BeautifulSoup(notepadplus_web.text,"lxml")
tags_a =notepadplus_soup.findAll(name="a",attrs={'href':re.compile(".*exe$")})
for tag_a in tags_a:
	print  "https://notepad-plus-plus.org%s" % tag_a["href"]



qq_web =requests.get("http://im.qq.com/pcqq/")
qq_soup = BeautifulSoup(qq_web.text,"lxml")
tags_a =qq_soup.findAll(name="a",attrs={'href':re.compile(".*exe[ ]*$")})
for tag_a in tags_a:
	print  "%s" % tag_a["href"]



TestDisk_PhotoRec_web =requests.get("http://www.cgsecurity.org/wiki/TestDisk_Download")
TestDisk_PhotoRec_soup = BeautifulSoup(TestDisk_PhotoRec_web.text,"lxml")
tags_a =TestDisk_PhotoRec_soup.findAll(name="a",attrs={'href':re.compile(".*[0-9]\.win64.zip$")})
for tag_a in tags_a:
	print  "%s" % tag_a["href"]


#winrar_web =requests.get("http://www.rarlab.com/download.htm")
#winrar_soup = BeautifulSoup(winrar_web.text,"lxml")
#print winrar_soup.prettify
#tags_a =winrar_soup.findAll(name="a",attrs={'href':re.compile("^http:.*$")})
#print  tags_a
#for tag_a in tags_a:
	#print  tag_a["href"]


#nmap_web =requests.get("https://nmap.org/download.html")
#nmap_soup = BeautifulSoup(nmap_web.text,"lxml")
#tags_a =nmap_soup.findAll(name="a",attrs={'href':re.compile("^.*(exe|msi|zip|rar)$")})
#for tag_a in tags_a:
#	print  tag_a["href"]

