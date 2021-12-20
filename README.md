# Django PlanetScale


[![pypi](https://img.shields.io/pypi/v/django-planetscale.svg)](https://pypi.org/project/django-planetscale/)
[![python](https://img.shields.io/pypi/pyversions/django-planetscale.svg)](https://pypi.org/project/django-planetscale/)
[![Build Status](https://github.com/birdcar/django-planetscale/actions/workflows/dev.yml/badge.svg)](https://github.com/birdcar/django-planetscale/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/birdcar/django-planetscale/branch/main/graphs/badge.svg)](https://codecov.io/github/birdcar/django-planetscale)



A Django database backend for PlanetScale

* GitHub: <https://github.com/birdcar/django-planetscale>
* PyPI: <https://pypi.org/project/django-planetscale/>
* Free software: GPL-3.0-only

## Features

* Enables you to use PlanetScale with your Django app
* Avoids you having to rewrite your model code to set the kwarg `db_constraint=False` on every relationship you model.
* Subclasses the existing MySQL database backend using the documented process, ensuring compatibility with all versions of Django.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.
