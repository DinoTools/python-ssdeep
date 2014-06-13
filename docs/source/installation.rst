Installation
============

Requirements
------------

* Python 2.6, 2.7, Python >= 3.2 or PyPy >= 2.0
* ssdeep/libfuzzy >= 2.10 (Some features might not be available with older versions. See :py:class:`ssdeep.Hash`)
* cffi
* six

Building python-ssdeep on Linux
-------------------------------

``python-ssdeep`` should build very easily on Linux.

For Debian and Ubuntu, the following command will ensure that the required
dependencies are installed:

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python-dev libfuzzy-dev

You should now be able to build and install python-ssdeep.

.. code-block:: console

    $ pip install ssdeep

Building python-ssdeep on Linux with libfuzzy
---------------------------------------------

If the fuzzy library isn't available on you Linux system. You can use the included lib.

On Debian and Ubuntu the following command will ensure that all additional required
dependencies are installed.

.. code-block:: console

    $ sudo apt-get install automake autoconf

You should now be able to build and install python-ssdeep with the included library.

.. code-block:: console

    $ BUILD_LIB=1 pip install ssdeep
