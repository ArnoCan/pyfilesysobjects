# -*- coding: utf-8 -*-
""""
The common basic reference data for::

    os.path.normpath() 

and::

    filesysobjects.pathts.normpathx.

This data set provides reference data for "Posix", 
and "MS-Windows" based local file path names.
The alphabet for this generic test is based on ASC-II
focusing on reserved processing characters, which may
basically not be altered by local native language 
support with 8bits.

Including the special control characters::

    r'file://\a', r'\b', r'\f', r'\n', r'\r', r'\t', r'\v',

Including the special printable characters::

    r'file://"', r"'", r':', r' ',

Including the special on some platforms prohibited characters, 
which could occur in shared multi-platform mounts from others::

    r'file:///', '\\', r';'

"""
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.16'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

norm_data = [
#--- 0
    'file://\w1\w1\w2',
    'file://\\w2\\w1\\w2',
    'file://\\\w3\\\w1\\\w2',
    'file://\\\\w4\\\\w1\\\\w2',
    'file://\\\\\w5\\\\\w1\\\\\w2',
#--- 5
    'file://\\\\\\w6\\\\\\w1\\\\\\w2',
    'file://\\\\\\\w7\\\\\\\w1\\\\\\\w2',
    'file://\\\\\\\\w8\\\\\\\\w1\\\\\\\\w2',
    'file://\\\\\\\\\w9\\\\\\\\\w1\\\\\\\\\w2',
    'file://\\\\\\\\\\w10\\\\\\\\\\w1\\\\\\\\\\w2',
#--- 10
    'file:///w1/w1/w2',
    'file:////w2//w1//w2',
    'file://///w3///w1///w2',
    'file://////w4////w1////w2',
    'file:///////w5/////w1/////w2',
#--- 15
    'file:////////w6//////w1//////w2',
    'file://///////w7///////w1///////w2',
    'file://////////w8////////w1////////w2',
    'file:///////////w9/////////w1/////////w2',
    'file:////////////w10//////////w1//////////w2',
#--- 20
    'file://\/w1/\w1\/w2',
    'file://\\//w2//\\w1\\//w2',
    'file://\\\///w3\\\///w1\\\///w2',
    'file://\\\\////w4\\\\////w1\\\\////w2',
    'file://\\\\\/////w5\\\\\/////w1\\\\\/////w2',
#--- 25
    'file://\/w1/\w1\/w2',
    'file://\/\/w2\/\/w1\/\/w2',
    'file://\/\/\/\/w3\/\/\/\/w1\/\/\/\/w2',
    'file://\/\/\/\/\w4\/\/\/\/\w1\/\/\/\/\w2',
    'file://\/\/\/\/\/w5\/\/\/\/\/w1\/\/\/\/\/w2',
#--- 30
    'file://\//w1//\w1\//w2',
    'file://\//\//w2\//\//w1\//\//w2',
    'file://\///\///\///\///w3\///\///\///\///w1',
    'file://\////\////\////\////\w4\////\////\////w1',
    'file://\/////\/////\/////\/////\/////w5',
#--- 35
    'file://\\/w1/\\w1\\/w2',
    'file://\\\/\\\/w2\\\/\\\/w1\\\/\\\/w2',
    'file://\\\\/\\\\/\\\\/\\\\/w3\\\\/\\\\/\\\\/\\\\/w1',
    'file://\\\\\/\\\\\/\\\\\/\\\\\/\\\\\w4\\\\\/\\\\\/\\\\\/\\\\\/\\\\\w1',
    'file://\\\\\\/\\\\\\/\\\\\\/\\\\\\/\\\\\\/w5',
#--- 40
    'file:///\a',
    'file:///\b',
    'file:///\f',
    'file:///\n',
    'file:///\r',
#--- 45
    'file:///\t',
    'file:///\v',
    'file://\\a',
    'file://\\b',
    'file://\\f',
#--- 50
    'file://\\n',
    'file://\\r',
    'file://\\t',
    'file://\\v',
    'file://\\\a',
#--- 55
    'file://\\\b',
    'file://\\\f',
    'file://\\\n',
    'file://\\\r',
    'file://\\\t',
#--- 60
    'file:///\v',
    'file:///\a',
    'file:///\b',
    'file:///\f',
    'file:///\n',
#--- 65
    'file:///\r',
    'file:///\t',
    'file:///\v',
    'file:///\\a',
    'file:///\\b',
#--- 70
    'file:///\\f',
    'file:///\\n',
    'file:///\\r',
    'file:///\\t',
    'file:///\\v',
#--- 75
    'file:///\\\a',
    'file:///\\\b',
    'file:///\\\f',
    'file:///\\\n',
    'file:///\\\r',
#--- 80
    'file:///\\\t',
    'file:///\\\v',
    'file://\/\\a',
    'file://\/\\b',
    'file://\/\\f',
#--- 85
    'file://\/\\n',
    'file://\/\\r',
    'file://\/\\t',
    'file://\/\\v',
    'file://\\/\a',
#--- 90
    'file://\\/\b',
    'file://\\/\f',
    'file://\\/\n',
    'file://\\/\r',
    'file://\\/\t',
#--- 95
    'file://\\/\v',
    'file://\\\/a',
    'file://\\\/b',
    'file://\\\/f',
    'file://\\\/n',
#--- 100
    'file://\\\/r',
    'file://\\\/t',
    'file://\\\/v',
    'file:///\a/\b/\f/\n/\r/\t/\v',
    'file://\\a\\b\\f\\n\\r\\t\\v',
#--- 105
    'file://\\\a\\\b\\\f\\\n\\\r\\\t\\\v',
    'file://\\\\a\\\\b\\\\f\\\\n\\\\r\\\\t\\\\v',
    'file:////host/share/\a/\b/\f/\n/\r/\t/\v',
    'file:///\a/\b/\f/\n/\r/\t/\v',
    'file:///\a/\b/\f/\n/\r/\t/\v',
#--- 110
    'file://\"\"',
    'file://\\"\\"',
    'file://\\\"\\\"',
    'file://\\\\"\\\\"',
    'file:///"/"',
#--- 115
    'file:////"/"',
    'file:///"/"',
    'file:///"/"',
    'file://\:\:',
    'file://\\:\\:',
#--- 120
    'file://\\\:\\\:;',
    'file://\\\\:;\\\\:',
    'file:///:/:;',
    'file:////:;/:',
    'file:///:/::',
#--- 125
    'file:///:/:',
    'file://\ \ ',
    'file://\\ \\ ',
    'file://\\\ \\\ ',
    'file://\\\\ \\\\ ',
#--- 130
    r'file:/// / ',
    r'file://// / ',
    r'file:/// / ',
    r'file:/// / ',
    r'file://\;\;',
#--- 135
    r'file://\\;\\;',
    r'file://\\\;\\\;',
    r'file://\\\\;\\\\;',
    r'file:///;/;',
    r'file:////;/;',
#--- 140
    r'file:///;/;',
    r'file:///;/;',
    r'file://\
',
    r'file:///\
/',
    r'file:///\
/A/\
',
#--- 145
    r'file:///\
/A',
    r'file:///\
/A/\
/B\
',
    r'file:///\
/w0/\
/w1/\
/',
    u'\u0041', # utf-16 'A'
    u'/\u0041/\u0042/', # utf-16 '/A/B'
#--- 150
    u'//\u0041//\u0042/', # utf-16 '/A/B'
    u'///\u0041///\u0042/', # utf-16 '/A/B'
    u'////\u0041////\u0042/', # utf-16 '/A/B'
    u'\\u0041\\u0042/', # utf-16 '/A/B'
    u'\\\u0041\\\u0042/', # utf-16 '/A/B'
#--- 155
    u'\\\\u0041\\\\u0042/', # utf-16 '/A/B'
    'file://\041', # octal 'A'
    'file:///\041/\042', # octal '/A/B'
    'file:////\041//\042', # octal '/A/B'
    'file://///\041///\042', # octal '/A/B'
#--- 160
    'file://////\041////\042', # octal '/A/B'
    'file://\041', # octal 'A'
    'file://\\041\\042', # octal '\A\B'
    'file://\\041\042', # octal '\A\B'
    'file://\\\041\\\042', # octal '\A\B'
#--- 165
    'file://\\\\041\\\\042', # octal '\A\B'
    'file://\\\\\041\\\\\042', # octal '\A\B'
    'file://\x41', # hex 'A'
    'file:///\x41/\x42', # hex '/A/B'
    'file:////\x41//\x42', # hex '/A/B'
#--- 170
    'file://///\x41///\x42', # hex '/A/B'
    'file://////\x41////\x42', # hex '/A/B'
    'file://\\x41\\x42', # hex '\A\B'
    'file://\\\x41\\\x42', # hex '\A\B'
    'file://\\\\x41\\\\x42', # hex '\A\B'
#--- 175
    'file://\\\\\x41\\\\\x42', # hex '\A\B'
    r'file://\/',
    r'file://\/\/',
    r'file://\/\/\/',
    r'file://\/\/\/\/',
#--- 180
    r'file://\/\/\/\/\/',
    r'file://\\/',
    r'file://\\/\\/',
    r'file://\\/\\/\\/',
    r'file://\\/\\/\\/\\/',
#--- 185
    r'file://\\/\\/\\/\\/\\/',
    r'file://\/\\',
    r'file://\/\\/\\',
    r'file://\/\\/\\/\\',
    r'file://\/\\/\\/\\/\\',
#--- 190
    r'file://\/\\/\\/\\/\\/\\',
    r'file://\\\/',
    r'file://\\\/\\\/',
    r'file://\\\/\\\/\\/',
    r'file://\\\/\\\/\\\/\\\/',
#--- 195
    r'file://\\\/\\\/\\\/\\\/\\/',
    r'file://\\\/',
    r'file://\\\/\\/',
    r'file://\\\/\\/\\/',
    r'file://\\\/\\/\\/\\/',
#--- 200
    r'file://\\\/\\/\/\\/\\/',
    r'file:////"\a\\a\b\\b"///"\\f\f"',
    r'file:///\a/"\a\\a\b\\b"/\b/\f/"\\f\f"',
    r"/\a/'\a\\a\b\\b'/\b/\f/'\\f\f'",
]
""""The common reference input."""

import sys, os

try:
    import unittest2 as unittest #@UnusedImport
except:
    import unittest # @Reimport

from pysourceinfo.fileinfo import getcaller_filepathname, getcaller_linenumber
from filesysobjects.paths import escapepathx


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
    *norm_data*.
     
    The controlling parameters are:
 
    * result: From unittest.TestCase.run()
    * tpf/curtpf: from derived class by setUp()
    * norm_result: from derived class by setUp()
    * curidx: current index
    * erridx: current error index
 
    """
 
    def setUp(self):
        unittest.TestCase.setUp(self)
 
        self.norm_result = None 
        """Sets the expected appropriate result data for comparison. """
 
        self.norm_result_source = None 
        """Ref-Data source. """
 
        self.curtpf = None
        """Assigns the current call type for conversion parameter of normpathx(tpfx=mytpf)."""
 
        self.curidx = -1
         
        self.erridx = -1
         
        self._continue = False
        self._continue = True
 
 
    def __str__(self):
        res  = ("TEST[%s]: norm_data[%d] of total=%d\n")%(self.curtpf,self.curidx,len(norm_data))
        res += "#-------\n"
        res += ("# INPUT:   refdata[%3d]   = '%s'\n")%(self.curidx,str(norm_data[self.curidx]))
        res += ("# EXPECT:  refresult[%3d] = '%s'\n")%(self.curidx,str(self.norm_result[self.curidx]))
        res += ("# GOT:     result[%3d]    = '%s'")%(self.curidx,str(escapepathx(norm_data[self.curidx],tpf=self.curtpf,strip=self._strip)))
        return res
 
    def printInput(self):
        print("norm_data = [")
        for i in range(len(norm_data)):
            if i%5 == 0:
                print ("#--- %d")%(i)
            print ("\tr'%s', # %d")%(str(norm_data[i]),i)
        print("]")
        pass
 
    def printExpect(self):
        print("norm_result = [")
        for i in range(len(norm_data)):
            if i%5 == 0:
                print ("#--- %d")%(i)
            print ("\tr'%s', # %d")%(str(escapepathx(norm_data[i],tpf=self.curtpf,strip=self._strip)),i)
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
#         return len(norm_data)
 
    
    def calltests(self,**kargs):
        """
        Calls test function for elements from array.
         
        Args:
            **kargs:
 
                first: Start at element
                    default:=0
 
                last:  Finish at element, [first,last)
                    default:=len(norm_data)
 
                single: Only the given, ignores first,last
 
        """
        self._strip=kargs.get('strip',True)

        s=kargs.get('single',-1)
        if s == -1:
            f=kargs.get('first',0)
            l=kargs.get('last',len(norm_data))
        else:
            if s == len(norm_data):
                self.assertEqual(
                    s,
                    len(norm_data),
                    "Out of range(0,"+str(len(norm_data))+"):single="+str(s)
                    )
            f=s
            l=s+1
        if l==-1:
            l = len(norm_data)
        if f<0 or f>=l or l>len(norm_data):
            self.assertEqual(
                f,
                len(norm_data),
                "Range(0,"+str(len(norm_data)) + ") requires first<last, error: first=" +\
                    str(f)+" last="+str(l)
                )
        if len(norm_data) != len(self.norm_result):
            sys.stderr.write("# TRACE:      "+str(os.path.splitext(__file__)[0]+'.py')+" : "+str(getcaller_linenumber())+"\n")
            sys.stderr.write("# DATA:       "+str(os.path.splitext(__file__)[0]+'.py')+" : "+str(42)+"\n")
            sys.stderr.write("# REF-DATA:   "+str(self.norm_result_source)+"\n")
            sys.stderr.write("# CALLER:     "+str(getcaller_filepathname(2))+" : "+str(getcaller_linenumber(2))+"\n")

            self.assertEqual(
                len(norm_data),
                len(self.norm_result),
                "Sets mismatch: norm_data="+str(len(norm_data))+" norm_result="+str(len(self.norm_result))
                )
 
        i=0

        try:
            kwargs = self.kwargs  # init
        except:
            kwargs = {}
        
        for i in range(f,l):
            self.curidx = i # for __str__
            try:
                # INFO: linennumber for eclipse-console
                testgetcall_linenumber = getcaller_linenumber() + 3
                #
                # INFO: breakpoint for i value
                ret = escapepathx(norm_data[i], tpf=self.curtpf, **kwargs)

                # 4TEST: print as ref data
#                 if not i%5:
#                     print("4TEST:#--- " + str(i))
#                 print("4TEST:     r'file://" + str(ret) + "',")
                # # r'/w1/w1/w2', 

                
                self.assertEqual(ret, self.norm_result[i])
                self.myresult.addSuccess(self)
 
            except Exception as e:
                 
                self.myresult.addError(self, sys.exc_info())
 
                sys.stderr.write("# FAILED: "+str(self.curtpf)+" "+str(i)+"/"+str(len(norm_data))+"\n")
                
                _line_estimate = 44 + i + i/5
                _line_estimate_ref = 14 + i + i/5
                
                sys.stderr.write("# TRACE:      "+str(os.path.splitext(__file__)[0]+'.py')+" : "+str(getcaller_linenumber())+"\n")
                sys.stderr.write("# TEST-CALL:  "+str(os.path.splitext(__file__)[0]+'.py')+" : "+str(testgetcall_linenumber)+"\n")
                sys.stderr.write("# DATA:       "+str(os.path.splitext(__file__)[0]+'.py')+" : "+str(_line_estimate)+"\n")
                sys.stderr.write("# REF-DATA:   "+str(self.norm_result_source) + " : " + str(_line_estimate_ref) +"\n")
                sys.stderr.write("# CALLER:     "+str(getcaller_filepathname(2))+" : "+str(getcaller_linenumber(2))+"\n")
                sys.stderr.write(("  ->  INPUT:     refdata[%3d]          = '%s'\n")%(i,str(norm_data[i])))
                sys.stderr.write(("  ==  EXPECT:    result[%3d]           = '%s'\n")%(i,str(self.norm_result[i])))
                sys.stderr.write(("  <-  GOT:       escapepathx()[%3d] = '%s'\n")%(i,str(escapepathx(norm_data[i],tpf=self.curtpf,strip=self._strip))))
                sys.stderr.write(("  *   posixpath  normpath()[%3d]       = '%s'\n")%(i,str(posixpath.normpath(norm_data[i]))))
                sys.stderr.write(("  *   ntpath     normpath()[%3d]       = '%s'\n")%(i,str(ntpath.normpath(norm_data[i]))))
                self.erridx += 1
    
                if not self._continue:
                    self.assertTrue(
                        False,
                        "Abort on first failure"
                        )

            # FIXME: i += 1
            self.myresult.testsRun += 1


if __name__ == '__main__':
    unittest.main()