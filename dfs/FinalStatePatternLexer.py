# Generated from FinalStatePattern.g4 by ANTLR 4.5.2
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\fQ\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3")
        buf.write(u"\3\4\3\4\3\5\3\5\3\6\3\6\6\6\"\n\6\r\6\16\6#\3\7\5\7")
        buf.write(u"\'\n\7\3\7\6\7*\n\7\r\7\16\7+\3\7\5\7/\n\7\3\7\7\7\62")
        buf.write(u"\n\7\f\7\16\7\65\13\7\3\7\3\7\6\79\n\7\r\7\16\7:\5\7")
        buf.write(u"=\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bH\n\b\3")
        buf.write(u"\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\2\2\f\3\3\5\4\7\5")
        buf.write(u"\t\6\13\7\r\b\17\t\21\n\23\13\25\f\3\2\6\4\2C\\c|\7\2")
        buf.write(u"//\62;C\\aac|\3\2\62;\5\2\f\f\17\17\"\"\\\2\3\3\2\2\2")
        buf.write(u"\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write(u"\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write(u"\3\2\2\2\3\27\3\2\2\2\5\31\3\2\2\2\7\33\3\2\2\2\t\35")
        buf.write(u"\3\2\2\2\13\37\3\2\2\2\r<\3\2\2\2\17G\3\2\2\2\21I\3\2")
        buf.write(u"\2\2\23K\3\2\2\2\25M\3\2\2\2\27\30\7*\2\2\30\4\3\2\2")
        buf.write(u"\2\31\32\7+\2\2\32\6\3\2\2\2\33\34\7.\2\2\34\b\3\2\2")
        buf.write(u"\2\35\36\7\60\2\2\36\n\3\2\2\2\37!\t\2\2\2 \"\t\3\2\2")
        buf.write(u"! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\f\3\2\2\2")
        buf.write(u"%\'\7/\2\2&%\3\2\2\2&\'\3\2\2\2\')\3\2\2\2(*\t\4\2\2")
        buf.write(u")(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2,=\3\2\2\2-/")
        buf.write(u"\7/\2\2.-\3\2\2\2./\3\2\2\2/\63\3\2\2\2\60\62\t\4\2\2")
        buf.write(u"\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2")
        buf.write(u"\2\2\64\66\3\2\2\2\65\63\3\2\2\2\668\7\60\2\2\679\t\4")
        buf.write(u"\2\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;=\3\2")
        buf.write(u"\2\2<&\3\2\2\2<.\3\2\2\2=\16\3\2\2\2>H\7@\2\2?@\7@\2")
        buf.write(u"\2@H\7?\2\2AH\7>\2\2BC\7>\2\2CH\7?\2\2DH\7?\2\2EF\7#")
        buf.write(u"\2\2FH\7?\2\2G>\3\2\2\2G?\3\2\2\2GA\3\2\2\2GB\3\2\2\2")
        buf.write(u"GD\3\2\2\2GE\3\2\2\2H\20\3\2\2\2IJ\7=\2\2J\22\3\2\2\2")
        buf.write(u"KL\7<\2\2L\24\3\2\2\2MN\t\5\2\2NO\3\2\2\2OP\b\13\2\2")
        buf.write(u"P\26\3\2\2\2\13\2#&+.\63:<G\3\2\3\2")
        return buf.getvalue()


class FinalStatePatternLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    NAME = 5
    NUMBER = 6
    BINARY_OP = 7
    LEOF = 8
    COLON = 9
    WS = 10

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'('", u"')'", u"','", u"'.'", u"';'", u"':'" ]

    symbolicNames = [ u"<INVALID>",
            u"NAME", u"NUMBER", u"BINARY_OP", u"LEOF", u"COLON", u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"NAME", u"NUMBER", 
                  u"BINARY_OP", u"LEOF", u"COLON", u"WS" ]

    grammarFileName = u"FinalStatePattern.g4"

    def __init__(self, input=None):
        super(FinalStatePatternLexer, self).__init__(input)
        self.checkVersion("4.5.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


