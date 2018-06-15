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
from filesysobjects.paths import normpathx
from filesysobjects.apppaths import escapepathx

from filesysobjects import RTE, RTE_WIN32, T_ALL, T_DIR

#
#######################
#

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'

class UseCase(unittest.TestCase):

    def testCase080(self):
        kargs = {}
        kargs['whitelist'] = [
            escapepathx(tdata+os.path.normpath('/.*/.*/c.sh')),
        ]
        retX = [
            tdata+os.path.normpath('/b/c/c.sh'),
            tdata+os.path.normpath('/b2/c/c.sh'),
            tdata+os.path.normpath('/b0/c/c.sh'),
        ]
        retX = [normpathx(x) for x in retX]

        ret = findpattern(escapepathx(tdata),**kargs)

        ret = sorted(ret)
        retX.sort()

        self.maxDiff = None
        self.assertEqual(sorted(ret), sorted(retX))
        pass


    def testCase091(self):
        kargs = {}
        kargs['whitelist'] = [
            tdata+os.path.normpath('/.*/c/c.sh'),
        ]
        kargs['whitelist'] = [escapepathx(x) for x in kargs['whitelist']]

        kargs['types'] = T_ALL ^ T_DIR

        retX = [
            tdata+os.path.normpath('/b/c/c.sh'),
            tdata+os.path.normpath('/b2/c/c.sh'),
            tdata+os.path.normpath('/b0/c/c.sh'),
        ]
        retX = [normpathx(x) for x in retX]

        ret = findpattern(escapepathx(tdata),**kargs)

        ret = sorted(ret)
        retX.sort()
        self.maxDiff = None
        self.assertEqual(ret, retX)
        pass

    def testCase100(self):
        kargs = {}
        kargs['whitelist'] = [
            tdata+os.path.normpath('/.*/b.sh'),
            tdata+os.path.normpath('/.*/.*//[bc].sh'),
            tdata+os.path.normpath('/.*//[lxz]ibb3/libb3.sh'),
            tdata+os.path.normpath('/.*/.*/hook.sh'),
            tdata+os.path.normpath('/a.smod'),
            tdata+os.path.normpath('/.*/.*/a.smod'),
            tdata+os.path.normpath('/.*/.*/.*/a.smod'),
            tdata+os.path.normpath('/.*/.*/.*/.*/a.smod'),
            tdata+os.path.normpath('/.*/.*/.*/.*/.*/a.smod'),
            tdata+os.path.normpath('/.*/.*/c.smod'),
            tdata+os.path.normpath('/.*/.*/.*/c.smod'),
        ]
        kargs['whitelist'] = [escapepathx(x) for x in kargs['whitelist']]


        kargs['types'] = T_ALL ^ T_DIR

        retX = [
            tdata+os.path.normpath('/b/b.sh'),
            tdata+os.path.normpath('/b3/libb3/b.sh'),
            tdata+os.path.normpath('/b3/libb4/b.sh'),

            tdata+os.path.normpath('/b/c/c.sh'),
            tdata+os.path.normpath('/b2/c/c.sh'),
            tdata+os.path.normpath('/b0/c/c.sh'),

            tdata+os.path.normpath('/b3/libb3/libb3.sh'),

            tdata+os.path.normpath('/b3/libb4/hook.sh'),

            tdata+os.path.normpath('/a.smod'),
            tdata+os.path.normpath('/b3/smods/a.smod'),
            tdata+os.path.normpath('/b3/smods/b/c/a.smod'),
            tdata+os.path.normpath('/b3/smods/c/c/a.smod'),
            tdata+os.path.normpath('/b3/smods/c/c/d/a.smod'),
            tdata+os.path.normpath('/b3/smods/c/c/d/e/a.smod'),
            tdata+os.path.normpath('/b3/smods/c/d/a.smod'),
            tdata+os.path.normpath('/b3/smods/a/a.smod'),
            tdata+os.path.normpath('/b3/smods/a/c/a.smod'),

            tdata+os.path.normpath('/b/c/c.smod'),
            tdata+os.path.normpath('/b0/c/c.smod'),
            tdata+os.path.normpath('/b2/c/c.smod'),
            tdata+os.path.normpath('/b3/smods/b/c.smod'),
            tdata+os.path.normpath('/b3/smods/c.smod'),
            tdata+os.path.normpath('/b3/smods/c/c.smod'),

        ]

        ret = findpattern(tdata,**kargs)

        ret = sorted(ret)
        retX.sort()
        self.maxDiff = None

#         print("4TEST:" + str(ret))
#         print("4TEST:" + str(retX))

        self.assertEqual(ret, retX)
        pass


if __name__ == '__main__':
    unittest.main()

