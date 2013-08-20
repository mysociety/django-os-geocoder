#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

file_dir = os.path.abspath(os.path.dirname(__file__))

def read_file(filename):
    filepath = os.path.join(file_dir, filename)
    return open(filepath).read()

setup(
    name="django-os-geocoder",
    version='0.1.5',
    description='A Django app that lets you load Ordnance Survey data and use it to find places.',
    long_description=read_file('README.rst'),
    author='mySociety',
    author_email='programmers@mysociety.org',
    url='https://github.com/mysociety/django-os-geocoder',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_file('requirements.txt'),
    classifiers=[
        'Framework :: Django',
    ],
)
