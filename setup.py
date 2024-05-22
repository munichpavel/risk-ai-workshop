#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()


requirements = [
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO put package test requirements here
]

setup(
    name='risk_learning',
    version='2024.1.1',
    author="Paul Larsen",
    author_email='munichpavel@gmail.com',
    url='https://github.com/munichpavel/risk_learning',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='risk_learning',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.6',
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
