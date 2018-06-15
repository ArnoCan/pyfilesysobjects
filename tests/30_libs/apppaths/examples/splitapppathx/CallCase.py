from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest

#
#######################
#

import filesysobjects.paths

class CallUnits(unittest.TestCase):
    """Sets the specific data array and required parameters for test case.
    """

    def testCase000(self):
        arg = r'/my/odd/searchpath/[/xyz].*/myfile.z'

        res = filesysobjects.paths.splitpathx(
            arg,
            tpf='posix',
            strip=True,
            apppre=False)
        resX = ('', 'my', 'odd', 'searchpath', '[/xyz].*', 'myfile.z')

        self.assertEqual(res, resX)
        self.assertEqual('/'.join(res), arg)

    def testCase020(self):
        arg = r'/my/odd/searchpath/"""this/part/is/spared/[/xyz].*/to/this/point"""/myfile.z'

        res = filesysobjects.paths.splitpathx(
            arg,
            tpf='posix',
            strip=True,
            apppre=False)
        resX = ('', 'my', 'odd', 'searchpath', '"""this/part/is/spared/[/xyz].*/to/this/point"""', 'myfile.z')

        self.assertEqual(res, resX)
        self.assertEqual('/'.join(res), arg)
   
    def testCase030(self):
        arg = r"/my/odd/searchpath/'''this/part/is/spared/[/xyz].*/to/this/point'''/myfile.z"

        res = filesysobjects.paths.splitpathx(
            arg,
            tpf='posix',
            strip=True,
            apppre=False)
        resX = ('', 'my', 'odd', 'searchpath', "'''this/part/is/spared/[/xyz].*/to/this/point'''", 'myfile.z')

        self.assertEqual(res, resX)
        self.assertEqual('/'.join(res), arg)

    def testCase040(self):
        arg = r'\my\odd/searchpath\"""this\part\is\spared\[\\xyz].*\to\this\point"""\myfile.z'

        res = filesysobjects.paths.splitpathx(
            arg,
            tpf='posix',
            strip=True,
            apppre=False)
        resX = (
            '', 'my', 'odd', 'searchpath', '"""this\\part\\is\\spared\\[\\\\xyz].*\\to\\this\\point"""', 'myfile.z'
            )

        self.assertEqual(res, resX)

    def testCase050(self):
        arg = r"\my\odd\searchpath\'''this\part\is\spared\[/xyz].*\to\this\point'''\myfile.z"
        
        res = filesysobjects.paths.splitpathx(
            arg,
            tpf='posix',
            strip=True,
            apppre=False)
        resX = (
            '', 'my', 'odd', 'searchpath', "'''this\\part\\is\\spared\\[/xyz].*\\to\\this\\point'''", 'myfile.z'
            )

        self.assertEqual(res, resX)

    def testCase060(self):
        arg = r'/my/odd/searchpath/"""this/part/is/spared/[/xyz].*/to/this/point"""/myfile.z'
        
        res = filesysobjects.paths.splitpathx(
            arg,
            )
        resx = (
            '', 'my', 'odd', 'searchpath', '"""this/part/is/spared/[/xyz].*/to/this/point"""', 'myfile.z'
            )

        self.assertEqual(res, resx)
        self.assertEqual('/'.join(res), arg)

    def testCase070(self):
        arg = r'/my/odd/searchpath/"""this/part/is/spared/[/xyz].*/to/this/point"""/myfile.z'
        
        res = filesysobjects.paths.splitpathx(
            arg,
            )
        resx = (
           '', 'my', 'odd', 'searchpath', '"""this/part/is/spared/[/xyz].*/to/this/point"""', 'myfile.z'
        )

        self.assertEqual(res, resx)
        self.assertEqual('/'.join(res), arg)

    def testCase080(self):
        arg = r'/my/odd/searchpath/"""this/part/is/spared/[/xyz].*/to/this/point"""/myfile.z'
        
        res = filesysobjects.paths.splitpathx(
            arg,
            stripquotes=True  # default is False
            )
        resx = (
           '', 'my', 'odd', 'searchpath', '"""this/part/is/spared/[/xyz].*/to/this/point"""', 'myfile.z'
        )

        self.assertEqual(res, resx)

    def testCase090(self):
        arg = r'/my/odd/searchpath/"""this/part/is/spared/[/xyz].*/to/this/point"""/myfile.z'
        
        res = filesysobjects.paths.splitpathx(
            arg,
            stripquote=True  # default is False
            )
        resx = (
            '', 'my', 'odd', 'searchpath', 'this/part/is/spared/[/xyz].*/to/this/point', 'myfile.z'
        )

        self.assertEqual(res, resx)



#
#######################
#

if __name__ == '__main__':
    unittest.main()

