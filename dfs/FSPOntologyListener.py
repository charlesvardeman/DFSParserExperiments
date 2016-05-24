# -*- coding: utf-8 -*-
'''dfs

Usage:
  dfs  FILE
  dfs -h | --help
  dfs --version

Options:
  -h --help     Show this screen.
  --version     Show version.
'''
from __future__ import unicode_literals, print_function
from FinalStatePatternListener import FinalStatePatternListener


class FSPOntologyListener(FinalStatePatternListener):
    FSOs = []

    def enterObjectSpecNameOnly(self, ctx):
        pass


    # Enter a parse tree produced by FinalStatePatternParser#ObjectSpecNameAndCutLis
    def enterObjectSpecNameAndCutList(self, ctx):
        pass

    def exitObjectSpecNameAndCutList(self, ctx):
        pass
