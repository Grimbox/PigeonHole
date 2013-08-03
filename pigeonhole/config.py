# -*- coding: UTF8 -*- 
# Configuration file

### Defines the folder to watch and the destination folder
ROOT_FOLDER = r'/home/<username>/Videos/Series' 
DL_FOLDER = r'/home/<username>/Downloads/complete'

### If a folder only contains these types of files, we can delete it.
useless_files_extensions = ('srr', 'nfo', 'sfv', 'nzb')

### Consider only files with these extensions
shows_extensions = ('avi', 'mkv', 'mp4')

### Dictionary for special filename contents
shows_dict = {
	'wc' : 'white collar',
	'tbbt' : 'the big bang theory',
	'beingerica' : 'being erica',
