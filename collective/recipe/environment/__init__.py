# -*- coding: utf-8 -*-
"""Recipe environment."""
import os
import re

match_string = re.compile('.*[:]+.*').match


class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options, read_only=False):
        self.buildout, self.name, self.options = buildout, name, options
        if not read_only:
            os.environ.update(options)
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

class ReadOnly(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        super(self).__init__(buildout, name, options, read_only=True)
