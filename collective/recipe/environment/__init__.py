# -*- coding: utf-8 -*-
"""Recipe environment."""
import os
import re


class Recipe(object):
    """zc.buildout recipe"""

    _PROBLEMATIC_VALUE_PATTERN = re.compile(r'\${\S+?}', re.I)

    def __init__(self, buildout, name, options):
        self.options = options
        os.environ.update(options)

        env_vars = {k: self._escape_var_substitutions(v) for (k, v) in os.environ.iteritems()}
        options.update(env_vars)

    def install(self):
        return ()

    update = install

    def _escape_var_substitutions(self, value):
        u"""Escape what looks like variable substituion in buildout syntax.

        Eg.: ${foo} => $${foo}

        If this is not done things break.

        See: regression test in README.
        """

        def repl(m):
            return m.group(0).replace('$', '$$')

        return self._PROBLEMATIC_VALUE_PATTERN.sub(repl=repl, string=value)
