from __future__ import absolute_import
from linecache import getline


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os,sys

import filesysobjects.apppaths

#
#######################
#


class CallUnits(unittest.TestCase):

    def testCase010(self):
        apstr = filesysobjects.paths.normpathx('a/b/c'+os.pathsep+'/d/e',**{'tpf':'win'})
        ret = filesysobjects.apppaths.splitapppathx(apstr,**{'tpf':'win','appsplit':True,})
        retRef = [
            ('lfsys','', '', filesysobjects.paths.normpathx('a/b/c',**{'tpf':'win'})),
            ('lfsys','', '', filesysobjects.paths.normpathx('/d/e',**{'tpf':'win'})),
        ]
        self.assertEqual(retRef, ret)

    def testCase020(self):
        apstr = filesysobjects.paths.normpathx('a/b/c'+os.pathsep+'/d/e'+os.pathsep+'/f/g')
        ret = filesysobjects.apppaths.splitapppathx(apstr,**{'tpf':'win','appsplit':True,})
        retRef = [
            ('lfsys','', '', filesysobjects.paths.normpathx('a/b/c',**{'tpf':'win'})),
            ('lfsys','', '', filesysobjects.paths.normpathx('/d/e',**{'tpf':'win'})),
            ('lfsys','', '', filesysobjects.paths.normpathx('/f/g',**{'tpf':'win'})),
        ]
        self.assertEqual(retRef, ret)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

