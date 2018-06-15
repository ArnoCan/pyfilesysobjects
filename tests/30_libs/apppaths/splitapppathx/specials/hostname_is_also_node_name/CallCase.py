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

    def testCase010(self):

        arg = filesysobjects.paths.normpathx('//hostname/tests//////a/b/hostname//c////////d/tests/b///c', tpf='win')
        res = filesysobjects.apppaths.splitapppathx(arg, appsplit=True)

        resx = [
            ('share', 'hostname', 'tests', '\\a\\b\\hostname\\c\\d\\tests\\b\\c')
        ]
        self.assertEqual(resx, res)
        pass


    def testCase030(self):

        arg = filesysobjects.paths.normpathx(
            '//hostname/tests//////a/b/hostname//c////////d/tests/b///c',
            tpf='win',
            strip=False,
            )
        res = filesysobjects.apppaths.splitapppathx(
            arg, appsplit=True,
            # escape=False, unescape=False,
            strip=True,
            keepsep=True,
            )

        resx = [
            ('share', 'hostname', 'tests', '\\a\\b\\hostname\\c\\d\\tests\\b\\c')
        ]
        self.assertEqual(resx, res)
        pass

if __name__ == '__main__':
    unittest.main()

