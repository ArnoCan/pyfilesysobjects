# -*- coding: utf-8 -*-
from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

import os
s = os.path.sep
ps = os.pathsep

#
#######################
#

import string
# ascii_lower = set(string.lowercase)
ascii_lower = set(string.ascii_lowercase)
ascii_lower_escape = r'\a\b\c\d\e\f\g\h\i\j\k\l\m\n\o\p\q\r\s\t\\u\v\w\x\y\z'
ascii_lower_escape_set = ['\a','\b','\c','\d','\e','\f','\g','\h','\i','\j','\k','\l','\m','\n','\o','\p','\q','\r','\s','\t','\\u','\v','\w','\\x','\y','\z',]
# ascii_upper = set(string.uppercase)
ascii_upper = set(string.ascii_uppercase)
ascii_upper_escape = '\A\B\C\D\E\F\G\H\I\J\K\L\M\\N\O\P\Q\R\S\T\\U\V\W\X\Y\Z'
ascii_upper_escape_set = ['\A','\B','\C','\D','\E','\F','\G','\H','\I','\J','\K','\L','\M','\\N','\O','\P','\Q','\R','\S','\T','\\U','\V','\W','\X','\Y','\Z',]

class CallUnits(unittest.TestCase):
    
    def testCase_abc00(self):
        _llow = len(ascii_lower)
        _llowesc = len(ascii_lower_escape)
        _llowesc = len(ascii_lower_escape_set)
        _lup = len(ascii_upper)
        _lupesc = len(ascii_upper_escape)
        _lupesc = len(ascii_upper_escape_set)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

