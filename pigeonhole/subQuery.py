import urllib2
import re
from BeautifulSoup import BeautifulSoup

"""
	Querying non web services interfaces 
	through http interrogation and regex results retrieval.
"""

languages = ('en', 'es', 'fr', 'de')

def queryUrl(baseurl, baseregex):
	print 'Querying %s w/ %s' % baseurl, baseregex

def query(showname):
	print "Trying " + showname
	socket = urllib2.urlopen('http://www.tvsubtitles.net/search.php?q=' + showname.replace(' ', '%20'))
	soup = BeautifulSoup(socket.read())
	socket.close()

	results = soup.findAll(href=re.compile("/tvshow-([A-Za-z0-9]*)\.html$"))


	# a yield here would be cool ! :)
	if len(results) == 1:
		print str(results[0])
		return results[0]
		
	elif len(results) == 0:
		print "No results found for " + showname
		return None
	else:
		print "Here are the possible results for " + showname
		for res in results: 
			print "\t" + str(res)
		return None
	

def getSeason(showname, seasonNumber):
	season = query(showname)

	#idem

	if season is not None:
		print str(season).replace('.html', '-' + seasonNumber + '.html')

	else:
		print "no season found"

def getEpisode(showname, seasonNumber, episodeNumber):
	season = query(showname, seasonNumber)

	urllib2.urlopen(season)


	#idem

	if episode is not None:
		print str(episode).replace('.html', '-')
	else:
		print "no episode found"

def getUrl(showname, seasonNumber, episodeNumber, language):
	"""Supposed to send to the right page, according to the right episode number"""
	pass

if __name__ == "__main__":
	query('the big bang theory')
	query('being erica')
	query('white collar')
	query('scrubs')
	query('castle')