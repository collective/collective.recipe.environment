# -*- coding: utf-8 -*-
"""Recipe environment."""
import os

class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.options = options
        os.environ.update(options)
        options.update(os.environ)

    def install(self):
        """Installer"""
        return tuple()

    update = install

