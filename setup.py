# -*- coding: utf-8 -*-
"""Setup file for Mail Room."""

from setuptools import setup

setup(
  name="Donate Tracker",
  description="quickly keep track of gifters and their donations",
  version=0.1,
  author="David Flegal",
  author_email="flegal.david@gmail.com",
  license="MIT",
  py_modules=["mail_room"],
  package_dir={'': 'src'},
  install_requires=['sys'],
  extras_require={'test': ['pytest', 'pytest-xdist', "tox"]},
  )