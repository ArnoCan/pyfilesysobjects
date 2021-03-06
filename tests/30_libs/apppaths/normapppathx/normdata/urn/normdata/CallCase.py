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

import testdata.filesysobjects.normdata.normapppathx.normdata as normdata
import os
from filesysobjects import RTE, RTE_WIN32, RTE_CYGWIN, RTE_DARWIN,\
    RTE_LINUX, RTE_BSD

refdata = None
mytpf = 'uri'
myspf = 'uri'

from testdata.filesysobjects.normdata.normapppathx.uri.urn.data import norm_data
import testdata.filesysobjects.normdata.normapppathx.normdata as normdata
import testdata.filesysobjects.normdata.normapppathx.uri.urn.data
norm_data_source = testdata.filesysobjects.normdata.normapppathx.uri.urn.data.__file__

from testdata.filesysobjects.normdata.normapppathx.uri.urn.normresult.urn import norm_result
import testdata.filesysobjects.normdata.normapppathx.uri.urn.normresult.urn
norm_result_source = testdata.filesysobjects.normdata.normapppathx.uri.urn.normresult.urn.__file__


class CallUnits(normdata.CallUnitsBase):
    """Sets the specific data array and required parameters for test case.
    """

    def setUp(self):
        normdata.CallUnitsBase.setUp(self) 
        # Perform the base class init, e.g. unittest.TestResult assignment.

        self.curtpf = mytpf
        """Assigns the current call type for conversion parameter of normapppathx(tpfx=mytpf)."""
        
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
        self.skipTest("not supported in this release")
        
        self.calltests(strip=False, appsplit=True)

#
#######################
#

if __name__ == '__main__':
    unittest.main()

