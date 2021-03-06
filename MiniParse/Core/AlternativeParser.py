# -*- coding: utf-8 -*-

# Copyright 2013 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of MiniParse. http://jacquev6.github.com/MiniParse

# MiniParse is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# MiniParse is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with MiniParse.  If not, see <http://www.gnu.org/licenses/>.


class AlternativeParser:
    def __init__(self, elements, match=lambda x: x):
        self.__elements = elements
        self.__match = match

    def apply(self, cursor):
        with cursor.backtracking as bt:  # @todo Here, we need backtracking only because of self.__expected.
            for element in self.__elements:
                if element.apply(cursor):
                    return bt.success(self.__match(cursor.value))
            return bt.failure()
