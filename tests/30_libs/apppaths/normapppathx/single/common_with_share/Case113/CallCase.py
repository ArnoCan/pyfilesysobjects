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

import filesysobjects.paths

#
#######################
#


class CallUnits(unittest.TestCase):
    """Network resources IEEE.1003.1/CIFS/SMB/UNC - respect hostname
    """

    def testCase000(self):

        start = filesysobjects.apppaths.normapppathx('hostname/tests//////a/b/hostname//c////////d/tests/b///c')
        startRef = ('lfsys', '', '', 'hostname/tests/a/b/hostname/c/d/tests/b/c')
        ret = filesysobjects.apppaths.splitapppathx(start, appsplit=True, tpf='posix')[0]
        self.assertEqual(startRef, ret)


        top = filesysobjects.apppaths.normapppathx('hostname', apppre=False)
        topRef = [('lfsys', '', '', 'hostname')]
        ret = filesysobjects.apppaths.splitapppathx(top, appsplit=True, tpf='posix')
        self.assertEqual(topRef, ret)
        pass

    def testCase020(self):

        start = filesysobjects.apppaths.normapppathx('hostname/tests//////a/b/hostname//c////////d/tests/b///c')
        startRef = ('lfsys', '', '', 'hostname/tests/a/b/hostname/c/d/tests/b/c')
        ret = filesysobjects.apppaths.splitapppathx(start, appsplit=True, tpf='posix')[0]
        self.assertEqual(startRef, ret)


        top = filesysobjects.apppaths.normapppathx('hostname', apppre=False)
        topRef = [('lfsys', '', '', 'hostname')]
        ret = filesysobjects.apppaths.splitapppathx(top, appsplit=True, tpf='posix')
        self.assertEqual(topRef, ret)


        top=filesysobjects.apppaths.normapppathx('hostname/tests/a/b/hostname')
        topRef = ('lfsys', '', '', 'hostname/tests/a/b/hostname')
        top = filesysobjects.apppaths.gettop_from_pathstring(top, [start])
        ret = filesysobjects.apppaths.splitapppathx(top, appsplit=True, tpf='posix')[0]

        self.assertEqual(topRef, ret)
        pass

if __name__ == '__main__':
    unittest.main()

