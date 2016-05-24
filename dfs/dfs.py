#!/usr/bin/env python
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

from docopt import docopt
from antlr4 import *
from antlr4.tree.Trees import Trees
from FinalStatePatternLexer import FinalStatePatternLexer
from FinalStatePatternParser import FinalStatePatternParser
from FinalStatePatternListener import FinalStatePatternListener
from FSPOntologyListener import FSPOntologyListener

__version__ = "0.1.0"
__author__ = "Charles Vardeman"
__license__ = "MIT"

class FinalStatePatternPrintListener(FinalStatePatternListener):
    def  enterTop_level(self, ctx):
        print("Hello")
        print ("Hello: %s"  %  ctx.LEOF())

def main():
    '''Main entry point for the dfs CLI.'''
    args = docopt(__doc__, version=__version__)
    dslfile = args["FILE"]
    input = FileStream(dslfile)
    lexer = FinalStatePatternLexer(input)
    stream = CommonTokenStream(lexer)
    parser = FinalStatePatternParser(stream)
    tree = parser.top_level()
    traverser = FSPOntologyListener()
    walker = ParseTreeWalker()
    walker.walk(traverser, tree)
    print(Trees.toStringTree(tree, None, parser))



if __name__ == '__main__':
    main()
