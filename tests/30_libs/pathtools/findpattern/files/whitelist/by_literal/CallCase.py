"""Check default values, and with defaults as passed parameters. 
"""
from __future__ import absolute_import
# from __future__ import print_function

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
from filesysobjects import T_ALL, T_DIR
#
#######################
#

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'

class UseCase(unittest.TestCase):

    def testCase080(self):
        kargs = {}
        kargs['whitelist'] = [
            tdata + os.path.normpath('/b/c/c.sh'),
            tdata + os.path.normpath('/b2/c/c.sh'),
            tdata + os.path.normpath('/b0/c/c.sh'),
        ]
        kargs['types'] = T_ALL ^ T_DIR
        retX = [
            tdata + os.path.normpath('/b/c/c.sh'),
            tdata + os.path.normpath('/b2/c/c.sh'),
            tdata + os.path.normpath('/b0/c/c.sh'),
        ]
        
        ret = findpattern(tdata, **kargs)
        
        ret = sorted(ret)
        retX.sort()
        
        self.maxDiff = None
        self.assertEqual(sorted(ret), sorted(retX))
        pass

    def testCase090(self):
        kargs = {}
        kargs['whitelist'] = [
            tdata + os.path.normpath('/b/c/c.sh'),
            tdata + os.path.normpath('/b2/c/c.sh'),
            tdata + os.path.normpath('/b0/c/c.sh'),

            tdata + os.path.normpath('/a.smod'),
            tdata + os.path.normpath('/b3/smods/a.smod'),
            tdata + os.path.normpath('/b3/smods/b/c/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/c/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/c/d/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/c/d/e/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/d/a.smod'),
            tdata + os.path.normpath('/b3/smods/a/a.smod'),
            tdata + os.path.normpath('/b3/smods/a/c/a.smod'),
        ]
        kargs['types'] = T_ALL ^ T_DIR
        retX = [
            tdata + os.path.normpath('/b/c/c.sh'),
            tdata + os.path.normpath('/b2/c/c.sh'),
            tdata + os.path.normpath('/b0/c/c.sh'),

            tdata + os.path.normpath('/a.smod'),
            tdata + os.path.normpath('/b3/smods/a.smod'),
            tdata + os.path.normpath('/b3/smods/b/c/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/c/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/c/d/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/c/d/e/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/d/a.smod'),
            tdata + os.path.normpath('/b3/smods/a/a.smod'),
            tdata + os.path.normpath('/b3/smods/a/c/a.smod'),
        ]
        
        ret = findpattern(tdata, **kargs)

        ret = sorted(ret)
        retX.sort()
        self.maxDiff = None
        self.assertEqual(ret, retX)
        pass

    def testCase100(self):
        kargs = {}
        kargs['whitelist'] = [
            tdata + os.path.normpath('/b/b.sh'),
            tdata + os.path.normpath('/b3/libb3/b.sh'),
            tdata + os.path.normpath('/b3/libb4/b.sh'),

            tdata + os.path.normpath('/b/c/c.sh'),
            tdata + os.path.normpath('/b2/c/c.sh'),
            tdata + os.path.normpath('/b0/c/c.sh'),

            tdata + os.path.normpath('/b3/libb3/libb3.sh'),

            tdata + os.path.normpath('/b3/libb4/hook.sh'),

            tdata + os.path.normpath('/a.smod'),
            tdata + os.path.normpath('/b3/smods/a.smod'),
            tdata + os.path.normpath('/b3/smods/b/c/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/c/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/c/d/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/c/d/e/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/d/a.smod'),
            tdata + os.path.normpath('/b3/smods/a/a.smod'),
            tdata + os.path.normpath('/b3/smods/a/c/a.smod'),

            tdata + os.path.normpath('/b/c/c.smod'),
            tdata + os.path.normpath('/b0/c/c.smod'),
            tdata + os.path.normpath('/b2/c/c.smod'),
            tdata + os.path.normpath('/b3/smods/b/c.smod'),
            tdata + os.path.normpath('/b3/smods/c.smod'),
            tdata + os.path.normpath('/b3/smods/c/c.smod'),            
        ]
        kargs['types'] = T_ALL ^ T_DIR
        retX = [
            tdata + os.path.normpath('/b/b.sh'),
            tdata + os.path.normpath('/b3/libb3/b.sh'),
            tdata + os.path.normpath('/b3/libb4/b.sh'),

            tdata + os.path.normpath('/b/c/c.sh'),
            tdata + os.path.normpath('/b2/c/c.sh'),
            tdata + os.path.normpath('/b0/c/c.sh'),

            tdata + os.path.normpath('/b3/libb3/libb3.sh'),

            tdata + os.path.normpath('/b3/libb4/hook.sh'),

            tdata + os.path.normpath('/a.smod'),
            tdata + os.path.normpath('/b3/smods/a.smod'),
            tdata + os.path.normpath('/b3/smods/b/c/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/c/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/c/d/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/c/d/e/a.smod'),
            tdata + os.path.normpath('/b3/smods/c/d/a.smod'),
            tdata + os.path.normpath('/b3/smods/a/a.smod'),
            tdata + os.path.normpath('/b3/smods/a/c/a.smod'),

            tdata + os.path.normpath('/b/c/c.smod'),
            tdata + os.path.normpath('/b0/c/c.smod'),
            tdata + os.path.normpath('/b2/c/c.smod'),
            tdata + os.path.normpath('/b3/smods/b/c.smod'),
            tdata + os.path.normpath('/b3/smods/c.smod'),
            tdata + os.path.normpath('/b3/smods/c/c.smod'),

        ]
        
        ret = findpattern(tdata, **kargs)

        ret = sorted(ret)
        retX.sort()
        self.maxDiff = None
        self.assertEqual(ret, retX)
        pass

    def testCase200(self):
        kargs = {}
        kargs['types'] = T_ALL ^ T_DIR
        retX = [
            tdata + os.sep + os.path.normpath("a.smod"),
            tdata + os.sep + os.path.normpath("b3/smods/a.smod"),
            tdata + os.sep + os.path.normpath("b3/smods/a/a.smod"),
            tdata + os.sep + os.path.normpath("b3/smods/a/c/a.smod"),
            tdata + os.sep + os.path.normpath("b3/smods/b/c/a.smod"),
            tdata + os.sep + os.path.normpath("b3/smods/c/c/a.smod"),
            tdata + os.sep + os.path.normpath("b3/smods/c/c/d/a.smod"),
            tdata + os.sep + os.path.normpath("b3/smods/c/c/d/e/a.smod"),
            tdata + os.sep + os.path.normpath("b3/smods/c/d/a.smod"),
        ]

        ret = findpattern(
            tdata,
            whitelist=[
                tdata + os.sep + os.path.normpath("a.smod"),
                tdata + os.sep + os.path.normpath("b3/smods/a.smod"),
                tdata + os.sep + os.path.normpath("b3/smods/a/a.smod"),
                tdata + os.sep + os.path.normpath("b3/smods/a/c/a.smod"),
                tdata + os.sep + os.path.normpath("b3/smods/b/c/a.smod"),
                tdata + os.sep + os.path.normpath("b3/smods/c/c/a.smod"),
                tdata + os.sep + os.path.normpath("b3/smods/c/c/d/a.smod"),
                tdata + os.sep + os.path.normpath("b3/smods/c/c/d/e/a.smod"),
                tdata + os.sep + os.path.normpath("b3/smods/c/d/a.smod"),
            ],
            **kargs
            )

        ret = sorted(ret)
        retX.sort()
        self.maxDiff = None
        
        # # gen retX
        # for i in ret:
        #    print('tdata + os.path.normpath("' + i + '"),')

        self.assertEqual(ret, retX)
        pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

