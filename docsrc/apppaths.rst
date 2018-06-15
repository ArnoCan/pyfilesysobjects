'filesysobjects.apppaths' - Module
==================================

The *filesysobjects.apppaths* module provides advanced operations on application resource
paths and search paths.

Implementation Details
----------------------

Glob Parameters
^^^^^^^^^^^^^^^
The '*glob*' wildcard definitions are a subset of regular expressions 
which additionally deviate slightly by their semantics.
In the case of a dot for example this could be in addition ambiguous.

.. code-block:: python
   :linenos:

   # file path name: /a/b/xname
   path0 = '/a/b/x.*'

   # regexpr: matches
   # glob:    does not match

Therefore the resolution of contained path-elements as '*glob'* expressions 
are resolved dynamically by applying the glob module onto the file system nodes.
See also `Variants of Pathname Parameters - Literals, RegExpr, and Glob <path_syntax.html#variantspathnameparams>`_.

Regular Expressions
^^^^^^^^^^^^^^^^^^^
The regular expressions support the full scope of the standard Pyhton '*re*' module.
The expressions are used as post-filter onto a set of fetched file system node path names.

The regexpr are by default compiled/loaded statically during load time of the module.
The regular expressions for the path analysis contain the '*os.path.sep*' of the current platform
which could be altered as parameter by some interfaces.
In this case the function interfaces compile the adapted regexpr into a local stack-variable,
where the compiled match object is cached by the module '*re*', but potentially will be compiled
for each call again.
The object interface may nont have to handle with this within the lifetime of the instances. 
See also `Variants of Pathname Parameters - Literals, RegExpr, and Glob <path_syntax.html#variantspathnameparams>`_.

Common Call Parameters
^^^^^^^^^^^^^^^^^^^^^^
spath
"""""
The path to be processed.
Valid scope types:


+---------+--------------------------------+-------------------------------+
| type    | description                    | example                       |
+=========+================================+===============================+
| literal | literal match                  | '/my/path/file01.ext'         |
+---------+--------------------------------+-------------------------------+
| re      | Python regular expression *re* | '/my/path/file[0-3]{2}.ext'   |
+---------+--------------------------------+-------------------------------+
| glob    | Python *glob*                  | '/my/path/file[0-3][0-3].ext' |
+---------+--------------------------------+-------------------------------+

Special precautions are required in case of ambiguity.
For example the syntax term ::

   /./  or \\.\\

has already different meanings in the syntax domains,
but last not least adds another semantic for common filesystems.

#. the dot is literally a dot for literals and globs
#. the dot is any character for regualr expressions
#. the dot as a single character is the current directory for most filesystems 

The ambiguity could be resolved e.g. by ::

   /.{1}/
   /\./
   /[.]/



plist
"""""
List of path strings to be searched. By default first match
is used. The concrete processing varies by the interfaces. ::

   ['/my/search/path0', '/my/search/path1', '/my/search/path2']

default := sys.path

appre - Application Prefix
""""""""""""""""""""""""""
Adds application prefix, URI scheme.
This also forces the appropriate path separator for specific standards. ::

  apppre = (True|False)

The application prefix e.g. for file-URI [RFC8089]_ is added as

.. parsed-literal::

  **apppre = True**

   /a/b/c             =>  file:///a/b/c
   c:\\a\\b\\c           =>  file:c:/a/b/c    # see [RFC8089]_ Appendix
   \\a\\b\\c             =>  file:///a/b/c    # see [RFC8089]_ Appendix

.. parsed-literal::

  **apppre = False**

   /a/b/c              =>  /a/b/c
   c:\\a\\b\\c            =>  c:\\a\\b\\c        # see [RFC8089]_ Appendix
   \\a\\b\\c              =>  \\a\\b\\c          # see [RFC8089]_ Appendix
   file:///a/b/c       =>  file:///a/b/c
   file:c:\\a\\b\\c       =>  file:c:/a/b/c   # see [RFC8089]_ Appendix
   file:c:/a/b/c       =>  file:c:/a/b/c   # see [RFC8089]_ Appendix
   file://\\a\\b\\c       =>  file:///a/b/c   # see [RFC8089]_ Appendix
   file:///a/b/c       =>  file:///a/b/c   # see [RFC8089]_ Appendix

default := False

appsplit - Split
""""""""""""""""
Adds application prefix, URI scheme.
This also forces the appropriate path separator for specific standards. ::

  appsplit = (True|False)

The application prefix e.g. for file-URI [RFC8089]_ is added as

.. parsed-literal::

   /a/b/c    =>  file:///a/b/c
   c:\\a\\b\\c  =>  file:c:/a/b/c  # see [RFC8089]_ Appendix
   \\a\\b\\c    =>  file:///a/b/c  # see [RFC8089]_ Appendix

default := False

keepsep
"""""""
Modifies the behavior of 'strip' parameter.
If 'False', the trailing separator is dropped. ::

   splitapppathx('/a/b', keepsep=False)   => ('', 'a', 'b')
   splitapppathx('/a/b/', keepsep=False)  => ('', 'a', 'b')

for 'True' trailing separators are kept as directory
marker::

   splitapppathx('/a/b', keepsep=True)    => ('', 'a', 'b')
   splitapppathx('/a/b/', keepsep=True)   => ('', 'a', 'b', '')

The following defaults apply: ::

   default := False # for URIs except file://, smb://
   default := True  # for file path names

pathsep
"""""""
Replaces path separator set by the *spf*, e.g. for a URI
pathlist from an alternate platform.
The resulting character selects the type of the
scanner *APPPATHSCANNER* [`source <_modules/filesysobjects/apppaths.html#>`_]. ::

   pathsep := (';' | ':')

Is used in the absence of *spf* as the platform discriminator.

The path separator also effects the compilation of regular expressions, 
when these contain free separator characters, which are interpreted 
and transformed accordingly to the choosen platform.

strip
"""""
Strips null-entries, reduces by dropping redundancies. The strip parameter
influences the match of regular expressions, which just
do a pattern match, thus hit null-separator directories too.
The strip of these prevents from unwanted matches on separator
characters. ::

 strip := (
      True      # clear null-separators
    | False     # no strip at all
    | all       # clear any redundancy
    | contain   # contained sub directories
    | multiple  # multiple occurance
 )

The *True* and *False* parameters are supported commonly,
while the remaining are supported by special interfaces only.

default := True

stripquote
""""""""""
Strips special Python style *filesysobject* triple-quotes. ::

   /my/path/with/"""double-quoted"""/dirs => /my/path/with/double-quoted/dirs
   /my/path/with/'''single-quoted'''/dirs => /my/path/with/single-quoted/dirs 

Current version does not support nested triple-quotes; neither homogeneous,
nor heterogeneous.

spf - Source Platform
"""""""""""""""""""""
The Source-Platform, defines the characters to be used as path
separator, and the additional concrete semantics for the specific platform.
The platform is hereby associated with a specific resource address type,
this is the common standard. 
Default is the current platform, with a single character
for the 'os.pathsep' and the support for the specific semantics
like DOS drives for the platform 'win'.
Application and URL/URI file prefixes and tags like 'smb://',
'file:', 'file://', 'file:////', and 'file://///' are detected in
any case. Thus these are treated as reserved words.

The syntax is: ::

   spf := (<predefined>|<bitmask>|<pathsep>)

   bitmask := (
         RTE_WIN32  | RTE_POSIX | RTE_LINUX
       | RTE_DARWIN | RTE_BSD
   )
   pathsep := (':' | ';')
   predefined := (
       'bsd' | 'darwin' | 'linux' | 'posix' | 'solaris'
       | 'uri' | 'win' | 'win32'
   )

For details refer to `paths.getspf() <paths.html#getspf>`_

* *posix*, *RTE_POSIX*:

  The Posix platform, is aware of the posix
  syntax and semantics, single character '/' as separator.
  Ignored pattern for potential DOS drives.

* *win*, *RTE_WIN32*:

  The Windows platform. Is aware of the Windows
  syntax and semantics, single character '\\' as separator.
  Recognizes string pattern of DOS drives.

* *RTE_LINUX*, *RTE_DARWIN*, *RTE_BSD*

  The Linux, Darwin/OS-X, BSD, and the Solaris platform
  are mapped to the Posix style file path names.

For mixed input for example: ::

   spf := ':;'


See also `tpf and spf <filesysobjects_design.html#tpf-and-spf>`_.

tpf - Target Platform
"""""""""""""""""""""
Target platform for the file pathname.
The platform is hereby associated with a specific resource address type,
this is the common standard. 
Due to some deviations from the expected behavior in
case of cross platform development the following options 
are defined:

+---------+-----------+----------------+-------------------------+-------------------------------------------------------+
| tpf     | numeric   | compatible     | cross                   | behaviour                                             |
|         |           | to os.normpath | platform                |                                                       |
+=========+===========+================+=========================+=======================================================+
| cnp     |           | yes(posix)     | no                      | calls posixpath.normpath()                            |
+---------+-----------+----------------+-------------------------+-------------------------------------------------------+
| cnw     |           | yes(win)       | no                      | calls ntpath.normpath()                               |
+---------+-----------+----------------+-------------------------+-------------------------------------------------------+
| local   |           | yes            | no                      | calls local os.path.normpath()                        |
+---------+-----------+----------------+-------------------------+-------------------------------------------------------+
| posix   | RTE_POSIX | no             | yes*                    | transforms all separators to '/' or ':'               |
|         |           | (*pchar)       | Portable for IEEE1003.1 |                                                       |
+---------+-----------+----------------+-------------------------+-------------------------------------------------------+
| uri     |           | no             | yes                     | transforms all separators to '/'                      |
+---------+-----------+----------------+-------------------------+-------------------------------------------------------+
| win     | RTE_WIN32 | no             | no                      | transforms all separators to '\\\\' or ';'            |
+---------+-----------+----------------+-------------------------+-------------------------------------------------------+
| default |           | no             | no                      | adapts 'win'(on win) or 'posix'(on posix) to local os |
+---------+-----------+----------------+-------------------------+-------------------------------------------------------+

For details refer to `paths.gettpf() <paths.html#gettpf>`_, for a detailed comparison refer to
:ref:`'filesysobjects.normpathx' vs. 'os.path.normpath' <FILESYSOBJECTSNORMPATHX>`.

**local**:

  Compatible to local 'os.path.normpath()', this includes the original
  permitted input characters.

  On POSIX platforms(Linux, MacOS, ...), e.g.::

      d:/  => d:
      d:\\  => d:\\

  On Windows platforms, e.g.::

      d:/  => d:\\
      d:\\  => d:\\

**posix**:

  POSIX  based style with os.path.sep = '/' and os.pathsep = ';'.
  The special escape-characters are kept, additionally the
  following chars by escaping: [/\\\\:;].
  The special case of ambiguous non-intentionally escape-character
  '\\\\\\\\' could be eliminated by an odd number of '\\\\'.

  E.g. Linux, MacOS/OS-X, BSD, Solaris, etc.::

      d:/  => d:/
      d:\\  => d:/

  This mode is literally compatible across all supported platforms.

**win**:

  MS-Windows style with os.path.sep= '\\\\' and os.pathsep = ':'.
  The special escape-characters are kept, additionally the following
  chars by escaping: [/\\\\:;].
  The special case of ambiguous non-intentionally escape-character 
  '\\\\\\\\' could be eliminated by an odd number of '\\\\'. ::

      d:/  => d:\\
      d:\\  => d:\\

  This mode is literally compatible across all supported platforms.

**default**:

  Adapt 'os.path.sep' and 'os.pathsep' to local native os, else wise
  the same behavior as the modes 'posix' or 'win'.

  This mode is in term of the structure including drives of Windows
  based file systems compatible across all supported platforms. But
  the os.path.sep, and the os.pathsep are adapted to the local
  platform.

  On POSIX platforms(Linux, MacOS, ...), e.g.::

      d:/  => d:
      d:\\  => d:\\

  On Windows platforms, e.g.::

      d:/  => d:\\
      d:\\  => d:\\


See also `tpf and spf <filesysobjects_design.html#tpf-and-spf>`_.

Supported Conversions
^^^^^^^^^^^^^^^^^^^^^
The *filesysobjects* provides functions for the normalization and the split of resource paths.
This includes the cross-conversion of the major filesysytem platforms Posix and Windows.
In addition various conversions are supported. 
These comprise the equivalent conversion between
semantically compatible representations, and the conversion between syntactical compatible
respresentations without assured semantic equivalency.
The latter requires for the semantical equivalency additional conventions, e.g. for the
conversion of 'z:\my\path' from windows to Posix. 

The split of all supported platforms for custom applications is supported.

normpathx
"""""""""
The *normpathx* supports the normalization of resource paths for the native platform, and
the cross-conversion for a limited set of other platforms when the call parameters *spf* 
and *tpf* are used.

The following basic cross-conversions are supported.

+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+
|          | posix | win | cygwin | file (0) | file (2) | file (3) | file (4) | file (5) | unc |
+==========+=======+=====+========+==========+==========+==========+==========+==========+=====+
| posix    | c     | f   | c      | c        | c        | c        |          |          |     |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+
| win      | f     | c   | c      | c        | c        | c        |          |          |     |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+
| cygwin   | c     | c   | c      | c        | c        | c        |          |          |     |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+
| file (0) | c     | c   | c      | c        | c        | c        |          |          |     |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+
| file (2) |       |     |        |          | c        |          |          |          |     |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+
| file (3) | c     | c   | c      | c        | c        | c        |          |          |     |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+
| file (4) |       |     |        |          |          |          | c        | c        | c   |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+
| file (5) |       |     |        |          |          |          | c        | c        | c   |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+
| unc      |       | f   | f      |          |          |          | c        | c        | c   |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+


**c**: Could be converted into equivalent representation.

**f**: Format conversion without assured equivalency. The accuracy depends on additional conventions.

**(0)**: file uri - short form: ::

   'file:/my/path'   == '/my/path'
   'file:c:/my/path' == 'c:/my/path' == 'c:\my\path'

**(2)**: file uri - remote file: ::

   'file\://myhost/my/path' == '//myhost/my/path'

**(3)**: file uri - traditional: ::

   'file:///my/path'== '/my/path'

**(4)**: file uri - UNC: ::

   'file:////myhost/myshare/my/path' == '\\myhost\myshare\my\path'

**(5)**: file uri - UNC: ::

   'file://///myhost/myshare/my/path' == '\\myhost\myshare\my\path' 

For details of the sub-conversion, e.g. file-URI with 4 or 5 slashes
refer to the API.

normapppathx and normpathx
""""""""""""""""""""""""""
The following basic cross-conversions by the functions
*normapppathx* and *normpathx* between source and 
target platforms are supported.
The call parameters *spf* and *tpf* control the representation.

+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+
|          | posix | win | cygwin | file (0) | file (2) | file (3) | file (4) | file (5) | unc | smb | cifs | http | https |
+==========+=======+=====+========+==========+==========+==========+==========+==========+=====+=====+======+======+=======+
| posix    | c     | f   | c      | c        | c        | c        |          |          |     |     |      |      |       |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+
| win      | f     | c   | c      | c        | c        | c        |          |          | c   |     |      |      |       |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+
| cygwin   | c     | c   | c      |          |          |          |          |          |     |     |      |      |       |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+
| file (0) | c     | c   | c      | c        | c        | c        |          |          |     |     |      |      |       |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+
| file (2) |       |     |        |          |          |          |          |          |     | f   | f    |      |       |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+
| file (3) | c     | c   | c      | c        |          | c        |          |          |     | f   | f    |      |       |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+
| file (4) |       |     |        |          |          |          |          |          | c   | f   | f    |      |       |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+
| file (5) |       |     |        |          |          |          |          |          | c   | f   | f    |      |       |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+
| unc      |       | c   |        |          |          |          | c        | c        | c   | c   | c    |      |       |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+
| smb      |       | c   |        |          |          |          | c        | c        | c   | c   | c    |      |       |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+
| cifs     |       | c   |        |          |          |          | c        | c        | c   | c   | c    |      |       |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+
| http     |       |     |        |          |          |          |          |          |     |     |      | c    | c     |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+
| https    |       |     |        |          |          |          |          |          |     |     |      | c    | c     |
+----------+-------+-----+--------+----------+----------+----------+----------+----------+-----+-----+------+------+-------+

**c**: Could be converted into equivalent representation.

**f**: Format conversion without assured equivalency. The accuracy depends on additional conventions.

(0): file uri - short form: 'file:/my/path', 'file:c:/my/path'

(2): file uri - remote file: 'file://myhost/my/path'

(3): file uri - traditional: 'file:///my/path'

(4): file uri - UNC: 'file:////myhost/myshare/my/path'

(5): file uri - UNC: 'file://///myhost/myshare/my/path'

For details of the sub-conversion, e.g. file-URI with 4 or 5 slashes
refer to the API.

spliapppathx and splitpathx
"""""""""""""""""""""""""""
The split-functions *splitapppathx* and *splitpathx* for custom behaviour
are applicable on all supported types.
This includes also the conversion of the path component.

Module
------

.. automodule:: filesysobjects.apppaths

.. role:: raw-html(raw)
   :format: html

Constants
---------

.. _APPLICATIONPATHSCANNERPARSER:

Application Path Scanner - Parser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The scanner and parser for application resource name rules in accordance to  
Posix/IEEE-1003.1 [POSIX]_, UNC [MS-DTYP]_/[MS-SMB]_/[MS-CIFS]_/[FAT]_, URI [RFC8089]_/[RFC3986]_,
and others.
Provides for multiple mixed entries in search-path syntax, 
adds some minor causal constraints on esoteric and rare cases for ambiguity resolution.

The base for the application resource path compilers of *filesysobjects.apppaths.normapppathx*
and *filesysobjects.apppaths.splitapppathx*.

* **APPPATHPARSER**

  The main regular expression for split of PATH variables with support for URIs.

  .. autodata:: APPPATHSCANNER_COL

  .. autodata:: APPPATHSCANNER_SEM

* **APPPATHINDEX**

  .. autodata:: APPPATHINDEX

* **APPTYPES**

  .. autodata:: APPTYPES

* **APPTYPES_L2**

  .. autodata:: APPTYPES_L2


Functions
---------

addpath_to_searchpath
^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: addpath_to_searchpath

delpath_from_searchpath
^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: delpath_from_searchpath 

.. _def_gettop_from_pathstring:

gettop_from_pathstring
^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: gettop_from_pathstring

gettop_from_pathstring_iter
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: gettop_from_pathstring_iter

join_apppathx_entry
^^^^^^^^^^^^^^^^^^^
.. autofunction:: join_apppathx_entry

.. _def_normapppathx:

normapppathx
^^^^^^^^^^^^
.. autofunction:: normapppathx

set_uppertree_searchpath
^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: set_uppertree_searchpath

.. _def_splitapppathx:

splitapppathx
^^^^^^^^^^^^^
.. autofunction:: splitapppathx

splitapppathx_getlocalpath
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: splitapppathx_getlocalpath

Exceptions
----------

AppPathError
^^^^^^^^^^^^
.. autoexception:: AppPathError

