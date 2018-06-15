"""Use-Cases: Search by literals + globs + regexpr

Find a matching relative filepathname in upper directory
tree for a given name/relative path containing literals, 
globs, and regexpr components. 

**Example**:

See testdata/findnodes

Calls::
    
    gettop_from_pathstring
    set_uppertree_searchpath
    findrelpath_in_searchpath

"""