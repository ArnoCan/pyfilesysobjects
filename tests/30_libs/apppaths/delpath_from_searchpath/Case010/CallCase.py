from __future__ import absolute_import
from __future__ import print_function

__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.0.1'
__uuid__ = "4135ab0f-fbb8-45a2-a6b1-80d96c164b72"

__docformat__ = "restructuredtext en"

import unittest
import os

import testdata.filesysobjects

from filesysobjects.apppaths import addpath_to_searchpath
from filesysobjects.apppaths import delpath_from_searchpath 
from filesysobjects.apppaths import set_uppertree_searchpath
from filesysobjects.pathtools import findrelpath_in_searchpath, clearpath


#
#######################
#
_plist_ref = [ 
    os.path.normpath(testdata.filesysobjects.mypath+'/examples/a/b0/c/a/b0/c'),
    os.path.normpath(testdata.filesysobjects.mypath+'/examples/a/b0/c/a/b0'),
    os.path.normpath(testdata.filesysobjects.mypath+'/examples/a/b0/c/a'),
    os.path.normpath(testdata.filesysobjects.mypath+'/examples/a/b0/c'),
    os.path.normpath(testdata.filesysobjects.mypath+'/examples/a/b0'),
    os.path.normpath(testdata.filesysobjects.mypath+'/examples/a'),
]
"""reference data for usecase"""


# start of upward search - file is converted into it's containing directory node
any_sub_path = os.path.normpath('examples/a/b0/c/a/b0/c/F')

spath  = testdata.filesysobjects.mypath
spath += os.sep+ any_sub_path
# check environment
assert os.path.exists(spath)


class CallUnits(unittest.TestCase):

    def reset_plist(self):
        """
        0. build a search path list - if not yet available
           adds each directory from spath to its matching 
           subnode  "a/b"
        """
        self._plist = []
        set_uppertree_searchpath(spath,os.path.normpath('a/b0'), self._plist)
        assert _plist_ref[:-1] == self._plist 

    def testCase100_append(self):
        self.reset_plist()

    def testCase110_append(self):
        """1. append an item"""       
        self.reset_plist()
        
        _addp = _plist_ref[-1]
        _px = addpath_to_searchpath(_addp, self._plist,**{'append':True})
        assert _px == len(_plist_ref)-1  # here just a demo
        assert _plist_ref == self._plist 
        pass

    def testCase120_prepend_same_again(self):
        """2. append same item again - with success"""
        self.reset_plist()

        _addp = _plist_ref[-1]
        
        _px = addpath_to_searchpath(_addp, self._plist,**{'prepend':True,'redundant':True})
        assert len(self._plist) == len(_plist_ref)  # here just a demo
        assert _plist_ref[:-1] == self._plist[1:]
        assert _plist_ref[-1] == self._plist[0] 
 
    def testCase120_append_try_same_again_nonredundant(self):
        """3. try to add same item again - with failure"""
        self.reset_plist()
 
        _addp = self._plist[-1]
        _plist_in = self._plist[:]
        _px = addpath_to_searchpath(_addp, self._plist,**{'prepend':True,'redundant':False})

        assert _px == None
        self.assertEqual(_plist_in, self._plist)

    def testCase121_append_try_same_again_nonredundant(self):
        """3. try to add same item again - with failure"""
        self.reset_plist()

        _addp = self._plist[-1]
        _plist_in = self._plist[:]

        _px = addpath_to_searchpath(_addp, self._plist,**{'append':True,'redundant':False})
        assert _px == None
        self.assertEqual(_plist_in, self._plist)
 
        _px = addpath_to_searchpath(_addp, self._plist,**{'append':True,'redundant':False})
        assert _px == None
        self.assertEqual(_plist_in, self._plist)

    def testCase130_prepend_same_again_checkreal(self):
        """4. prepend same item again - with checkreal"""
        self.reset_plist()

        _addp = self._plist[-1]

        _plist_in = self._plist[:]
        _plist_in.insert(0,os.path.realpath(_addp))
        
        _px = addpath_to_searchpath(_addp, self._plist,**{'prepend':True,'redundant':True,'checkreal':True,})
        assert _px == 0
        assert _plist_in == self._plist 
 
    def testCase200_delete_same(self):
        """remove all items"""
        self.reset_plist()

        _addp = self._plist[-1]
        delpath_from_searchpath (_addp, self._plist)
        assert _plist_ref[:-2] == self._plist 

    
#
#######################
#

if __name__ == '__main__':
    unittest.main()

