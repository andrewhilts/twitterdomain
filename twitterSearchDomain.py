import json
from TwitterAPI import TwitterAPI
import oauth
import requests
import twittercredentials
import re

def getAccount(domain):
	accounts = []
	api = TwitterAPI(twittercredentials.consumer_key, twittercredentials.consumer_secret, twittercredentials.access_token_key, twittercredentials.access_token_secret)

	r = api.request('users/search', {'q':domain, 'count':'10'})
	for item in r:
	    accounts.append(item['screen_name'])
	if len(accounts):
		return accounts
	else:
		return False

def getAccountNoTLD(domain):
	m = re.search('(.+?)\.', domain)
	try:
		domainWithoutTld = m.group(0)[:-1]
		return getAccount(domainWithoutTld)
	except:
		return False