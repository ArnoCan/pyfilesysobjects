from __future__ import absolute_import

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import sys, os

#
#######################
#

import testdata.filesysobjects.normdata.normpathx.normdata as normdata
from testdata.filesysobjects.normdata.normpathx.pathnames.data import norm_data
import testdata.filesysobjects.normdata.normapppathx.pathnames.data
norm_data_source = testdata.filesysobjects.normdata.normapppathx.pathnames.data.__file__

refdata = None
myspf = 'posix'
if sys.platform == 'cygwin':
    mytpf = 'posix'
    from testdata.filesysobjects.normdata.normpathx.pathnames.nostrip.normresult.Cygwin.posix import norm_result #@UnresolvedImport #@UnusedImport #@Reimport
    import testdata.filesysobjects.normdata.normpathx.pathnames.nostrip.normresult.Cygwin.posix
    norm_result_source = testdata.filesysobjects.normdata.normpathx.pathnames.nostrip.normresult.Cygwin.posix.__file__
elif sys.platform == 'openbsd5':
    mytpf = 'posix'
    from testdata.filesysobjects.normdata.normpathx.pathnames.nostrip.normresult.BSD.posix import norm_result #@UnresolvedImport #@UnusedImport #@Reimport
    norm_result_source = 'NONE'
elif sys.platform in ('linux', 'linux2',):
    mytpf = 'posix'
    from testdata.filesysobjects.normdata.normpathx.pathnames.nostrip.normresult.Linux.posix import norm_result #@UnresolvedImport #@UnusedImport #@Reimport
    import testdata.filesysobjects.normdata.normpathx.pathnames.nostrip.normresult.Linux.posix
    norm_result_source = testdata.filesysobjects.normdata.normpathx.pathnames.nostrip.normresult.Linux.posix.__file__
elif sys.platform == 'win32':
    mytpf = 'win'
    from testdata.filesysobjects.normdata.normpathx.pathnames.nostrip.normresult.Windows.win import norm_result #@UnresolvedImport #@UnusedImport #@Reimport
    import testdata.filesysobjects.normdata.normpathx.pathnames.nostrip.normresult.Windows.win
    norm_result_source = testdata.filesysobjects.normdata.normpathx.pathnames.nostrip.normresult.Windows.win.__file__
elif sys.platform == 'darwin':
    mytpf = 'posix'
    from testdata.filesysobjects.normdata.normpathx.pathnames.nostrip.normresult.OSX.posix import norm_result #@UnresolvedImport #@UnusedImport #@Reimport
    norm_result_source = 'NONE'


class CallUnits(normdata.CallUnitsBase):
    """Sets the specific data array and required parameters for test case.
    """

    def setUp(self):
        normdata.CallUnitsBase.setUp(self) 
        # Perform the base class init, e.g. unittest.TestResult assignment.

        self.curtpf = mytpf
        """Assigns the current call type for conversion parameter of normpathx(tpfx=mytpf)."""
        
        self.curspf = myspf
        """Assigns the current call type for conversion parameter of normapppathx(spf=myspf)."""

        self.norm_data = norm_data
        """Input data for normative tests."""

        self.norm_data_source = os.path.splitext(norm_data_source)[0]+'.py'
        """Source of data. """

        self.norm_result = norm_result 
        """Sets the expected appropriate result data for the set tpf-parameter. """
        
        self.norm_result_source = os.path.splitext(norm_result_source)[0]+'.py'
        """Source of ref-data. """

        self.refdata = refdata
        """Link for exception-reports."""

    def testCase_callDataArray(self):
        """Calls the prepared tests from provided array.
        """
        self.calltests(strip=False)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

