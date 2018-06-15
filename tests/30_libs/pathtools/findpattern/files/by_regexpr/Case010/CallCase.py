"""Check default values, and with defaults as passed parameters. 
"""
from __future__ import absolute_import
from __future__ import print_function

_author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.6'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

import testdata.filesysobjects

from filesysobjects.pathtools import findpattern

#
#######################
#

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'

import re
_cx = re.compile("""
    (
        ((\[[^\]]*\]))
        |(([^/\\\\]*\[[^\]]*\][^/\\\\]*){1,3}[/\\\\])
#        |(([^/\\\\]*\[[^\]]*\][^/\\\\]*){1,3}[/\\\\])
        |(([^/\\\\]*)[/\\\\])
        |(([^/\\\\]*)$)
    )
    """,
    re.VERBOSE
    )

def splitpathx(pattern):
    parts = []
    _split = _cx.finditer(pattern) 
    _cur = ""
    for i in _split:
        _cur += i.string[i.start():i.end()]
        if i.string[i.end()-1] != os.path.sep:
            if i.end() == len(pattern):
                parts.append(_cur)
            else:
                continue
        else:
            parts.append(_cur)
            _cur = ""
    return parts

class UseCase(unittest.TestCase):

    def testCase010_temp_check(self):
        pattern0 = '/a/[^/]+x[^/]+/.*/[c]+.sh'
        parts = splitpathx(pattern0)

        # print("# 4TEST:")
        # print("#----")
        # print(pattern0)
        # print(parts)
        # pass

if __name__ == '__main__':
    unittest.main()

