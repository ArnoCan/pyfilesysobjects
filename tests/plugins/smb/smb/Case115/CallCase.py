from __future__ import absolute_import


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

import filesysobjects.apppaths

#
#######################
#


class CallUnits(unittest.TestCase):
    """Network resources IEEE.1003.1/CIFS/SMB/UNC - respect hostname
    """

    def testCase021(self):
        
        start = filesysobjects.paths.normpathx('//hostname/tests//////a/b/hostname//c////////d/tests/b///c', tpf='win')
        startRef = [('share', 'hostname', 'tests', filesysobjects.paths.normpathx('/a/b/hostname/c/d/tests/b/c', tpf='win'))]
        ret = filesysobjects.apppaths.splitapppathx(start,appsplit=True, tpf='win')
        self.assertEqual(startRef, ret) 


        top = filesysobjects.paths.normpathx('/hostname', tpf='win')
        topRef = [('lfsys', '', '', filesysobjects.paths.normpathx('/hostname', tpf='win'))]
        ret = filesysobjects.apppaths.splitapppathx(top,appsplit=True, tpf='win')
        self.assertEqual(topRef, ret) 


        top0ref = filesysobjects.paths.normpathx('//hostname/tests/a/b/hostname', tpf='win')
        topRef  = [
            ('share', 'hostname', 'tests', filesysobjects.paths.normpathx('/a/b/hostname', tpf='win'))
        ]
        
        topres = filesysobjects.apppaths.gettop_from_pathstring(top, [start], tpf='win')

        topres = filesysobjects.apppaths.escapepathx(topres)

        ret = filesysobjects.apppaths.splitapppathx(topres, appsplit=True, tpf='win')

        self.assertEqual(top0ref, topres) 
        self.assertEqual(topRef, ret) 
        pass


if __name__ == '__main__':
    unittest.main()

