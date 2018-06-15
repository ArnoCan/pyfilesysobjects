from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

import filesysobjects.apppaths

#
#######################
#


class CallUnits(unittest.TestCase):
    """Network resources IEEE.1003.1/CIFS/SMB/UNC - respect hostname
    """

    def testCase020(self):
        
        start = filesysobjects.paths.normpathx('//hostname/tests//////a/b/hostname//c////////d/tests/b///c', tpf='win')
        top = filesysobjects.paths.normpathx('/hostname', tpf='win')

        top = filesysobjects.paths.escapepathx(top, force=True)
        start = filesysobjects.paths.escapepathx(start, force=True)

        top = filesysobjects.apppaths.gettop_from_pathstring(top, [start], tpf='win')

        top0ref = r'\hostname'

        self.assertEqual(top0ref, top) 
        pass

    def testCase021(self):
        
        start = filesysobjects.paths.normpathx('//hostname/tests//////a/b/hostname//c////////d/tests/b///c', tpf='win')
        top = filesysobjects.paths.normpathx('/hostname', tpf='win')

        top = filesysobjects.apppaths.gettop_from_pathstring(top, [start], spf='win', tpf='win', matchidx=0)

        top0ref=filesysobjects.paths.normpathx('//hostname/tests/a/b/hostname', tpf='win')

        self.assertEqual(top0ref, top) 
        pass

    def testCase030(self):
        
        start = filesysobjects.paths.normpathx('//hostname/tests//////a/b/hostname//c////////d/tests/b///c', tpf='win')
        top = filesysobjects.paths.normpathx('/hostname', tpf='win')

        top = filesysobjects.paths.escapepathx(top, force=False)
        start = filesysobjects.paths.escapepathx(start, force=False)

        top = filesysobjects.apppaths.gettop_from_pathstring(top, [start], tpf='win')

        top = filesysobjects.paths.escapepathx(top, force=False)

        ret = filesysobjects.apppaths.splitapppathx(top, appsplit=True, tpf='win')

        topRef = [('share', 'hostname', 'tests', '\\a\\b\\hostname')]

        self.assertEqual(topRef, ret) 
        pass

    def testCase040(self):
        
        start = filesysobjects.paths.normpathx('//hostname/tests//////a/b/hostname//c////////d/tests/b///c', tpf='win')
        top = filesysobjects.paths.normpathx('/hostname', tpf='win')

        top = filesysobjects.paths.escapepathx(top, force=True)
        start = filesysobjects.paths.escapepathx(start, force=True)

        top = filesysobjects.apppaths.gettop_from_pathstring(top, [start], tpf='win')

        top = filesysobjects.paths.escapepathx(top, force=False)

        ret = filesysobjects.apppaths.splitapppathx(top, appsplit=True, tpf='win')

        topRef = [('lfsys', '', '', '\\hostname')]

        self.assertEqual(topRef, ret) 
        pass

    def testCase050(self):
        
        start = filesysobjects.paths.normpathx('//hostname/tests//////a/b/hostname//c////////d/tests/b///c', tpf='win')
        top = filesysobjects.paths.normpathx('/hostname', tpf='win')

        top = filesysobjects.apppaths.gettop_from_pathstring(top, [start], spf='win', tpf='win', matchidx=1)

        ret = filesysobjects.apppaths.splitapppathx(top, appsplit=True, spf='win', tpf='win')

        topRef = [('share', 'hostname', 'tests', '\\a\\b\\hostname')]

        self.assertEqual(topRef, ret) 
        pass

if __name__ == '__main__':
    unittest.main()

