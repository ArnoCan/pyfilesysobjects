from __future__ import absolute_import
from __future__ import print_function

import sys

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.10'
__uuid__ = '9de52399-7752-4633-9fdc-66c87a9200b8'

__docformat__ = "restructuredtext en"

import unittest
import os

import filesysobjects.configdata


#
#######################
#


class CallUnits(unittest.TestCase):

    def testCase010(self):
        cf = filesysobjects.configdata.ConfigPath(
            prepend=os.path.dirname(__file__)
            )
        res = str(cf)
        resx = '[\n' + " " * 4 + '"' + os.path.dirname(__file__)
        
        assert res.startswith(resx)

    def testCase020(self):
        cf = filesysobjects.configdata.ConfigPath(
            append=os.path.dirname(__file__)
            )

        res = str(cf)
        resx = os.path.dirname(__file__) + '",\n' + ']'

        assert res.endswith(resx)

    def testCase030(self):
        cf = filesysobjects.configdata.ConfigPath(
            replace=os.path.dirname(__file__)
            )

        res = str(cf)
        resx = '[\n' + " " * 4 + '"' + os.path.dirname(__file__) + '",\n]'

        assert res == resx

if __name__ == '__main__':
    unittest.main()
