API Shortcuts - filesysobjects
==============================

filesysobjects.FileSysObjects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Filesystem Positions and Navigation for *sys.path*, and extended alternatives.
`[docs] <filesysobjects.html#>`_

* manage search paths - checks filesystem

  match-scope: 
  `[literal, glob, semi-glob(==glob), regexpr(for delPathFromSearchPath)] <path_syntax.html#variants-of-pathname-parameters-literals-regexpr-and-glob>`_

  +---------------------------------+----------------------------------------------------+
  | [docs]                          | [source]                                           | 
  +=================================+====================================================+
  | `addPathToSearchPath`_          | `FileSysObjects.addPathToSearchPath`_              |
  +---------------------------------+----------------------------------------------------+
  | `clearPath`_                    | `FileSysObjects.clearPath`_                        |
  +---------------------------------+----------------------------------------------------+
  | `delPathFromSearchPath`_        | `FileSysObjects.delPathFromSearchPath`_            |
  +---------------------------------+----------------------------------------------------+
  | `setUpperTreeSearchPath`_       | `FileSysObjects.setUpperTreeSearchPath`_           |
  +---------------------------------+----------------------------------------------------+

.. _FileSysObjects.addPathToSearchPath: _modules/filesysobjects/FileSysObjects.html#addPathToSearchPath
.. _FileSysObjects.delPathFromSearchPath: _modules/filesysobjects/FileSysObjects.html#delPathFromSearchPath
.. _FileSysObjects.clearPath: _modules/filesysobjects/FileSysObjects.html#clearPath
.. _FileSysObjects.setUpperTreeSearchPath: _modules/filesysobjects/FileSysObjects.html#setUpperTreeSearchPath

.. _addPathToSearchPath: filesysobjects.html#addpathtosearchpath
.. _clearPath: filesysobjects.html#clearpath
.. _delPathFromSearchPath: filesysobjects.html#delpathfromsearchpath
.. _setUpperTreeSearchPath: filesysobjects.html#setuppertreesearchpath


* search for appended paths of files, directories, and branches - checks filesystem
 
  match-scope:
  `[literal, gllob, semi-glob(==glob)] <path_syntax.html#variants-of-pathname-parameters-literals-regexpr-and-glob>`_

  +---------------------------------+----------------------------------------------------+
  | [docs]                          | [source]                                           | 
  +=================================+====================================================+
  | `findRelPathInSearchPath`_      | `FileSysObjects.findRelPathInSearchPath`_          |
  +---------------------------------+----------------------------------------------------+
  | `findRelPathInSearchPathIter`_  | `FileSysObjects.findRelPathInSearchPathIter`_      |
  +---------------------------------+----------------------------------------------------+
  | `findRelPathInUpperTree`_       | `FileSysObjects.findRelPathInUpperTree`_           |
  +---------------------------------+----------------------------------------------------+

.. _FileSysObjects.findRelPathInSearchPath: _modules/filesysobjects/FileSysObjects.html#findRelPathInSearchPath
.. _FileSysObjects.findRelPathInSearchPathIter: _modules/filesysobjects/FileSysObjects.html#findRelPathInSearchPathIter
.. _FileSysObjects.findRelPathInUpperTree: _modules/filesysobjects/FileSysObjects.html#findRelPathInUpperTree

.. _findRelPathInSearchPath: filesysobjects.html#findrelpathinsearchpath
.. _findRelPathInSearchPathIter: filesysobjects.html#findrelpathinsearchpathiter
.. _findRelPathInUpperTree: filesysobjects.html#findrelpathinuppertree

* match files, directories, and branches into path strings - works on strings only

  match-scope:
  `[literal, regexpr, semi-regexpr] <path_syntax.html#variants-of-pathname-parameters-literals-regexpr-and-glob>`_

  +---------------------------------+----------------------------------------------------+
  | [docs]                          | [source]                                           | 
  +=================================+====================================================+
  | `getTopFromPathString`_         | `FileSysObjects.getTopFromPathString`_             |
  +---------------------------------+----------------------------------------------------+
  | `getTopFromPathStringIter`_     | `FileSysObjects.getTopFromPathStringIter`_         |
  +---------------------------------+----------------------------------------------------+

.. _FileSysObjects.getTopFromPathString: _modules/filesysobjects/FileSysObjects.html#getTopFromPathString
.. _FileSysObjects.getTopFromPathStringIter: _modules/filesysobjects/FileSysObjects.html#getTopFromPathStringIter

.. _getTopFromPathString: filesysobjects.html#gettopfrompathstring
.. _getTopFromPathStringIter: filesysobjects.html#gettopfrompathstringiter

Canonical Node Address
^^^^^^^^^^^^^^^^^^^^^^

* Manage pathnames - files, directories, and branches

  +---------------------------------+----------------------------------------------------+
  | [docs]                          | [source]                                           | 
  +=================================+====================================================+
  | `escapeFilePath`_               | `FileSysObjects.escapeFilePath`_                   |
  +---------------------------------+----------------------------------------------------+
  | `getAppPrefixLocalPath`_        | `FileSysObjects.getAppPrefixLocalPath`_            |
  +---------------------------------+----------------------------------------------------+
  | `normpathX`_                    | `FileSysObjects.normpathX`_                        |
  +---------------------------------+----------------------------------------------------+
  | `splitAppPrefix`_               | `FileSysObjects.splitAppPrefix`_                   |
  +---------------------------------+----------------------------------------------------+
  | `unescapeFilePath`_             | `FileSysObjects.unescapeFilePath`_                 |
  +---------------------------------+----------------------------------------------------+

.. _FileSysObjects.escapeFilePath: _modules/filesysobjects/FileSysObjects.html#escapeFilePath
.. _FileSysObjects.getAppPrefixLocalPath: _modules/filesysobjects/FileSysObjects.html#getAppPrefixLocalPath
.. _FileSysObjects.normpathX: _modules/filesysobjects/FileSysObjects.html#normpathX
.. _FileSysObjects.splitAppPrefix: _modules/filesysobjects/FileSysObjects.html#splitAppPrefix
.. _FileSysObjects.unescapeFilePath: _modules/filesysobjects/FileSysObjects.html#unescapeFilePath

.. _escapeFilePath: filesysobjects.html#escapefilepath
.. _getAppPrefixLocalPath: filesysobjects.html#getappprefixlocalpath
.. _normpathX: filesysobjects.html#normpathx
.. _splitAppPrefix: filesysobjects.html#splitappprefix
.. _unescapeFilePath: filesysobjects.html#unescapefilepath


* For now experimental and non-productive, for review and comments
  `[docs] <netfiles.html#>`_

  +---------------------------------+-------------------------------------------------+
  | [docs]                          | [source]                                        | 
  +=================================+=================================================+
  | `netNormpathX`_                    | `NetFiles.netNormpathX`_                     |
  +---------------------------------+-------------------------------------------------+

.. _netNormpathX: netfiles.html#filesysobjects.NetFiles.netNormpathX
.. _NetFiles.normpathX: _modules/filesysobjects/NetFiles.html#normpathX



