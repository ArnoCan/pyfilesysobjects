from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

#
#######################
#

from filesysobjects import V3K
from filesysobjects.paths import normpathx

class CallUnits(unittest.TestCase):
    """Evaluates unicode character sets
    """

    def setUp(self):

        self.kwargs = {}
        self.kwargs['spf'] = 'posix'
        self.kwargs['tpf'] = 'posix'
        self.kwargs['strip'] = False
        self.kwargs['delnulpsep'] = True
        self.kwargs['apppre'] = False

    def testCase010_unicode(self):
        arg = u'\\u0041\u0042/\a/\b'
        if not V3K:
            resX = u'\\u0041B/\a/\b'

        else:
            #arg = str(arg_r)
            resX = u'\\u0041B/\a/\b'

        res = normpathx(arg, **self.kwargs)

        self.assertEqual(res, resX)

    def testCase011_unicode(self):
        arg = '\\u0041\u0042/\a/\b'
        if not V3K:
            # arg = unicode(arg_r)  # @UndefinedVariable
            resX = u'\\u0041\\u0042/\a/\b'

        else:
            resX = u'\\u0041\u0042/\a/\b'

        res = normpathx(arg, **self.kwargs)

        self.assertEqual(res, resX)

    def testCase020_unicode(self):
        arg_r = r'\\u0041\u0042/\a/\b'
        if not V3K:
            arg = unicode(arg_r)  # @UndefinedVariable
            resX = r'//u0041\u0042//a//b'

        else:
            arg = str(arg_r)
            resX = r'//u0041\u0042//a//b'

        res = normpathx(arg, **self.kwargs)

        self.assertEqual(res, resX)

    def testCase030_unicode(self):
        arg_r = r'\u0041\u0042/\a/\b'
        if not V3K:
            arg = unicode(arg_r)  # @UndefinedVariable
            resX = r'\u0041\u0042//a//b'

        else:
            arg = str(arg_r)
            resX = r'\u0041\u0042//a//b'

        res = normpathx(arg, **self.kwargs)

        self.assertEqual(res, resX)

if __name__ == '__main__':
    unittest.main()

