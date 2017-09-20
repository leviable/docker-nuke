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
    Stopping container: identidock_identidock_1
    Stopping container: identidock_redis_1
    Stopping container: identidock_dnmonster_1
    Removing container: identidock_identidock_1
    Removing container: identidock_redis_1
    Removing container: identidock_dnmonster_1
    Removing image: ['identidock_identidock:latest']
    Removing image: ['amouat/dnmonster:1.0']
    Removing image: ['python:3.6']
    Removing image: ['redis:3.0']
    Removing volume: 15cd0eca3196513657b12ba9b8d27a7d220f49f6a374124abd21d9aae5672d55
