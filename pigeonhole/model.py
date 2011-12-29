from subQuery import *
import os

class Structure(object):
	"""Represents the complete structure, with its shows, seasons and episodes"""
	
	def __init__(self, path):
		self.shows = [Show(os.path.join(path, x)) for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]

	def writeUrls(self):
		for s in self.shows:
			for season in s.seasons:
				season.writeUrl()

class Show(object):
	""" Represents a show file; ie. a file associated to its fullname """

	def __init__(self, path):

		self.path = path
		self.name = os.path.basename(path)

		self.url = queryShow(self.name)

		self.seasons = [Season(self, os.path.join(path, x)) for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]

	def __str__(self):
		return self.name

class Season(object):
	""" Represents a season within a show """

	def __init__(self, parent, path):

		self.parent = parent
		self.path = path
		self.name = os.path.basename(path)
		self.seasonnumber = re.findall('[0-9]+', os.path.basename(path))[0]
		self.episodes = [Episode(self, os.path.join(path, x)) for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]

		self.url = querySeason(parent.name, self.seasonnumber)

	def writeUrl(self):
		if len(self.url) == 1:
			results = querySeason(self.parent.name, self.seasonnumber)

			if len(results) == 1:
				print 'Writing subtitles shortcut for ' + self.parent.name
				writeUrlShortcut(self.path, self.parent.name + '.url', str(self.url[0]), 'InternetShortcut')
			elif len(results) == 0:
				print 'no results have been found for ' + self.parent.name
			else:
				print 'too much results have been found'
		elif len(self.url) == 0:
			print 'too few urls for ' + self.parent.name
		else:
			print 'too many urls for ' + self.parent.name

class Episode(object):
	""" Represents an episode within a season """

	def __init__(self, parent, path):
		print 'Building an episode: ' + path

		self.parent = parent
		self.path = path
		self.name = os.path.basename(path)

	def __str__(self):
		return self.name

class Folder(object):
	""" Directory show instanciation, relative to a path on the disk
		ie. Show name
			- Season 1
			- Season 2
			- ...
	"""
	
	directory = None
	name = None

	def __init__(self, path):
		self.directory = path;
		self.name = os.path.basename(self.directory)

	def __str__(self):
		return self.name + ' [' + self.directory + ']'