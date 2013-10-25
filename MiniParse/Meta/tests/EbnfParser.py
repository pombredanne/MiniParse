# -*- coding: utf-8 -*-

# Copyright 2013 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of MiniParse. http://jacquev6.github.com/MiniParse

# MiniParse is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# MiniParse is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with MiniParse.  If not, see <http://www.gnu.org/licenses/>.

import os
import unittest

import MiniParse.Meta.Ebnf.Tokens as Tok
from MiniParse.Meta.Ebnf.Lexer import Lexer
from MiniParse.Meta.Ebnf.Parser import Parser
from MiniParse.Meta.Ebnf.NonTerminals import *


class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self.lexer = Lexer()
        self.parser = Parser()

    def parse(self, input, output):
        self.assertEqual(self.parser(self.lexer(input)), output)

    def testTerminalRule(self):
        self.parse("foo = 'bar';", Syntax([SyntaxRule("foo", Terminal("bar"))]))

    def testSeveralDefinitions(self):
        self.parse("foo = 'bar'; foo='baz';", Syntax([SyntaxRule("foo", Terminal("bar")), SyntaxRule("foo", Terminal("baz"))]))

    def testDefinitionsList(self):
        self.parse("foo = 'bar' | 'baz';", Syntax([SyntaxRule("foo", DefinitionsList([Terminal("bar"), Terminal("baz")]))]))

    # def testEbnfSyntax(self):
    #     self.parse(open(os.path.join(os.path.dirname(__file__), "..", "Ebnf", "ebnf.ebnf")).read())
