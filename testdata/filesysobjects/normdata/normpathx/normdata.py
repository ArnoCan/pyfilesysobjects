# -*- coding: utf-8 -*-
""""
The common basic reference data for::

    os.path.normpath()

and::

    filesysobjects.pathts.normapppathx.

This data set provides reference data for "Posix",
and "MS-Windows" based local file path names.
The alphabet for this generic test is based on ASC-II
focusing on reserved processing characters, which may
basically not be altered by local native language
support with 8bits.

Including the special control characters::

    r'\a', r'\b', r'\f', r'\n', r'\r', r'\t', r'\v',

Including the special printable characters::

    r'"', r"'", r':', r' ',

Including the special on some platforms prohibited characters,
which could occur in shared multi-platform mounts from others::

    r'/', '\\', r';'

"""
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.16'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import sys, os

try:
    import unittest2 as unittest #@UnusedImport @UnresolvedImport
except:
    import unittest # @Reimport @UnresolvedImport

from pysourceinfo.fileinfo import getcaller_filepathname, getcaller_linenumber
from filesysobjects.paths import normpathx


# Note ( os.path - doc)
#
# Since different operating systems have different path name conventions, there
# are several versions of this module in the standard library. The os.path module
# is always the path module suitable for the operating system Python is running on,
# and therefore usable for local paths. However, you can also import and use the
# individual modules if you want to manipulate a path that is always in one of the
# different formats. They all have the same interface:
#
#     posixpath for UNIX-style paths
#     ntpath for Windows paths
#     macpath for old-style MacOS paths
#     os2emxpath for OS/2 EMX paths
#
import ntpath
import posixpath


class CallUnitsBaseException(BaseException):
    pass

class CallUnitsBase(unittest.TestCase):
    """Validates against a set of equal long transformed data,
    updates the total counter of performed testst by size of
    *self.norm_data*.

    The controlling parameters are:

    * result: From unittest.TestCase.run()
    * tpf/curtpf: from derived class by setUp()
    * norm_result: from derived class by setUp()
    * curidx: current index
    * erridx: current error index

    """

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.curtpf = None
        """Assigns the current call type for conversion parameter of normapppathx(tpf=mytpf)."""

        self.curspf = None
        """Assigns the current call type for conversion parameter of normapppathx(spf=myspf)."""

        self.norm_data = None
        """Input data for normative tests."""

        self.norm_data_source = None
        """Source of data. """

        self.norm_result = None
        """Sets the expected appropriate result data for comparison. """

        self.norm_result_source = None
        """Ref-Data source. """

        self.norm_data = None
        """Input data for normative tests."""

        self.curidx = -1

        self.erridx = -1

        self._continue = False
        self._continue = True


    def __str__(self):
        res = ''
        res += super(CallUnitsBase,self).__str__()
        if self.norm_data:
            res += ("TEST[%s]: norm_data[%d] of total=%d\n")%(self.curtpf,self.curidx,len(self.norm_data))
            res += "#-------\n"
            res += ("# INPUT:   refdata[%3d]   = '%s'\n")%(self.curidx,str(self.norm_data[self.curidx]))
            res += ("# EXPECT:  refresult[%3d] = '%s'\n")%(self.curidx,str(self.norm_result[self.curidx]))
            res += ("# GOT:     result[%3d]    = '%s'")%(self.curidx,str(normpathx(self.norm_data[self.curidx],tpf=self.curtpf,strip=self._strip)))
        return res

    def printInput(self):
        print("self.norm_data = [")
        for i in range(len(self.norm_data)):
            if i%5 == 0:
                print ("#--- %d")%(i)
            print ("\tr'%s', # %d")%(str(self.norm_data[i]),i)
        print("]")
        pass

    def printExpect(self):
        print("norm_result = [")
        for i in range(len(self.norm_data)):
            if i%5 == 0:
                print ("#--- %d")%(i)
            print ("\tr'%s', # %d")%(str(normpathx(self.norm_data[i],tpf=self.curtpf,strip=self._strip)),i)
        print("]")
        pass

    def run(self, result=None, **kargs):
        self.myresult = result
        self.assertTrue(result, "Requires a result object for accurate counter.")
        try:
            super(CallUnitsBase,self).run(result)
        except:
            # debug reminder
            raise

#     def countTestCases(self):
#         return len(self.norm_data)


    def calltests(self,**kargs):
        """
        Calls test function for elements from array.

        Args:
            **kargs:

                first: Start at element
                    default:=0

                last:  Finish at element, [first,last)
                    default:=len(self.norm_data)

                single: Only the given, ignores first,last

        """
        self._strip=kargs.get('strip',True)
        self._spf=kargs.get('spf',self.curspf)

        s=kargs.get('single',-1)
        if s == -1:
            f=kargs.get('first',0)
            l=kargs.get('last',len(self.norm_data))
        else:
            if s == len(self.norm_data):
                self.assertEqual(
                    s,
                    len(self.norm_data),
                    "Out of range(0,"+str(len(self.norm_data))+"):single="+str(s)
                    )
            f=s
            l=s+1
        if l==-1:
            l = len(self.norm_data)
        if f<0 or f>=l or l>len(self.norm_data):
            self.assertEqual(
                f,
                len(self.norm_data),
                "Range(0,"+str(len(self.norm_data)) + ") requires first<last, error: first=" +\
                    str(f)+" last="+str(l)
                )
        if len(self.norm_data) != len(self.norm_result):

#             sys.stderr.write("# TRACE:      "+str(os.path.splitext(__file__)[0]+'.py')+" : "+str(getcaller_linenumber())+"\n")
#             sys.stderr.write("# DATA:       "+str(os.path.splitext(self.norm_data_source)[0]+'.py')+" : "+str(13)+"\n")
#             sys.stderr.write("# REF-DATA:   "+str(self.norm_result_source)+"\n")
#             sys.stderr.write("# CALLER:     "+str(getcaller_filepathname(2))+" : "+str(getcaller_linenumber(2))+"\n")

            _txt = (
                "\n# TRACE:      "+str(os.path.splitext(__file__)[0]+'.py')+" : "+str(getcaller_linenumber())+"\n"
                + "# DATA:       "+str(os.path.splitext(self.norm_data_source)[0]+'.py')+" : "+str(13)+"\n"
                + "# REF-DATA:   "+str(self.norm_result_source)+"\n"
                + "# CALLER:     "+str(getcaller_filepathname(2))+" : "+str(getcaller_linenumber(2))+"\n"
            )

            self.assertEqual(
                len(self.norm_data),
                len(self.norm_result),
                _txt + "Sets mismatch: self.norm_data="+str(len(self.norm_data))+" norm_result="+str(len(self.norm_result))
                )

        i=0

        try:
            kwargs = self.kwargs  # init
        except:
            kwargs = {}

        kwargs['spf'] = self.curspf  # forced
        kwargs['tpf'] = self.curtpf  # forced
        kwargs['strip'] = self._strip  # forced
        kwargs['delnulpsep'] = kargs.get('delnulpsep', True)
        kwargs['apppre'] = False  # TODO: check

        for i in range(f,l):
            self.curidx = i # for __str__
            try:
                # INFO: linennumber for eclipse-console
                testgetcall_linenumber = getcaller_linenumber() + 3
                #
                # INFO: breakpoint for i value
                res = normpathx(self.norm_data[i],tpf=self.curtpf,spf=self.curspf,strip=self._strip)

                # 4TEST: print as ref data - needs some manual post-processing
                # if not i%5:
                #     print("4TEST:#--- " + str(i))
                # print("4TEST:     r'" + str(ret) + "',")
                # # r'/w1/w1/w2',

                self.assertEqual(res, self.norm_result[i])
                self.myresult.addSuccess(self)

            except Exception as e:

                self.myresult.addError(self, sys.exc_info())

                sys.stderr.write("# FAILED: "+str(self.curtpf)+" "+str(i)+"/"+str(len(self.norm_data))+"\n")

                _line_estimate = 14 + i + i/5
                _line_estimate_ref = 14 + i + i/5

                sys.stderr.write("# TRACE:      "+str(os.path.splitext(__file__)[0]+'.py')+" : "+str(getcaller_linenumber())+"\n")
                sys.stderr.write("# TEST-CALL:  "+str(os.path.splitext(__file__)[0]+'.py')+" : "+str(testgetcall_linenumber)+"\n")
                sys.stderr.write("# DATA:       "+str(os.path.splitext(self.norm_data_source)[0]+'.py')+" : "+str(_line_estimate)+"\n")
                sys.stderr.write("# REF-DATA:   "+str(self.norm_result_source) + " : " + str(_line_estimate_ref) +"\n")
                sys.stderr.write("# CALLER:     "+str(getcaller_filepathname(2))+" : "+str(getcaller_linenumber(2))+"\n")
                sys.stderr.write(("  ->  INPUT:     refdata[%3d]        = '%s'\n")%(i,str(self.norm_data[i])))
                sys.stderr.write(("  ==  EXPECT:    result[%3d]         = '%s'\n")%(i,str(self.norm_result[i])))
                sys.stderr.write(("  <-  GOT:       normpathx()[%3d]    = '%s'\n")%(i,str(res)))
                sys.stderr.write(("  *   posixpath  normpath()[%3d]     = '%s'\n")%(i,str(posixpath.normpath(self.norm_data[i]))))
                sys.stderr.write(("  *   ntpath     normpath()[%3d]     = '%s'\n")%(i,str(ntpath.normpath(self.norm_data[i]))))
                self.erridx += 1

                if e is not AssertionError:
                    sys.stderr.write(("# EXCEPTION:     [%3d] = '%s'\n\n")%(i,str(e)))

                if not self._continue:
                    self.assertTrue(
                        False,
                        "Abort on first failure" + str(e)
                        )

            self.myresult.testsRun += 1


if __name__ == '__main__':
    unittest.main()
