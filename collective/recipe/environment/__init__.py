# -*- coding: utf-8 -*-
"""Recipe environment."""
import os

class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        os.environ.update(options)

    def install(self):
        """Installer"""
        return tuple()

    update = install

