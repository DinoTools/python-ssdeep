Usage
=====

Import the required module.

.. code-block:: pycon

    >>> import ssdeep

Use the :py:func:`ssdeep.hash` function to compute a fuzzy hash.

.. code-block:: pycon

    >>> hash1 = ssdeep.hash('Also called fuzzy hashes, Ctph can match inputs that have homologies.')
    >>> hash1
    '3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C'
    >>> hash2 = ssdeep.hash('Also called fuzzy hashes, CTPH can match inputs that have homologies.')
    >>> hash2
    '3:AXGBicFlIHBGcL6wCrFQEv:AXGH6xLsr2C'


The :py:func:`ssdeep.compare` function returns the match score of two hashes. The score is an integer value from 0 (no match) to 100.

.. code-block:: pycon

    >>> ssdeep.compare(hash1, hash2)
    22

The :py:func:`ssdeep.hash_from_file` function accepts a filename as argument and calculates the hash of the contents of the file.

.. code-block:: pycon

    >>> ssdeep.hash_from_file('/etc/resolv.conf')
    '3:S3yE29cFrrMOoiECAaHJgvn:S3m+COoiUCuvn'

The :py:class:`ssdeep.Hash` class provides a hashlib like interface.

.. code-block:: pycon

    >>> h = ssdeep.Hash()
    >>> h.update('Also called fuzzy hashes, ')
    >>> h.digest()
    '3:AXGBicFlF:AXGHR'
    >>> h.update('Ctph can match inputs that have homologies.')
    >>> h.digest()
    '3:AXGBicFlgVNhBGcL6wCrFQEv:AXGHsNhxLsr2C'
