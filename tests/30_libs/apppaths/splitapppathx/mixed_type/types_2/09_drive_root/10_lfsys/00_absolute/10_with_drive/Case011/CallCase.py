from __future__ import absolute_import


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

    def testCase000(self):
        apstr = filesysobjects.paths.normpathx('//hostname/share/a/b/c')
        apstr += os.pathsep + filesysobjects.paths.normpathx('d:/',**{'tpf':'win'})
        apstr += os.pathsep + filesysobjects.paths.normpathx('//hostname/share/a/b/c')
        apstr += os.pathsep + filesysobjects.paths.normpathx('d:/',**{'tpf':'win'})
        apstr += os.pathsep + filesysobjects.paths.normpathx('//hostname/share/a/b/c')
        apstr += os.pathsep + filesysobjects.paths.normpathx('d:/',**{'tpf':'win'})
        if RTE & RTE_WIN32:
            retRef = [
                ('share', 'hostname', 'share', '\\a\\b\\c'),
                ('ldsys', '', 'd:', '\\'),
                ('share', 'hostname', 'share', '\\a\\b\\c'),
                ('ldsys', '', 'd:', '\\'),
                ('share', 'hostname', 'share', '\\a\\b\\c'),
                ('ldsys', '', 'd:', '\\')
            ]
            ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True, spf="win")
        else:
            retRef = [
                ('share','hostname', 'share', filesysobjects.paths.normpathx('/a/b/c', tpf='win')),
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', '\\'),
                ('share','hostname', 'share', filesysobjects.paths.normpathx('/a/b/c', tpf='win')),
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', '\\'),
                ('share','hostname', 'share', filesysobjects.paths.normpathx('/a/b/c', tpf='win')),
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', '\\'),
            ]
            ret = filesysobjects.apppaths.splitapppathx(apstr,apppre=False,appsplit=True, spf="posix", tpf='win')
        self.assertEqual(retRef, ret)

    def testCase001(self):
        apstr = filesysobjects.paths.normpathx('//hostname/share/a/b/c')
        apstr += os.pathsep + filesysobjects.paths.normpathx('d:/',**{'tpf':'win'})
        apstr += os.pathsep + filesysobjects.paths.normpathx('//hostname/share/a/b/c')
        apstr += os.pathsep + filesysobjects.paths.normpathx('d:/',**{'tpf':'win'})
        apstr += os.pathsep + filesysobjects.paths.normpathx('//hostname/share/a/b/c')
        apstr += os.pathsep + filesysobjects.paths.normpathx('d:/',**{'tpf':'win'})
        if RTE & RTE_WIN32:
            retRef = [
                ('share', 'hostname', 'share', '\\a\\b\\c'),
                ('ldsys', '', 'd:', '\\'),
                ('share', 'hostname', 'share', '\\a\\b\\c'),
                ('ldsys', '', 'd:', '\\'),
                ('share', 'hostname', 'share', '\\a\\b\\c'),
                ('ldsys', '', 'd:', '\\')
            ]
            ret = filesysobjects.apppaths.splitapppathx(apstr,appsplit=True, spf="win")
        else:
            retRef = [
                ('share','hostname', 'share', filesysobjects.paths.normpathx('/a/b/c', tpf='posix')),
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', '/'),
                ('share','hostname', 'share', filesysobjects.paths.normpathx('/a/b/c', tpf='posix')),
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', '/'),
                ('share','hostname', 'share', filesysobjects.paths.normpathx('/a/b/c', tpf='posix')),
                ('lfsys', '', '', 'd'),
                ('lfsys', '', '', '/'),
            ]
            ret = filesysobjects.apppaths.splitapppathx(apstr,apppre=False,appsplit=True, spf="posix", tpf='posix')
        self.assertEqual(retRef, ret)


#
#######################
#

if __name__ == '__main__':
    unittest.main()

