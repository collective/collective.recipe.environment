# -*- coding: utf-8 -*-
"""Recipe environment."""
import os
import re

match_string = re.compile('.*[:]+.*').match


class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options
        options.update(os.environ)
        options['UID'] = str(os.getuid())
        options['GID'] = str(os.getgid())

        for i in options:
            if match_string(i):
                i_safe = re.sub(':', '-', i)
                options[i_safe] = options[i]
                del options[i]

    def install(self):
        """Installer"""
        return tuple()

    update = install
