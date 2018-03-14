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
* pip
* six

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
    $ sudo yum install libffi-devel python-devel python-pip ssdeep-devel ssdeep-libs

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

Install on Debian 8/9
---------------------

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

Python 3
~~~~~~~~

**Use included ssdeep lib**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python3 python3-dev python3-pip automake autoconf libtool

Build and install Python module.

.. code-block:: console

    $ sudo BUILD_LIB=1 pip3 install ssdeep


Install on Ubuntu 16.04
-----------------------

Python 2
~~~~~~~~

**Use lib from official Ubuntu repository (recommended)**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python python-dev python-pip libfuzzy-dev

Build and install Python module.

.. code-block:: console

    $ pip install ssdeep

**Use included ssdeep lib**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python python-dev python-pip automake autoconf libtool

Build and install Python module.

.. code-block:: console

    $ BUILD_LIB=1 pip install ssdeep


Python 3
~~~~~~~~

**Use lib from official Ubuntu repository (recommended)**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python3 python3-dev python3-pip libfuzzy-dev

Build and install Python module.

.. code-block:: console

    $ pip3 install ssdeep

**Use included ssdeep lib**

Install required packages.

.. code-block:: console

    $ sudo apt-get install build-essential libffi-dev python3 python3-dev python3-pip automake autoconf libtool

Build and install Python module.

.. code-block:: console

    $ BUILD_LIB=1 pip3 install ssdeep

Install on Fedora 27
--------------------

Python 2
~~~~~~~~

**Use lib from Fedora repository**

Install required packages.

.. code-block:: console

    $ sudo dnf groupinstall "Development Tools"
    $ sudo dnf install libffi-devel python-devel python-pip ssdeep-devel ssdeep-libs

Build and install Python module.

.. code-block:: console

    $ sudo pip install ssdeep

Python 3
~~~~~~~~

**Use lib from Fedora repository**

Install required packages.

.. code-block:: console

    $ sudo dnf groupinstall "Development Tools"
    $ sudo dnf install libffi-devel python3-devel python3-pip ssdeep-devel ssdeep-libs

Build and install Python module.

.. code-block:: console

    $ sudo pip3 install ssdeep
