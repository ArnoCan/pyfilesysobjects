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
        ret = cf.get_filepathname_by_ext('multiconf')
        assert os.path.abspath(os.path.dirname(__file__) + os.sep + 'multiconf.ini') == ret

    def testCase020(self):
        cf = filesysobjects.configdata.ConfigPath(
            prepend=os.path.dirname(__file__)
            )
        ret = cf.get_filepathname_by_ext('multiconf', ['.json', '.ini'])
        assert os.path.abspath(os.path.dirname(__file__) + os.sep + 'multiconf.json') == ret


if __name__ == '__main__':
    unittest.main()
