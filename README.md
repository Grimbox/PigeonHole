PigeonHole
==========

The main purpose of this application is to sort some specific types of files into a well-arranged directory. 

I used it for classifying tv shows from a garbage folder into the right one, based on the filename which will be cleaned to help sorting.

How it works
------------

The project is splitted into several files : 
* pigeonhole/pigeonhole.py : the one that should be run :)
* setup.py : not used yet, sorry.
* pigeonhole/config.py : where you should put your configuration.

### config.py ###

The configuration file contains the declaration of three variables : 

1. useless_files_extensions : used to clean a folder when the content of this directory (and its subdirectories) is only composed by this kind of files. Do not try to put `*` inside this filter, I don't know the behavior yet...
2. shows_extensions : the files that need to be organized. The `process` method of the `PigeonHole` class won't look for anything else than these filetype (sorry to based the recognition on extensions and not on [magic numbers](http://en.wikipedia.org/wiki/List_of_file_signatures))
3. shows_dict : used for file that have a 'special name'
(ie. using 'tbbt' while the real name that can be found in the destination folder is much much longer)

Unit testing
------------

All tests are located inside the `pigeonhole/tests` directory. To launch them, use the following command, based on the python handbook:

	python -m unittest discover 

Temporary files and folders are created (and cleaned) to verify that the file behavior is going okay.