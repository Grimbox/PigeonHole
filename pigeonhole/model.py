from subQuery import *

class Structure(object):

	def __init__(self):
		print 'building myself'

class Show(object):
	""" Represents a show file; ie. a file associated to its fullname """
	
	path = None
	name = None
	directory = None

	url = None

	Seasons = list()

	def append(self, season):
		self.Seasons.append(season)
		season.parent = self

	def __init__(self, fullname, filename):
		self.path = fullname
		self.name = filename
		self.directory = os.path.dirname(self.path)
		url = queryShow(self.name)

	def __str__(self):
		return self.name

class Season(object):
	""" Represents a season within a show """

	seasonnumber = None
	parent = None

	def __init__(self, seasonnumber):
		self.seasonnumber = seasonnumber

class Episode(object):
	""" Represents an episode within a season """

	title = None

	def __init__(self, title):
		self.title = title