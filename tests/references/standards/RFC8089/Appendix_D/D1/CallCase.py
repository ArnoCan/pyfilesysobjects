""" [RFC8089]_ - Appendix D.1. POSIX Systems

.. seealso:

   In a POSIX file system, the root of the file system is represented as
   a directory with a zero-length name, usually written as "/"; the
   presence of this root in a file URI can be taken as given by the
   initial slash in the "path-absolute" rule.
   Common UNIX shells such as the Bourne-Again SHell (bash) and Z SHell
   (zsh) provide a function known as "tilde expansion" [Bash-Tilde] or
   "filename expansion" [Zsh-Tilde], where a path that begins with a
   tilde character "~" can be expanded out to a special directory name.
   No such facility exists using the file URI scheme; a tilde in a file
   URI is always just a tilde.

"""
from __future__ import absolute_import
from __future__ import print_function

import os
import re
import unittest

from filesysobjects import RTE, RTE_WIN32, PathError
import filesysobjects.apppaths
from filesysobjects.pathtools import expandpath
import posixpath

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"


#
#######################
#


class UseCase(unittest.TestCase):

    def testCase000(self):
        """
        rfc8089 - D1: Currently no checks on the "absolute-path" rule is proceeded.
        Thus as a result this is as 'the user originally expects', it the application
        (want to...) handles this.
        """

        arg = "file:~/userfile"

        try:
            res = filesysobjects.apppaths.normapppathx(arg, apppre=True)
        except PathError:
            pass

    def testCase010(self):
        """See RFC8089: D.1. POSIX Systems
        """
        arg = "~/userfile"

        try:
            res = filesysobjects.apppaths.normapppathx(arg, apppre=True)
        except PathError:
            pass

    def testCase011(self):

        arg = "~/userfile"

        if RTE & RTE_WIN32:
            resX = "~\\userfile"
        else:
            resX = "~/userfile"

        res = filesysobjects.apppaths.normapppathx(arg, apppre=False)
        self.assertEqual(res, resX)

    def testCase020(self):
        """See RFC8089: D.1. POSIX Systems
        """

        arg = "~/userfile"

        arg = os.path.expanduser(arg)

        if RTE & RTE_WIN32:
            resX = "file:///" + re.sub('\\\\', '/', arg)
        else:
            resX = "file://" + re.sub('\\\\', '/', arg)

        res = filesysobjects.apppaths.normapppathx(arg, apppre=True)
        self.assertEqual(res, resX)

if __name__ == '__main__':
    unittest.main()

