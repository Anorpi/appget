import urllib,requests,time
a=0
b=0
while 1:
	time.sleep(3)
	urllib_web =urllib.urlopen("http://www.liaoxuefeng.com/")
	a = a+1
	print "url count:%s" % a
	time.sleep(3)
	requ_web = requests.get("http://www.liaoxuefeng.com/")
	b = b + 1
	print "req count %s" % b

