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

import testdata.filesysobjects.normdata.unescapepathx.normdata as normdata
import os
from filesysobjects import RTE, RTE_WIN32, RTE_CYGWIN, RTE_DARWIN,\
    RTE_LINUX, RTE_BSD, RTE_POSIX

refdata = None
mytpf = 'win'
if RTE & RTE_CYGWIN:
    from testdata.filesysobjects.normdata.unescapepathx.normresult.Cygwin.win import norm_result #@UnresolvedImport #@UnusedImport #@Reimport
    import testdata.filesysobjects.normdata.unescapepathx.normresult.Cygwin.win
    norm_result_source = testdata.filesysobjects.normdata.unescapepathx.normresult.Cygwin.win.__file__
if RTE & 255 | RTE_POSIX  ==  RTE_BSD:
    from testdata.filesysobjects.normdata.unescapepathx.normresult.BSD.win import norm_result #@UnresolvedImport #@UnusedImport #@Reimport
    norm_result_source = 'NONE'
if RTE & 255 | RTE_POSIX  ==  RTE_LINUX:
    from testdata.filesysobjects.normdata.unescapepathx.normresult.Linux.win import norm_result #@UnresolvedImport #@UnusedImport #@Reimport
    import testdata.filesysobjects.normdata.unescapepathx.normresult.Linux.win
    norm_result_source = testdata.filesysobjects.normdata.unescapepathx.normresult.Linux.win.__file__
if RTE & RTE_WIN32:
    from testdata.filesysobjects.normdata.unescapepathx.normresult.Windows.win import norm_result #@UnresolvedImport #@UnusedImport #@Reimport
    import testdata.filesysobjects.normdata.unescapepathx.normresult.Windows.win
    norm_result_source = testdata.filesysobjects.normdata.unescapepathx.normresult.Windows.win.__file__
if RTE & 255 | RTE_POSIX  ==  RTE_DARWIN:
    from testdata.filesysobjects.normdata.unescapepathx.normresult.OSX.win import norm_result #@UnresolvedImport #@UnusedImport #@Reimport
    norm_result_source = 'NONE'


class CallUnits(normdata.CallUnitsBase):
    """Sets the specific data array and required parameters for test case.
    """

    def setUp(self):
        normdata.CallUnitsBase.setUp(self) 
        # Perform the base class init, e.g. unittest.TestResult assignment.

        self.curtpf = mytpf
        """Assigns the current call type for conversion parameter of normpathx(tpfx=mytpf)."""
        
        self.norm_result = norm_result 
        """Sets the expected appropriate result data for the set tpf-parameter. """
        
        self.norm_result_source = os.path.splitext(norm_result_source)[0]+'.py'
        """Source of ref-data. """

        self.refdata = refdata
        """Link for exception-reports."""
        
        self.kwargs = {'force': True}
        """Context specific keyword arguments."""

    def testCase_callDataArray(self):
        """Calls the prepared tests from provided array.
        """
        self.calltests(strip=False)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

