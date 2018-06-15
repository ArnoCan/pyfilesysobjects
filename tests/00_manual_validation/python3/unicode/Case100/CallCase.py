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
    """Evaluates character sets


    * bytes => str
    * bytes => unicode

    * raw => bytes
    * raw => str
    * raw => unicode

    * str => bytes
str => raw
    * str => str
    * str => unicode

unicode => bytes
unicode => str


    """

    def setUp(self):

        self.kwargs = {}
        self.kwargs['spf'] = 'posix'
        self.kwargs['tpf'] = 'posix'
        self.kwargs['strip'] = False
        self.kwargs['delnulpsep'] = True
        self.kwargs['apppre'] = False

    def testCase_bytes_str(self):
        """bytes => str

        arg_b = b'\u0041\u0042/'

        # displayed / str:
        #   arg_b:          python2 - str: \u0041\u0042/
        #   arg_b:          python3 - bytes: b'\\u0041\\u0042/'
        #   arg_b_bytes:    python2 - str: \u0041\u0042/
        #   arg_b_bytes:    python3 - bytes: b'AB/'

        """

        arg_b = b'\u0041\u0042/'

        if not V3K:
            # arg = str(arg_b)
            arg = arg_b.decode('ascii')
            resX = '\\u0041\\u0042/'
#            resX = 'AB/'

        else:
            # arg = arg_b.decode('ascii')
            arg = arg_b.decode('utf_8', errors='strict')  # => str: \u0041\u0042/
            resX = '\\u0041\\u0042/'

        # 4TEST:
        #print("4TEST:")
        #arg_b = '\u0041\u0042/'
        #x0 = len(arg_b)
        #x1 = len(arg)

        res = normpathx(arg, **self.kwargs)

        self.assertEqual(res, resX)

    def testCase_bytes_unicode(self):
        """bytes => unicode

        arg_b = b'\u0041\u0042/'

        # displayed / str:
        #   arg_b:          python2 - str: \u0041\u0042/
        #   arg_b:          python3 - bytes: b'\\u0041\\u0042/'
        #   arg_b_bytes:    python2 - str: \u0041\u0042/
        #   arg_b_bytes:    python3 - bytes: b'AB/'

        """

        arg_b = b'\u0041\u0042/'

        if not V3K:
            # OK: arg = unicode(arg_b)  # @UndefinedVariable
            # OK: resX = unicode('/u0041/u0042/')  # @UndefinedVariable

            arg = arg_b.decode('utf_8', errors='strict')
            resX = '\\u0041\\u0042/'.decode('utf_8', errors='strict')  # @UndefinedVariable

        else:
            # OK: arg = str(arg_b,'utf_8')  # => str: \u0041\u0042/
            # NOK: arg = str(arg_b)  # => str: b'\\u0041\\u0042/'
            arg = arg_b.decode('utf_8', errors='strict')  # => str: \u0041\u0042/
            resX = '\\u0041\\u0042/'

        res = normpathx(arg, **self.kwargs)

        self.assertEqual(res, resX)

    def testCase_raw_bytes(self):
        """raw => bytes

        arg_r = r'\u0041\u0042/'

        # displayed / str:
        #   arg_r:          python2 - str: \u0041\u0042/
        #   arg_r:          python3 - str: \u0041\u0042/
        #   arg_r_bytes:    python2 - str: \u0041\u0042/
        #   arg_r_bytes:    python3 - str: bytes: b'AB/'

        """

        arg_r = r'\u0041\u0042/'
        if not V3K:
            arg = arg_r
            resX = b'\\u0041\\u0042/'

        else:
            arg = arg_r
            resX = b'\\u0041\\u0042/'

        res = normpathx(arg, **self.kwargs)

        if not V3K:
            res = bytes(res)
        else:
            res = bytes(res, 'ascii')
            # res = res.encode('ascii')

        self.assertEqual(res, resX)


    def testCase_raw_str(self):
        """raw => str

        arg_r = r'\u0041\u0042/'

        # displayed / str:
        #   arg_r:          python2 - str: \u0041\u0042/
        #   arg_r:          python3 - str: \u0041\u0042/
        #   arg_r_bytes:    python2 - str: \u0041\u0042/
        #   arg_r_bytes:    python3 - str: bytes: b'AB/'

        """

        arg_r = r'\u0041\u0042/'
        if not V3K:
            arg = arg_r
            resX = '\\u0041\\u0042/'

        else:
            arg = str(arg_r)
            arg = arg_r.encode('utf_8')

            arg = arg_r

            resX = '\\u0041\\u0042/'

        res = normpathx(arg, **self.kwargs)

        self.assertEqual(res, resX)

    def testCase_raw_unicode(self):
        """raw => unicode

        arg_r = r'\u0041\u0042/'

        # displayed / str:
        #   arg_r:          python2 - str: \u0041\u0042/
        #   arg_r:          python3 - str: \u0041\u0042/
        #   arg_r_bytes:    python2 - str: \u0041\u0042/
        #   arg_r_bytes:    python3 - str: bytes: b'AB/'

        """

        # arg_r = r'\u0041\u0042/'
#        arg_r = r'\u0041\u0042/\a/\b'
#        arg_r = r'\\u0041\u0042/\a/\b'
        arg_r = r'\u0041\u0042/\a/\b'
        if not V3K:
            arg = unicode(arg_r)  # @UndefinedVariable
            resX = '\\u0041\\u0042//a//b'

        else:
            arg = str(arg_r)
            resX = '\\u0041\\u0042//a//b'

        res = normpathx(arg, **self.kwargs)

        self.assertEqual(res, resX)

    def testCase_str_bytes(self):
        """str => bytes

        arg = '\u0041\u0042/'

        # displayed / str:
        #   arg:           python2 - str: /u0041/u0042/
        #   arg:           python3 - str: AB/
        #   arg_bytes:     python2 - str: \u0041\u0042/
        #   arg_bytes:     python3 - bytes: b'AB/'

        """

        arg = '\u0041\u0042/'
        if not V3K:
            arg = arg
            resX = '\\u0041\\u0042/'

        else:
            arg = arg
            resX = b'AB/'

        res = normpathx(arg, **self.kwargs)

        if not V3K:
            # res = bytes(res)
            res = res.encode('ascii')

        else:
            # res = bytes(res, 'ascii')
            res = res.encode('ascii')

            # res = res.decode('ascii')
            # res = res.encode('ascii')

        self.assertEqual(res, resX)

    def testCase_str_str(self):
        """str => str

        arg = '\u0041\u0042/'

        # displayed / str:
        #   arg:           python2 - str: /u0041/u0042/
        #   arg:           python3 - str: AB/
        #   arg_bytes:     python2 - str: \u0041\u0042/
        #   arg_bytes:     python3 - bytes: b'AB/'

        """

        arg = '\u0041\u0042/'
        if not V3K:
            arg = arg
            resX = '\\u0041\\u0042/'

            arg_bytes = bytes(arg)

        else:
            arg = arg
            resX = 'AB/'

            arg_bytes = bytes(arg, 'ascii')

        res = normpathx(arg, **self.kwargs)

        self.assertEqual(res, resX)

    def testCase_str_unicode(self):
        """str => unicode

        arg = '\u0041\u0042/'

        # displayed / str:
        #   arg:           python2 - str: /u0041/u0042/
        #   arg:           python3 - str: AB/
        #   arg_unicode:   python2 - unicode: \u0041\u0042/
        #   arg_unicode:   python3 - str: AB/

        """

        arg = '\u0041\u0042/'
        if not V3K:
            arg = unicode(arg)  # @UndefinedVariable
            resX = u'\\u0041\\u0042/'

        else:
            arg = arg
            resX = 'AB/'

        res = normpathx(arg, **self.kwargs)

        self.assertEqual(res, resX)

    def testCase_unicode_str(self):
        """unicode => str

        arg = '\u0041\u0042/'

        # displayed / str:
        #   arg:           python2 - str: /u0041/u0042/
        #   arg:           python3 - str: AB/
        #   arg_unicode:   python2 - unicode: \u0041\u0042/
        #   arg_unicode:   python3 - str: AB/

        """

        arg = u'\u0041\u0042/'
        if not V3K:
            # arg = str(arg)  # @UndefinedVariable
            arg = arg.encode('ascii')  # @UndefinedVariable
            resX = 'AB/'

        else:
            arg = arg
            resX = 'AB/'

        res = normpathx(arg, **self.kwargs)

        self.assertEqual(res, resX)

if __name__ == '__main__':
    unittest.main()

