# -*- coding: utf-8 -*-
"""Doctest runner."""

from zope.testing import renormalizing
import doctest
import mr.scripty
import unittest
import zc.buildout.testing
import zc.buildout.tests

__docformat__ = 'restructuredtext'

optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE | doctest.REPORT_ONLY_FIRST_FAILURE)


def setUp(test):
    zc.buildout.testing.buildoutSetUp(test)

    cmd = test.globs['buildout'] + ' buildout:offline=true'
    system = test.globs['system']

    def run_buildout():
        print('START')
        print(system(cmd))
        print('END')

    test.globs['run_buildout'] = run_buildout

    # Install the recipe in develop mode
    zc.buildout.testing.install_develop('collective.recipe.environment', test)

    # Install any other recipes that should be available in the tests
    zc.buildout.testing.install(mr.scripty.__name__, test)


def test_suite():
    suite = unittest.TestSuite((
            doctest.DocFileSuite(
                '../../../../README.rst',
                setUp=setUp,
                tearDown=zc.buildout.testing.buildoutTearDown,
                optionflags=optionflags,
                checker=renormalizing.RENormalizing([
                        # If want to clean up the doctest output you
                        # can register additional regexp normalizers
                        # here. The format is a two-tuple with the RE
                        # as the first item and the replacement as the
                        # second item, e.g.
                        # (re.compile('my-[rR]eg[eE]ps'), 'my-regexps')
                        zc.buildout.testing.normalize_path,
                        ]),
                ),
            ))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
