# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Simple sample Python Module',
    long_description=readme,
    author='Chris Fowler',
    author_email='chrispfowler@gmail.com',
    url='https://github.com/chrisfowler/py_sample',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

