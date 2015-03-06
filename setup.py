# -*- coding: utf-8 -*-
import os
from setuptools import setup


def read(fname):
    return open(
        os.path.join(
            os.path.dirname(__file__), fname)
        ).read()

setup(
    name='drf-pdf',
    version='0.1.0',
    install_requires=['djangorestframework>=2.4'],
    author='Diego Garcia',
    author_email='drgarcia1986@gmail.com',
    keywords='django djangorestframework render response pdf',
    description='A simple PDF renderer for Django Rest Framework',
    long_description=read('README.md'),
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
