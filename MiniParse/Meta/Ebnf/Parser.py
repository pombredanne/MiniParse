# -*- coding: utf-8 -*-

# Copyright 2013 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of MiniParse. http://jacquev6.github.com/MiniParse

# MiniParse is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# MiniParse is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with MiniParse.  If not, see <http://www.gnu.org/licenses/>.

import MiniParse
from MiniParse import LiteralParser, SequenceParser, AlternativeParser, OptionalParser, RepetitionParser

import Tokens as Tok
from NonTerminals import *


class TransformingParser:  # Temporary class to TDD the parser
    def __init__(self, parser, match):
        self.__parser = parser
        self.__match = match

    def apply(self, cursor):
        with cursor.backtracking as bt:
            if self.__parser.apply(cursor):
                return bt.success(self.__match(cursor.value))
            else:
                return bt.failure()


class ClassParser:
    def __init__(self, class_, match):
        self.__class = class_
        self.__match = match

    def apply(self, cursor):
        with cursor.backtracking as bt:
            if cursor.finished or not isinstance(cursor.current, self.__class):
                return bt.expected(self.__class.__name__)
            else:
                m = cursor.current
                cursor.advance()
                return bt.success(self.__match(m))


class Parser:
    # 4.16
    terminal = ClassParser(Tok.Terminal, lambda t: Terminal(t.value))

    # 4.14
    metaIdentifier = ClassParser(Tok.MetaIdentifier, lambda name: " ".join(name.value))
    nonTerminal = ClassParser(Tok.MetaIdentifier, lambda name: NonTerminal(" ".join(name.value)))

    # 4.13
    class groupedSequence:
        @staticmethod
        def apply(cursor):
            return SequenceParser(
                [
                    LiteralParser(Tok.StartGroup),
                    Parser.definitionsList,
                    LiteralParser(Tok.EndGroup)
                ],
                lambda s, d, e: d
            ).apply(cursor)

    # 4.12
    class repeatedSequence:
        @staticmethod
        def apply(cursor):
            return SequenceParser(
                [
                    LiteralParser(Tok.StartRepeat),
                    Parser.definitionsList,
                    LiteralParser(Tok.EndRepeat)
                ],
                lambda s, d, e: Repeated(d)
            ).apply(cursor)

    # 4.11
    class optionalSequence:
        @staticmethod
        def apply(cursor):
            return SequenceParser(
                [
                    LiteralParser(Tok.StartOption),
                    Parser.definitionsList,
                    LiteralParser(Tok.EndOption)
                ],
                lambda s, d, e: Optional(d)
            ).apply(cursor)

    # 4.10
    syntacticPrimary = AlternativeParser(
        [
            optionalSequence,
            repeatedSequence,
            groupedSequence,
            nonTerminal,
            terminal,
            # specialSequence,  # @todo Implement?
            # emptySequence  # @todo Implement?
        ]
    )

    # 4.9
    integer = ClassParser(Tok.Integer, lambda i: i.value)

    # 4.8
    syntacticFactor = AlternativeParser(
        [
            SequenceParser(
                [integer, LiteralParser(Tok.Repetition), syntacticPrimary],
                lambda i, rep, p: Repetition(i, p)
            ),
            syntacticPrimary
        ]
    )

    # @todo Implement 4.6 (and 4.7)
    syntacticTerm = syntacticFactor

    # 4.5
    singleDefinition = SequenceParser(
        [
            syntacticTerm,
            RepetitionParser(
                SequenceParser(
                    [LiteralParser(Tok.Concatenate), syntacticTerm],
                    lambda s, d: d
                )
            )
        ],
        lambda t1, ts: t1 if len(ts) == 0 else SingleDefinition([t1] + ts)
    )

    # 4.4
    definitionsList = SequenceParser(
        [
            singleDefinition,
            RepetitionParser(
                SequenceParser(
                    [LiteralParser(Tok.DefinitionSeparator), singleDefinition],
                    lambda s, d: d
                )
            )
        ],
        lambda d1, ds: d1 if len(ds) == 0 else DefinitionsList([d1] + ds)
    )

    # 4.3
    syntaxRule = SequenceParser(
        [metaIdentifier, LiteralParser(Tok.Defining), definitionsList, LiteralParser(Tok.Terminator)],
        lambda name, defining, value, terminator: SyntaxRule(name, value)
    )

    # 4.2
    syntax = RepetitionParser(syntaxRule, Syntax)

    def __call__(self, tokens):
        try:
            return MiniParse.parse(self.syntax, tokens)
        except MiniParse.SyntaxError, e:
            print "Expected", " or ".join(str(x) for x in e.expected)
            print "Here:", tokens[e.position:], ">>>", tokens[e.position], "<<<", tokens[e.position + 1]
