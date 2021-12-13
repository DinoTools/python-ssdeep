Changelog
=========

3.x (`master`_)
~~~~~~~~~~~~~~~

.. note:: This version is not yet released and is under development.

3.4.1 (2021-12-13)
~~~~~~~~~~~~~~~~~~

* Add internal build improvements
* Update CI pipelines

3.4 (2019-10-01)
~~~~~~~~~~~~~~~~

* Update documentation
* Replace Jenkins and Travis CI with Drone CI
* Add new copy() function to Hash() and PseudoHash() class
* Add new attributes to Hash() and PseudoHash() class
  * name
  * block_size

3.3 (2018-01-10)
~~~~~~~~~~~~~~~~

* Update ssdeep lib to 2.14.1
* Fix issues with Travis CI
* Add additional CI test with Python 3.6
* Build docs during CI builds
* Remove deprecated PKGBUILD

3.2 (2016-11-27)
~~~~~~~~~~~~~~~~

* Update ssdeep lib to 2.13(thanks to Charles Lindsay)
* Update install instructions
* Add additional CI tests on CentOS 7, Debian 8 and Ubuntu 14.04/16.04

3.1.1 (2014-12-20)
~~~~~~~~~~~~~~~~~~

* Updated ssdeep lib to 2.12
* Added additional tests
* Fixed build issues on Windows(thanks to Paul Chaignon)
* Added option to run tests with PyPy3
* Fixed build to prevent automake version missmatch errors
* Updated documentation

3.1 (2014-08-07)
~~~~~~~~~~~~~~~~

* Fix build issue with ssdeep < 2.10

3.0 (2014-06-25)
~~~~~~~~~~~~~~~~

* Completely rewritten to use CFFI
* Interface in the spirit of hashlib
* Use pytest and tox for tests
* Use installed fuzzy lib by default

2.9-0.3 (2013-03-12)
~~~~~~~~~~~~~~~~~~~~

* Fix build issue with Python 2.6

2.9-0.2 (2012-10-11)
~~~~~~~~~~~~~~~~~~~~

* Fixing small bug in setup.py

2.9-0.1 (2012-08-01)
~~~~~~~~~~~~~~~~~~~~

* Updated ssdeep from 2.5 to 2.9
* Added Python 3.x support

2.5 (2010-09-03)
~~~~~~~~~~~~~~~~

* Initial release

.. _`master`: https://github.com/DinoTools/python-ssdeep
