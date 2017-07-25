.. contents::

.. image:: https://travis-ci.org/collective/collective.recipe.environment.svg?branch=master
   :target: https://travis-ci.org/collective/collective.recipe.environment
   :alt: Build status

Overview
========

This recipe allows to set and get environment variables during the execution of a buildout.

The recipe mirrors the current environment variables into its section, so that e.g.
``${environment:USER}`` will give the current user.

To set an environment variable you just set it in the section.

The environment variables are set and get during the initialization of the ``Recipe`` instance,
i.e. after ``buildout.cfg`` is read but before any recipe is installed or updated.

Example usage: Use an environment variable
==========================================

We'll start by creating a buildout that uses the recipe::

    >>> write('buildout.cfg',
    ... """
    ... [buildout]
    ... parts = environment print
    ...
    ... [some-section]
    ... some-option = ${environment:SOME_VARIABLE}
    ...
    ... [environment]
    ... recipe = collective.recipe.environment
    ...
    ... [print]
    ... recipe = mr.scripty
    ... install =
    ...     ... print self.buildout['some-section']['some-option']
    ...     ... return []
    ... """)

The `mr.scripty`_ recipe is used to print out the value of the ${some-section:some-option}
option.

Now we set the environment variable::

    >>> import os
    >>> os.environ['SOME_VARIABLE'] = 'some_value'

Running the buildout gives us::

    >>> print 'start', system(buildout)
    start...
    some_value
    ...


Example usage: Set an environment variable
==========================================

We'll start by creating a buildout that uses the recipe::

    >>> write('buildout.cfg',
    ... """
    ... [buildout]
    ... parts = environment print
    ...
    ... [some-section]
    ... some-option = value2
    ...
    ... [environment]
    ... recipe = collective.recipe.environment
    ... var1 = value1
    ... var2 = ${some-section:some-option}
    ...
    ... [print]
    ... recipe = mr.scripty
    ... install =
    ...     ... import os
    ...     ... for var in ('var1', 'var2'):
    ...     ...     print '%s = %s' % (var, os.environ[var])
    ...     ... return []
    ... """)

The `mr.scripty`_ recipe is used to print out the values of the environment variables.

Running the buildout gives us::

    >>> print 'start', system(buildout)
    start...
    var1 = value1
    var2 = value2
    ...


Similar recipes
===============

The functionality to mirror the environment variables into the recipe's section is largely copied
from `gocept.recipe.env`_.


Regression test: Values containing variable substitution syntax breaks things
=============================================================================

Problem: if an environment variable value contains something looking like variable substitution
in Buildout syntax then things break. We fix this by escaping the variable substitutions using
two dollar signs. Eg.: ``${foo}`` becomes ``$${foo}``.

Let's see if it works.

Set environment variables::

    >>> os.environ['PROBLEM_VAR_1'] = '${foo}'
    >>> os.environ['PROBLEM_VAR_2'] = '${foo:bar}'
    >>> os.environ['PROBLEM_VAR_3'] = 'Contains ${foo} and also ${foo:bar}.'
    >>> os.environ['LEGAL_VAR_1'] = '$foo'
    >>> os.environ['LEGAL_VAR_2'] = '{foo}'

Write a buildout using those variables::

    >>> write('buildout.cfg',
    ... """
    ... [buildout]
    ... parts = environment print
    ...
    ... [some-section]
    ... option-1 = ${environment:PROBLEM_VAR_1}
    ... option-2 = ${environment:PROBLEM_VAR_2}
    ... option-3 = ${environment:PROBLEM_VAR_3}
    ... option-4 = ${environment:LEGAL_VAR_1}
    ... option-5 = ${environment:LEGAL_VAR_2}
    ...
    ... [environment]
    ... recipe = collective.recipe.environment
    ...
    ... [print]
    ... recipe = mr.scripty
    ... install =
    ...     ... section = self.buildout['some-section']
    ...     ... for (k, v) in sorted(section.iteritems()):
    ...     ...     print '{} = {}'.format(k, v)
    ...     ... return []
    ...
    ... """)

Running the buildout gives us::

    >>> print 'start', system(buildout)
    start...
    option-1 = $${foo}
    option-2 = $${foo:bar}
    option-3 = Contains $${foo} and also $${foo:bar}.
    option-4 = $foo
    option-5 = {foo}
    ...

.. References
.. _`mr.scripty`: http://pypi.python.org/pypi/mr.scripty
.. _`gocept.recipe.env`: http://pypi.python.org/pypi/gocept.recipe.env
