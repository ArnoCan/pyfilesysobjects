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

    def testCase000(self):
        
        arg = '//hostname/tests//////a/b/hostname//c////////d/tests/b///c' 
        resx = r'\\hostname\tests\a\b\hostname\c\d\tests\b\c'

        res = filesysobjects.paths.normpathx(
            arg, 
            tpf='win',
            # strip=True
            )

        self.assertEqual(resx, res) 
        pass

    def testCase010(self):
        
        arg = '//hostname/tests//////a/b/hostname//c////////d/tests/b///c' 
        resx = r'\\hostname\tests\a\b\hostname\c\d\tests\b\c'

        res = filesysobjects.paths.normpathx(
            arg, 
            tpf='win',
            strip=True
            )

        self.assertEqual(resx, res) 
        pass

    def testCase020(self):
        
        arg =  r'//hostname/tests//////a/b/hostname//c////////d/tests/b///c' 
        resx = r'\\hostname\tests\\\\\\a\b\hostname\\c\\\\\\\\d\tests\b\\\c'

        res = filesysobjects.paths.normpathx(
            arg, 
            tpf='win',
            strip=False
            )

        self.assertEqual(resx, res) 
        pass

if __name__ == '__main__':
    unittest.main()

