%define name python-ssdeep
%define version 3.2
%define unmangled_version 3.2
%define unmangled_version 3.2
%define release 1

Summary: Python wrapper for the ssdeep library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: LGPLv3+
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: PhiBo (DinoTools) <UNKNOWN>
Url: http://github.com/DinoTools/python-ssdeep
Requires: python-cffi, python-six, libffi, ssdeep-libs
BuildRequires: libffi-devel, ssdeep-devel

%description
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

.. image:: https://travis-ci.org/DinoTools/python-ssdeep.svg?branch=master
    :target: https://travis-ci.org/DinoTools/python-ssdeep

.. image:: https://ci.dinotools.org/buildStatus/icon?job=python-ssdeep-master
    :target: https://ci.dinotools.org/job/python-ssdeep-master/
    :alt: Build state


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
* Debian 8
* Ubuntu 14.04, 16.04

Licensing
=========

The code is licensed under the terms of the LGPLv3+.

This wrapper includes the unchanged source distribution of `ssdeep version 2.13`_. It is licensed under the GPLv2.

.. _ssdeep by Jesse Kornblum: http://ssdeep.sourceforge.net/
.. _ssdeep version 2.13: http://ssdeep.sourceforge.net/changes.txt
.. _python-ssdeep documentation: https://python-ssdeep.readthedocs.io


%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
