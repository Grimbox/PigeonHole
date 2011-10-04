import urllib2
import re
from BeautifulSoup import BeautifulSoup

"""
	Querying non web services through http interrogation and regex results retrieval.
"""

def query(showname):
	print "Trying " + showname
	socket = urllib2.urlopen('http://www.tvsubtitles.net/search.php?q=' + showname.replace(' ', '%20'))
	soup = BeautifulSoup(socket.read())
	socket.close()

	results = soup.findAll(href=re.compile("/tvshow-([A-Za-z0-9]*)\.html$"))

	if len(results) == 1:
		"ouh yeah baby " + showname + " " + str(results[0])
		
	elif len(results) == 0:
		print "No results found for " + showname
	else:
		print "Here are the possible results for " + showname
		for res in results: 
			print "\t" + str(res)

if __name__ == "__main__":
	query('the big bang theory')
	query('being erica')
	query('white collar')
	query('scrubs')
	query('castle')