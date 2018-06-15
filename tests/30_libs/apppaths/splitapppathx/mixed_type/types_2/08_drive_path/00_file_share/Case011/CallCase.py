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

    def testCase020(self):
        apstr = 'd:/hostname/share/a/b/c'
        apstr += ';' + filesysobjects.paths.normpathx('//hostname/share/a/b/c', tpf='win')
        apstr += ';'+ filesysobjects.paths.normpathx('d:/hostname/share/a/b/c', tpf='win')
        apstr += ';'+ filesysobjects.paths.normpathx('//hostname/share/a/b/c', tpf='win')
        apstr += ';'+ filesysobjects.paths.normpathx('d:/hostname/share/a/b/c', tpf='win')
        apstr += ';'+ filesysobjects.paths.normpathx('//hostname/share/a/b/c', tpf='win')
        retRef = [
            ('ldsys','', 'd:', filesysobjects.paths.normpathx('/hostname/share/a/b/c', tpf='win')),
            ('share','hostname', 'share', filesysobjects.paths.normpathx('/a/b/c', tpf='win')),
            ('ldsys','', 'd:', filesysobjects.paths.normpathx('/hostname/share/a/b/c', tpf='win')),
            ('share','hostname', 'share', filesysobjects.paths.normpathx('/a/b/c', tpf='win')),
            ('ldsys','', 'd:', filesysobjects.paths.normpathx('/hostname/share/a/b/c', tpf='win')),
            ('share','hostname', 'share', filesysobjects.paths.normpathx('/a/b/c', tpf='win')),
        ]
        ret = filesysobjects.apppaths.splitapppathx(apstr, apppre=False, appsplit=True,spf='win', tpf='win')
        self.assertEqual(retRef, ret)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

