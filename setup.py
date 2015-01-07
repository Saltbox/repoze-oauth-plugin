# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages
from os.path import join, dirname
import sys
# Fool distutils to accept more than ASCII
reload(sys).setdefaultencoding('utf-8')

version = '0.3.2'

setup(name='repoze-oauth-plugin',
    version=version,
    description='OAuth plugin for repoze.who and repoze.what',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='auth repoze repoze.who repoze.what predicate oauth',
    author=u'Linas Juškevičius',
    author_email='linas.juskevicius@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    namespace_packages=['repoze', 'repoze.who', 'repoze.who.plugins',
        'repoze.what', 'repoze.what.plugins'],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    dependency_links=[
        'https://github.com/saebyn/repoze.who/tarball/ed6d1c826786e8f2f25441df6b13b34e15367d0b#egg=repoze.who-1.0.20',
    ],
    install_requires=[
        'repoze.who===1.0.20',
        'repoze.what>=1.0.9',
        'oauth2>=1.2.0',
        'SQLAlchemy>=0.5.5',
        'webob',
    ],
    tests_require=[
        'nose',
    ],
)
