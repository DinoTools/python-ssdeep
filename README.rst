ssdeep Python Wrapper
=====================

This is a straightforward Python wrapper for `ssdeep by Jesse Kornblum`_, which is a library for computing context
triggered piecewise hashes (CTPH). Also called fuzzy hashes, CTPH can match inputs that have homologies. Such inputs
have sequences of identical bytes in the same order, although bytes in between these sequences may be different in both
content and length.

.. image:: https://pypip.in/version/ssdeep/badge.svg
    :target: https://pypi.python.org/pypi/ssdeep/
    :alt: Latest Version

.. image:: https://travis-ci.org/DinoTools/python-ssdeep.svg?branch=master
    :target: https://travis-ci.org/DinoTools/python-ssdeep


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

For more information have a look at the `python-ssdeep documentation`_.

Licensing
=========

The code is licensed under the terms of the LGPLv3+.

This wrapper includes the unchanged source distribution of `ssdeep version 2.10`_. It is licensed under the GPLv2.

.. _ssdeep by Jesse Kornblum: http://ssdeep.sourceforge.net/
.. _ssdeep version 2.10: http://ssdeep.sourceforge.net/changes.txt
.. _python-ssdeep documentation: http://python-ssdeep.readthedocs.org
