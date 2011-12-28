import urllib2
import re
import os
from BeautifulSoup import BeautifulSoup

"""
	Querying non web services interfaces 
	through http interrogation and regex results retrieval.
"""

languages = ('en', 'es', 'fr', 'de')

""" not documented yet
"""
class CustomUrl(object):
	fullUrl = None
	suffix = None
	base = None

	def __init__(self, base, suffix):
		self.base = base
		self.suffix = suffix
		self.fullUrl = base + suffix

	def __str__(self):
		return str(self.fullUrl)

	def __unicode__(self):
		return str(self.fullUrl)

	def replace(self, oldstr, newstr):
		return CustomUrl(self.base, self.suffix.replace(oldstr, newstr))

"""
	Querying a base url with a specific regex and a query.

	eg. baseurl = http://duckduckgo.com/?q=
		query = my_query
		baseregex = ... :)

	It will query the url, adds the query string and will fetch every href link that match the regular expression.
"""
def queryUrl(baseurl, paramindicator, regex, querystring):
	#print '\tProbing ' + baseurl + ' ' + paramindicator + ' ' + regex + ' ' + querystring
	socket = urllib2.urlopen(baseurl + paramindicator + querystring)
	soup = BeautifulSoup(socket.read())
	socket.close()

	tags = soup.findAll(href=re.compile(regex))

	mylist = list()

	for tag in tags:
		bsoup = BeautifulSoup(str(tag))
		mylist.append(CustomUrl(baseurl, bsoup.a['href']))

	return mylist

def queryShow(showname):
	return queryUrl('http://www.tvsubtitles.net', '/search.php?q=', '/tvshow-([A-Za-z0-9]*)\.html$', showname.replace(' ', '%20'))

def querySeason(showname, seasonnumber):
	return [x.replace('.html', '-' + str(seasonnumber) + '.html') for x in queryShow(showname)]


"""Supposed to return the url, according to the show name and season number"""
def getUrl(showname, seasonNumber, episodenumber, language):
	Raise("not implemented yet")
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

def walk(foldername):
	for root, dirs, files in os.walk(foldername):
		for directory in dirs:
			

def echo(var):
	for x in var:
		print x

if __name__ == "__main__":
	for x in walk(r'C:\temp'):
		print x

	echo(queryShow('saison 1'))