""" [RFC8089]_ - Appendix E.4. Backslash as Separator

.. seealso:


   Historically, some usages have copied entire file paths into the path
   components of file URIs. Where DOS or Windows file paths were thus
   copied, the resulting URI strings contained unencoded backslash "\"
   characters, which are forbidden by both [RFC1738] and [RFC3986].

   It may be possible to translate or update such an invalid file URI by
   replacing all backslashes "\" with slashes "/" if it can be
   determined with reasonable certainty that the backslashes are
   intended as path separators.

"""
from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

from filesysobjects import RTE, RTE_WIN32, PathError
import filesysobjects.apppaths

#
#######################
#


class UseCase(unittest.TestCase):

    def testCase040(self):
        """
        rfc8089 - mapped to path-absolute rule
        """

        arg = "file:c:\\home1\\user"

        if RTE & RTE_WIN32:
            resX = "file:///c:/home1/user"
        else:
            resX = "file:///c:/home1/user"
        
        res = filesysobjects.apppaths.normapppathx(arg, apppre=True)
        self.assertEqual(res, resX)


if __name__ == '__main__':
    unittest.main()

