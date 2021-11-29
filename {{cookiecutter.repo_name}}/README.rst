=============================
{{ cookiecutter.project_name }}
=============================

.. image:: https://badge.fury.io/py/{{ cookiecutter.repo_name }}.svg/?style=flat-square
    :target: https://badge.fury.io/py/{{ cookiecutter.repo_name }}

.. image:: https://readthedocs.org/projects/pip/badge/?version=latest&style=flat-square
    :target: https://{{ cookiecutter.repo_name }}.readthedocs.io/en/latest/

.. image:: https://img.shields.io/coveralls/github/frankhood/{{ cookiecutter.repo_name }}/main?style=flat-square
    :target: https://coveralls.io/github/frankhood/{{ cookiecutter.repo_name }}?branch=main
    :alt: Coverage Status

{{ cookiecutter.project_short_description}}

Documentation
-------------

The full documentation is at https://{{ cookiecutter.repo_name }}.readthedocs.io.

Quickstart
----------

Install {{ cookiecutter.project_name }}::

    pip install {{ cookiecutter.repo_name }}

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        '{{ cookiecutter.app_name }}',
        ...
    )

Add {{ cookiecutter.project_name }}'s URL patterns:

.. code-block:: python

    from {{ cookiecutter.app_name }} import urls as {{ cookiecutter.app_name }}_urls


    urlpatterns = [
        ...
        url(r'^', include({{ cookiecutter.app_name }}_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
