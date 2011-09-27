#encoding: utf-8

import os
import re
import shutil
import filecmp
import config

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

class Show(object):
	""" Represents a show file; ie. a file associated to its fullname """
	
	path = None
	name = None

	def __init__(self, fullname, filename):
		self.path = fullname
		self.name = filename

	def __str__(self):
		return self.name
		

class PigeonHole(object):
	""" Takes all the media files in a (download) folder and sort 
		them into the corresponding folder, based on the found file name
	"""
	
	directories = None
	series = None
	matches = None

	downloadDir = ""
	rootShows = ""

	def __init__(self, root, downloaddir):
		self.downloadDir = downloaddir
		self.rootShows = root
		self.directories = os.listdir(self.rootShows)
		self.series = list()

	def walk(self):		
		""" Walks through the downloaded folders and yields .avi and .mkv files """
		for root, dirs, files in os.walk(self.downloadDir):
			for filename in files:			
				if filename.endswith(config.shows_extensions):
					yield Show(os.path.join(root, filename), filename)

	def walk(self, foldername, extensions):
		for root, dirs, files in os.walk(foldername):
			for filename in files:
				if not filename.endswith(extensions):
					yield os.path.join(root, filename)
	
	def process(self):
		""" Parses the directories within the 'rootShows' folder and stores them as shows in a list. """
		self.series = [ Folder(os.path.join(self.rootShows, x)) for x in self.directories]

		for path in self.walk(config.shows_extensions):
			self.moveToFolder(path)
	
	def moveToFolder(self, show):
		""" Moves a specific show to its right folder. """
		
		destinationfile = self.findFolder(show)

		if destinationfile is not None:
			self.move(show.path, destinationfile)

			if self.isDeletable(show.path):
				shutil.rmtree(show.path)

	def findFolder(self, show):
		"""Finds and returns the complete destinationpath for a specific show."""
		
		rx = re.compile('\W+')
		result = rx.sub(' ', show.name.lower()).strip()

		for s in self.series:
			if s.name.lower() in result:
				return os.path.join(s.directory, show.name)


	def move(self, originalfile, destinationfile):
		""" Moves the downloaded file to the found folder. """
		print "Moving " + show.name + " to " + destinationfile
		shutil.move(originalfile, destinationfile)

	def isDeletable(self, foldername):
		""" Walks through the current directory and deletes it if nothing's really important in it
			ie. .nfo, .srr or .sfv files. 
		"""
		if foldername is None:
			return False

		if foldername == self.downloadDir or foldername == self.rootShows:
			return False

		if self.downloadDir in foldername or self.rootShows in foldername:
			return False
		
		if sum(1 for x in self.walk(foldername, config.useless_files_extensions)) is 0:
			return True

		return False
		
	def __str__(self):
		return 'PigeonHole module'
	
	def __name__(self):
		return 'PigeonHole'

if __name__ == "__main__":
	pHole = PigeonHole(r'C:\test', r'C:\temp')
	pHole.process()
