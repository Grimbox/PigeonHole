#encoding: utf-8

import os
import re
import shutil
import filecmp
import config

from model import *

class PigeonHole(object):
	""" Takes all the media files in a (download) folder and sort 
		them into the corresponding folder, based on the found file name
	"""
	
	matches = None

	def __init__(self, root, downloaddir):
		print "Building pigeon hole with %s and %s" % (root, downloaddir)

		self.structure = Structure(root)

		self.downloadDir = downloaddir
		self.rootShows = root
		self.directories = os.listdir(self.rootShows)

		self.series = list()
		self.movedFiles = list()

	def walk(self):		
		""" Walks through the downloaded folders and yields .avi and .mkv files """
		for root, dirs, files in os.walk(self.downloadDir):
			for filename in files:			
				if filename.endswith(config.shows_extensions):
					yield Show(os.path.join(root, filename))

	def walk2(self, foldername, extensions):
		for root, dirs, files in os.walk(foldername):
			for filename in files:
				if not filename.endswith(extensions):
					print "%s doesn't end with %s" % (filename, extensions)
					yield os.path.join(root, filename)
	
	def process(self):
		""" Parses the directories within the 'rootShows' folder and stores them as shows in a list. """
		self.series = [ Folder(os.path.join(self.rootShows, x)) for x in self.directories]

		for show in self.series:
			print show

		for path in self.walk():
			self.moveToFolder(path)
	
	def moveToFolder(self, show):
		""" Moves a specific show to its right folder. """
		
		print "Trying to find %s" % (show)

		destinationfile = self.findFolder(show)

		if destinationfile is not None:
			self.move(show.path, destinationfile)
			self.movedFiles.append(destinationfile)

			if self.isDeletable(show.directory()):
				print '\tDeleting ' + show.directory()
				shutil.rmtree(show.directory())
				
		else:
			for key in config.shows_dict:
				if key.lower() in show.name.lower():
					if os.path.exists(os.path.join(self.rootShows, config.shows_dict[key])):
						destinationfile = os.path.join(self.rootShows, config.shows_dict[key], show.name)
						print destinationfile
						self.move(show.path, destinationfile)

	def findFolder(self, show):
		"""Finds and returns the complete destinationpath for a specific show."""
		
		rx = re.compile('\W+')
		result = rx.sub(' ', show.name.lower()).strip()

		for s in self.series:
			if s.name.lower() in result:
				print "Association found %s %s" % (s.directory, show.name)
				return os.path.join(s.directory, show.name)


	def move(self, originalfile, destinationfile):
		""" Moves the downloaded file to the found folder. """
		print 'Moving ' + originalfile + ' to ' + destinationfile
		shutil.move(originalfile, destinationfile)

	def isDeletable(self, foldername):
		""" Walks through the current directory and deletes it if nothing's really important in it
			ie. .nfo, .srr or .sfv files. 
		"""
		if foldername is None:
			return Show(os.path.join(root, filename))


		print "Foldername value is %s" % (foldername)

		if foldername == self.downloadDir or foldername == self.rootShows:
			return False

		if foldername in self.downloadDir or foldername in self.rootShows:
			return False
		
		print 'I got ' + str(sum(1 for x in self.walk2(foldername, config.useless_files_extensions))) + ' int. files'

		if sum(1 for x in self.walk2(foldername, config.useless_files_extensions)) is 0:
			return True

		return False
		
	def getSubtitles(self):
		import subprocess
		for file in self.movedFiles:
			### subliminal -l en The.Big.Bang.Theory.S05E18.HDTV.x264-LOL.mp4
			 subprocess.call(["subliminal", "-l", "fr", file])
		
	def __str__(self):
		return 'PigeonHole module'
	
	def __name__(self):
		return 'PigeonHole'

if __name__ == "__main__":
	pHole = PigeonHole(config.ROOT_FOLDER, config.DL_FOLDER)
	pHole.process()
	pHole.getSubtitles()
	#pHole.structure.writeUrls()

