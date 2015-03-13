import sys
import googleScrape
import homepageScrape
import twitterSearchDomain
import twitterBestMatchTest

args = sys.argv

args.pop(0)

try:
    domain = args[0]
except IndexError:
  print "please provide a domain as the first argument"
  sys.exit()

print "Determining Twitter account for {0}".format(domain)

dataCollectionFuncs = [
	googleScrape.scrape,
	homepageScrape.scrape,
	twitterSearchDomain.getAccount,
	twitterSearchDomain.getAccountNoTLD
]

accountCandidates = []

#Run data collection
for f in dataCollectionFuncs:
	account = f(domain)
	if account:
		if isinstance(account, list):
			for acc in account:
				print "Found account {0}".format(acc)
				accountCandidates.append(acc)
		else:
			print "Found account {0}".format(account)
			accountCandidates.append(account)
	else:
		print "No account found"

#Run test to determine best match
if len(accountCandidates):
	print "Running best match analysis on {0} accounts for {1}".format(len(accountCandidates), domain)
	bestMatch = twitterBestMatchTest.runTest(domain, list(set(accountCandidates)))
	if bestMatch:
		print "Best match account for {0} is: {1}".format(domain, bestMatch)
	else:
		print "No best match account found for {0}.".format(domain)
else:
	print "No accounts found for {0}".format(domain)