# -*- coding: utf-8 -*-
import os
from setuptools import setup


def read(fname):
    """ Return file content. """

    return open(
        os.path.join(
            os.path.dirname(__file__), fname)
        ).read()


def get_packages(package):
    """ Return root package and all sub-packages. """

    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a package themselves.
    """

    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

setup(
    name='drf-pdf',
    version='0.2.0',
    install_requires=['djangorestframework>=2.4'],
    url='https://github.com/drgarcia1986/drf-pdf',
    author='Diego Garcia',
    author_email='drgarcia1986@gmail.com',
    keywords='django djangorestframework render response pdf',
    description='A simple PDF renderer for Django Rest Framework',
    long_description=read('README.md'),
    packages=get_packages('drf_pdf'),
    packages_data=get_package_data('drf_pdf'),
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
