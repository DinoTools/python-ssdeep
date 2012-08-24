ssdeep Python Wrapper
=====================

This is a straightforward Python wrapper for `ssdeep by Jesse Kornblum`_, which is a library for computing context
triggered piecewise hashes (CTPH). Also called fuzzy hashes, CTPH can match inputs that have homologies. Such inputs
have sequences of identical bytes in the same order, although bytes in between these sequences may be different in both
content and length.

How to use it
=============

To compute a fuzzy hash, use ``hash`` function:

    >>> import ssdeep
    >>> hash1 = ssdeep.hash('Also called fuzzy hashes, Ctph can match inputs that have homologies.')
    >>> hash1
    '3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C'
    >>> hash2 = ssdeep.hash('Also called fuzzy hashes, CTPH can match inputs that have homologies.')
    >>> hash2
    '3:AXGBicFlIHBGcL6wCrFQEv:AXGH6xLsr2C'

The ``compare`` function returns the match between 2 hashes, an integer value from 0 (no match) to 100.

    >>> ssdeep.compare(hash1, hash2)
    22

The ``hash_from_file`` accepts filename as argument and calculates the hash of the contents of the file.

    >>> ssdeep.hash_from_file('/etc/resolv.conf')
    '3:S3yE29cFrrMOoiECAaHJgvn:S3m+COoiUCuvn'

This wrapper includes the unchanged source distribution of `ssdeep version 2.9`_ and has no external dependencies.

Install
=======

To build the package the following dependencies have to be installed.

* Python 2.7 or Python 3.x including development files
* gcc and build essentials
* Cython

If all requirements are met it is possible to install the wrapper by using pip or easy_install.

    pip install ssdeep

FAQ
===

- **When comparing two hashes the result is always 0**

    The result depends on the algorithms in the ssdeep library. There are some issues if the length of provided data is to short or if the algorithm could not find enough patterns.

    The following example must not return the expected value.

        >>> hash1 = ssdeep.hash('foo'\*4096)
        >>> hash2 = ssdeep.hash('foo'\*4096)
        >>> ssdeep.compare(hash1, hash2)
        0

Licensing
=========

The code is licensed under the terms of the GPLv2.

History
=======

The initial version was published in 2010 by `Denis Bilenko on bitbucket`_. Since 2012 the source is maintained by Philipp Seidel(`DinoTools`_) and has been published on `github`_.

.. _ssdeep by Jesse Kornblum: http://ssdeep.sourceforge.net/
.. _ssdeep version 2.9: http://ssdeep.sourceforge.net/changes.txt
.. _Denis Bilenko on bitbucket: https://bitbucket.org/denis/ssdeep
.. _github: https://github.com/DinoTools/python-ssdeep
.. _Dinotools: http://www.dinotools.org/
