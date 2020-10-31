..
    This file is part of the python-ssdeep

    SPDX-FileCopyrightText: 2017-2020 PhiBo (DinoTools)

    SPDX-License-Identifier: LGPL-3.0-or-later

Contributing
============

First of all, thank you for your interest in contributing to this project!


Filing bug reports
------------------

Bug reports are very welcome.
Please file them on the `GitHub issue tracker`_.
Good bug reports come with extensive descriptions of the error and how to reproduce it.
Try to use the provided issue template, it should be displayed by the GitHub website when creating a new issue.


Patches
-------

All patches should be submitted in the form of pull requests to the main repository, `DinoTools/python-ssdeep`_.
These pull requests should satisfy the following properties:

Code
^^^^

- A pull request should focus on **one** particular improvement or change.
- Create different pull requests for unrelated features or bugfixes.
- Python code should follow `PEP 8`_, especially in the "do what code around you does" sense.
- Add test if possible


Documentation
^^^^^^^^^^^^^

When introducing new functionality, please remember to write documentation.

First time setup
^^^^^^^^^^^^^^^^

- Download and install the `latest version of git`_
- Configure git with your username and email

.. code::

    $ git config user.name 'Your Name'
    $ git config user.email 'your.email@example.org'

- Make sure you have a `GitHub account`_
- Fork `DinoTools/python-ssdeep`_ to your GitHub account by using the Fork button
- Clone the main repository locally

.. code::

    $ git clone https://github.com/DinoTools/python-ssdeep.git
    $ cd python-ssdeep

- Add your fork as a remote to push your work to. Replace <username> with your username.

.. code::

    $ git remote add fork https://github.com/<username>/python-ssdeep

- Install `pre-commit`_ by using a virtualenv.

.. code::

    $ python3 -m venv venv_git
    $ source venv_git/bin/activate
    $ pip install pre-commit

- Install pre-commit hooks.

.. code::

    $ pre-commit install

Review
------

Finally, pull requests must be reviewed before merging.
Everyone can perform reviews; this is a very valuable way to contribute, and is highly encouraged.


.. _GitHub issue tracker: https://github.com/DinoTools/python-ssdeep/issues
.. _DinoTools/python-ssdeep: https://github.com/DinoTools/python-ssdeep
.. _PEP 8: https://www.python.org/dev/peps/pep-0008/
.. _latest version of git: https://git-scm.com/downloads
.. _GitHub account: https://github.com/join
.. _pre-commit: https://pre-commit.com/
