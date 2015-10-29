#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_f:
    README = readme_f.read()

with open('tests/requirements.txt') as test_requirements_f:
    TEST_REQUIREMENTS = test_requirements_f.readlines()

setup(
    name='logdecorator',
    version='0.0.0',
    description='Log function calls via a decorator',
    long_description=README,
    author='Chris Down',
    author_email='chris@chrisdown.name',
    url='https://github.com/cdown/logdecorator',
    py_modules=['logdecorator'],
    license='ISC',
    zip_safe=False,
    keywords='log decorator',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: Public Domain',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='nose.collector',
    tests_require=TEST_REQUIREMENTS
)
