Installation
============

Requirements
------------

* Python

  * Python 2.6, 2.7
  * Python >= 3.2
  * PyPy >= 2.0

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

Building python-ssdeep on Linux without libfuzzy
------------------------------------------------

If the fuzzy library isn't available on you Linux system. You can use the included lib.

On Debian and Ubuntu the following command will ensure that all additional required
dependencies are installed.

.. code-block:: console

    $ sudo apt-get install automake autoconf

You should now be able to build and install python-ssdeep with the included library.

.. code-block:: console

    $ BUILD_LIB=1 pip install ssdeep

Install on CentOS 7
-------------------

Python 2
~~~~~~~~

**Use included ssdeep lib**

Install required packages.

.. code-block:: console

    $ sudo yum groupinstall "Development Tools"
    $ sudo yum install epel-release
    $ sudo yum install libffi-devel python-devel python-pip automake autoconf libtool

Build and install Python module.

.. code-block:: console

    $ sudo BUILD_LIB=1 pip install ssdeep

**Use lib from epel**

Install required packages.

.. code-block:: console

    $ sudo yum groupinstall "Development Tools"
    $ sudo yum install epel-release
    $ sudo yum install libffi-devel python-devel python-pip ssdeep-devel ssdeep-lib

Build and install Python module.

.. code-block:: console

    $ sudo pip install ssdeep


Install on Debian 7
-------------------

Python 2
~~~~~~~~

**Use included ssdeep lib**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python python-dev python-pip automake autoconf libtool

Build and install Python module.

.. code-block:: console

    $ sudo BUILD_LIB=1 pip install ssdeep

Python 3
~~~~~~~~

**Use included ssdeep lib**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python3 python3-dev python3-pip automake autoconf libtool

Build and install Python module.

.. code-block:: console

    $ sudo BUILD_LIB=1 pip install ssdeep

Install on Debian 8
-------------------

Python 2
~~~~~~~~

**Use included ssdeep lib**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python python-dev python-pip automake autoconf libtool

Build and install Python module.

.. code-block:: console

    $ sudo BUILD_LIB=1 pip install ssdeep

**Use ssdeep from Debian repository**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python python-dev python-pip libfuzzy-dev

Build and install Python module.

.. code-block:: console

    $ sudo pip install ssdeep

Python 3
~~~~~~~~

**Use included ssdeep lib**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python3 python3-dev python3-pip automake autoconf libtool

Build and install Python module.

.. code-block:: console

    $ sudo BUILD_LIB=1 pip3 install ssdeep

**Use ssdeep from Debian repository**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python3 python3-dev python3-pip libfuzzy-dev

Build and install Python module.

.. code-block:: console

    $ sudo pip3 install ssdeep


Install on Ubuntu 12.04
-----------------------

Python 2
~~~~~~~~

**Use included ssdeep lib**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python python-dev python-pip automake autoconf libtool

Build and install Python module.

.. code-block:: console

    $ sudo BUILD_LIB=1 pip install ssdeep

Python 3
~~~~~~~~

**Use included ssdeep lib**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python3 python3-dev python3-setuptools automake autoconf libtool

Build and install Python module.

.. code-block:: console

    $ sudo easy_install3 pip
    $ sudo BUILD_LIB=1 pip3 install ssdeep


Install on Ubuntu 14.04
-----------------------

Python 2
~~~~~~~~

**Use included ssdeep lib**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python python-dev python-pip automake autoconf libtool

Build and install Python module.

.. code-block:: console

    $ sudo BUILD_LIB=1 pip install ssdeep

**Use ssdeep from Ubuntu repository**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python python-dev python-pip libfuzzy-dev

Build and install Python module.

.. code-block:: console

    $ sudo pip install ssdeep

Python 3
~~~~~~~~

**Use included ssdeep lib**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python3 python3-dev python3-pip automake autoconf libtool

Build and install Python module.

.. code-block:: console

    $ sudo BUILD_LIB=1 pip3 install ssdeep

**Use ssdeep from Ubuntu repository**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python3 python3-dev python3-pip libfuzzy-dev

Build and install Python module.

.. code-block:: console

    $ sudo pip3 install ssdeep
