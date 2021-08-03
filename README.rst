ssdeep Python Wrapper
=====================

This is a straightforward Python wrapper for `ssdeep by Jesse Kornblum`_, which is a library for computing context
triggered piecewise hashes (CTPH). Also called fuzzy hashes, CTPH can match inputs that have homologies. Such inputs
have sequences of identical bytes in the same order, although bytes in between these sequences may be different in both
content and length.

.. image:: https://img.shields.io/pypi/v/ssdeep.svg
    :target: https://pypi.python.org/pypi/ssdeep/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/ssdeep.svg
    :target: https://pypi.python.org/pypi/ssdeep/
    :alt: License

.. image:: https://img.shields.io/pypi/pyversions/ssdeep.svg
    :target: https://pypi.python.org/pypi/ssdeep/
    :alt: Python Versions

.. image:: https://readthedocs.org/projects/python-ssdeep/badge/
    :target: https://python-ssdeep.readthedocs.io/en/latest/
    :alt: Latest Docs

.. image:: https://github.com/dinotools/python-ssdeep/actions/workflows/codeql-analysis.yml/badge.svg?branch=master
    :target: https://github.com/DinoTools/python-ssdeep/actions/workflows/codeql-analysis.yml
    :alt: CodeQL tests

.. image:: https://github.com/dinotools/python-ssdeep/actions/workflows/python-linux.yml/badge.svg?branch=master
    :target: https://github.com/DinoTools/python-ssdeep/actions/workflows/python-linux.yml
    :alt: CI test status on Linux

.. image:: https://github.com/dinotools/python-ssdeep/actions/workflows/debian.yml/badge.svg?branch=master
    :target: https://github.com/DinoTools/python-ssdeep/actions/workflows/debian.yml
    :alt: CI test status on Debian

.. image:: https://github.com/dinotools/python-ssdeep/actions/workflows/ubuntu.yml/badge.svg?branch=master
    :target: https://github.com/DinoTools/python-ssdeep/actions/workflows/ubuntu.yml
    :alt: CI test status on Debian


How to use it
=============

To compute a fuzzy hash, use ``hash`` function:

.. code-block:: pycon

    >>> import ssdeep
    >>> hash1 = ssdeep.hash('Also called fuzzy hashes, Ctph can match inputs that have homologies.')
    >>> hash1
    '3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C'
    >>> hash2 = ssdeep.hash('Also called fuzzy hashes, CTPH can match inputs that have homologies.')
    >>> hash2
    '3:AXGBicFlIHBGcL6wCrFQEv:AXGH6xLsr2C'

The ``compare`` function returns the match between 2 hashes, an integer value from 0 (no match) to 100.

.. code-block:: pycon

    >>> ssdeep.compare(hash1, hash2)
    22


More examples are available in the `python-ssdeep documentation`_.

Install
=======

If all requirements are met it is possible to install the wrapper by using pip or easy_install.

.. code-block:: console

    $ pip install ssdeep

The build will fail if the ssdeep library isn't installed.
To use the included version of the ssdeep library use the following command.

.. code-block:: console

    $ BUILD_LIB=1 pip install ssdeep

For more information have a look at the `python-ssdeep documentation`_.

Tested on ...
=============

* CentOS 7
* Debian 8, 9
* Ubuntu 14.04, 16.04, 18.04

Documentation
=============

Feel free to use the prebuild `python-ssdeep documentation`_ or use the steps below to build the documentation.

.. code-block:: console

    $ cd docs
    $ pip install -r requirements.txt
    $ make html

Licensing
=========

The code is licensed under the terms of the LGPLv3+.

This wrapper includes the unchanged source distribution of `ssdeep version 2.14.1`_. It is licensed under the GPLv2.

.. _ssdeep by Jesse Kornblum: https://ssdeep-project.github.io/ssdeep/
.. _ssdeep version 2.14.1: https://github.com/ssdeep-project/ssdeep/releases/tag/release-2.14.1
.. _python-ssdeep documentation: https://python-ssdeep.readthedocs.io
