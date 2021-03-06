# -*- coding: utf-8 -*-

# Copyright 2013 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of MiniParse. http://jacquev6.github.com/MiniParse

# MiniParse is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# MiniParse is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with MiniParse.  If not, see <http://www.gnu.org/licenses/>.

import unittest

from MiniParse import parse, ParsingError


class ParserTestCase(unittest.TestCase):
    def expectSuccess(self, input, value):
        self.assertEqual(parse(self.p, input), value)

    def expectFailure(self, input, position, expected):
        with self.assertRaises(ParsingError) as cm:
            parse(self.p, input)
        self.assertEqual(cm.exception.message, "Syntax error")
        self.assertEqual(cm.exception.position, position)
        self.assertEqual(cm.exception.expected, set(expected))
