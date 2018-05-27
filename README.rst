Docker Nuke
===========

|PyPIVersion| |TravisCI| |CoverageStatus| |CodeHealth| |PythonVersions|

.. |TravisCI| image:: https://travis-ci.org/levi-rs/docker-nuke.svg?branch=master
    :target: https://travis-ci.org/levi-rs/docker-nuke
.. |CoverageStatus| image:: https://coveralls.io/repos/github/levi-rs/docker-nuke/badge.svg
   :target: https://coveralls.io/github/levi-rs/docker-nuke
.. |CodeHealth| image:: https://landscape.io/github/levi-rs/docker-nuke/master/landscape.svg?style=flat
   :target: https://landscape.io/github/levi-rs/docker-nuke/master
.. |PyPIVersion| image:: https://badge.fury.io/py/docker-nuke.svg
    :target: https://badge.fury.io/py/docker-nuke
.. |PythonVersions| image:: https://img.shields.io/pypi/pyversions/docker-nuke.svg
    :target: https://wiki.python.org/moin/Python2orPython3

docker-nuke, for when you want to blow away every docker object in sight


Installation
------------
docker-nuke is availiable on PyPI and can be pip installed

.. code-block:: bash

    $ pip install docker-nuke

Running
-------

.. code-block:: bash

    $ docker-nuke
    Stopping container 50bd26e339: Succeeded
    Removing container 50bd26e339: Succeeded
    Removing container 913061d931: Succeeded
    Removing image     59507b30b4: Failed (retry with "--force")
    Removing image     3fd9065eaf: Failed (retry with "--force")
    Removing volume    140bb8e5cc: Succeeded


Use the ``--force`` option to force remove docker objects:

.. code-block:: bash

    $ docker-nuke --force
    Removing image     59507b30b4: Succeeded
    Removing image     3fd9065eaf: Succeeded
