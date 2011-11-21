import urllib2
import re
import os
from BeautifulSoup import BeautifulSoup

"""
	Querying non web services interfaces 
	through http interrogation and regex results retrieval.
"""

languages = ('en', 'es', 'fr', 'de')

def queryUrl(baseurl, baseregex):
	print 'Querying %s w/ %s' % (baseurl, baseregex)

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
	
""" Get a specific season, based on the show name and the season number
	
	eg. getSeason('suits', 1)
		getSeason('dexter', 3)
"""
def getSeason(showname, seasonNumber):
	season = query(showname)

	#idem

	if season is not None:
		print str(season).replace('.html', '-' + str(seasonNumber) + '.html')

	else:
		print "no season found"

""" Get a specific episode, based on the show name, the season number and the episode number
	
	eg. getEpisode('being erica', 2, 12)
		getEpisode('the big bang theory', 3, 15)
"""
def getEpisode(showname, seasonNumber, episodeNumber):

	raise Exception('not implemented yet')

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

""" Write a shortcut to a specific web page and fix the shortcutname within the writtent file.
	
	eg. writeUrlShortcut('/opt/tmp', 'google.url', 'http://www.google.com', 'Google')	
	>>> [Google]
	>>> URL=http://www.google.com
	>>> inside a file named /opt/tmp/google.url
"""
def writeUrlShortcut(folderpath, filename, url, shortcutname):
	if not os.path.exists(folderpath):
		raise Exception('Writing Url : Path does not exists')

	filecontent = """[%s]\nURL=%s""" % (shortcutname, url)

	with open(os.path.join(folderpath, filename), 'w+') as f:
		f.write(filecontent)


if __name__ == "__main__":
	#queryUrl('http://www.tvsubtitles.net/search?q=', 'tvshow')

	# query('the big bang theory')
	# query('being erica')
	# query('white collar')
	# query('scrubs')
	# query('castle')

	getSeason('the big bang theory', 2)
	getSeason('white collar', 1)
	getSeason('suits', 1)
	getSeason('being erica', 2)