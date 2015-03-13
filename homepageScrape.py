import requests
import re
from urlparse import urlparse
from StringIO import StringIO
from BeautifulSoup import BeautifulSoup

def scrape(domain):
	m = re.search('(.+?)\.', domain)
	domainWithoutTld = m.group(0)[:-1]
	url = 'http://' + domain
	print url
	
	r = requests.get(url, allow_redirects=True)
	
	accounts = []

	soup = BeautifulSoup(r.text)

	for tag in soup.findAll('a', href=True):
		o = urlparse(tag['href'])
		if o.netloc == 'twitter.com':
			try:
				print o.path
				path = o.path[1:]
				index = path.find('/')
				if index > 0:
					path = path[0:index]
				accounts.append(path)
			except:
				pass

	return accounts