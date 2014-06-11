python-ssdeep
=============

This is a straightforward Python wrapper for `ssdeep by Jesse Kornblum`_, which is a library for computing context
triggered piecewise hashes (CTPH). Also called fuzzy hashes, CTPH can match inputs that have homologies. Such inputs
have sequences of identical bytes in the same order, although bytes in between these sequences may be different in both
content and length.

Contents:

.. toctree::
   :maxdepth: 2

   api
   changelog


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _ssdeep by Jesse Kornblum: http://ssdeep.sourceforge.net/
