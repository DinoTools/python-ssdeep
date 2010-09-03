This is a Python wrapper for ssdeep_, which is a library for computing context triggered piecewise hashes (CTPH).
Also called fuzzy hashes, CTPH can match inputs that have homologies. Such inputs have sequences of identical bytes
in the same order, although bytes in between these sequences may be different in both content and length.

  >>> import ssdeep

  To compute the fuzzy hash, use ``hash_buf`` function:

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

The wrapper includes the original source distribution of ssdeep_ version 2.5_

.. _ssdeep: http://ssdeep.sourceforge.net/
.. _2.5: http://ssdeep.sourceforge.net/changes.txt
