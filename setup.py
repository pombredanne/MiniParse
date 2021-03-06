#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of MiniParse. http://jacquev6.github.com/MiniParse

# MiniParse is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# MiniParse is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with MiniParse.  If not, see <http://www.gnu.org/licenses/>.

import setuptools
import textwrap

version = "0.2.0"


if __name__ == "__main__":
    setuptools.setup(
        name="MiniParse",
        version=version,
        description="Minimal, hence simple, parsing library, with a focus on clear error messages",
        author="Vincent Jacques",
        author_email="vincent@vincent-jacques.net",
        url="http://jacquev6.github.com/MiniParse",
        long_description=textwrap.dedent("""\
        Documentation
        =============

        See http://jacquev6.github.com/MiniParse
        """),
        packages=[
            "MiniParse",
            "MiniParse.Core",
            "MiniParse.Core.tests",
            "MiniParse.Examples",
            "MiniParse.Examples.StringArithmetic",
            "MiniParse.Meta",
            "MiniParse.Meta.Grammars",
            "MiniParse.Meta.Grammars.HandWrittenEbnf",
            "MiniParse.Meta.Drawable",
            "MiniParse.Meta.Generable",
        ],
        package_data={
            "MiniParse": ["COPYING*"],
        },
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.3",
            "Topic :: Software Development",
        ],
        test_suite="MiniParse.tests",
        use_2to3=True
    )
