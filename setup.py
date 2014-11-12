# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages
from os.path import join, dirname
import sys
# Fool distutils to accept more than ASCII
reload(sys).setdefaultencoding('utf-8')

version = '0.3.1-saltbox'

setup(
    name='repoze-oauth-plugin',
    version=version,
    description='OAuth plugin for repoze.who and repoze.what',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[],
    keywords='auth repoze repoze.who repoze.what predicate oauth',
    author=u'Linas Juškevičius',
    author_email='linas.juskevicius@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    namespace_packages=[
        'repoze', 'repoze.who', 'repoze.who.plugins',
        'repoze.what', 'repoze.what.plugins'],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    dependency_links=[
        'https://github.com/saebyn/repoze.who/tarball/4007e894724e51ffd143230c736be118f30c8982#egg=repoze.who-1.0.19-saltbox',
    ],
    install_requires=[
        'repoze.who==1.0.19-saltbox',
        'repoze.what>=1.0.9',
        'oauth2>=1.2.0',
        'SQLAlchemy>=0.5.5',
        'webob',
    ],
    tests_require=[
        'nose',
    ],
)
