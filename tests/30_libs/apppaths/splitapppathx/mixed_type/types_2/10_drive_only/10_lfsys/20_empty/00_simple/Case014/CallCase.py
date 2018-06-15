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
from filesysobjects import RTE, RTE_WIN32
#
#######################
#


class CallUnits(unittest.TestCase):

    def testCase002(self):
        apstr = filesysobjects.paths.normpathx('d:')
        apstr += os.pathsep + filesysobjects.paths.normpathx('')
        apstr += os.pathsep + filesysobjects.paths.normpathx('e:')
        apstr += os.pathsep + filesysobjects.paths.normpathx('')
        apstr += os.pathsep + filesysobjects.paths.normpathx('f:')
        apstr += os.pathsep + filesysobjects.paths.normpathx('')
        if RTE & RTE_WIN32:
            retRef = [
                ('', '', 'd:', ''),
                ('', '', 'e:', ''),
                ('', '', 'f:', ''),
            ]
        else:
            retRef = [('', '', 'd:', '::e:::f::')]
        ret = filesysobjects.apppaths.splitapppathx(
            apstr,delnulpsep=True, rtype=True, appsplit=True, spf='win', tpf='win')
        self.assertEqual(retRef, ret)
        pass

    def testCase010(self):
        apstr = filesysobjects.paths.normpathx('d:')
        apstr += os.pathsep + filesysobjects.paths.normpathx('')
        apstr += os.pathsep + filesysobjects.paths.normpathx('e:')
        apstr += os.pathsep + filesysobjects.paths.normpathx('')
        apstr += os.pathsep + filesysobjects.paths.normpathx('f:')
        apstr += os.pathsep + filesysobjects.paths.normpathx('')
        if RTE & RTE_WIN32:
            retRef = [
                ('', '', 'd:', ''),
                ('','', '', ''),
                ('', '', 'e:', ''),
                ('','', '', ''),
                ('', '', 'f:', ''),
                ('','', '', ''),
            ]
        else:
            retRef = [
                ('lfsys','', '', 'd'),
                ('lfsys','', '', ''),
                ('','', '', ''),
                ('lfsys','', '', 'e'),
                ('lfsys','', '', ''),
                ('','', '', ''),
                ('lfsys','', '', 'f'),
                ('lfsys','', '', ''),
                ('','', '', ''),
            ]
        ret = filesysobjects.apppaths.splitapppathx(apstr,delnulpsep=False, rtype=True, pathsep=os.pathsep, appsplit=True)
        self.assertEqual(retRef, ret)
        pass
#
#######################
#

if __name__ == '__main__':
    unittest.main()

