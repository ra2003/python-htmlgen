#!/usr/bin/python

from setuptools import setup


setup(
    name="htmlgen",
    version="0.99.0",
    description="HTML 5 Generator",
    author="Sebastian Rittau",
    author_email="srittau@rittau.biz",
    url="https://github.com/srittau/python-htmlgen",
    packages=["htmlgen", "test_htmlgen"],
    tests_require=["asserts >= 0.8.0, < 0.9"],
    license="MIT",
)
