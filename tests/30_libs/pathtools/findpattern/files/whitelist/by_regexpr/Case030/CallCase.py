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
_TMP_CSPLIT = re.compile( #: static compiled: split pathnames with literal + glob + regexpr
    """
    (
        ((\[[^\]]*\]))                          # 2
        |(([^/\\\\]*\[[^\]]*\]))                # 4
        |(([^/\\\\]*[\\\\]*(?<=[\\\\])[/\\\\])) # 6
        |(([^/\\\\]*)[/\\\\])                   # 8
        |(([^/\\\\]*)$)                         # 10
    )
    """,
    re.VERBOSE
    )

def splitpathx(pattern):
    """Split pathnames with literal + glob + regexpr.
    """
    parts = []
    _split = _TMP_CSPLIT.finditer(pattern) 
    _cur = ""

    for i in _TMP_CSPLIT.finditer(pattern):
        _cur += i.string[i.start():i.end()]
        
        if i.group(2) or i.group(4) or i.group(6):
            if i.end() == len(pattern):
                parts.append(_cur)
                break
            else:
                continue

        # REMINDER: here trustingly fall-through -> else:
        # elif i.group(8) or i.group(10):
        #     parts.append(_cur)
        #     _cur = ""

        else:
            parts.append(_cur)
            if i.end() == len(pattern):
                break
            _cur = ""
            
    return parts

class UseCase(unittest.TestCase):

    def testCase010_temp_check(self):
        pattern0 = '/a/[^/]+\/x[^/]+/.*/[c]+.sh'
        parts = splitpathx(pattern0)

        # print("# 4TEST:")
        # print("#----")
        # print(pattern0)
        # print(parts)
        # pass

if __name__ == '__main__':
    unittest.main()

