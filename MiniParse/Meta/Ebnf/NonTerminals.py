# -*- coding: utf-8 -*-

# Copyright 2013 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of MiniParse. http://jacquev6.github.com/MiniParse

# MiniParse is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# MiniParse is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with MiniParse.  If not, see <http://www.gnu.org/licenses/>.

import collections


Syntax = collections.namedtuple("Syntax", "rules")
SyntaxRule = collections.namedtuple("SyntaxRule", "name,definition")
SingleDefinition = collections.namedtuple("SingleDefinition", "terms")
DefinitionsList = collections.namedtuple("DefinitionsList", "definitions")
Repetition = collections.namedtuple("Repetition", "number,primary")
Optional = collections.namedtuple("Optional", "definition")
Repeated = collections.namedtuple("Repeated", "definition")
Terminal = collections.namedtuple("Terminal", "value")
NonTerminal = collections.namedtuple("NonTerminal", "name")
