.. raw:: html

   <div class="shortcuttab">

.. _shortcs:
Shortcuts
=========
.. toctree::
   :maxdepth: 2

   shortcuts

.. _DEVELOPMENTDOCS:

Development Documents
---------------------

* `A Primer on File and Directory Resources <filesysobjects_doc.html#FILEANDDIRECTORYRESOURCES>`_ 
* `Addresses for File-Like Resources <path_syntax.html#>`_

  * :ref:`Filesystem Elements as Objects <FILESYSELEMASOBJECTS>`
  * :ref:`Variants of Pathname Parameters - Literals, RegExpr, and Glob <VARIANTSPATHNAMEPARAMS>`
  * :ref:`Syntax Elements <SYNTAXELEMENTS>`
  * :ref:`Call Parameters of the API <CALLPARAMSAPI>`
* `Filesystem Adress Interfaces on Multiple Platforms <filesysobjects_multiplatform_api.html#>`_ 
* `Filename Encoding and Decoding <python_encode_decode.html#>`_ 
* `User Data <user_data.html#>`_ 
* `OS Data <os_data.html#>`_ 
* `Configuration Data <config_data.html#>`_ 
* `SW-Design of 'filesysobjects' <filesysobjects_design.html#>`_ 
* :ref:`The filesysobjects API <FILESYSOBJECTSAPI>`
* `HowTo <howto.html#>`_ 

.. _DEVELOPMENTAPI:

API Shortcuts - filesysinfo
---------------------------
The package *filesysobjects* contains the modules: 

* :ref:`filesysobjects.__init__ <SC_FILESYSOBJECTS>`
* :ref:`filesysobjects.confdata <SC_FILESYSOBJECTS_CONFIGDATA>`
* :ref:`filesysobjects.netfiles <SC_FILESYSOBJECTS_NETFILES>`
* :ref:`filesysobjects.osdata <SC_FILESYSOBJECTS_OSDATA>`
* :ref:`filesysobjects.paths <SC_FILESYSOBJECTS_PATHS>`
* :ref:`filesysobjects.pathtools <SC_FILESYSOBJECTS_PATHTOOLS>`
* :ref:`filesysobjects.userdata <SC_FILESYSOBJECTS_USERDATA>`

The following tables present the shortcut references to the API.
The applicable match scope for a filepathname input is displayed
in the optional column *[scope]*.

* **L**, **l**: literal

* **R**, **r**: regexpr by 're'

* **G**, **g**: 'glob'

The case of the characters for resolution indicate the processing:
 
* **L**, **R**, **G** - Upper case letters indicate active resolution including in-memory processing and filesystem access.

* **l**, **r**, **g** - Lower case letters indicate passive string acceptance with some in-memory processing.

The optional column *[fs]* displays whether the filesystem is accessed, or in mem file search path
string resolution is performed only.
The search path list is supported as literal only.
Function calls which access the filesystem are marked in the column '[fs]' with 'X'.

.. index::
   single: filesysobject

.. _SC_FILESYSOBJECTS:

filesysobjects
^^^^^^^^^^^^^^
The init module of the *filesysobjects* package contains global definitions.

+-------------------+----------------------------+
| [docs]            | [source]                   |
+===================+============================+
| `filesysobjects`_ | `filesysobjects.__init__`_ |
+-------------------+----------------------------+

.. _filesysobjects.__init__: _modules/filesysobjects/__init__.html#
.. _filesysobjects: filesysobjects_init.html#

.. index::
   single: pathtools
   single: filesysobjects.pathtools

.. _SC_FILESYSOBJECTS_APPPATHS:

filesysobjects.apppaths
^^^^^^^^^^^^^^^^^^^^^^^
The module '*filesysobjects.apppaths*' provides for the processing of application resource path names
intermixed with file path names, and search paths.
This enables for the transparent search and addressing of local and remote resources.

The procedures try to use in-memory access only - **scope=lrg** - including the static resolution
of regular expressions and globs - **scope=LRG**.

The function interfaces are based on context parameter sets, which is thread safe.

.. note::

   Thread-Safety is not yet sytematically tested.

Process Resource Paths
""""""""""""""""""""""
Syntactically and semantically transform and disassemble resource path names
for multiple platforms.

**Application Paths**

+-------------------------------+-------------------------------------------------------+---------+------+----------------+
| [docs]                        | [source]                                              | [scope] | [fs] | [map]          |
+===============================+=======================================================+=========+======+================+
| `splitapppathx`_              | `filesysobjects.apppaths.splitapppathx`_              | lrg     | --   | APPPATHSCANNER |
+-------------------------------+-------------------------------------------------------+---------+------+----------------+
| `splitapppathx_getlocalpath`_ | `filesysobjects.apppaths.splitapppathx_getlocalpath`_ | lrg     | --   | APPPATHSCANNER |
+-------------------------------+-------------------------------------------------------+---------+------+----------------+
| `normapppathx`_               | `filesysobjects.apppaths.normapppathx`_               | lrg     | --   | APPPATHSCANNER |
+-------------------------------+-------------------------------------------------------+---------+------+----------------+



These interfaces mainly rely on the following scanners and parsers.

.. _filesysobjects.apppaths.normapppathx: _modules/filesysobjects/apppaths.html#normapppathx
.. _filesysobjects.apppaths.splitapppathx: _modules/filesysobjects/apppaths.html#splitapppathx
.. _filesysobjects.apppaths.splitapppathx_getlocalpath: _modules/filesysobjects/apppaths.html#splitapppathx_getlocalpath
.. _normapppathx: apppaths.html#filesysobjects.apppaths.normapppathx
.. _splitapppathx: apppaths.html#filesysobjects.apppaths.splitapppathx
.. _splitapppathx_getlocalpath: apppaths.html#filesysobjects.apppaths.splitapppathx_getlocalpath

Parsers and Scanners
""""""""""""""""""""
Internal functions for the resolution of the mapping tables via dynamic regular expressions.
Based on:

* *APPPATHPARSER, APPPATHINDEX, APPTYPES* [:ref:`doc <APPLICATIONPATHSCANNERPARSER>`]

Helper
""""""

+--------------------------------+--------------------------------------------------------+---------+------+
| [docs]                         | [source]                                               | [scope] | [fs] |
+================================+========================================================+=========+======+
| `join_apppathx_entry`_         | `filesysobjects.apppaths.join_apppathx_entry`_         | --      | --   |
+--------------------------------+--------------------------------------------------------+---------+------+
| `gettop_from_pathstring`_      | `filesysobjects.apppaths.gettop_from_pathstring`_      | lr      | --   |
+--------------------------------+--------------------------------------------------------+---------+------+
| `gettop_from_pathstring_iter`_ | `filesysobjects.apppaths.gettop_from_pathstring_iter`_ | lr      | --   |
+--------------------------------+--------------------------------------------------------+---------+------+

.. _filesysobjects.apppaths.gettop_from_pathstring: _modules/filesysobjects/apppaths.html#gettop_from_pathstring
.. _filesysobjects.apppaths.gettop_from_pathstring_iter: _modules/filesysobjects/apppaths.html#gettop_from_pathstring_iter
.. _filesysobjects.apppaths.join_apppathx_entry: _modules/filesysobjects/apppaths.html#join_apppathx_entry
.. _gettop_from_pathstring: apppaths.html#gettop-from-pathstring
.. _gettop_from_pathstring_iter: apppaths.html#gettop-from-pathstring-iter
.. _join_apppathx_entry: apppaths.html#filesysobjects.apppaths.join_apppathx_entry

Manage Search Paths
"""""""""""""""""""
+-----------------------------+-----------------------------------------------------+---------+------+
| [docs]                      | [source]                                            | [scope] | [fs] |
+=============================+=====================================================+=========+======+
| `addpath_to_searchpath`_    | `filesysobjects.apppaths.addpath_to_searchpath`_    | L       | X    |
+-----------------------------+-----------------------------------------------------+---------+------+
| `delpath_from_searchpath`_  | `filesysobjects.apppaths.delpath_from_searchpath`_  | LRG     | X    |
+-----------------------------+-----------------------------------------------------+---------+------+
| `set_uppertree_searchpath`_ | `filesysobjects.apppaths.set_uppertree_searchpath`_ | L       | X    |
+-----------------------------+-----------------------------------------------------+---------+------+

.. _addpath_to_searchpath: apppaths.html#addpath-to-searchpath
.. _delpath_from_searchpath : apppaths.html#delpath-from-searchpath
.. _filesysobjects.apppaths.addpath_to_searchpath: _modules/filesysobjects/apppaths.html#addpath_to_searchpath
.. _filesysobjects.apppaths.delpath_from_searchpath : _modules/filesysobjects/apppaths.html#delpath_from_searchpath 
.. _filesysobjects.apppaths.set_uppertree_searchpath: _modules/filesysobjects/apppaths.html#set_uppertree_searchpath
.. _set_uppertree_searchpath: apppaths.html#set-uppertree-searchpath

.. _SC_FILESYSOBJECTS_PATHS:

filesysobjects.paths
^^^^^^^^^^^^^^^^^^^^
The module '*filesysobjects.paths*' provides for the processing of path names, file path names,
and search paths.
This is mainly based on the in-memory syntax analysis - **scope=lrg**, and includes in addition the static resolution
of regular expressions and globs - **scope=LRG**.

The calculation of canonicial resources is provided by function interfaces and path classes.
The implementation is based on the standard *re* package, with static compiled regexpr and
callback based dynamic evaluation of the regular expressions.

The function interfaces are based on context parameter sets, which is thread safe.

.. note::

   Thread-Safety is not yet sytematically tested.

Process Resource Paths
""""""""""""""""""""""
Syntactically and semantically transform and disassemble file resource path names
for multiple platforms.

**Paths**

+------------------+---------------------------------------+---------+------+
| [docs]           | [source]                              | [scope] | [fs] |
+==================+=======================================+=========+======+
| `escapepathx`_   | `filesysobjects.paths.escapepathx`_   | lg      | --   |
+------------------+---------------------------------------+---------+------+
| `getspf`_        | `filesysobjects.paths.getspf`_        | --      | --   |
+------------------+---------------------------------------+---------+------+
| `gettpf`_        | `filesysobjects.paths.gettpf`_        | --      | --   |
+------------------+---------------------------------------+---------+------+
| `normpathx`_     | `filesysobjects.paths.normpathx`_     | l       | --   |
+------------------+---------------------------------------+---------+------+
| `splitpathx`_    | `filesysobjects.paths.splitpathx`_    | lrg     | --   |
+------------------+---------------------------------------+---------+------+
| `unescapepathx`_ | `filesysobjects.paths.unescapepathx`_ | lg      | --   |
+------------------+---------------------------------------+---------+------+

These interfaces mainly rely on the following scanners and parsers.

.. _escapepathx: paths.html#filesysobjects.paths.escapepathx
.. _filesysobjects.paths.escapepathx: _modules/filesysobjects/paths.html#escapepathx
.. _filesysobjects.paths.getspf: _modules/filesysobjects/paths.html#getspf
.. _filesysobjects.paths.gettpf: _modules/filesysobjects/paths.html#gettpf
.. _filesysobjects.paths.normpathx: _modules/filesysobjects/paths.html#normpathx
.. _filesysobjects.paths.splitpathx: _modules/filesysobjects/paths.html#splitpathx
.. _filesysobjects.paths.unescapepathx: _modules/filesysobjects/paths.html#unescapepathx
.. _getspf: paths.html#getspf
.. _gettpf: paths.html#gettpf
.. _normpathx: paths.html#def-normpathx
.. _splitpathx: paths.html#splitpathx
.. _unescapepathx: paths.html#filesysobjects.paths.unescapepathx

Parsers and Scanners
""""""""""""""""""""
Internal functions for the resolution of the mapping tables via dynamic regular expressions.
Based on:

* *PATHSCANNER, ASCII_SC_CTRL* [:ref:`doc <SIMPLEPATHSCANNERPARSER>`]

The following parser and scanner maps apply.

+--------------+-----------------------------------+---------+------+------------------------------+
| [docs]       | [source]                          | [scope] | [fs] | [map]                        |
+==============+===================================+=========+======+==============================+
| `sub_esc`_   | `filesysobjects.paths.sub_esc`_   | lg      | --   | *PATHSCANNER, ASCII_SC_CTRL* |
+--------------+-----------------------------------+---------+------+------------------------------+
| `sub_keep`_  | `filesysobjects.paths.sub_keep`_  | lg      | --   |                              |
+--------------+-----------------------------------+---------+------+------------------------------+
| `sub_posix`_ | `filesysobjects.paths.sub_posix`_ | lg      | --   | *PATHSCANNER, ASCII_SC_CTRL* |
+--------------+-----------------------------------+---------+------+------------------------------+
| `sub_win`_   | `filesysobjects.paths.sub_win`_   | lg      | --   | *PATHSCANNER, ASCII_SC_CTRL* |
+--------------+-----------------------------------+---------+------+------------------------------+
| `sub_unesc`_ | `filesysobjects.paths.sub_unesc`_ | lg      | --   | *PATHSCANNER, ASCII_SC_CTRL* |
+--------------+-----------------------------------+---------+------+------------------------------+

.. _filesysobjects.paths.sub_esc: _modules/filesysobjects/paths.html#sub_esc
.. _filesysobjects.paths.sub_keep: _modules/filesysobjects/paths.html#sub_keep
.. _filesysobjects.paths.sub_posix: _modules/filesysobjects/paths.html#sub_posix
.. _filesysobjects.paths.sub_unesc: _modules/filesysobjects/paths.html#sub_unesc
.. _filesysobjects.paths.sub_win: _modules/filesysobjects/paths.html#sub_win
.. _sub_esc: paths.html#filesysobjects.paths.sub_esc
.. _sub_keep: paths.html#filesysobjects.paths.sub_keep
.. _sub_posix: paths.html#filesysobjects.paths.sub_posix
.. _sub_unesc: paths.html#filesysobjects.paths.sub_unesc
.. _sub_win: paths.html#filesysobjects.paths.sub_win

Remarks:

* In general: roll-back operations for conversions are not provided.
* *strip*: A conversion with the *strip* option could not be reverted.
* *sub_unesc*: Simply removes escape masks, is context aware. Application on e.g.
  non-escaped NTFS paths containing separators '\\' leads to unpredictable results.
  While the application onto previously escaped paths is reversable. 
* *revert*: A literal revert is not supported, but each valid path representation
  could be converted to one of the other provided options and vice versa.

.. note::

   The scanners and parsers/path-compilers support the masking by quoting. Quoted segments of a
   pathname are kept literally as part of a nodename. These could be excluded e.g. from escaping
   by option. Thus can include any character, so also regular expressions and globs.

.. _SC_FILESYSOBJECTS_PATHTOOLS:

filesysobjects.pathtools
^^^^^^^^^^^^^^^^^^^^^^^^
The module *filesysobjects.pathtools* supports the dynamic evaluation by creation of


Filesystem Positions and Navigation for *sys.path*, and extended alternatives.
`[docs] <path_syntax.html#>`_ `[API] <pyfilesysobjects.html#>`_


Search and Find
"""""""""""""""
+------------------------------+-------------------------------------------------------+---------+------+
| [docs]                       | [source]                                              | [scope] | [fs] |
+==============================+=======================================================+=========+======+
| `findpattern`_               | `filesysobjects.pathtools.findpattern`_               | LRG     | X    |
+------------------------------+-------------------------------------------------------+---------+------+
| `findrelpath_in_searchpath`_ | `filesysobjects.pathtools.findrelpath_in_searchpath`_ | LG      | X    |
+------------------------------+-------------------------------------------------------+---------+------+
| `findrelpath_in_uppertree`_  | `filesysobjects.pathtools.findrelpath_in_uppertree`_  | LG      | X    |
+------------------------------+-------------------------------------------------------+---------+------+

.. _filesysobjects.pathtools.findpattern: _modules/filesysobjects/pathtools.html#findpattern
.. _filesysobjects.pathtools.findrelpath_in_searchpath: _modules/filesysobjects/pathtools.html#findrelpath-in-searchpath
.. _filesysobjects.pathtools.findrelpath_in_uppertree: _modules/filesysobjects/pathtools.html#findrelpath-in-uppertree
.. _findpattern: pathtools.html#filesysobjects.pathtools.findpattern
.. _findrelpath_in_searchpath: pathtools.html#filesysobjects.pathtools.findrelpath_in_searchpath
.. _findrelpath_in_uppertree: pathtools.html#filesysobjects.pathtools.findrelpath_in_uppertree

Iterators
"""""""""
+-----------------------------------+------------------------------------------------------------+---------+------+
| [docs]                            | [source]                                                   | [scope] | [fs] |
+===================================+============================================================+=========+======+
| `findrelpath_in_searchpath_iter`_ | `filesysobjects.pathtools.findrelpath_in_searchpath_iter`_ | LG      | X    |
+-----------------------------------+------------------------------------------------------------+---------+------+
| `findrelpath_in_uppertree_iter`_  | `filesysobjects.pathtools.findrelpath_in_uppertree_iter`_  | LG      | X    |
+-----------------------------------+------------------------------------------------------------+---------+------+

.. _filesysobjects.pathtools.findrelpath_in_searchpath_iter: _modules/filesysobjects/pathtools.html#findrelpath-in-searchpath-iter
.. _filesysobjects.pathtools.findrelpath_in_uppertree_iter: _modules/filesysobjects/pathtools.html#findrelpath-in-uppertree-iter
.. _findrelpath_in_searchpath_iter: pathtools.html#filesysobjects.pathtools.findrelpath_in_searchpath_iter
.. _findrelpath_in_uppertree_iter: pathtools.html#filesysobjects.pathtools.findrelpath_in_uppertree_iter


Paths and Search Paths
""""""""""""""""""""""
+------------------------+-------------------------------------------------+---------+------+
| [docs]                 | [source]                                        | [scope] | [fs] |
+========================+=================================================+=========+======+
| `clearpath`_           | `filesysobjects.pathtools.clearpath`_           | L       | X    |
+------------------------+-------------------------------------------------+---------+------+
| `expandpath`_          | `filesysobjects.pathtools.expandpath`_          | LRG     | X    |
+------------------------+-------------------------------------------------+---------+------+
| `get_subpath_product`_ | `filesysobjects.pathtools.get_subpath_product`_ | L       | X    |
+------------------------+-------------------------------------------------+---------+------+

.. _clearpath: pathtools.html#filesysobjects.pathtools.clearpath
.. _expandpath: pathtools.html#filesysobjects.pathtools.expandpath
.. _get_subpath_product: pathtools.html#filesysobjects.pathtools.get_subpath_product
.. _filesysobjects.pathtools.clearpath: _modules/filesysobjects/pathtools.html#clearpath
.. _filesysobjects.pathtools.expandpath: _modules/filesysobjects/pathtools.html#expandpath
.. _filesysobjects.pathtools.get_subpath_product: _modules/filesysobjects/pathtools.html#get_subpath_product

Miscellaneous
"""""""""""""
+---------------+----------------------------------------+
| [docs]        | [source]                               |
+===============+========================================+
| `glob_to_re`_ | `filesysobjects.pathtools.glob_to_re`_ |
+---------------+----------------------------------------+

.. _glob_to_re: pathtools.html#filesysobjects.pathtools.glob_to_re
.. _filesysobjects.pathtools.glob_to_re: _modules/filesysobjects/pathtools.html#glob_to_re

.. _SC_FILESYSOBJECTS_PPRINT:

filesysobjects.pprint
^^^^^^^^^^^^^^^^^^^^^

+--------------+---------------------------------------------+
| [docs]       | [source]                                    |
+==============+=============================================+
| `PPPathVar`_ | `filesysobjects.pprint.PPPathVar.__init__`_ |
+--------------+---------------------------------------------+
| `__repr__`_  | `filesysobjects.pprint.PPPathVar.__repr__`_ |
+--------------+---------------------------------------------+
| `__str__`_   | `filesysobjects.pprint.PPPathVar.__str__`_  |
+--------------+---------------------------------------------+

.. _PPPathVar: pprint.html#filesysobjects.pprint.PPPathVar
.. _filesysobjects.pprint.PPPathVar.__init__: _modules/filesysobjects/pprint.html#PPPathVar.__init__
.. _\__str__: pprint.html#filesysobjects.pprint.PPPathVar.__str__
.. _filesysobjects.pprint.PPPathVar.__str__: _modules/filesysobjects/pprint.html#PPPathVar.__str__
.. _\__repr__: pprint.html#filesysobjects.pprint.PPPathVar.__repr__
.. _filesysobjects.pprint.PPPathVar.__repr__: _modules/filesysobjects/pprint.html#PPPathVar.__repr__



.. _SC_FILESYSOBJECTS_USERDATA:

filesysobjects.userdata
^^^^^^^^^^^^^^^^^^^^^^^
Filesystem Positions and Navigation for *sys.path*, and extended alternatives.
`[docs] <userdata.html#>`_ `[API] <pyfilesysobjects.html#>`_

+--------------------------+--------------------------------------------------+---------+------+
| [docs]                   | [source]                                         | [scope] | [fs] |
+==========================+==================================================+=========+======+
| `gethome`_               | `filesysobjects.userdata.gethome`_               | lrg     | --   |
+--------------------------+--------------------------------------------------+---------+------+
| `getdir_userhome`_       | `filesysobjects.userdata.getdir_userhome`_       | lrg     | --   |
+--------------------------+--------------------------------------------------+---------+------+
| `getdir_userdata`_       | `filesysobjects.userdata.getdir_userdata`_       | lrg     | --   |
+--------------------------+--------------------------------------------------+---------+------+
| `getdir_userconfigdata`_ | `filesysobjects.userdata.getdir_userconfigdata`_ | lrg     | --   |
+--------------------------+--------------------------------------------------+---------+------+
| `getdir_userappdata`_    | `filesysobjects.userdata.getdir_userappdata`_    | lrg     | --   |
+--------------------------+--------------------------------------------------+---------+------+
| `getcurrent_username`_   | `filesysobjects.userdata.getcurrent_username`_   | lrg     | --   |
+--------------------------+--------------------------------------------------+---------+------+

.. _filesysobjects.userdata.getcurrent_username: _modules/filesysobjects/userdata.html#getcurrent_username
.. _filesysobjects.userdata.getdir_userappdata: _modules/filesysobjects/userdata.html#getdir_userappdata
.. _filesysobjects.userdata.getdir_userconfigdata: _modules/filesysobjects/userdata.html#getdir_userconfigdata
.. _filesysobjects.userdata.getdir_userdata: _modules/filesysobjects/userdata.html#getdir_userdata
.. _filesysobjects.userdata.getdir_userhome: _modules/filesysobjects/userdata.html#getdir_userhome
.. _filesysobjects.userdata.gethome: _modules/filesysobjects/userdata.html#gethome
.. _getcurrent_username: userdata.html#filesysobjects.userdata.getcurrent_username
.. _getdir_userappdata: userdata.html#filesysobjects.userdata.getdir_userappdata
.. _getdir_userconfigdata: userdata.html#filesysobjects.userdata.getdir_userconfigdata
.. _getdir_userdata: userdata.html#filesysobjects.userdata.getdir_userdata
.. _getdir_userhome: userdata.html#filesysobjects.userdata.getdir_userhome
.. _gethome: userdata.html#filesysobjects.userdata.gethome

.. _SC_FILESYSOBJECTS_OSDATA:

filesysobjects.osdata
^^^^^^^^^^^^^^^^^^^^^
Search path object for OS specific configurations.
`[docs] <os_data.html#>`_ `[API] <osdata.html#>`_

+---------------------------+-------------------------------------------------+---------+------+
| [docs]                    | [source]                                        | [scope] | [fs] |
+===========================+=================================================+=========+======+
| `getdir_osconfigdata`_    | `filesysobjects.osdata.getdir_osconfigdata`_    | lrg     | --   |
+---------------------------+-------------------------------------------------+---------+------+
| `getdir_osappdata`_       | `filesysobjects.osdata.getdir_osappdata`_       | lrg     | --   |
+---------------------------+-------------------------------------------------+---------+------+
| `getdir_osappconfigdata`_ | `filesysobjects.osdata.getdir_osappconfigdata`_ | lrg     | --   |
+---------------------------+-------------------------------------------------+---------+------+

.. _filesysobjects.osdata.getdir_osconfigdata: _modules/filesysobjects/osdata.html#getdir_osconfigdata
.. _filesysobjects.osdata.getdir_osappdata: _modules/filesysobjects/osdata.html#getdir_osappdata
.. _filesysobjects.osdata.getdir_osappconfigdata: _modules/filesysobjects/osdata.html#getdir_osappconfigdata
.. _getdir_osconfigdata: osdata.html#filesysobjects.osdata._getdir_osconfigdata
.. _getdir_osappdata: osdata.html#filesysobjects.osdata.getdir_osappdata
.. _getdir_osappconfigdata: osdata.html#filesysobjects.osdata.getdir_osappconfigdata

.. _SC_FILESYSOBJECTS_CONFIGDATA:

filesysobjects.configdata
^^^^^^^^^^^^^^^^^^^^^^^^^
Search path object for configuration files
`[docs] <config_data.html#>`_ `[API] <configdata.html#>`_

+----------------------------------------+-------------------------------------------------------+---------+------+
| [docs]                                 | [source]                                              | [scope] | [fs] |
+========================================+=======================================================+=========+======+
| `ConfigPath`_                          | `filesysobjects.configdata.__init__`_                 | LRG     | X    |
+----------------------------------------+-------------------------------------------------------+---------+------+
| `ConfigPath.get_config_path_list`_     | `filesysobjects.configdata.get_config_path_list`_     | LRG     | X    |
+----------------------------------------+-------------------------------------------------------+---------+------+
| `ConfigPath.get_config_filepath`_      | `filesysobjects.configdata.get_config_filepath`_      | LRG     | X    |
+----------------------------------------+-------------------------------------------------------+---------+------+
| `ConfigPath.get_config_filepath_list`_ | `filesysobjects.configdata.get_config_filepath_list`_ | LRG     | X    |
+----------------------------------------+-------------------------------------------------------+---------+------+
| `ConfigPath.get_filepathname_by_ext`_  | `filesysobjects.configdata.get_filepathname_by_ext`_  | LRG     | X    |
+----------------------------------------+-------------------------------------------------------+---------+------+

.. _filesysobjects.configdata.__init__: _modules/filesysobjects/configdata.html#ConfigPath.__init__
.. _filesysobjects.configdata.get_config_path_list: _modules/filesysobjects/configdata.html#ConfigPath.get_config_path_list
.. _filesysobjects.configdata.get_config_filepath: _modules/filesysobjects/configdata.html#ConfigPath.get_config_filepath
.. _filesysobjects.configdata.get_config_filepath_list: _modules/filesysobjects/configdata.html#ConfigPath.get_config_filepath_list
.. _filesysobjects.configdata.get_filepathname_by_ext: _modules/filesysobjects/configdata.html#ConfigPath.get_filepathname_by_ext
.. _ConfigPath: configdata.html#init
.. _ConfigPath.get_config_path_list: configdata.html#get-config-path-list
.. _ConfigPath.get_config_filepath: configdata.html#get-config-filepath
.. _ConfigPath.get_config_filepath_list: configdata.html#get-config-filepath-list
.. _ConfigPath.get_filepathname_by_ext: configdata.html#get-filepathname-by-ext


.. _SC_FILESYSOBJECTS_NETFILES:

netfiles.net_normpathx
^^^^^^^^^^^^^^^^^^^^^^
For now experimental and non-productive, for review and comments `[docs] <netfiles.html#>`_

+------------------+---------------------------+---------+------+
| [docs]           | [source]                  | [scope] | [fs] |
+==================+===========================+=========+======+
| `net_normpathx`_ | `netfiles.net_normpathx`_ |         |      |
+------------------+---------------------------+---------+------+

.. _net_normpathx: netfiles.html#filesysobjects.netfiles.net_normpathx
.. _netfiles.net_normpathx: _modules/filesysobjects/netfiles.html#net_normpathx

.. _RUNTIMETESTDATA:

Tests
-----
The tests are base on *PyUnit* and *Eclipse*.
These are contained in the subdirectory *tests* and optionally in the subdirectory *UseCases*.

The test cases are in particular based on normative input data arrays - *data.py*,
and related normative result arrays.
With additional explicit test cases.
The contained tests at the time of writing is in total about 4400 test-cases. 


.. raw:: html

   </div>
