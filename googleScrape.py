import pycurl
import re
from urlparse import urlparse
from StringIO import StringIO

def scrape(domain):
	m = re.search('(.+?)\.', domain)
	domainWithoutTld = m.group(0)[:-1]
	url = 'https://www.google.ca/search?q=%22{0}%22%20%22{1}%22%20twitter%20-%22Welcome%20to%20Twitter%22%20-%22Login%20on%20Twitter%22%20site%3Atwitter.com%20-inurl%3A%2Flists%2F%20-inurl%3A%3Flang%20-inurl%3A%2Fstatus%2F'.format(domainWithoutTld, domain)
	uastring = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30"

	buffer = StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.USERAGENT, uastring)
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()

	body = buffer.getvalue()
	m = re.search('twitter.com/([^\.]*?)\"', body)
	try:
		account = m.group(0)[:-1][12:]
	except:
		account = False
	return account