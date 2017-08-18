#!/usr/bin/env python
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='wilddog-sms',
    version='1.0.1',
    description='A python sdk for wilddog sms',
    license="MIT",
    long_description="""\
    Wilddog SMS Python SDK
    ----------------------------
    DESCRIPTION
    The Wilddog SMS Python SDK simplifies the process of sending sms using the Wilddog SMS API.
    See https://github.com/WildDogTeam/sms-sdk-python for more information.
    LICENSE The Wilddog SMS Python SDK is distributed under the MIT License
    """,
    keywords='wilddog sms python',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        'Natural Language :: English',
    ],
    author='duanjienan',
    author_email='duanjienan@wilddog.com',
    url="https://github.com/WildDogTeam/sms-sdk-python",
    packages=['wilddog'],
    install_requires=['requests'],
)
