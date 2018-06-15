.. raw:: html

   <div class="shortcuttab">

.. _FILESYSOBJECTSAPI:

The filesysobjects API
**********************
The *filesysobjects* API covers a variety of interfaces for the processing of 
resource path addresses, and the search of resources.
The initial set of interfaces forcusses on filesystem resources in a basic distributed
environment.
This covers in particular a basic set of call parameters, which are common for a
subset of the call interfaces. 


API
---
Interfaces
^^^^^^^^^^
.. raw:: html

   <div class="apisynopsis">

* :ref:`process paths <IF_PROCESSPATHS>`
* :ref:`manage search paths <IF_MANAGESEARCHPATHS>`
* :ref:`search for files, directories, and branches <IF_SEARCHPATHS>`
* :ref:`match files, directories, and branches into path strings <IF_MATCHPATHS>`
* :ref:`configuration <IF_CONFIG>`
* :ref:`os <IF_OS>`
* :ref:`user <IF_USER>`

.

.. _IF_PROCESSPATHS:

* **process paths** - normalize, split, and join resource paths

 .. parsed-literal::

    `normapppathx(spath, **kargs) <apppaths.html#filesysobjects.apppaths.normapppathx>`_
    `normpathx(spath, **kargs) <paths.html#normpathx>`_

    `splitapppathx(spath, **kargs) <apppaths.html#filesysobjects.apppaths.splitapppathx>`_
    `splitapppathx_getlocalpath(elems, **kargs) <apppaths.html#filesysobjects.apppaths.splitapppathx_getlocalpath>`_
    `join_apppathx_entry(entry, tpf=5, **kw) <apppaths.html#filesysobjects.apppaths.join_apppathx_entry>`_

    `splitpathx(p, tpf=5, **kw) <paths.html#splitpathx>`_

    `escapepathx(spath, tpf=None, **kargs) <paths.html#filesysobjects.paths.escapepathx>`_
    `expandpath(*paths, **kargs) <pathtools.html#filesysobjects.pathtools.expandpath>`_
    `unescapepathx(p, tpf=None, **kargs) <paths.html#filesysobjects.paths.unescapepathx>`_

.. _IF_MANAGESEARCHPATHS:

* **manage search paths** - create, add, remove, and clear search paths

 .. parsed-literal::

    `addpath_to_searchpath(spath, plist=None, **kargs) <apppaths.html#addpath-to-searchpath>`_
    `clearpath(plist=None, **kargs) <pathtools.html#filesysobjects.pathtools.clearpath>`_
    `delpath_from_searchpath(dellist, plist=None, **kargs)  <apppaths.html#delpath-from-searchpath>`_

    `set_uppertree_searchpath(start=None, top=None, plist=None, **kargs) <apppaths.html#set-uppertree-searchpath>`_

.. _IF_SEARCHPATHS:

* **search for files, directories, and branches** - find resources by search on media

 .. parsed-literal::

    `findpattern(*srcdirs, **kargs) <pathtools.html#filesysobjects.pathtools.findpattern>`_

    `findrelpath_in_searchpath(spath, plist=None, **kargs) <pathtools.html#filesysobjects.pathtools.findrelpath_in_searchpath>`_
    `findrelpath_in_searchpath_iter(spath, plist=None, **kargs) <pathtools.html#filesysobjects.pathtools.findrelpath_in_searchpath_iter>`_

    `findrelpath_in_uppertree(spath, plist=None, **kargs) <pathtools.html#filesysobjects.pathtools.findrelpath_in_uppertree>`_
    `findrelpath_in_uppertree_iter(spath, plist=None, **kargs) <pathtools.html#filesysobjects.pathtools.findrelpath_in_uppertree_iter>`_
   

.. _IF_MATCHPATHS:

* **match files, directories, and branches into path strings** - search resources on strings only

 .. parsed-literal::

    `gettop_from_pathstring(start, plist=None, **kargs) <apppaths.html#gettop-from-pathstring>`_
    `gettop_from_pathstring_iter(start, plist=None, **kargs) <apppaths.html#gettop-from-pathstring-iter>`_

    `get_subpath_product(dirs, subpaths) <pathtools.html#filesysobjects.pathtools.get_subpath_product>`_

.. _IF_CONFIG:

* **configuration** - abstraction of specific configuration directories for various platforms

 .. parsed-literal::

   `get_config_filepath(conf) <configdata.html#get-config-filepath>`_
   `get_config_filepath_list() <configdata.html#get-config-filepath-list>`_
   `get_config_path_list() <configdata.html#get-config-path-list>`_
   `get_filepathname_by_ext(fnam, fext=[]) <configdata.html#get-filepathname-by-ext>`_

.. _IF_OS:

* **os** - abstraction of specific OS directories for various platforms

 .. parsed-literal::

   `getdir_osappconfigdata() <osdata.html#filesysobjects.osdata.getdir_osappconfigdata>`_
   `getdir_osappdata(appname='') <osdata.html#filesysobjects.osdata.getdir_osappdata>`_
   `getdir_osconfigdata(appname='') <osdata.html#filesysobjects.osdata._getdir_osconfigdata>`_

.. _IF_USER:

* **user** - abstraction of specific user directories for various platforms

 .. parsed-literal::

   `getcurrent_username() <userdata.html#filesysobjects.userdata.getcurrent_username>`_
   `gethome() <userdata.html#filesysobjects.userdata.gethome>`_

   `getdir_userappdata(appname='', user=None) <userdata.html#filesysobjects.userdata.getdir_userappdata>`_
   `getdir_userappconfigdata(appname='', user=None) <userdata.html#filesysobjects.userdata.getdir_userappconfigdata>`_

   `getdir_userconfigdata(user=None) <userdata.html#filesysobjects.userdata.getdir_userconfigdata>`_
   `getdir_userdata(user=None) <userdata.html#filesysobjects.userdata.getdir_userdata>`_
   `getdir_userhome(user='') <userdata.html#filesysobjects.userdata.getdir_userhome>`_

.. raw:: html

   </div>


Major Options by Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The cross-platform related options are 

* :ref:`apppre <opt_apppre>` - application prefix - scheme
* :ref:`pathsep <opt_pathsep>` - special path separator
* :ref:`spf <opt_spf>` - source platform
* :ref:`tpf <opt_tpf>` - target platform 
 
The following table displays the support of interfaces with some additional
path separator processing options.
For the full set of options refer to the interfaces.

.. raw:: html

   <div class="tabcolumncolor">

+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| interface                         | spath                | apppre                | spf                | tpf                | pathsep                | appsplit                | keepsep                | strip                |
+===================================+======================+=======================+====================+====================+========================+=========================+========================+======================+
| `addpath_to_searchpath`_          | :ref:`x <opt_spath>` |                       | :ref:`x <opt_spf>` | :ref:`x <opt_tpf>` | :ref:`x <opt_pathsep>` |                         |                        | :ref:`x <opt_strip>` |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `clearpath`_                      | --                   |                       | :ref:`x <opt_spf>` | :ref:`x <opt_tpf>` | :ref:`x <opt_pathsep>` |                         |                        | :ref:`x <opt_strip>` |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `delpath_from_searchpath`_        | :ref:`x <opt_spath>` |                       |                    | :ref:`x <opt_tpf>` | :ref:`x <opt_pathsep>` |                         |                        | :ref:`x <opt_strip>` |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `escapepathx`_                    | :ref:`x <opt_spath>` |                       | :ref:`x <opt_spf>` | :ref:`x <opt_tpf>` |                        |                         |                        | :ref:`x <opt_strip>` |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `expandpath`_                     | :ref:`x <opt_spath>` |                       | :ref:`x <opt_spf>` | :ref:`x <opt_tpf>` |                        |                         |                        |                      |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `findpattern`_                    | :ref:`x <opt_spath>` |                       |                    |                    |                        |                         |                        |                      |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `findrelpath_in_searchpath_iter`_ | :ref:`x <opt_spath>` |                       |                    |                    |                        |                         |                        |                      |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `findrelpath_in_searchpath`_      | :ref:`x <opt_spath>` |                       |                    |                    |                        |                         |                        |                      |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `findrelpath_in_uppertree_iter`_  | :ref:`x <opt_spath>` |                       |                    |                    |                        |                         |                        |                      |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `findrelpath_in_uppertree`_       | :ref:`x <opt_spath>` |                       |                    |                    |                        |                         |                        |                      |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `get_subpath_product`_            |                      |                       |                    |                    |                        |                         |                        |                      |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| :ref:`def_gettop_from_pathstring` | :ref:`x <opt_spath>` |                       | :ref:`x <opt_spf>` | :ref:`x <opt_tpf>` | :ref:`x <opt_pathsep>` |                         | :ref:`x <opt_keepsep>` |                      |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `join_apppathx_entry`_            |                      | :ref:`x <opt_apppre>` | --                 | :ref:`x <opt_tpf>` |                        |                         |                        |                      |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| :ref:`def_normapppathx`           | :ref:`x <opt_spath>` | :ref:`x <opt_apppre>` | :ref:`x <opt_spf>` | :ref:`x <opt_tpf>` | :ref:`x <opt_pathsep>` | :ref:`x <opt_appsplit>` |                        | :ref:`x <opt_strip>` |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| :ref:`def_normpathx`              | :ref:`x <opt_spath>` |                       | :ref:`x <opt_spf>` | :ref:`x <opt_tpf>` | :ref:`x <opt_pathsep>` |                         |                        | :ref:`x <opt_strip>` |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `set_uppertree_searchpath`_       |                      |                       | :ref:`x <opt_spf>` | :ref:`x <opt_tpf>` | :ref:`x <opt_pathsep>` |                         |                        | :ref:`x <opt_strip>` |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| :ref:`def_splitpathx`             | :ref:`x <opt_spath>` |                       | :ref:`x <opt_spf>` | :ref:`x <opt_tpf>` |                        |                         |                        | :ref:`x <opt_strip>` |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| :ref:`def_splitapppathx`          | :ref:`x <opt_spath>` | :ref:`x <opt_apppre>` | :ref:`x <opt_spf>` | :ref:`x <opt_tpf>` | :ref:`x <opt_pathsep>` | :ref:`x <opt_appsplit>` | :ref:`x <opt_keepsep>` | :ref:`x <opt_strip>` |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `splitapppathx_getlocalpath`_     |                      |                       | :ref:`x <opt_spf>` | :ref:`x <opt_tpf>` |                        |                         |                        | :ref:`x <opt_strip>` |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+
| `unescapepathx`_                  | :ref:`x <opt_spath>` |                       | :ref:`x <opt_spf>` | :ref:`x <opt_tpf>` |                        |                         |                        | :ref:`x <opt_strip>` |
+-----------------------------------+----------------------+-----------------------+--------------------+--------------------+------------------------+-------------------------+------------------------+----------------------+

.. raw:: html

   </div>

.. _addpath_to_searchpath: apppaths.html#addpath-to-searchpath
.. _clearpath: pathtools.html#filesysobjects.pathtools.clearpath
.. _delpath_from_searchpath: apppaths.html#delpath-from-searchpath
.. _escapepathx: paths.html#filesysobjects.paths.escapepathx
.. _expandpath: pathtools.html#filesysobjects.pathtools.expandpath
.. _findpattern: pathtools.html#filesysobjects.pathtools.findpattern>`_
.. _findrelpath_in_searchpath: pathtools.html#filesysobjects.pathtools.findrelpath_in_searchpath
.. _findrelpath_in_searchpath_iter: pathtools.html#filesysobjects.pathtools.findrelpath_in_searchpath_iter
.. _findrelpath_in_uppertree: pathtools.html#filesysobjects.pathtools.findrelpath_in_uppertree
.. _findrelpath_in_uppertree_iter: pathtools.html#filesysobjects.pathtools.findrelpath_in_uppertree_iter
.. _get_config_filepath: configdata.html#get-config-filepath
.. _get_config_filepath_list: configdata.html#get-config-filepath-list
.. _get_config_path_list: configdata.html#get-config-path-list
.. _get_filepathname_by_ext: configdata.html#get-filepathname-by-ext
.. _get_subpath_product: pathtools.html#filesysobjects.pathtools.get_subpath_product
.. _getcurrent_username: userdata.html#filesysobjects.userdata.getcurrent_username
.. _getdir_osappconfigdata: osdata.html#filesysobjects.osdata.getdir_osappconfigdata
.. _getdir_osappdata: osdata.html#filesysobjects.osdata.getdir_osappdata
.. _getdir_osconfigdata: osdata.html#filesysobjects.osdata._getdir_osconfigdata
.. _getdir_userappconfigdata: userdata.html#filesysobjects.userdata.getdir_userappconfigdata
.. _getdir_userappdata: userdata.html#filesysobjects.userdata.getdir_userappdata
.. _getdir_userconfigdata: userdata.html#filesysobjects.userdata.getdir_userconfigdata>
.. _getdir_userdata: userdata.html#filesysobjects.userdata.getdir_userdata
.. _getdir_userhome: userdata.html#filesysobjects.userdata.getdir_userhome
.. _gethome: userdata.html#filesysobjects.userdata.gethome
.. _gettop_from_pathstring: apppaths.html#gettop-from-pathstring
.. _gettop_from_pathstring_iter: apppaths.html#gettop-from-pathstring-iter
.. _join_apppathx_entry: apppaths.html#filesysobjects.apppaths.join_apppathx_entry
.. _set_uppertree_searchpath: apppaths.html#set-uppertree-searchpath
.. _splitapppathx_getlocalpath: apppaths.html#filesysobjects.apppaths.splitapppathx_getlocalpath
.. _unescapepathx: paths.html#filesysobjects.paths.unescapepathx


.. index::
   pair: options; tpf
   pair: options; spf

.. _TPF_AND_SPF:

*tpf* and *spf*
"""""""""""""""
The *filesysobjects* provides crossplatform conversion of resource addresses for a variety
of platforms, including ordinary local filesystems, network filesystes, UNC, URI, URL and
others. 
Therefore the source and target platfors could be adapted by the parameters *tpf* for the
target and *spf* for the source.

The source and target platform options define the separators 'sep' and 'pathsep',
and some structural context such as drive letters on the path layer, 
and additional application schemes as prefixes and additional structural information
such as fragments and queries for URLs.
While the target platform parameter supports one value only, the source platform parameter
enables the combination of multiple platforms.
The latter enables in particular the cross-conversion of mixed terms by accurate handling
of the structural components of all platforms. 

+----------+-------------+-------------+------------+----------------+----------+--------------+------+----------+
| type     | constant    | tpf         | spf        | scheme         | host     | share        | path | option   |
+==========+=============+=============+============+================+==========+==============+======+==========+
| URL/URI  | RTE_URI,    | http, https |            | http/https     | hostname |              | path | query    |
|          | RTE_HTTP,   |             |            |                |          |              |      | fragment |
|          | RTE_HTTPS   |             |            |                |          |              |      |          |
+----------+-------------+-------------+------------+----------------+----------+--------------+------+----------+
| file-URI | RTE_FILEURI | posix, win  | posix, win | file           | hostname | drive, share | path | --       |
+----------+-------------+-------------+------------+----------------+----------+--------------+------+----------+
| ldsys    | RTE_WIN32   | win         | win        | --             | --       | drive        | path | --       |
+----------+-------------+-------------+------------+----------------+----------+--------------+------+----------+
| lfsys    | RTE_POSIX,  | posix, win  | posix, win | --             | --       | --           | path | --       |
|          | RTE_WIN32   |             |            |                |          |              |      |          |
+----------+-------------+-------------+------------+----------------+----------+--------------+------+----------+
| RAW      |             | all         | all        |                |          |              |      | --       |
+----------+-------------+-------------+------------+----------------+----------+--------------+------+----------+
| share    |             | win         | win        | //, \\\\       | hostname | share        | path | --       |
+----------+-------------+-------------+------------+----------------+----------+--------------+------+----------+
| SMB/CIFS | RTE_SMB     | win, posix  |            | smb            | hostname | share        | path | --       |
+----------+-------------+-------------+------------+----------------+----------+--------------+------+----------+
| UNC      | RTE_UNC     | win, posix  |            | file, //, \\\\ | hostname | share        | path | --       |
+----------+-------------+-------------+------------+----------------+----------+--------------+------+----------+

* *RAW*
* *SMB* - SMB File Sharing URI Scheme [SMBURI]_, [SAMBA]_, [MS-DTYP]_, [MS-SMB]_, [MS-SMB2]_, [MS-CIFS]_ 
* *UNC* - UNC: Common definition in [MS-DTYP]_ Windows Data Types [UNC]_
* *URL* / *URI* - Uniform Resource Identifier - URI: Generic Syntax [RFC3986]_, [URLPARSING]_
* *file-URI* - RFC8089 [RFC8089]_, [URISCHEME]_
* *ldsys* - Local Drive File System - [MS-DTYP]_
* *lfsys* - Local File System - [POSIX]_, [MS-DTYP]_
* *share* UNC [UNC]_ or Posix network app [POSIX]_

Options
^^^^^^^
The call interface provides for groups of functions and classes with a set of 
common parameters and additional context specific modifications.

The provided function sets comprise the categories:

* Filesystem Positions and Navigation

* Canonical Node Address

Various common options are supported, which may not be available for each interface.
 
.. index::
   pair: options; spath

.. _opt_spath:

*spath*
"""""""
The processed path, either to be added to the search list,
or to be find in a earch list.

.. index::
   pair: options; plist

.. _opt_plist:

*plist*
"""""""
A path list for search operations, default is 'sys.path'.

kargs
"""""
.. index::
   pair: options; apppre

.. _opt_apppre:

*apppre*
''''''''
Application prefix, application scheme. ::

   appsplit := (
        True     # add application scheme
      | False    # remove application scheme
   )

default := False


.. index::
   pair: options; appsplit

.. _opt_appsplit:

appsplit
''''''''
Split into scheme and components of an application path.

.. index::
   pair: options; delnulpsep

.. _opt_delnulpsep:

*delnulpsep*
''''''''''''
Constraints the *strip* option. Keeps the separators after reduction.

default := True  


.. index::
   pair: options; keepsep

.. _opt_keepsep:

*keepsep*
'''''''''

Modifies the behavior of the 'strip' parameter.
If 'False', the trailing separator is dropped. ::

   normapppathx('/a/b', keepsep=False)   => '/a/b'
   normapppathx('/a/b/', keepsep=False)  => '/a/b'

for 'True' trailing separators are kept as directory
marker::

   normapppathx('/a/b', keepsep=True)    => '/a/b'
   normapppathx('/a/b/', keepsep=True)   => '/a/b/'

default := True # for URIs except: file://, smb://
default := False # for file path names

.. index::
   pair: options; pathsep

.. _opt_pathsep:

*pathsep*
'''''''''

Forces the use of the provided '*pathsep*' for the analysis of the input.
WHile the application related interfaces in general provide multiple paths
separated bu '*pathsep*', the path related interfaces provide this optionally.
Thus the parameter for path interfaces comes into effect when provided.

This could comprise '*:;*', which are applied literally as generic tokens,
while the options '*posix*' and/or '*win*' recognize the structural element
context too. ::

   pathsep := (
       True            # uses default from *spf*
     | False           # keeps unchanged
     | [:;]*           # replaces ':' and/or ';'
     | 'win'           # replaces ';'
     | 'posix'         # replaces ':'
   )

   default:=False

The value *True* just activates the application of the *pathsep* as defined by the
*spf*, which defaults to *os.pathsep*.

.. index::
   pair: options; raw

*raw*
'''''
Suppress normalization by call of 'os.path.normpath'.

.. index::
   pair: options; strip

.. _opt_strip:

*strip*
'''''''
Removes resulting *null-entries*.
This relies on the choosen target platform, because some chaarcters are used
for multiple syntax elements, thus without context information lead to ambiguity.
An example is here again the DOS-drive.
The interpretation of the separator characters by the undelying OS is the 
base for the processing of the strip operation.

.. code-block:: python
   :linenos:

   spf='posix':  d:/  => [ 'd',  '/']  # two directories
   spf='win':    d:/  => [ 'd:', '/']  # drive 'd:'. and the root directory on 'd:'
                                       # as node-name

Thus the option *strip* leads to the following results:

.. code-block:: python
   :linenos:

   spf='posix':  d:/  => [ 'd']        # one directory
   spf='win':    d:/  => [ 'd:', '/']  # drive 'd:'. and the root directory on 'd:'

The supported target platforms encounter the following effect when
*strip* is set to *True*.

* *URL* / *URI*

  * multiple occurances of *sep* and *pathsep*

* *ldsys*

  * multiple occurances of *sep* and *pathsep*
  * terminating  *sep* and *pathsep*

* *'lfsys'*

  * multiple occurances of *sep* and *pathsep*
  * terminating  *sep* and *pathsep*

* *RAW*

  n.a.

* *share*

  * multiple occurances of *sep* and *pathsep*
  * terminating  *sep* and *pathsep*

* *SMB*

  * multiple occurances of *sep* and *pathsep*
  * terminating  *sep* and *pathsep*

* *UNC*

  * multiple occurances of *sep* and *pathsep*
  * terminating  *sep* and *pathsep*


default := True  


.. index::
   pair: options; spf

.. _OPTS_SPF:

.. _opt_spf:

spf - Source Platform
'''''''''''''''''''''

+---------+--------+---------------+-------------+------------------------------------------------------------+-------------------------------------------------------+
| spf     | string | constant      | compatible  | cross                                                      | behaviour                                             |
|         |        |               | to normpath | platform                                                   |                                                       |
+=========+========+===============+=============+============================================================+=======================================================+
| local   | posix, | *RTE_POSIX*,  | yes         | no                                                         | calls local os.path.normpath()                        |
|         | win    | *RTE_WIN32*   |             |                                                            |                                                       |
+---------+--------+---------------+-------------+------------------------------------------------------------+-------------------------------------------------------+
| posix   | posix  | *RTE_POSIX*   | no          | yes,                                                       | transforms all separators to '/' or ':'               |
|         |        |               | (*pchar)    | Portable for IEEE1003.1, 2013/3.276 Portable Character Set |                                                       |
+---------+--------+---------------+-------------+------------------------------------------------------------+-------------------------------------------------------+
| uri     | http,  | *RTE_HTTP*,   | no          | yes                                                        | transforms all separators to '/'                      |
|         | https, | *RTE_HTTPS*,  |             |                                                            |                                                       |
|         | smb,   | *RTE_SMB*,    |             |                                                            |                                                       |
|         | file   | *RTE_FILEURI* |             |                                                            |                                                       |
+---------+--------+---------------+-------------+------------------------------------------------------------+-------------------------------------------------------+
| win     | win    | *RTE_WIN32*   | no          | no                                                         | transforms all separators to '\\\\' or ';'            |
+---------+--------+---------------+-------------+------------------------------------------------------------+-------------------------------------------------------+
| default |        | *RTE*         | no          | no                                                         | adapts 'win'(on win) or 'posix'(on posix) to local os |
+---------+--------+---------------+-------------+------------------------------------------------------------+-------------------------------------------------------+

Defines the characters to be used as path separator, and
the additional specific semantics. Default is the current
platform, with a single character for the 'os.pathsep' and
the support for the specific semantics like DOS drives for
the platform 'win'.

Application and URL/URI file prefixes and tags like 'smb://',
'file://', 'file:////', and 'file://///' are detected in
any case. Thus these are treated as reserved words.

The syntax is: ::

   spf := (<macros>|<char-string>)

   macros := ('posix'|'win')[, macros]
   char-string := (':'|';'|'')*

   default := ('posix'|'win')

* posix:

  String for POSIX based platforms. Is aware of the POSIX
  syntax and semantics, single character '/' as separator.
  Ignores pattern for potential DOS drives.

* win:

  String for the Windows platform. Is aware of the Windows
  syntax and semantics, single character '\\' as separator.
  Recognizes string pattern of DOS drives.
  Undestands in addition the separator '/'.

* URI char-string:

  Applies the selected URI.

For mixed input for example: ::

   spf := ':;'

.. index::
   pair: options; tpf

.. _OPTS_TPF:

.. _opt_tpf:

tpf - Target Platform
'''''''''''''''''''''

Due to some deviations from the expected behavior in
case of cross platform development the following options 
are defined:

+---------+-------------+-------------+------------------------------------------------------------+-------------------------------------------------------+
| tpf     | constant    | compatible  | cross                                                      | behaviour                                             |
|         |             | to normpath | platform                                                   |                                                       |
+=========+=============+=============+============================================================+=======================================================+
| cnp     |             | yes(posix)  | no                                                         | calls posixpath.normpath()                            |
+---------+-------------+-------------+------------------------------------------------------------+-------------------------------------------------------+
| cnw     |             | yes(win)    | no                                                         | calls ntpath.normpath()                               |
+---------+-------------+-------------+------------------------------------------------------------+-------------------------------------------------------+
| local   |             | yes         | no                                                         | calls local os.path.normpath()                        |
+---------+-------------+-------------+------------------------------------------------------------+-------------------------------------------------------+
| posix   | *RTE_POSIX* | no          | yes*                                                       | transforms all separators to '/' or ':'               |
|         |             | (*pchar)    | Portable for IEEE1003.1, 2013/3.276 Portable Character Set |                                                       |
+---------+-------------+-------------+------------------------------------------------------------+-------------------------------------------------------+
| uri     |             | no          | yes                                                        | transforms all separators to '/'                      |
+---------+-------------+-------------+------------------------------------------------------------+-------------------------------------------------------+
| win     | *RTE_WIN32* | no          | no                                                         | transforms all separators to '\\\\' or ';'            |
+---------+-------------+-------------+------------------------------------------------------------+-------------------------------------------------------+
| default | *RTE*       | no          | no                                                         | adapts 'win'(on win) or 'posix'(on posix) to local os |
+---------+-------------+-------------+------------------------------------------------------------+-------------------------------------------------------+

See also :ref:`tpf and spf <TPF_AND_SPF>`,
for a detailed comparison refer to
:ref:`'filesysobjects.normpathx' vs. 'os.path.normpath' <FILESYSOBJECTSNORMPATHX>`.

* **cnw**

  Calls transparently ::

     posixpath.normpath()

* **cnp**

  Calls transparently ::

     ntpath.normpath()

* **default**

  Adapt '*os.path.sep*' and '*os.pathsep*' to local native os, else wise
  the same behavior as the modes '*posix*' or '*win*'.

  This mode is in term of the structure including drives of Windows
  based file systems compatible across all supported platforms. But
  the *os.path.sep*, and the os.pathsep are adapted to the local
  platform.

  On POSIX platforms(Linux, MacOS, ...), e.g.::

      d:/  => d:
      d:\\  => d:\\

  On Windows platforms, e.g.::

      d:/  => d:\\
      d:\\  => d:\\

**local**:

  Compatible to local '*os.path.normpath()*', this includes the original
  permitted input characters.

  On POSIX platforms(Linux, MacOS, ...), e.g.::

      d:/  => d:
      d:\\  => d:\\

  On Windows platforms, e.g.::

      d:/  => d:\\
      d:\\  => d:\\

**posix**:

  POSIX  based style with "*os.path.sep = '/'*" and "*os.pathsep = ';'*".
  The special escape-characters are kept, additionally the
  following chars by escaping: "*[/\\\\:;]*".
  The special case of ambiguous non-intentionally escape-character
  '*\\\\\\\\*' could be eliminated by an odd number of '*\\\\*'.

  E.g. Linux, MacOS/OS-X, BSD, Solaris, etc.::

      d:/  => d:/
      d:\\  => d:/

  This mode is literally compatible across all supported platforms.

**uri**:


**win**:

  MS-Windows style with "*os.path.sep= '\\\\'*" and "*os.pathsep = ':'*".
  The special escape-characters are kept, additionally the following
  chars by escaping: "*[/\\\\:;]*".
  The special case of ambiguous non-intentionally escape-character 
  '*\\\\\\\\*' could be eliminated by an odd number of '*\\\\*'. ::

      d:/  => d:\\
      d:\\  => d:\\

  This mode is literally compatible across all supported platforms.

Literals, RegExpr, and Glob
---------------------------

The common variants of pathnames as parameters are provided by one of 
the categories:

* **Literal** - literal names

  The applicability varies on the scope.
  Whereas literals could be applied in any scope, these are the least flexible
  search pattern.
  These just provide native matches either on single nodes, or single goups
  in case of directories represented as containers. 

* **Regular Expression** - specific match pattern, which are implementation dependent

  The regular expressions in general are part of applications, either special 
  autonomous conversion filters, or embedded into a greater application,
  and/or programming environment.

  These are strongly implementation dependent, even though a broad commen set 
  is generally provided. These in particular lack the native support of 
  filesystems, thus could be only used as input and/or output filters.

* **Glob** - platform dependent native filesystem match

  The 'glob' expressions are a very basic type of regular expressions, which are
  platform dependent.
  These could be applied at the interface of the filesystems, and influence the
  responce of the filesystem interface directly.
  
  Globs can span multiple levels of directory paths. ::

    r"a[0-9]*/[!xy]*/???/*"

  Use e.g. the following patterns to restrict on a single node name: ::

    os.sep+r"a*b"+os.sep
    os.sep+r"a*b"

* **Combined** - literal names combined with glob, or regexpr

  The pathnames are internally processed depending on the category of the interface.
  Interfaces operating in memeory on strings only apply regular expressions, The
  implementation of interfaces accessing fthe filesystem, e.g. for existence tests
  and name resolution, use literal matches and glob.

  The Semi-Literal type arose from the design, that 'glob' and 'regexpr' must not
  be intermixed because of the possible ambiguities. One of the main differences is
  the scope of match. The 'glob' functions are aware of seperators, for regexpr 
  they represent simply a character. The pattern has some differences too, e.g. ::

       regexpr:  F[0-2]*  := (F, F0, F1, F2, )
       glob:     F[0-2]*  := (F.*, F0.*, F1.*, F2.*, )

  So this basicly also prohibits functions like 'fnmatch.translate()' on intermixed
  expressions. Anyhow, the user could prepare a string as regexpr before
  calling the interface. But be aware, for filesystem evaluation the glob-style is
  applied only.

  Literals and one only of the pattern types could be intermixed arbitrarily.

  The implementation and the possible intermix are provided due to the implemented 
  algorithm when the following is true:

  * 'regexpr' and 'glob' could be intermixed, when the 'glob' compiled by 're' does 
    not match. Than the algorithm keeps it simply as an unknown node, and continues 
    with 'glob' expansion. Thus the following strict pattern of path names is 
    provided, where the order is significant: ::

         <mixed-regexpr-glob> := <literal-or-regexpr><literal-or-glob>
 

  The rule of thumb is given by the following combinations:

  * literal + glob: 
      a literal path part matching the search path, a glob
      to be applied to the filesystem.

  * regexpr + literal: 
      a regexpr to be applied onto the in-memory path, followed
      by a literal applicable in any case.

  * literal + regexpr + literal + glob + literal: 
      this order is provided by the 
      algorithm but the input pattern is not verified to be of a consistent 
      type and though the applicability of the syntax has to be assured by 
      the caller
 
  * path-pattern := [path-pattern] + (literal|regexpr|glob): 
      Arbitrary pathname pattern are by default supported by trials to match 
      the longest valid parts for each type. This is inherently ambiguous when
      glob and regexpr has to be detected. Thus in cases where arbitrary types
      are required a grouping type-keyword has to be provided. ::

        path-pattern := [path-pattern] + (
        	literal   | 'literal(' literal ')' | 'l(' literal ')' 
        	| regexpr | 'regexpr(' regexpr ')' | 'r(' regexpr ')'
        	| glob    | 'glob(' glob ')'       | 'g(' glob ')'
        	)

The overall applicability  for specific execution and call contexts is depicted in
the following table.

The automatic resolution in absence of type-keyword starts in general with literals
and globs from left. Than the regexpr is tried to be resolved. 

+------------------------------+----------+---------------+---------+--------+
| Application Processing Scope | Literals | Semi-Literals | RegExpr | glob   |
+==============================+==========+===============+=========+========+
| In-Memory Path Strings       | yes      | yes           | yes     | no (1) |
+------------------------------+----------+---------------+---------+--------+
| Filesystem                   | yes      | yes           | no      | yes    |
+------------------------------+----------+---------------+---------+--------+
| Filesystem-Extension(3)      | yes      | yes           | yes(2)  | yes    |
+------------------------------+----------+---------------+---------+--------+

  (1) is treated as an 'regexpr', when matches this is resolved, else ends 
      re-processing and is applied as a 'glob'
  (2) is handled by caching the file system component into memory and applying
      the 'regexpr' onto the in-mem-string
  (3) in case of ambiguity type-keywords have to be provided on the 
      syntax parts, see 'path-pattern'

Thus the application  of RegExpr is implemented as an optional parameter 
performed on in.memory strings only. 
The workflow in case of required searches for unknown filesystem nodes by 
re-patterns is:

  #. filter and collect filesystem entries by 'literal' and 'glob' parameters

  #. post-filter the collected set by  'literal' and 'RegExpr' type parameters.


Common Path-Rules
-----------------
The *filesysobjects* supports an abstract API for the transparent application of resource paths.
This includes in reality a bunch of redundancies and ambiguities of tokens ans structures.
Therefore some minor 'esoteric' limits are accepted, while still the escaping and masking for some
application URIs is required.
The basic concept relies on specific tokens and token characters, which indicate the applications
and seperators of the syntax elements. 
Thus these are required in order to reliably distinguish between the various path syntaxes.
When multiple characters - e.g. ';' or ':' as parts of the path constructs of URLs are reuqired,
these have to be masked, or replaced by the character codes and processed by the requesting application.
An overall generic processing for all applications e.g. by *splitapppathx()* could not be provided reliable.
Even the masking by 'backslash' runs finally into ambiguity, e.g. due to supported Windows filesystems.
Therefore the package contains at the time of writing already more than 4000 Unit tests. 

The resulting advance after these practically minor - if at all - constraints is the seamless access
to various resources by mixed resource paths. Where the major part of the management and the assignment of
the resource locators is provided by the *filesysobjects*.

This syntax represents e.g. the following valid filepathanmes with the 
current position(PWD) as reference point for relative positions.
For the conversion API refer to
*splitapppathx*
`[docs] <filesysobjects.html#filesysobjects.apppaths.splitapppathx>`_
`[source] <_modules/filesysobjects/pathtools.html#splitapppathx>`_
and 
*splitapppathx_getlocalpath*
`[docs] <filesysobjects.html#filesysobjects.pathtools.splitapppathx_getlocalpath>`_
`[source] <_modules/filesysobjects/pathtools.html#splitapppathx_getlocalpath>`_
: ::

    /local/path/access

Where the following equivalent transformations result ::

     /local/path/access/dir/ => /local/path/access/dir/ # forces a directory
     /local/path/access/dir  => /local/path/access/dir  # could be a file too
     ./dir/                  => /local/path/access/dir/ # forces a directory
     ./dir                   => /local/path/access/dir  # could be a file too
     ../dir/                 => /local/path/dir/        # forces a directory
     ../dir                  => /local/path/dir         # could be a file too
     dir/                    => /local/path/access/dir/ # forces a directory
     dir                     => /local/path/access/dir  # could be a file too

Where the following basic paths are equivalent ::

    /local/path/access/dir/ == /local////////path/access//dir/////
    /local/path/access/dir/ == /local//.///./././path/access//dir//././/
    /local/path/access/dir/ == /local//../path/////path/access/../../path/access/dir/////
    /local/path/access/dir  != /local////////path/access//dir/////
    /local/path/access/dir  != //local////////path/access//dir/////
    /local/path/access/dir  != //local////////path/access//dir

Where the following basic URI paths are still equivalent ::

    file:///local/path/access/dir/ == /local////////path/access//dir/////
    file:///local/path/access/dir/ == /local//.///./././path/access//dir//././/
    file:///local/path/access/dir/ == /local//../path/////path/access/../../path/access/dir/////
    file:///local/path/access/dir  != file:///local////////path/access//dir/////
    file:///local/path/access/dir  != //local////////path/access//dir/////
    file:///local/path/access/dir  != //local////////path/access//dir

Same for the first basic URI paths on both sides ::

    file:///local/path/access/dir/ == file:///local////////path/access//dir/////
    file:///local/path/access/dir/ == file:///local//.///./././path/access//dir//././/
    file:///local/path/access/dir/ == file:///local//../path/////path/access/../../path/access/dir/////
    file:///local/path/access/dir  != file:///local////////path/access//dir/////

But for the last two no longer, because '2SEP' has to be at the beginning of the string,
which is interpreted here as the beginning of the raw string representation ::

    file:///local/path/access/dir  == file:////local////////path/access//dir/////
    file:///local/path/access/dir  == file:////local////////path/access//dir

.. _FILESYSOBJECTS_REFERENCES:

Resources
---------

* [pathlib]_ lib/pathlib - Python3
* [URLVALIDATOR]_: W3C Link Checker
* [macpath]_: legacy lib/macpath - *macpath()* variants
* [normpath]_: lib/os.path - *os.path.normpath()*
* [os.path]_: lib/os.path - *os.path.normpath()* variants


.. raw:: html

   </div>
