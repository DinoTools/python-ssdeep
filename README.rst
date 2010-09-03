This is a straightforward Python wrapper for `ssdeep by Jesse Kornblum`_, which is a library for computing context
triggered piecewise hashes (CTPH). Also called fuzzy hashes, CTPH can match inputs that have homologies. Such inputs
have sequences of identical bytes in the same order, although bytes in between these sequences may be different in both
content and length.

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

This wrapper includes the unchanged source distribution of `ssdeep version 2.5`_ and has no external dependencies.

.. _ssdeep by Jesse Kornblum: http://ssdeep.sourceforge.net/
.. _ssdeep version 2.5: http://ssdeep.sourceforge.net/changes.txt
