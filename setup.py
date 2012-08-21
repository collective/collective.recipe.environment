# -*- coding: utf-8 -*-
"""
This module contains the tool of collective.recipe.environment
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '0.2.0'

long_description = (
    '.. contents::\n'
    + '\n' +
    read('collective', 'recipe', 'environment', 'README.txt')
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    read('CHANGES.txt')
)

entry_point = 'collective.recipe.environment:Recipe'
entry_points = {"zc.buildout": ["default = %s" % entry_point]}

tests_require = ['zope.testing', 'zc.buildout', 'mr.scripty']

setup(name='collective.recipe.environment',
      version=version,
      description="zc.buildout recipe to set environment variables during the execution of a buildout.",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='zc.buildout buildout recipe',
      author='Rafael Oliveira',
      author_email='rafaelbco@gmail.com',
      url='http://svn.plone.org/svn/collective/buildout/collective.recipe.environment',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout'
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='collective.recipe.environment.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
