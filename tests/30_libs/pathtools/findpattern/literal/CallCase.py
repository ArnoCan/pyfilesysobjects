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
from filesysobjects import T_ALL, T_DIR

#
#######################
#

tdata = testdata.filesysobjects.mypath + os.path.sep + 'a'

class UseCase(unittest.TestCase):

    def testCase080(self):
        kargs = {}
        kargs['types'] = T_ALL ^ T_DIR
        retX = [
            tdata+os.path.normpath('/b/c/c.sh'),
            tdata+os.path.normpath('/b2/c/c.sh'),
            tdata+os.path.normpath('/b0/c/c.sh'),
        ]
        kargs['whitelist'] = retX
        
        ret = findpattern(tdata,**kargs)
        
        ret = sorted(ret)
        retX.sort()
        
        self.maxDiff = None
        self.assertEqual(sorted(ret), sorted(retX))
        pass

    def testCase090(self):
        kargs = {}
        kargs['types'] = T_ALL ^ T_DIR
        retX = [
            tdata+os.path.normpath('/b/c/c.sh'),
            tdata+os.path.normpath('/b2/c/c.sh'),
            tdata+os.path.normpath('/b0/c/c.sh'),

            tdata+os.path.normpath('/a.smod'),
            tdata+os.path.normpath('/b3/smods/a.smod'),
            tdata+os.path.normpath('/b3/smods/b/c/a.smod'),
            tdata+os.path.normpath('/b3/smods/c/c/a.smod'),
            tdata+os.path.normpath('/b3/smods/c/c/d/a.smod'),
            tdata+os.path.normpath('/b3/smods/c/c/d/e/a.smod'),
            tdata+os.path.normpath('/b3/smods/c/d/a.smod'),
            tdata+os.path.normpath('/b3/smods/a/a.smod'),
            tdata+os.path.normpath('/b3/smods/a/c/a.smod'),
            
        ]
        kargs['whitelist'] = retX
        
        ret = findpattern(tdata,**kargs)

        ret = sorted(ret)
        retX.sort()
        self.maxDiff = None
        self.assertEqual(ret, retX)
        pass

    def testCase100(self):
        kargs = {}
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
        kargs['whitelist'] = retX
        
        ret = findpattern(tdata,**kargs)

        ret = sorted(ret)
        retX.sort()
        self.maxDiff = None
        self.assertEqual(ret, retX)
        pass

    def testCase200(self):
        kargs = {}
        kargs['types'] = T_ALL ^ T_DIR
        retX = [
            tdata + os.path.normpath("/..pl"),
            tdata + os.path.normpath("/..pm"),
            tdata + os.path.normpath("/..pod"),
            tdata + os.path.normpath("/..py"),
            tdata + os.path.normpath("/A.txt"),
            tdata + os.path.normpath("/__init__.py"),
            tdata + os.path.normpath("/a.sh"),
            tdata + os.path.normpath("/a.smod"),
            tdata + os.path.normpath("/b/B.txt"),
            tdata + os.path.normpath("/b/__init__.py"),
            tdata + os.path.normpath("/b/b.pl"),
            tdata + os.path.normpath("/b/b.pm"),
            tdata + os.path.normpath("/b/b.pod"),
            tdata + os.path.normpath("/b/b.py"),
            tdata + os.path.normpath("/b/b.sh"),
            tdata + os.path.normpath("/b/b.smod"),
            tdata + os.path.normpath("/b/c/C.txt"),
            tdata + os.path.normpath("/b/c/__init__.py"),
            tdata + os.path.normpath("/b/c/c.pl"),
            tdata + os.path.normpath("/b/c/c.pm"),
            tdata + os.path.normpath("/b/c/c.pod"),
            tdata + os.path.normpath("/b/c/c.py"),
            tdata + os.path.normpath("/b/c/c.sh"),
            tdata + os.path.normpath("/b/c/c.smod"),
            tdata + os.path.normpath("/b/c/d/D.txt"),
            tdata + os.path.normpath("/b/c/d/__init__.py"),
            tdata + os.path.normpath("/b/c/d/d.pl"),
            tdata + os.path.normpath("/b/c/d/d.pm"),
            tdata + os.path.normpath("/b/c/d/d.pod"),
            tdata + os.path.normpath("/b/c/d/d.py"),
            tdata + os.path.normpath("/b/c/d/d.sh"),
            tdata + os.path.normpath("/b/c/d/d.smod"),
            tdata + os.path.normpath("/b/libb.sh"),
            tdata + os.path.normpath("/b0/B.txt"),
            tdata + os.path.normpath("/b0/__init__.py"),
            tdata + os.path.normpath("/b0/b0.pl"),
            tdata + os.path.normpath("/b0/b0.pm"),
            tdata + os.path.normpath("/b0/b0.pod"),
            tdata + os.path.normpath("/b0/b0.py"),
            tdata + os.path.normpath("/b0/b0.sh"),
            tdata + os.path.normpath("/b0/b0.smod"),
            tdata + os.path.normpath("/b0/c/C.txt"),
            tdata + os.path.normpath("/b0/c/__init__.py"),
            tdata + os.path.normpath("/b0/c/c.pl"),
            tdata + os.path.normpath("/b0/c/c.pm"),
            tdata + os.path.normpath("/b0/c/c.pod"),
            tdata + os.path.normpath("/b0/c/c.py"),
            tdata + os.path.normpath("/b0/c/c.sh"),
            tdata + os.path.normpath("/b0/c/c.smod"),
            tdata + os.path.normpath("/b0/c/d/D.txt"),
            tdata + os.path.normpath("/b0/c/d/__init__.py"),
            tdata + os.path.normpath("/b0/c/d/d.pl"),
            tdata + os.path.normpath("/b0/c/d/d.pm"),
            tdata + os.path.normpath("/b0/c/d/d.pod"),
            tdata + os.path.normpath("/b0/c/d/d.py"),
            tdata + os.path.normpath("/b0/c/d/d.sh"),
            tdata + os.path.normpath("/b0/c/d/d.smod"),
            tdata + os.path.normpath("/b0/libb0.sh"),
            tdata + os.path.normpath("/b1/B1.txt"),
            tdata + os.path.normpath("/b1/__init__.py"),
            tdata + os.path.normpath("/b1/b1.pl"),
            tdata + os.path.normpath("/b1/b1.pm"),
            tdata + os.path.normpath("/b1/b1.pod"),
            tdata + os.path.normpath("/b1/b1.py"),
            tdata + os.path.normpath("/b1/b1.sh"),
            tdata + os.path.normpath("/b1/b1.smod"),
            tdata + os.path.normpath("/b1/c1/C1.txt"),
            tdata + os.path.normpath("/b1/c1/__init__.py"),
            tdata + os.path.normpath("/b1/c1/c1.pl"),
            tdata + os.path.normpath("/b1/c1/c1.pm"),
            tdata + os.path.normpath("/b1/c1/c1.pod"),
            tdata + os.path.normpath("/b1/c1/c1.py"),
            tdata + os.path.normpath("/b1/c1/c1.sh"),
            tdata + os.path.normpath("/b1/c1/c1.smod"),
            tdata + os.path.normpath("/b1/c1/d1/D1.txt"),
            tdata + os.path.normpath("/b1/c1/d1/__init__.py"),
            tdata + os.path.normpath("/b1/c1/d1/d1.pl"),
            tdata + os.path.normpath("/b1/c1/d1/d1.pm"),
            tdata + os.path.normpath("/b1/c1/d1/d1.pod"),
            tdata + os.path.normpath("/b1/c1/d1/d1.py"),
            tdata + os.path.normpath("/b1/c1/d1/d1.sh"),
            tdata + os.path.normpath("/b1/c1/d1/d1.smod"),
            tdata + os.path.normpath("/b1/libb1.sh"),
            tdata + os.path.normpath("/b2/B.txt"),
            tdata + os.path.normpath("/b2/__init__.py"),
            tdata + os.path.normpath("/b2/b2.pl"),
            tdata + os.path.normpath("/b2/b2.pm"),
            tdata + os.path.normpath("/b2/b2.pod"),
            tdata + os.path.normpath("/b2/b2.py"),
            tdata + os.path.normpath("/b2/b2.sh"),
            tdata + os.path.normpath("/b2/b2.smod"),
            tdata + os.path.normpath("/b2/c/C.txt"),
            tdata + os.path.normpath("/b2/c/__init__.py"),
            tdata + os.path.normpath("/b2/c/c.pl"),
            tdata + os.path.normpath("/b2/c/c.pm"),
            tdata + os.path.normpath("/b2/c/c.pod"),
            tdata + os.path.normpath("/b2/c/c.py"),
            tdata + os.path.normpath("/b2/c/c.sh"),
            tdata + os.path.normpath("/b2/c/c.smod"),
            tdata + os.path.normpath("/b2/c/d/D.txt"),
            tdata + os.path.normpath("/b2/c/d/__init__.py"),
            tdata + os.path.normpath("/b2/c/d/d.pl"),
            tdata + os.path.normpath("/b2/c/d/d.pm"),
            tdata + os.path.normpath("/b2/c/d/d.pod"),
            tdata + os.path.normpath("/b2/c/d/d.py"),
            tdata + os.path.normpath("/b2/c/d/d.sh"),
            tdata + os.path.normpath("/b2/c/d/d.smod"),
            tdata + os.path.normpath("/b2/c0/C.txt"),
            tdata + os.path.normpath("/b2/c0/__init__.py"),
            tdata + os.path.normpath("/b2/c0/c0.pl"),
            tdata + os.path.normpath("/b2/c0/c0.pm"),
            tdata + os.path.normpath("/b2/c0/c0.pod"),
            tdata + os.path.normpath("/b2/c0/c0.py"),
            tdata + os.path.normpath("/b2/c0/c0.sh"),
            tdata + os.path.normpath("/b2/c0/c0.smod"),
            tdata + os.path.normpath("/b2/c0/d/D.txt"),
            tdata + os.path.normpath("/b2/c0/d/__init__.py"),
            tdata + os.path.normpath("/b2/c0/d/d.pl"),
            tdata + os.path.normpath("/b2/c0/d/d.pm"),
            tdata + os.path.normpath("/b2/c0/d/d.pod"),
            tdata + os.path.normpath("/b2/c0/d/d.py"),
            tdata + os.path.normpath("/b2/c0/d/d.sh"),
            tdata + os.path.normpath("/b2/c0/d/d.smod"),
            tdata + os.path.normpath("/b2/c1/C.txt"),
            tdata + os.path.normpath("/b2/c1/__init__.py"),
            tdata + os.path.normpath("/b2/c1/c1.pl"),
            tdata + os.path.normpath("/b2/c1/c1.pm"),
            tdata + os.path.normpath("/b2/c1/c1.pod"),
            tdata + os.path.normpath("/b2/c1/c1.py"),
            tdata + os.path.normpath("/b2/c1/c1.sh"),
            tdata + os.path.normpath("/b2/c1/c1.smod"),
            tdata + os.path.normpath("/b2/c1/d1/D.txt"),
            tdata + os.path.normpath("/b2/c1/d1/__init__.py"),
            tdata + os.path.normpath("/b2/c1/d1/d1.pl"),
            tdata + os.path.normpath("/b2/c1/d1/d1.pm"),
            tdata + os.path.normpath("/b2/c1/d1/d1.pod"),
            tdata + os.path.normpath("/b2/c1/d1/d1.py"),
            tdata + os.path.normpath("/b2/c1/d1/d1.sh"),
            tdata + os.path.normpath("/b2/c1/d1/d1.smod"),
            tdata + os.path.normpath("/b2/c2/C.txt"),
            tdata + os.path.normpath("/b2/c2/__init__.py"),
            tdata + os.path.normpath("/b2/c2/c2.pl"),
            tdata + os.path.normpath("/b2/c2/c2.pm"),
            tdata + os.path.normpath("/b2/c2/c2.pod"),
            tdata + os.path.normpath("/b2/c2/c2.py"),
            tdata + os.path.normpath("/b2/c2/c2.sh"),
            tdata + os.path.normpath("/b2/c2/c2.smod"),
            tdata + os.path.normpath("/b2/c2/d/D.txt"),
            tdata + os.path.normpath("/b2/c2/d/D1.txt"),
            tdata + os.path.normpath("/b2/c2/d/D2.txt"),
            tdata + os.path.normpath("/b2/c2/d/__init__.py"),
            tdata + os.path.normpath("/b2/c2/d/d.pl"),
            tdata + os.path.normpath("/b2/c2/d/d.pm"),
            tdata + os.path.normpath("/b2/c2/d/d.pod"),
            tdata + os.path.normpath("/b2/c2/d/d.py"),
            tdata + os.path.normpath("/b2/c2/d/d.sh"),
            tdata + os.path.normpath("/b2/c2/d/d.smod"),
            tdata + os.path.normpath("/b2/libb2.sh"),
            tdata + os.path.normpath("/b3/libb0.sh"),
            tdata + os.path.normpath("/b3/libb3/a.sh"),
            tdata + os.path.normpath("/b3/libb3/b.sh"),
            tdata + os.path.normpath("/b3/libb3/libb3.sh"),
            tdata + os.path.normpath("/b3/libb4/a.sh"),
            tdata + os.path.normpath("/b3/libb4/b.sh"),
            tdata + os.path.normpath("/b3/libb4/hook.sh"),
            tdata + os.path.normpath("/b3/smods/a.smod"),
            tdata + os.path.normpath("/b3/smods/a/a.smod"),
            tdata + os.path.normpath("/b3/smods/a/b.smod"),
            tdata + os.path.normpath("/b3/smods/a/c/a.smod"),
            tdata + os.path.normpath("/b3/smods/a/c/h.smod"),
            tdata + os.path.normpath("/b3/smods/a/c/help.smod"),
            tdata + os.path.normpath("/b3/smods/a/c/self.smod"),
            tdata + os.path.normpath("/b3/smods/a/h.smod"),
            tdata + os.path.normpath("/b3/smods/a/help.smod"),
            tdata + os.path.normpath("/b3/smods/a/self.smod"),
            tdata + os.path.normpath("/b3/smods/b.smod"),
            tdata + os.path.normpath("/b3/smods/b/c.smod"),
            tdata + os.path.normpath("/b3/smods/b/c/a.smod"),
            tdata + os.path.normpath("/b3/smods/b/c/h.smod"),
            tdata + os.path.normpath("/b3/smods/b/c/help.smod"),
            tdata + os.path.normpath("/b3/smods/b/c/self.smod"),
            tdata + os.path.normpath("/b3/smods/b/h.smod"),
            tdata + os.path.normpath("/b3/smods/b/help.smod"),
            tdata + os.path.normpath("/b3/smods/b/self.smod"),
            tdata + os.path.normpath("/b3/smods/c.smod"),
            tdata + os.path.normpath("/b3/smods/c/c.smod"),
            tdata + os.path.normpath("/b3/smods/c/c/a.smod"),
            tdata + os.path.normpath("/b3/smods/c/c/d/a.smod"),
            tdata + os.path.normpath("/b3/smods/c/c/d/e/a.smod"),
            tdata + os.path.normpath("/b3/smods/c/c/d/e/h.smod"),
            tdata + os.path.normpath("/b3/smods/c/c/d/e/help.smod"),
            tdata + os.path.normpath("/b3/smods/c/c/d/e/self.smod"),
            tdata + os.path.normpath("/b3/smods/c/c/d/h.smod"),
            tdata + os.path.normpath("/b3/smods/c/c/d/help.smod"),
            tdata + os.path.normpath("/b3/smods/c/c/d/self.smod"),
            tdata + os.path.normpath("/b3/smods/c/c/h.smod"),
            tdata + os.path.normpath("/b3/smods/c/c/help.smod"),
            tdata + os.path.normpath("/b3/smods/c/c/self.smod"),
            tdata + os.path.normpath("/b3/smods/c/d/a.smod"),
            tdata + os.path.normpath("/b3/smods/c/d/h.smod"),
            tdata + os.path.normpath("/b3/smods/c/d/help.smod"),
            tdata + os.path.normpath("/b3/smods/c/d/self.smod"),
            tdata + os.path.normpath("/b3/smods/c/h.smod"),
            tdata + os.path.normpath("/b3/smods/c/help.smod"),
            tdata + os.path.normpath("/b3/smods/c/self.smod"),

        ]
        kargs['whitelist'] = retX

        ret = findpattern(tdata,**kargs)

        ret = sorted(ret)
        retX.sort()
        
        # 4TEST:
        # # gen retX
        # for i in ret:
        #     print('tdata + os.path.normpath("' + i + '"),')
        # 
        # self.maxDiff = None
        # self.assertEqual(ret, retX)
        # pass

#
#######################
#

if __name__ == '__main__':
    unittest.main()

