# -*- coding: utf-8 -*-

from setuptools import setup

setup(
  name="gifter",
  description="quickly keep track of gifters and their donations",
  version=0.1,
  author="David Flegal",
  author_email="flegal.david@gmail.com",
  license="MIT",
  py_modules=["gifter"],
  package_dir={'': 'src'},
  install_requires=[],
  extras_require={'test': ['pytest', 'pytest-xdist', "tox"]},
  )