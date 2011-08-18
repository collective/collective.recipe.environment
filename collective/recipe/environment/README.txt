Overview
========

This recipe allows to set environment variables during the execution of a buildout.

There isn't any options for this recipe: all options in the part are set as environment variables.

The environment variables are set during the initialization of the ``Recipe`` instance, i.e. after 
``buildout.cfg`` is read but before any recipe is installed or updated.

Example usage
=============

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
    <BLANKLINE>


.. References
.. _`mr.scripty`: http://pypi.python.org/pypi/mr.scripty
