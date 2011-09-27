import random
import unittest
import tempfile
import shutil
import os
from pigeonhole import PigeonHole
import config

class TestPigeonHoleFunctions(unittest.TestCase):
	"""Test the methods defined inside the PigeonHole class"""
	
	def setUp(self):
		"""Set up the test environment"""
		self.rootdir = tempfile.mkdtemp(prefix='pigeonHole_root_')
		self.downloaddir = tempfile.mkdtemp(prefix='pigeonHole_dl_dir_')

		# Create an environment with three folders
		os.mkdir(os.path.join(self.rootdir, 'White Collar'))
		os.mkdir(os.path.join(self.rootdir, 'The Big Bang Theory'))
		os.mkdir(os.path.join(self.rootdir, 'Being Erica'))

		self.pigeonHole = PigeonHole(self.rootdir, self.downloaddir)
		
		self.notDeletableTmpDir = tempfile.mkdtemp(prefix='pigeonHole_')
		self.deletableTmpDir = tempfile.mkdtemp(prefix='pigeonHole_')

	def tearDown(self):
		"""Tear down the test environment"""
		self.pigeonHole = None
		
		shutil.rmtree(self.notDeletableTmpDir)
		shutil.rmtree(self.deletableTmpDir)

		shutil.rmtree(self.rootdir)
		shutil.rmtree(self.downloaddir)

		
	def test_init(self):
		""" Testing the constructor """
		self.assertEqual(self.pigeonHole.rootShows, self.rootdir)
		self.assertEqual(self.pigeonHole.downloadDir, self.downloaddir)
		self.assertTrue(str(self.pigeonHole) == 'PigeonHole module', 'The module string is not correct.')
		self.assertTrue(str(self.pigeonHole.__name__ == 'PigeonHole'), 'The module name is not correct.')

	def test_clean(self):
		"""Testing the cleaning method"""

		self.generatedfiles_bad = list()
		self.generatedfiles_good = list()

		for x in config.useless_files_extensions + config.shows_extensions:
			fd, temppath = tempfile.mkstemp(x, 'tmp', self.notDeletableTmpDir)
			self.generatedfiles_bad.append(temppath)
			os.close(fd)
			
		for y in config.useless_files_extensions:
			fd, temppath = tempfile.mkstemp(y, 'tmp', self.deletableTmpDir)
			self.generatedfiles_good.append(temppath)
			os.close(fd)

		self.assertFalse(self.pigeonHole.isDeletable(self.notDeletableTmpDir))
		self.assertTrue(self.pigeonHole.isDeletable(self.deletableTmpDir))

		self.assertFalse(self.pigeonHole.isDeletable(self.rootdir))
		self.assertFalse(self.pigeonHole.isDeletable(self.downloaddir))

	def test_findFolder(self):
		"""Try to move a file to a specific location"""

		
		

		

if __name__ == '__main__':
    unittest.main()