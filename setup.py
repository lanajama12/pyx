# -*- coding: utf-8 -*-
import os.path
from distutils.core import setup


NAME = 'pyc'


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.

    **NOTE** took from Django's setup.py
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)


def get_sources(src):
    """
    # Compile the list of packages available, because distutils doesn't have
    # an easy way to do this.

    **NOTE** tooke from Django's setup.py
    """
    packages, data_files = [], []
    root_dir = os.path.dirname(__file__)
    if root_dir != '':
        os.chdir(root_dir)

    for dirpath, dirnames, filenames in os.walk(src):
        # Ignore dirnames that start with '.'
        for i, dirname in enumerate(dirnames):
            if dirname.startswith('.'): del dirnames[i]
        if '__init__.py' in filenames:
            packages.append('.'.join(fullsplit(dirpath)))
        elif filenames:
            data_files.append([dirpath, [os.path.join(dirpath, f) for f in filenames]])

    return packages, data_files



version = __import__(NAME).get_version()

packages, data_files = get_sources(NAME)


setup(
    name = "pyc",
    version = version,
    url = 'https://github.com/jimzhan/pyc',
    author = 'Jim Zhan',
    author_email = 'jim.zhan@me.com',
    packages = packages,
    data_files = data_files,
    description = 'A high-level Python Tools Set.',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
   ],
)
