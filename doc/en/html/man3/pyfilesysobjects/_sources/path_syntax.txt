Addresses for File-Like Resources
*********************************

The package 'filesysobjects' supports the hierarchical 
navigation on filesystems.
This is similar to the hierarchy of object oriented class
hierarchies

.. note::

   The basic idea is to start a search operation for filenames 
   from a directory position on upward and get the first match.
   The first match is than the deepest position, which in terms of
   object orientation represents the most specialized class.

A typical application is the drop-in design of regression and 
unit tests.
In those cases a frequent requirement is the provisioning of test dummies.
This could be simply designed as an executable file for providing 
test values, or simulating the environment for a specific test.
When performing multiple tests on the same resource, the upward-search operation
provides for automatic detection from multiple cases which are positioned 
deeper within the filesystem hierarchy.
Thus these cases simply inherit an already present resource, which in addition
covers higher positioned files by a higher degree of specialization. 

* `Filesystem Elements as Objects <path_syntax.html#filesystem-elements-as-objects>`_ 
* `Variants of Pathname Parameters - Literals, RegExpr, and Glob <path_syntax.html#variants-of-pathname-parameters-literals-regexpr-and-glob>`_ 
* `Syntax Elements <path_syntax.html#syntax-elements>`_ 
* `Call Parameters of the API <path_syntax.html#call-parameters-of-the-api>`_ 
* `API in javadoc-style <epydoc/index.html>`_


Filesystem Addresses
====================

The path syntax elements supported by this module 
represent an abstraction of file system paths.
The representation is based on a common platform 
independent path compiler implemented based on
the *re* package.
This provides a canonical view on file resource paths.

* URIs based on RFC3986 and RFC8089 for local files are resolved to: ::

      file://///host/share/local/filesystem/path 
      file:////host/share/local/filesystem/path 
      file:///local/filesystem/path 
      file://localhost/local/filesystem/path 
      file://127.0.0.1/local/filesystem/path 
      file:/local/filesystem/path 
      file:d:/local/filesystem/path 

* IEEE Std 1003.1(TM), 2013 Edition; Chapter 4.12: ::

       //hostname/local/filesystem/path

* UNC/SMB/CIFS/NTFS/FAT: ::

      \\\\hostname\\local\\filesystem\\path
      \\local\\filesystem\\path
       d:\\a\\b

* Mac-OS:

  Current same as for Linux/Unix.

File Paths in Pyhton3
=====================
The Python release 3 supports a new library *pathlib* [pathlib]_,
which focusses on paths and distinguishes between static(Pure) and dynamic resolution. 

|pathlibinheritance|
|pathlibinheritance_zoom|

.. |pathlibinheritance_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/pathlib-inheritance.png
   :width: 16

.. |pathlibinheritance| image:: _static/pathlib-inheritance.png
   :width: 300

The independently developed *filesysobjects* contains these features and extends
the view onto arbitrary persistent objects.
The support comprises Python2.7 and Python3.5+, where due to the large codebase the Python2.7
release is seen to be in active use for another decade.  

The extended features like 'splitapppathx()' and 'splitpathx()',
'escapepathx()' and 'unescapepathx()' require a supporting path compiler,
thus could not be replaced by the new *pathlib*.
Another aspect is the dynamic registration and un-registration of additional application
packages, which may include completely different scanners and parsers for paths of virtual filesystems.
Thus these dispatcher parts are table-driven instead of inheritance based.

The cross-native features which currently use interfaces of the '*os*' package
are forseen to be migrated and/or alterntively based on the new lib for Python3.5+.

Arbitrary File-Like Resources
=============================
The Unix OS / IEEE-1003.1 provide a view of the file system based driver interfaces to arbitrary resources.
These comprise ordinary files, IO devices, storage devices, and others.
The Windows OS provides partially a similar view, e.g. by the Name-Spaces.

Therefore the *filesysobjects* package handles each supported resource as an object which
has an access-path.
The path could be preresnted by various syntaxes, e.g. as Windows-Path, or as a Posix-Path.
Where these common syntaxes could even be subdivided, e.g. by the onld MacOS syntax,
which is still present in OS-X.
Another common representation is here the file-URL of RFC8089.

The *filesysobjects* defines a canonical object namebinding for each resource and maps these
to the requested target syntax.
The conversion is controlled by the parameters *spf*, and *tpf* - source-platform and target-platform.
This comprises the pure syntax elements with additional context specific semantics for the
appropriate ambiguity resolution.
E.g. drive-names, host names, and shares as path parts,
also queries and fragments, or OIDs.

The internal decomposition is provided to the applicaiton by the *split* functions, which enable
for simplified loop constructs, e.g. for heterogeneous path-resolution, search and crawler operations.


Common Path Addresses
---------------------
The syntax elements for the normalization of pathnames are in particular 
essential for the treatment of the filesystem structure as a class and object
hierarchy.
Thus the behaviour has to be defined thoroughly from the beginning, even or
better in particular in case of the foreseen evolutionary add-on extension.  

The current release provides the following syntax, *successive
compatible extensions are going to follow soon*.  These the processing
of the provided syntax is designed in two layers in accordance to
common examples.

The lower layer provides the syntax elements to construct a pathname
for local access, whereas the upper layer provides the information for
the location of remote filesystems.

The following figure draftly weights the degree of exchangability and inter operability of the
supported name-binding by the resource file path specifications.
Where the darkness of the grey background symbolizes a tighter overall coupling.

|pathnametypes|
|pathnametypes_zoom|

.. |pathnametypes_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/pathname_types.png
   :width: 16

.. |pathnametypes| image:: _static/pathname_types.png
   :width: 500


Thus the functions of the lower layer:

* `escapepathx`_
* `normpathx`_
* `splitpathx`_
* `unescapepathx`_

are extended replacements of the standard system interfaces:

* *ntpath.normpath*, *ntpath.split*, *ntpath.splitdrive*,
* *os.path.normpath*, *os.path.split*, *os.path.splitdrive*,
* *posixpath.normpath*, *posixpath.split*, *posixpath.splitdrive*,

Whereas the functions of the upper layer:

* `normapppathx`_
* `splitapppathx`_
* `splitapppathx_getlocalpath`_

include support for application pathnames including schemes, and provide
intermixed search-paths.
This also contains the accurate feature of the interface *ntpath.splitunc*,
extended by file-URIs for UNC - RFC8089.

The escape and unescape functions provide for standard pathnames in particular for 
windows file systems, including the awareness of standard escape sequences.
The interfaces are:

* `escapepathx`_

  Escape backshlashes and standard escape characters.

* `unescapepathx`_

  Unescape, this simply reverses the *escapepathx*.

* mask

  Any text sequence could be masked - protected - by Python docstring like triple quotes. 

.. _escapepathx: paths.html#escapepathx
.. _normapppathx: apppaths.html#normapppathx
.. _normpathx: paths.html#normpathx
.. _splitapppathx: apppaths.html#splitapppathx
.. _splitapppathx_getlocalpath: apppaths.html#getappprefix-localpath
.. _splitpathx: paths.html#splitpathx
.. _unescapepathx: paths.html#unescapepathx

The following function hierarchy for pathname conversion including
UNC, SMB, POSIX-Apps, and local filenames is supported.
The layer for the abstract search and interator interfaces relies herby on the resource paths
as processed by the lower layers.
The results are provided in the available representations of the application resource paths
and/or standar local file system path name layer.

|pathnamefunctions|
|pathnamefunctions_zoom|

.. |pathnamefunctions_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/pathname_functions.png
   :width: 16

.. |pathnamefunctions| image:: _static/pathname_functions.png
   :width: 500

Due to some specific position dependent interpretation of the
'os.sep' and the 'os.pathsep' the application layer has the app specific knowledge 
and is foreseen to break the provided resource paths into the chunks understood by the
lower layer interfaces.
This also normalizes the 'os.sep' and 'os.pathsep' by conversion and elimination of 
neutral repetitons as well as special semantics of the reserved dot-names '.' and '..'.
A single pathname is hereby represented by the following syntax: ::

    filesystemNodeName := (
       pathname + SEP + filename
       | pathname [ + SEP ]
       | [ SEP ] + filename
       | SEP
    )

    pathname := [ PREFIXKEY ] + dirname [ + SEP + pathname ]
    dirname := <valid-name-of-dir-node> 
    filename := <valid-name-of-file-node>
    <valid-name-of-dir-node> := <-node-name> [ + SEP$ ]
    <valid-name-of-file-node> := <valid-node-name>
    <valid-node-name> := 1*(x)nodechar | 1*(x)<node-name-chars>
    <node-name=chars> := 1*(a)nodechar + 3QUOTE + 1*(b)anychar + 3QUOTE [ + <node-name=chars> ]  

    PREFIXKEY := (
         'file:///' + 2SEP + SPECIALNODE + 1SEP + share-name 
       | 'file://'
       | 'file:'  # short form, see RFC8089
       | 'smb://' + SPECIALNODE + 1SEP + share-name
       | DRV
       | 2SEP  SPECIALNODE  [varSEP]
       | nSEP       
    )
    DRV := [a-z] + ':'   # On MS-Windows
    SPECIALNODE := (
       <networknode-access>
    )
    share-name := (
       1*80pchar  # see [MS-DTYP]_
    )
    <networknode-access> := [^SEP]+
    varSEP := ( '' | 1SEP | 2SEP | nSEP )
    1SEP := ^SEP + !SEP
    2SEP := ^SEP + SEP + !SEP       # in accordance to IEEE Std 1003.1 and/or CIFS/SMB
    nSEP := ^SEP + SEP + SEP + SEP* # more than 2xSEP
    SEP := <OS-specific-seperator>
    3QUOTE := ( '"' + '"' + '"' | "'" + "'" + "'")  # 3x'"' or 3x"'"
    <OS-specific-seperator> := ( '/' | '\' ) # for now only two are known

    SPECIAL_SYNTAX_DIAGRAM_CHARS_AND_REGEXPR := { 
       '^', '$', '!', '+', '{', '}', '[', ']', ':=', '|', '<', '>', '#' 
    }

   anychar := "any character"  # any character in quoted sections, e.g. globs and/or regular expressions

The seperator commonly used in this document is '/'. This could be interchaned by
the seperator '\\', which also defines an escape character, thus is omitted when not
required.

The following mappings of types to pathnames are supported.

+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| type             | prefix                                     | host/authority           | share | path          | path-options    |
+==================+============================================+==========================+=======+===============+=================+
| ldsys            | <drive>:, file://<drive>, file:<drive>     |                          | drive | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| lfsys            | file://, file:,                            |                          |       | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| lfsys(localhost) | file:localhost, file://localhost           | 'localhost', '127.0.0.1' |       | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| raw              |                                            |                          |       | resource-path |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| share            | '\\\\', '//'                               | hostname                 | share | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| smb, cifs        | smb://                                     | hostname                 | share | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| url              | http://, https://, ftp://, ...             | hostname                 |       | path          | query, fragment |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| unc              | file://///, file:////,'\\\\', '//', unc:// | hostname                 | share | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| Posix-App        | '//'                                       | app-prefix/hostname      |       | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+

The above syntax definition provides just a subset but very common set of possible naming schemes, 
additional are foreseen to be supported in next versions by custom plugins.

Thus the functions of the lower layer:

* `escapepathx`_
* `normpathx`_
* `splitpathx`_
* `unescapepathx`_

are extended replacements of the standard system interfaces:

* *ntpath.normpath*, *ntpath.split*, *ntpath.splitdrive*,
* *os.path.normpath*, *os.path.split*, *os.path.splitdrive*,
* *posixpath.normpath*, *posixpath.split*, *posixpath.splitdrive*,

Whereas the functions of the upper layer:

* `normapppathx`_
* `splitapppathx`_
* `splitapppathx_getlocalpath`_

include support for application pathnames including schemes, and provide
intermixed search-paths.
This also contains the accurate feature of the interface *ntpath.splitunc*,
extended by file-URIs for UNC - RFC8089.

The escape and unescape functions provide for standard pathnames in particular for 
windows file systems, including the awareness of standard escape sequences.
The interfaces are:

* `escapepathx`_

  Escape backshlashes and standard escape characters.

* `unescapepathx`_

  Unescape, this simply reverses the *escapepathx*.

* mask

  Any text sequence could be masked - protected - by Python docstring like triple quotes. 

.. _escapepathx: paths.html#escapepathx
.. _normapppathx: apppaths.html#normapppathx
.. _normpathx: paths.html#normpathx
.. _splitapppathx: apppaths.html#splitapppathx
.. _splitapppathx_getlocalpath: apppaths.html#getappprefix-localpath
.. _splitpathx: paths.html#splitpathx
.. _unescapepathx: paths.html#unescapepathx

The following function hierarchy for pathname conversion including
UNC, SMB, POSIX-Apps, and local filenames is supported.
The layer for the abstract search and interator interfaces relies herby on the resource paths
as processed by the lower layers.
The results are provided in the available representations of the application resource paths
and/or standar local file system path name layer.

|pathnamefunctions2|
|pathnamefunctions2_zoom|

.. |pathnamefunctions2_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/pathname_functions.png
   :width: 16

.. |pathnamefunctions2| image:: _static/pathname_functions.png
   :width: 500

Due to some specific position dependent interpretation of the
'os.sep' and the 'os.pathsep' the application layer has the app specific knowledge 
and is foreseen to break the provided resource paths into the chunks understood by the
lower layer interfaces.
This also normalizes the 'os.sep' and 'os.pathsep' by conversion and elimination of 
neutral repetitons as well as special semantics of the reserved dot-names '.' and '..'.
A single pathname is hereby represented by the following syntax: ::

    filesystemNodeName := (
       pathname + SEP + filename
       | pathname [ + SEP ]
       | [ SEP ] + filename
       | SEP
    )

    pathname := [ PREFIXKEY ] + dirname [ + SEP + pathname ]
    dirname := <valid-name-of-dir-node> 
    filename := <valid-name-of-file-node>
    <valid-name-of-dir-node> := <-node-name> [ + SEP$ ]
    <valid-name-of-file-node> := <valid-node-name>
    <valid-node-name> := 1*(x)nodechar | 1*(x)<node-name-chars>
    <node-name=chars> := 1*(a)nodechar + 3QUOTE + 1*(b)anychar + 3QUOTE [ + <node-name=chars> ]  

    PREFIXKEY := (
         'file:///' + 2SEP + SPECIALNODE + 1SEP + share-name 
       | 'file://'
       | 'file:'  # short form, see RFC8089
       | 'smb://' + SPECIALNODE + 1SEP + share-name
       | DRV
       | 2SEP  SPECIALNODE  [varSEP]
       | nSEP       
    )
    DRV := [a-z] + ':'   # On MS-Windows
    SPECIALNODE := (
       <networknode-access>
    )
    share-name := (
       1*80pchar  # see [MS-DTYP]_
    )
    <networknode-access> := [^SEP]+
    varSEP := ( '' | 1SEP | 2SEP | nSEP )
    1SEP := ^SEP + !SEP
    2SEP := ^SEP + SEP + !SEP       # in accordance to IEEE Std 1003.1 and/or CIFS/SMB
    nSEP := ^SEP + SEP + SEP + SEP* # more than 2xSEP
    SEP := <OS-specific-seperator>
    3QUOTE := ( '"' + '"' + '"' | "'" + "'" + "'")  # 3x'"' or 3x"'"
    <OS-specific-seperator> := ( '/' | '\' ) # for now only two are known

    SPECIAL_SYNTAX_DIAGRAM_CHARS_AND_REGEXPR := { 
       '^', '$', '!', '+', '{', '}', '[', ']', ':=', '|', '<', '>', '#' 
    }

   anychar := "any character"  # any character in quoted sections, e.g. globs and/or regular expressions

The seperator commonly used in this document is '/'. This could be interchaned by
the seperator '\\', which also defines an escape character, thus is omitted when not
required.

The following mappings of types to pathnames are supported.

+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| type             | prefix                                     | host/authority           | share | path          | path-options    |
+==================+============================================+==========================+=======+===============+=================+
| ldsys            | <drive>:, file://<drive>, file:<drive>     |                          | drive | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| lfsys            | file://, file:,                            |                          |       | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| lfsys(localhost) | file:localhost, file://localhost           | 'localhost', '127.0.0.1' |       | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| raw              |                                            |                          |       | resource-path |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| share            | '\\\\', '//'                               | hostname                 | share | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| smb, cifs        | smb://                                     | hostname                 | share | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| url              | http://, https://, ftp://, ...             | hostname                 |       | path          | query, fragment |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| unc              | file://///, file:////,'\\\\', '//', unc:// | hostname                 | share | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+
| Posix-App        | '//'                                       | app-prefix/hostname      |       | path          |                 |
+------------------+--------------------------------------------+--------------------------+-------+---------------+-----------------+

The above syntax definition provides just a subset but very common set of possible naming schemes, 
additional are foreseen to be supported in next versions by custom plugins.

Canonical Address
-----------------

For now experimental and non-productive, for review and
comments `[API] <shortcuts.html#>`_:  ::

    filesysobjects.NetFiles.normpathx

For syntax design requirements refer to "`Extended Filesystems - Network Features <path_netfiles.html>`_".

See also Python issue:

* Issue 26329: os.path.normpath("//") returns //
  - http://bugs.python.org/issue26329




.. _FILESYSELEMASOBJECTS:

Filesystem Elements as Objects
==============================

The common filesystems inherently support basic features for the application of hierarchical 
name binding structures.
This is commonly utilized by applications via various search path algorithms e.g. the PATH
variable for executables.
The package 'filesystemobjects' extends this feature for the upward search within hierarchies
including the search and extension by subpaths as branches.
This simulates inheritance within classes and objects.

The following two example features already provide for the required 
basic superposition of inheritance for files in directory hierarchies.

* The search for files and/or relative paths from a given 
  directory on upwards.
* The extension of search paths with any sub-directory portion 
  from a given directory on upwards.  

This provides e.g. the superposition of equal named files within different 
levels of the directory tree.
Thus a search operation upward from a start position will match the same 
name multiple times, similar to a method or member variable of a class 
within an inheritance hierarchy.

The following figure depicts the structure for some  examples(
see testdata.examples). 

.. image:: _static/filesysobjectsnav.png
   :width: 650

Or as tree output:
  ::

    a
    |-- b0
    |   |-- a
    |   |   `-- b0
    |   |       |-- c
    |   |       |   `-- F
    |   |       |-- F
    |   |       `-- F1
    |   |-- c
    |   |   |-- a
    |   |   |   `-- b0
    |   |   |       |-- c
    |   |   |       |   `-- F
    |   |   |       |-- F
    |   |   |       `-- F1
    |   |   `-- F
    |   `-- F
    |-- b1
    |   |-- c
    |   |   |-- F
    |   |   `-- F1
    |   `-- F
    |-- b2
    |   `-- a
    |       |-- b0
    |       |   |-- c
    |       |   |   `-- F
    |       |   |-- F
    |       |   `-- F1
    |       `-- F
    |-- F
    `-- F1



The basic idea is similar to any OO pattern for the implementation of holomorpy by 
upward search for identical named elements. Where by default the first 
match terminates the search.
Thus the first match defines the concrete feature, whereas the possible following
additional matches in the higher location of the filesystem tree were hidden.
This could be varied for specific applications as required.

The following search order simulates inheritance and could simply created by one
API call `set_uppertree_searchpath`_: ::

    0. a/b2/a/b0/c/F   => match, stop
    1. a/b2/a/b0/F
    2. a/b2/a/F
    3. a/F

.. _set_uppertree_searchpath: pyfilesysobjects.html#filesysobjects.pathtools.set_uppertree_searchpath

This algorithm in particular could be repeated after the first match for the remaining
upper tree again.
This is either applied for a single search, or an iterator, where collections has to
be processed. ::

    pyfilesysobjects.html#filesysobjects.pathtools.#set_uppertree_searchpath

    0. a/b2/a/b0/c/F
    1. a/b2/a/b0/F    => match, stop
    2. a/b2/a/F
    3. a/F

Next iteration, and so on... ::

    0. a/b2/a/b0/c/F
    1. a/b2/a/b0/F
    2. a/b2/a/F       => match, stop
    3. a/F

This also works for side branches when the in memory string function is applied onto plist.
Thus you can simply map e.g. the following branch by one call only: ::

    a/b0/x/y/z/file.txt

into: ::

    /a/b2/a/b0/c/F
          | |
          V V
          =/=/
              `-x/y/z/file.txt



The application of a low-level algorithm on files and directories in particular
provides for simplified drop-in designs, with generic determination of 
application features.
It is in particular possible to design quite powerful applications by just a few
interface conventions.
The provided library provides various parameters for the algorithm including 
reversed order, pattern match, and match-index based search.

A more complex application of this is Python itself, whereas a ligthweight
application for bash scripts is presented by the project

    bash-core-lib - https://sourceforge.net/p/bashcorelib/

    bash-core     - https://sourceforge.net/projects/bash-core/

which basically introduces OO elements and reusability by
repositories into bash scripting based on ShellScriptlets
and dotted object-tree-like notation.

Filesystems - Native and Standard Features
==========================================

The path syntax elements supported by this module 
represent an abstraction, but finally rely 
on the supported platforms. Therefore internally the 
function 'os.path.normpath' is widely applied for the
transformation of the native syntax elements into the 
internal canonical representation for processing. 
In addition in internal cases of textual syntax processing 
escaping may be occasianlly required.

In cases where special semantic treatment of the path elements is
required, these could be activated or disabled by 
parameters of the call interface.

The following list depicts shortly the relevant standards
and common APIs for the naming and namebinding of filesystem 
nodes, including some network aspects for specific filesystems
like NFS, and SMB/CIFS.

The focus is the local filesystem, therefore elements
dealing with local paths are managed.
But it is still required to define the interface for cases where
other address conventions are supplied.

* URIs based on RFC3986 for local files are resolved to ::

      PWD=/call/position/

      file:///local/filesystem/path => /local/filesystem/path 

  When this is literally a valid filename, the following could be applied ::

      PWD=/call/position/

      ./file:///local/filesystem/path => /call/position/file:/local/filesystem/path 
    
* Linux and UNIX:

  * IEEE Std 1003.1(TM), 2013 Edition; Chapter 4.12 ::

	    //hostname/local/filesystem/path

    The current version treats this literally, as a pathname, thus normally
    fails. The caller has to provide appropriate local filenames to local only
    interfaces.

    **REMARK**: When introducing remote filesystem support, this will be adapted.

    The behaviour could be changed by call parameter.

    * Ignore
        ::

	      //hostname/local/filesystem/path => /hostname/local/filesystem/path 

  * SMBFS:

    The anononymous case of SMB/CIFS without required authentication is handled
    by the case depicted before. 

    The additional cases where additional hostname parameters are reuquired are
    following in a later step.

 
* Microsoft(TM) Windows:

  * Network shares ::

	    \\hostname\local\filesystem\path

    Similar behaviour as depicted before for the compliance to the 
    IEEE-1003.1 standard.

    The behaviour could be changed by call parameter.

    * Ignore
        ::

	      \\hostname\local\filesystem\path => \hostname\local\filesystem\path

* Mac-OS:

  * Current same as for Linux/Unix.

Any other input format is simply ignored, and may lead to unpredictable behaviour. 
E.g. ::

    http://path/name => http:/path/name
 
Because this could actually be a valid local filename.

.. _SYNTAXELEMENTS:

Syntax Elements
===============

The syntax elements for the normalization of pathnames are in particular 
essential for the treatment of the filesystem structure as a class and object
hierarchy.
Thus the behaviour has to be defined thoroughly from the beginning, even or
better in particular in case of the foreseen evolutionary add-on extension.  

The current release provides the following syntax, *successive compatible extensions are going to follow soon*.
These the processing of the provided syntax is designed in two layers in accordance to common examples.

The lower layer provides the syntax elements to construct a pathname for local access, whereas the upper layer
provides the information for the location of remote filesystems.

.. image:: _static/pathname_types.png
   :width: 550 

Thus the functions of the lower layer:

* `escapepathx`_
* `unescapepathx`_

are similar to the system function 'os.path.normpath',
Whereas the functions of the upper layer:

* `splitapppathx`_
* `splitapppathx_getlocalpath`_

Assembles a tuple of components into a path name for access.

The escape and unescape funtions work basically similar to 'os.path.normpath'.
The behaviour is:

* `escapepathx`_

  Escape backshlashes only, consider specific control characters recognized by the 're' module.
  Any arbitrary number of seperator characters are normalized appropriately, including shares.

* `unescapepathx`_

  Unescape, this simply reverses the escape of a single character.
  Thus in particular the eventual normalization of 'escapepathx' for multiple present
  seperators is not reverted. 

.. _escapepathx: pyfilesysobjects.html#filesysobjects.pathtools.escapepathx
.. _unescapepathx: pyfilesysobjects.html#filesysobjects.pathtools.unescapepathx
.. _splitapppathx_getlocalpath: pyfilesysobjects.html#filesysobjects.pathtools.splitapppathx_getlocalpath
.. _splitapppathx: pyfilesysobjects.html#filesysobjects.apppaths.splitapppathx

The following function hierarchy for pathname conversion including UNC, SMB, POSIX-Apps, and local filenames is supported.

.. image:: _static/pathname_functions.png 
   :width: 600 

Anyhow, due to some specific poosition dependent interpretation of the
'os.sep' the lower layer has encoded the app specific knowledge into the
'escapepathx' routine.
This also normalizes the 'os.sep' by conversion and elimination of 
neutral repetitons as well as special semantics of '.' and '..'

A single pathname is hereby represented by the syntax, 
where 'cifs==smb': ::

    filesystemNodeName := (
       pathname + SEP + filename
       | pathname [ + SEP ]
       | [ SEP ] + filename
       | SEP
    )

    pathname := [ PREFIXKEY ] + dirname [ + SEP + pathname ]
    dirname := <valid-name-of-dir-node> 
    filename := <valid-name-of-file-node>

    <valid-name-of-dir-node> := <valid-name-of-dir-node> [ + SEP$ ]

    PREFIXKEY := (
         'file:///' + 2SEP + SPECIALNODE + varSEP + share-name 
       | 'file://'
       | 'smb://' + SPECIALNODE + varSEP + share-name
       | DRV
       | 2SEP  SPECIALNODE  [varSEP]
       | nSEP       
    )
    DRV := [a-z] + ':'   # On MS-Windows
    SPECIALNODE := (
       <networknode-access>
    )
    share-name := (
       1*80pchar  # see [MS-DTYP]
    )
    <networknode-access> := [^SEP]+
    varSEP := ( '' | 1SEP | 2SEP | nSEP )
    1SEP = ^SEP + !SEP
    2SEP = ^SEP + SEP + !SEP       # in accordance to IEEE Std 1003.1 and/or CIFS/SMB
    nSEP = ^SEP + SEP + SEP + SEP* # more than 2xSEP
    SEP := <OS-specific-seperator>
    <OS-specific-seperator> := ( '/' | '\' ) # for now only two are known

    SPECIAL_SYNTAX_DIAGRAM_CHARS_AND_REGEXPR := { 
       '^', '$', '!', '+', '{', '}', '[', ']', ':=', '|', '<', '>', '#' 
    }

The seperator commonly used in this document is '/'. This could be interchaned by
the seperator '\\', which also defines an escape character, thus is omitted when not
required.

The above syntax definition provides just a subset but very common set of possible naming schemes, 
additional may be supported in future versions.

For further details refer to:

* **UNC**: Common definition in [MS-DTYP]_: Windows Data Types - Chap. 2.2.57 UNC; 
  Microsoft Inc. ::

      UNC               = "\\" host-name "\" share-name [ "\" object-name ]
      host-name         = "[" IPv6address ‘]" / IPv4address / reg-name
         ; IPv6address, IPv4address, and reg-name as specified in [RFC3986]
      share-name        = 1*80pchar
      pchar             = %x20-21 / %x23-29 / %x2D-2E / %x30-39 / %x40-5A / %x5E-7B / %x7D-FF
      object-name       = *path-name [ "\" file-name ]
      path-name         = 1*255pchar
      file-name         = 1*255fchar [ ":" stream-name [ ":" stream-type ] ]
      fchar             = %x20-21 / %x23-29 / %x2B-2E / %x30-39 / %x3B / %x3D / %x40-5B / %x5D-7B
      /                         %x7D-FF
      stream-name       = *schar
      schar             = %x01-2E / %x30-39 / %x3B-5B /%x5D-FF
      stream-type       = 1*schar

* **file://**: The file URI Scheme - RFC8089 [RFC8089]_, 
  draft-kerwin-file-scheme-13 [URISCHEME]_ ::

      file-URI         = f-scheme ":" f-hier-part [ "?" query ]

      f-scheme         = "file"

      f-hier-part      = "//" auth-path
                       / local-path

      auth-path        = [ f-auth ] path-absolute
                       / unc-path
                       / windows-path

      f-auth           = [ userinfo "@" ] host

      local-path       = path-absolute
                       / windows-path
      unc-path         = 2*3"/" authority path-absolute

      windows-path     = drive-letter path-absolute
      drive-letter     = ALPHA [ drive-marker ]
      drive-marker     = ":" / "|"

* **smb://**: [MS-SMB]_: Server Message Block (SMB) Protocol; Microsoft Inc.
  The current implemented name resolution is a limited version of the file scheme.
  Thus based on "SMB File Sharing URI Scheme - draft-crhertel-smb-url-07".
  This is outdated, but for now the first attempt for start. ::

      smb_URI        = ( smb_absURI | smb_relURI )
      smb_absURI     = scheme "://" smb_service [ "?" [ nbt_context ] ]
      smb_relURI     = abs_path | rel_path

      scheme         = "smb" | "cifs"
      smb_service    = ( smb_browse | smb_net_path )

      smb_browse     = [ smb_userinfo "@" ] [ smb_srv_name ]
                         [ ":" port ] [ "/" ]
      smb_net_path   = smb_server [ abs_path ]

      smb_server     = [ smb_userinfo "@" ] smb_srv_name [ ":" port ]

      smb_srv_name   = nbt_name | host
      nbt_name       = netbiosname [ "." scope_id ]
      netbiosname    = 1*( netbiosnamec ) *( netbiosnamec | "*" )
      netbiosnamec   = ( alphanum | escaped  | ":" | "=" | "+" | "$" |
                         "," | "-" | "_" | "!" | "~" | "'" | "(" | ")" )
      scope_id       = domainlabel *( "." domainlabel )

      smb_userinfo   = [ auth_domain ";" ] userinfo_nosem
      auth_domain    = smb_srv_name
      userinfo_nosem = *( unreserved | escaped |
                         ":" | "&" | "=" | "+" | "$" | "," )

      nbt_context   = nbt_param *(";" nbt_param )

      nbt_param     = ( "BROADCAST=" IPv4address [ ":" port ]
                      | "CALLED=" netbiosname
                      | "CALLING=" netbiosname
                      | ( "NBNS=" | "WINS=" ) host [ ":" port ]
                      | "NODETYPE=" ("B" | "P" | "M" | "H")
                      | ( "SCOPEID=" | "SCOPE=" ) scope_id
                      )


 
* **cifs://**:  [MS-CIFS]_: Common Internet File System (CIFS) Protocol; Microsoft Inc.

  For now see SMB.

This syntax represents e.g. the following valid filepathanmes with the 
current position(PWD) as reference point for relative positions.
For the conversion API refer to
*splitapppathx*
`[docs] <pyfilesysobjects.html#filesysobjects.apppaths.splitapppathx>`_
`[source] <_modules/filesysobjects/pathtools.html#splitapppathx>`_
and 
*splitapppathx_getlocalpath*
`[docs] <pyfilesysobjects.html#filesysobjects.pathtools.splitapppathx_getlocalpath>`_
`[source] <_modules/filesysobjects/pathtools.html#splitapppathx_getlocalpath>`_
. ::

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

    #REMARK: Looking forward for qualified review comments!!!


.. _VARIANTSPATHNAMEPARAMS:

Variants of Pathname Parameters - Literals, RegExpr, and Glob
=============================================================

The common variants of pathnames as parameters are provided by one of 
the categories:

* Literal - literal names

  The applicability varies on the scope.
  Whereas literals could be applied in any scope, these are the least flexible
  search pattern.
  These just provide native matches either on single nodes, or single goups
  in case of directories represented as containers. 

* Regular Expression - specific match pattern, which are implementation dependent

  The regular expressions in general are part of applications, either special 
  autonomous conversion filters, or embedded into a greater application,
  and/or programming environment.

  These are strongly implementation dependent, even though a broad commen set 
  is generally provided. These in particular lack the native support of 
  filesystems, thus could be only used as input and/or output filters.

* Glob - platform dependent native filesystem match

  The 'glob' expressions are a very basic type of regular expressions, which are
  platform dependent.
  These could be applied at the interface of the filesystems, and influence the
  responce of the filesystem interface directly.
  
  Globs can span multiple levels of directory paths. ::

    r"a[0-9]*/[!xy]*/???/*"

  Use e.g. the following patterns to restrict on a single node name: ::

    os.sep+r"a*b"+os.sep
    os.sep+r"a*b"

* Semi-Literal - literal names combined with glob, or regexpr

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
Therefore a multi-level approach is reuqired  `[API] <shortcuts.html#>`_ 
`[UseCases] <usecases.html#>`_ when these has to be applied onto the results of
a filesystem search.
The workflow in case of required searches for unknown filesystem nodes by 
re-patterns is:

  #. filter and collect filesystem entries by 'literal' and 'glob' parameters

  #. post-filter the collected set by  'literal' and 'RegExpr' type parameters.


.. _CALLPARAMSAPI:

Call Parameters of the API
==========================

The call interface provides for groups of functions and classes with a set of 
common parameters and additional context specific modifications.

The provided function sets comprise the categories:

* Filesystem Positions and Navigation

* Canonical Node Address - Current: *Experimental / Non-Productive*

For the list of the interfaces refer to `[API] <shortcuts.html#>`_.

Filesystem Positions and Navigation
-----------------------------------

**SYNOPSIS** `[API] <shortcuts.html#>`_

  * manage search paths - checks filesystem

    .. code-block:: python
       :linenos:

       addpath_to_searchpath(spath,plist=None,**kargs)
       clearpath(plist=None,**kargs)
       set_uppertree_searchpath(start=None,top=None,plist=sys.path,**kargs)

  * search for files, directories, and branches - checks filesystem

    .. code-block:: python
       :linenos:

       findrelpath_in_searchpath(spath,plist=sys.path,**kargs)
       findrelpath_in_searchpath_iter(spath,plist=sys.path,**kargs)
       findrelpath_in_uppertree(spath,start=None,top=None,**kargs)
       findpattern(*wildcards, **kargs)

  * match files, directories, and branches into path strings - works on strings only

    .. code-block:: python
       :linenos:

       gettop_from_pathstring(start,plist=sys.path,**kargs)
       gettop_from_pathstring_iter(start,plist=sys.path,**kargs)


**DESCRIPTION**:

The filesystem navigation functions provide for the preparation of search
paths and the location of files and directories based on the created lists.
The default list is 'sys.path'.

The package provides for the file system search path operations the management
and application of filesystem search operations.
This supports multiple independent search path sets by the categories of functions:

* manage search paths

  * add paths to search lists 
    `[docs] <pyfilesysobjects.html#filesysobjects.pathtools.addpath_to_searchpath>`_
    `[source] <_modules/filesysobjects/pathtools.html#addpath_to_searchpath>`_

    .. code-block:: python
       :linenos:

       filesysobjects.addpath_to_searchpath(spath,plist=None,**kargs)

  * clear search paths 
    `[docs] <pyfilesysobjects.html#filesysobjects.pathtools.clearpath>`_
    `[source] <_modules/filesysobjects/pathtools.html#clearpath>`_

    .. code-block:: python
       :linenos:

       filesysobjects.clearpath(plist=None,**kargs)

  * set tsearch lists for path segments 
    `[docs] <pyfilesysobjects.html#filesysobjects.pathtools.set_uppertree_searchpath>`_
    `[source] <_modules/filesysobjects/pathtools.html#set_uppertree_searchpath>`_

    .. code-block:: python
       :linenos:

       filesysobjects.set_uppertree_searchpath(start=None,top=None,plist=sys.path,**kargs)

* search for files, directories, and branches

  * find relative paths on lists of search paths
    `[docs] <pyfilesysobjects.html#filesysobjects.pathtools.findrelpath_in_searchpath>`_
    `[source] <_modules/filesysobjects/pathtools.html#findrelpath_in_searchpath>`_

    .. code-block:: python
       :linenos:

       filesysobjects.findrelpath_in_searchpath(spath,plist=sys.path,**kargs)

  * iterator for search
    `[docs] <pyfilesysobjects.html#filesysobjects.pathtools.findrelpath_in_searchpath_iter>`_
    `[source] <_modules/filesysobjects/pathtools.html#findrelpath_in_searchpath_iter>`_

    .. code-block:: python
       :linenos:

       filesysobjects.findrelpath_in_searchpath_iter(spath,plist=sys.path,**kargs)

  * search filesystem segments 
    `[docs] <pyfilesysobjects.html#filesysobjects.pathtools.findrelpath_in_uppertree>`_
    `[source] <_modules/filesysobjects/pathtools.html#findrelpath_in_uppertree>`_

    .. code-block:: python
       :linenos:

       filesysobjects.findrelpath_in_uppertree(spath,start=None,top=None,**kargs)

  * search file system trees
    `[docs] <pyfilesysobjects.html#filesysobjects.pathtools.findpattern>`_
    `[source] <_modules/filesysobjects/pathtools.html#findpattern>`_

    .. code-block:: python
       :linenos:

       filesysobjects.findpattern(*wildcards, **kargs)

* match files, directories, and branches into path strings

  * match a pathname string into a path from a list of search paths 
    `[docs] <pyfilesysobjects.html#filesysobjects.apppaths.gettop_from_pathstring>`_
    `[source] <_modules/filesysobjects/pathtools.html#gettop_from_pathstring>`_

    .. code-block:: python
       :linenos:

       filesysobjects.gettop_from_pathstring(start,plist=sys.path,**kargs)

  * iterate on search paths
    `[docs] <pyfilesysobjects.html#filesysobjects.apppaths.gettop_from_pathstring_iter>`_
    `[source] <_modules/filesysobjects/pathtools.html#gettop_from_pathstring_iter>`_

    .. code-block:: python
       :linenos:

       filesysobjects.gettop_from_pathstring_iter(start,plist=sys.path,**kargs)


**OPTIONS**:

Various common options are supported, which may not be available for each interface.
 
* spath

  Search path, either to be added to the search list,
  or to be find in a earch list.

* start

  Start position for search and collect operations.
  This is within the file hierarchy the 'deeper' position
  under 'top'.

* top

  The top position where the search and collect operations
  are terminated.

* plist

  A path list for search operations, default is 'sys.path'.

* **kargs

  Various apperently applied parameters.

  * matchidx=#num:

    Increment of matched path component for a path. The counter
    is for a single path, thus reset for each of a path list.
    The valid range is {0..}

    The counter begins from top, so #num(1) will match M(1) in ::
                
        /a/b/M/c/M/d/M/w/e/M/bottom
             0   1   2     3
                 |   *
                 |
                 `-default

  * reverse: 

    This reverses the resulting search order from bottom-up
    to top-down.

Canonical Node Address
----------------------

For now experimental and non-productive, for review and comments `[API] <shortcuts.html#>`_: ::

    filesysobjects.NetFiles.normpathx

For syntax design requirements refer to "`Extended Filesystems - Network Features <path_netfiles.html>`_".

See also Python issue:

* Issue 26329: os.path.normpath("//") returns //
  - http://bugs.python.org/issue26329




