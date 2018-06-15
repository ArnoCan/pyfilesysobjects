The SW-Design of *filesysobjects*
*********************************

The 'filesysobjects' package provides address calculations for the simplified navigation in 
local and remote filesystem hierarchies.
This comprises functions for the application of object oriented patterns 
onto files, directories, and branches by various notations including multiple protocols.
In general - the application of object oriented concepts combined with advanced search patterns
onto cloud and web based distributed resources.

The support of multiple platforms in particular spans Posix based filesystems and Windows based filesystems,
which use different characters as separators for path names and search path variables.
Additionaly - even worst - the path name separator ‘\\’ is also the escape character on both platforms. 
This restricts in some cases the applicability of the provided common variables ‘os.pathsep‘ 
and ‘os.path.sep‘(no typo :*) ), and even leads to cases of ambiguity.

Extensions exist in addition to the simple local file address, which provide for application 
prefixes - for example for shares, network mounts, and URI/URL. A common issue arises here in 
particular when shared filesystems are accessed by clients and servers via various access paths. 
This is due to the common fact, that the filesystem is transparently used by various clients
operating on different OS. Again, modern applications work transparently for local and distributed 
applications, provide the transparent processing of file names - resource identifiers - provided 
by various formats and semantics. For local applications as well as distributed applications - in 
general for cloud applications including their management and infrastructure interfaces.

The filesysobjects API adds this features to the standard libraries by introducing an abstract 
address layer.

|filesysobjectcomponents|
|filesysobjectcomponents_zoom|

.. |filesysobjectcomponents_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/filesysobject-components.png
   :width: 16

.. |filesysobjectcomponents| image:: _static/filesysobject-components.png
   :width: 600

.. note::

   Although network file systems are treated as local by the most OSs once they are mounted/shared,
   these still encounter some limits due to their nature.
   The probably most prominent limits are the restriction of the number of access groups on mounted
   NFS(3), and the handling of so called symbolic links, which even led to the default of the prohibition
   of sharing mounted NFS filesystems by VirtualBox as '*vboxfs*' / '*shared folders*'
   (REMARK: which does not imply the agreement of the author/acue).
   
   Despite the potentially relevant lacks of NFS based mounts, the SMB/CIFS access via Samba [SAMBA]_ 
   based mounts of '*shared folders*' works flawless and is supported by VirtualBox [VIRTUALBOX]_ .
   This is on the other hand a security aspect of the SMB server, and requires of course additional
   processing resources.

The addressing support also introduces the common canonical representation for 
the supported platforms.
The overall major advances introduced by the *filesysinfo* are:

* **Gears for Filesystem Objects - Files, Directories, and Branches**

  The package provides a set of basic functions for implementing file system items 
  conceptually as classes and objects. Just a few interfaces are required in order to represent 
  some basic OO features on filesystems. This in particular comprises superposition 
  and encapsulation, polymorphism, class and object hierachies.

  * Filesystem elements as classes and objects with multiple search and iteration sets 
    [:ref:`details <FILESYSELEMASOBJECTS>`]
  * Standards compliant path support for the local and remote native access onto multiple platforms 
    [:ref:`details <SYNTAXELEMENTS>`]
    [`examples <path_syntax_examples.html>`_]
  * Programming Interface 
    `[API] <shortcuts.html#filesysobjects-pathtools>`_,
    `[UseCases] <usecases.html>`_.
    .

* **Manage multiple search lists and support 're' and 'glob' for path search**

  Provides the creation and usage of multiple search paths including the
  full scale pattern matching on search paths by '*re*' and '*glob*' 
  [:ref:`details <SYNTAXELEMENTS>`]

* **Iterators and Context Manager**

  Provides in combination with *re* and *glob* the iteration over resource trees
  [:ref:`details <SYNTAXELEMENTS>`]

* **Yet another attempt for file address processing on network storage - just the beginning...**

  Evaluation for an extension modul of the interface '*os.path.normpath*'.
  Thus the function is named for now '*filesysobjects.netfiles.normpathx*'.

  * `Extended Filesystems - Network Features <path_netfiles.html>`_
      .

The current release of the package *filesysobjects* contains the following components.

|layersmodules|
|layersmodules_zoom|

.. |layersmodules_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/layers-modules.png
   :width: 16

.. |layersmodules| image:: _static/layers-modules.png
   :width: 550

* '*apppaths*' - resolution and processing of application resource paths, with optional *globs* and *re* 
* '*configdata*' - file system locations of configuration files
* '*netfiles*' - still experimental
* '*osdata*' - file system locations of system directories
* '*paths*' - resolution and processing of file system paths, with optional *globs* and *re* 
* '*pathtools*' - dynamic sets of file system paths by search and filtering with *globs* and *re* 
* '*userdata*' - file system locations of user data

Last but not least the common interface finally saves development efforts as well
as enhances the overall performance by a centralized and neat library. In particular enhances
the quality by well tested interfaces covering the various special cases with more 
than 4500 test cases included into filesysobjects - at the time of writing.

For further information on concepts, workflows, and the API see
:ref:`'Shortcuts' <shortcs>`

For related projects adding transparent access by file-like objects and IOStreams
with additional support for pipes, sockets, and serial ports refer
to [asnoio]_ and [iobricks]_. 


.. image:: _static/pathname_types.png
   :width: 500 

The following function hierarchy for pathnames is supported.

.. image:: _static/pathname_functions.png 
   :width: 500 


Resource Paths
==============


Paths and Application Paths
---------------------------
The current version implements a two layered architecture of resource paths.
The lower layer focusses on the context paths, while the upper layer adds application
specific schemes for higher layer functions.
The assigned interfaces are kept similar with specific extensions.

The main focus of the current release is on literally file like resources [PATH]_ and 
associated common standards like [PATHVAR]_. The overall concept is designed
to support almost arbitrary application paths based on URIs, which is going to be 
extended within the next releases. 

|syntaxdomains|
|syntaxdomains_zoom|

.. |syntaxdomains_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/syntax-domains.png
   :width: 16

.. |syntaxdomains| image:: _static/syntax-domains.png
   :width: 750

Paths
-----
The components of the *paths* module represents a resource location within 
a specific context.
The most common resources are files and directories stored in file systems,
while otheres like Databases, Directory Systems or MIBs store information 
in various storage systems.
Posix based Unix and Linux systems maintain an abstraction layer, which 
transforms the hardware platform representation into the file system by specific nodes.
These filesystem paths actually represent devices and communicate through 
special drivers with the hardware by addressing and accessing file entries.

The target of the *filesysobjects* is to provide a common namebinding scheme
applicable to various resource trees.

The following figure depicts the main interfaces for resource paths.

|pathscomponents|
|pathscomponents_zoom|

.. |pathscomponents_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/path_functions.png
   :width: 16

.. |pathscomponents| image:: _static/path_functions.png
   :width: 650

The types of interface comprise

* *normpathx* - converts a path into it's canonical representation
* *splitpathx* - splits a path into it's segments
* *escapepathx* - escapes special characters within a path
* *unescapepathx* - unescapes special characters within a path

The internal design is based regular expressions provided by Python.
These are provided as a scanner and combined by callbacks into a parser
for multiple platforms.
The tokenizer rules are hereby schared by the provided functions.

The lower path layer provides hereby for multiple types of notations for the
context specific paths.
This also includes special schemes like 'file://' which is just another
syntactical representation of a local or remote file. 
The representation also include virtually local file resources, as these
are locally accessible by local path schemes. 

The current supported types by the path layer are:

+-----------+------------+----------+-------+---------+
| type      | prefix     | host     | share | path    |
+===========+============+==========+=======+=========+
| lfsys     |            |          |       | abspath |
+-----------+------------+----------+-------+---------+
| lfsys     | file://    |          |       | abspath |
+-----------+------------+----------+-------+---------+
| ldsys     | file://    |          | drive | abspath |
+-----------+------------+----------+-------+---------+
| raw       |            |          |       | abspath |
+-----------+------------+----------+-------+---------+
| share     | //, \\\\   | hostname | share | path    |
+-----------+------------+----------+-------+---------+
| share     | file:///// | hostname | share | path    |
+-----------+------------+----------+-------+---------+
| posix-app | //         | hostname |       | abspath |
+-----------+------------+----------+-------+---------+


Application Paths
-----------------
The application layer is designed similarly to the lower context path layer,
as it uses path functions, and adds application level extensions.
 

|apppathscomponents|
|apppathscomponents_zoom|

.. |apppathscomponents_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/apppath_functions.png
   :width: 16

.. |apppathscomponents| image:: _static/apppath_functions.png
   :width: 650

The current supported types by the application path layer are:

+-----------+------------+----------+-------+---------+
| type      | prefix     | host     | share | path    |
+===========+============+==========+=======+=========+
| http      | http/https | hostname |       | path    |
+-----------+------------+----------+-------+---------+
| lfsys     | file://    |          |       | abspath |
+-----------+------------+----------+-------+---------+
| ldsys     | file://    |          | drive | abspath |
+-----------+------------+----------+-------+---------+
| share     | //, \\\\   | hostname | share | abspath |
+-----------+------------+----------+-------+---------+
| share     | file:///// | hostname | share | path    |
+-----------+------------+----------+-------+---------+
| smb       | smb        | hostname | share | path    |
+-----------+------------+----------+-------+---------+
| posix-app | //         | hostname |       | abspath |
+-----------+------------+----------+-------+---------+

Path Tools
----------


Find vs. Expand
===============
The main design target of the *filesysobjects* includes the efficient path resolution
by arbitrary match pattern, which is very close to the search of resource trees with applied
match filters of arbitrary pattern.
While the search algorithms are regularly based on tree walk patterns, the expand algorithms
rely on the step wise expansion of a given pattern.

The *filesysobjects* package supports for the find pattern as well as for the expand pattern
by two basic types of operations:

* *findpattern*

* *expandpath*

Internally both interfaces make use of each other.
The *expandpath* interface starts with a list of provided paths and tries to match these onto potentially 
existing paths within the filesystem.
The *findpattern* interface starts a search operation and filters out matches of provided expressions match pattern.
The final result replied by both interfaces in case of redundant input parameter sets is equal, even though
their intentional applications are different.

The *expandpath* interface is foreseen to resolve present path lists, which has by definition
a more restricted input set, while the *findpattern* interface tries to scan a whole filesystem
for specific file path pattern at arbitrary locations.
The difference of these two approaches is the performance, while this deeply depends on the selected
filter parameters.

The *filesysobjects* internally make use of each other in order to limit the required code, 
and trying to apply the pest-fit algorithm at each stage of the search operations. 
The interface call proceeds hierarchical on the processed resource tree, either a physical
filesystem or any virtual resource storage. Therefore the provided wildcard filters are analysed
and pre-sorted and partially pre-executed in order to continously reduce the part of the 
remaining resource tree pending to be scanned. The actual processing is hereby a cross-over 
recursive filesystem scan of the two interfaces.

While the *findpattern* interface is obviously designed for resource tree searches of wildcard patterns,  
the *expandpath* seems to be more restricted.
This is not true, due to the supported application of regular expressions which are permitted to 
span multiple directory levels. Though the regular expression


Name Resolution and Ambiguity
=============================

The main design target of the *filesysobjects* includes the efficient path resolution
by arbitrary match pattern, which is very close to the search of resource trees with applied
match filters of arbitrary pattern.
Both rely deeply on the parameter sets for their performance.

Another aspect is the partial ambiguity of globs and regexpr, which
in addition is superposed by the different valid character sets of the
various OSs. This is even worst in case of mounted shares between different
OSs. Thus the final resolution of globs and regexpr require actual file system
access in order to reolve the ambiguity.
For wildcard expansion this results in final iterationn on the filesystem,
which could result in large sets of matched nodes. Thus 
it could cost for large sets of nodes a significant amount of performance.

The provided bitmask constants control the applied algorithms.

* **W_LITERAL(0)** - considers the provided expressions as *literal* match-patterns
* **W_GLOB(1)** - considers the provided expressions as *glob*s
* **W_RE(2)** - considers the provided expressions as *re*s
* **W_MIX(4)** - expects an intermixed pattern with *glob*s and *re*s
* **W_MULTIDIR(8)** - spans the regular expression across multiple directories
* **W_RE_FULL(16)** - disables performance optimization, enables re-groups

The following expression demonstrates the issue of name resolution in case of
ambiguity.

.. code-block:: python
   :linenos:

   filepathname = '/path/to/.*[d].*'

The expression is a valid *glob* and a valid *re*
on all platforms - in addition a *literal* on seemingly all platforms too.

* static name resolution

  For a generic path expansion function it is not possible to decide static offline,
  what actually matches.

* dynamic name resolution 

  In case of dynamic name binding resolution it is still not possible to determine accurately,
  which type(s) were intended by the caller. 

The following expressions are handled specifically.

The wildcard expression '.*' has for *glob* and *re* a different semantics.
While the *glob* semantics represent a literal dot followed by arbitrary characters
within a path segment, the regular expression represents an arbirary string.
The application of *re* as a post filter onto file system paths therefore produce
differnet results.  

.. code-block:: python
   :linenos:

   p = /my/path/to/a/b/c

      re:   /.*b  => /my/path/to/a/b
      glob: /.*b  => (empty)

The following regular expression matches as a post-filter on a path string
dependent from the greedy mode differently itself. 

.. code-block:: python
   :linenos:

   p = /.abc/path/to/c/x/c

      re:   /.*c  => /.abc/path/to/c/x/c
      re:   /.*?c => /.abc/path/to/c
      glob: /.*c  => /.abc

Thus the resource path resolution is controlled by the previously listed bitmask constants.
The major difference is hereby the ability to match on path strings, which includes expressions
spanning multiple subdirectories.
Even though this requires some runtime resources, the overall budget is better than using a
piped commandline tool-chain, which in sum requires more resources.
The integrated partial match filter enables the continous match of provided filter expressions, thus
avoids the build of large caches. 

The following defaults are provided:

+--------------+------------+-------------+
|              | expandpath | findpattern |
+==============+============+=============+
| *W_LITERAL*  | x          | x           |
+--------------+------------+-------------+
| *W_GLOB*     | x          |             |
+--------------+------------+-------------+
| *W_RE*       | x          | x           |
+--------------+------------+-------------+
| *W_MIX*      | x          |             |
+--------------+------------+-------------+
| *W_MULTIDIR* | x          | x           |
+--------------+------------+-------------+
| *W_RE_FULL*  |            |             |
+--------------+------------+-------------+

The defaults differ because of the different name resolution algorithms.
While the *expandpath* interface follows provided paths and resolves 
the segments in a top-down method, the *findpattern* performs scan 
of the filesystem and applies match expression patterns onto the 
results of the scan.

The following combinations apply:

#. wildcards = *W_LITERAL*

   Expands user and variables, matches literally.

#. wildcards = *W_GLOB*

   Expands user and variables, matches by *glob*, 
   which includes literal matches.

#. wildcards = *W_RE*

   Expands user and variables, list by *glob* with '*'
   and matches the intermediate results by *re*, 
   which includes literal matches.

#. wildcards = *W_RE | W_GLOB | W_MULTIDIR*

   Expands user and variables, list by *glob* and matches
   by *re*, which includes literal matches.

#. wildcards = *W_RE | W_MULTIDIR*

#. wildcards = *W_RE_FULL*





.. _SEARCHPERFORMANCEOPT:

Search Performance Optimization
===============================
The pathexpansion as well as the findpattern operations require to scan the filesystem
in case of requested wildcard operations for regular expressions.
The cost is here the performance degree, in case of casual use of regular expressions
on large file sets even a significant degredation.
This is for short caused by the internal split of tree-walk and the amount of node names
to be cached for match by *re* expressions.
Therefore by default the flags **W_MULTIDIR(8)** and **W_RE_FULL(16)** are deactivated.
The regular expression in this case work quite similar to *glob* while providing
the extended match syntax of *re* .

The regular expressions as provided by *re* provide for a quite capable and extended
syntax rule set, which includes some pitfalls, when the internal perfmance optimization
is applied. This comprises basically the application of regular expressions spanning 
multiple directories only.
Therefor the *re* syntax is quite moderately constrained in order to still apply
regular expressions spanning multiple directories, but with performance optimization
for potentially larger filesets.

The following syntax elements are broken by the current optimization, thus are not supported.

* groups
* Character classes intermixed with path separators for the specified platform '/', '\\'.
  while the non-targeted works.

The following limitations apply for the use of the *re* syntax when
search optimization is active.

+----------+-------+-------+----------------+----------------+-------+------+
| syntax   | glob  | re    | filesysobjects | filesysobjects | posix | nt   |
|          | valid | valid | opt            | no-opt         |       |      |
+==========+=======+=======+================+================+=======+======+
| [/]      | --    | x     | x              | x              | --    | --   |
+----------+-------+-------+----------------+----------------+-------+------+
| [\\]     | --    | x     | x              | x              | x     | --   |
+----------+-------+-------+----------------+----------------+-------+------+
| [!/]     | --    | x     | x              | x              | x     | x    |
+----------+-------+-------+----------------+----------------+-------+------+
| [^/]     | --    | x     | x              | x              | x     | x    |
+----------+-------+-------+----------------+----------------+-------+------+
| [^ab/cd] | --    | x     | x              | x              | x     | x    |
+----------+-------+-------+----------------+----------------+-------+------+
| [ab/cd]  | --    | x     | --             | x              | --/x  | --/x |
+----------+-------+-------+----------------+----------------+-------+------+
| .*       | x0    | x1    | y0             | y1             | z0    | z1   |
+----------+-------+-------+----------------+----------------+-------+------+
| a |pi| b | --    | x     | --             | x              | z2    | --   |
+----------+-------+-------+----------------+----------------+-------+------+
| (a)      | --    | x     | --             | x              | --    | x    |
+----------+-------+-------+----------------+----------------+-------+------+
| :        | x     | x     | x2             | x2             | x     | --   |
+----------+-------+-------+----------------+----------------+-------+------+


.. |pi| raw:: html

   <code>|</code>


* x0: Valid with literal '.'
* x1: Valid as arbitrary char
* x2: treated as ordinary char
* y0: supports for path segments
* y1: supports for spanning multiple path segments 
* z0: either as wildcard, or as literal
* z1: as wildcard
* z2: either as wildcard, or as literal

.. info:

   The complete path could consist of intermixed *literals*, *glob* and *re*, while
   for the optimized mode with active  **W_MULTIDIR** each segment can contain 
   either *re* or *glob*.

Encoding and Deconding
======================
The filename encoding and decoding is on one hand designed based on 
special characters representing a token for the file name scanners and parsers, 
on the other hand it is targeting a flexible representation in human readable formats.
Therefore in modern environments this makes use of multiple character sets and internaionalization.
This in particular makes excessive use of the character and string encoding and decoding.

The Python representation of strings has changed for Python3, which also effects the used
regular expressions.
For details including writing common code refer to `Filename Encoding and Decoding <python_encode_decode.html#>`_.

Match Syntax of *filesysobjects*
================================
The *filesysobjects* supports almost the complete range of the standard Python *re* expressions within
path segments.

Mixed expressions
-----------------
Due to several redundnacies and potential severe performance impacts, mixed expressions within path
segments are not supported. The intermix with literals is allways supported.

glob
----
The complete scope of *globs* is supported.

re
--
The regular expressions of Python are quite powerful, though these enable various
'dangerous' constructs, which could influence the perfomance devastatingly.
For example the expression

.. code-block:: python
   :linenos:

   arg = '/.*'  # this is a regular expression NOT a glob

matches the whole file system, and would cause of a scan of all node names into the memory.
Thus the pathname expansion by *expandpath* supports the regular expressions for path segments
only.

Any Char
^^^^^^^^
Matches any character of a path segment, supported.

.. code-block:: python
   :linenos:

   arg = tdata + '/b/(.*?)/([cd][.]s.*|[cd][.]p.*)'
                     *****

Groups
^^^^^^
Groups within a a path segment are supported. 

.. code-block:: python
   :linenos:

   arg = tdata + '/b/(.*?)/([cd][.]s.*|[cd][.]p.*)'
                     *   * *                     *
       
Logical OR
^^^^^^^^^^
Logical OR combination of groups and/or expressions within a path segment are provided.

.. code-block:: python
   :linenos:

   arg = tdata + '/b/(.*?)/([cd][.]s.*|[cd][.]p.*)'
                                      *

Character Classe
^^^^^^^^^^^^^^^^
Character classes within path segments are supported.

.. code-block:: python
   :linenos:

   arg = tdata + '/b/(.*?)/([cd][.]s.*|[cd][.]p.*)'
                                ***    *******

Common Options
==============
The major improvement of the standard Python library provided by the *filesysobjects*
is the accurate and easy cross-platform conversion of resource paths.
This is in particular based on the options collected in this chapter.

Two Resolution Layers
---------------------
The overall path resolution is designed as a two-layer architecture, where the first layer
contained in the *filesysobjects.paths* module handles basic local and remote filesystem resources.
The first layer also applies a generic rule for the extraction of the generic UIRs to be processed 
by the following second layer. 
The second layer contained in the *filesysobjects.apppaths* module handles additionally 
concrete URIs and provides a custom dispatcher for specific applications.

Internal String Processing
--------------------------
The internal  string processing of resource addresses is based on 
dynamic parsers impleented with the standard module *re*.
These provide various parameters for the runtime configuration
and adaptation to the source and target platforms.
  
Application Path Resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The scanner and parser for application resource name rules in accordance to  
Posix/IEEE-1003.1 [POSIX]_, UNC [MS-DTYP]_/[MS-SMB]_/[MS-CIFS]_/[FAT]_, URI [RFC8089]_/[RFC3986]_,
and others.
Provides for multiple mixed entries in search-path syntax, 
adds some minor causal constraints on esoteric and rare cases for ambiguity resolution.

The base for the application resource path compilers of *filesysobjects.apppaths.normapppathx*
and *filesysobjects.apppaths.splitapppathx*.

Path Resolution
^^^^^^^^^^^^^^^
The function for string processing are callback functions to be 
used by *re.sub*.
These base on the internal character mapping tables 'ASCII_SC_*'.
This table depicts the actually used input options.

+-----------+----+-----+-----+---------+-------+
| interface | it | spf | tpf | pathsep | strip |
+===========+====+=====+=====+=========+=======+
| sub_keep  | x  |     |     | x       | x     |
+-----------+----+-----+-----+---------+-------+
| sub_posix | x  | x   |     | x       | x     |
+-----------+----+-----+-----+---------+-------+
| sub_win   | x  | x   |     |         | x     |
+-----------+----+-----+-----+---------+-------+
| sub_unesc | x  | x   |     | x       | x     |
+-----------+----+-----+-----+---------+-------+

* *it* - iterator

  The match iterator passed bu *re.sub* 

* *spf* - source platform

  Specifies the source filesystem parameters, 
  selects finally the input application parser
  rules *APPPATHPARSER* or the processing callback
  of the *PATHPARSER*. 

* *tpf* - target platform

  Specifies conversion parameters for the target
  filesystem. The standards of the target platform
  are defined by the selected parser callback.

* *pathsep* - path separator

  Sets the precedence for the path separator independent
  from the source and/or target platform.
  
  E.g. the *NTFS* filesystem supports '*/*' as well as '*\\*',
  but defaults to the latter.

* *strip*

  The boolean control whether to strip the 'null-resulting' characters.

The Design of Scanners and Parsers
==================================
The design of the string analysis of common resource paths is
based on dynamic regular expressions.
These rely on static compiled state machines with dynamic assigned and 
parameterized callbacks for the processing of tokens and syntax elements.
The callbacks are in particularly context aware and track the history.

Application Path Resolution
---------------------------
The base for the application resource path compilers of *filesysobjects.apppaths.normapppathx*
and *filesysobjects.apppaths.splitapppathx*.

.. automodule:: filesysobjects.apppaths

.. role:: raw-html(raw)
   :format: html

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

* **Helper**

  * *_DUMMY*

    .. autodata:: _DUMMY

  * *_NOSEP_COL*

    .. autodata:: _NOSEP_COL

  * *_NOSEP_SEM*

    .. autodata:: _NOSEP_SEM

  * *INVALIDCHARS*

    .. autodata:: INVALIDCHARS


     * *INVALIDCHARSPOSIX*
   
       .. autodata:: INVALIDCHARSPOSIX
   
     * *INVALIDCHARSWIN*
   
       .. autodata:: INVALIDCHARSWIN


Path Resolution
---------------
The path resolution os nased on the common token scanner.
This implements an intermediate abstract token mapping layer in order to
avoid the volatility of relying on the group enumeration of the regualr expressions.  
The parsing is purely implemented by callbacks with dynamic states.

.. automodule:: filesysobjects.paths

.. role:: raw-html(raw)
   :format: html

* **PATHSCANNER**

  The generic path scanner for filesystem paths including RFC8089 and 
  network application of POSIX and shares of UNC.

  .. autodata:: PATHSCANNER


* **ASCII_SC_CTRL**

  .. autodata:: ASCII_SC_CTRL

  The following constants are defined for the dynamic positional remap of
  the token IDs.

  * *SC_BSPAIR(1000)* - '\\' pair
  * *SC_CIFS(1010)* - cifs:
  * *SC_CRMASK(1020)* - masked '\\n'
  * *SC_DOIT(1030)* - out of range
  * *SC_DQUOTED(1040)* - "
  * *SC_DRIVE(1050)* - DOS DRIVE LETTER - OR A DIRECTORY ON POSIX !!!
  * *SC_DRIVENPSEP(1060)* - dos drive letter following n * posix_sep
  * *SC_DRIVENWSEP(1070)* - dos drive letter following n * win_sep
  * *SC_DUMMY(1080)* - for tests
  * *SC_EACHOF(1090)* - assure for each
  * *SC_ESCCHAR(1100)* - '\\[abf...]'
  * *SC_FABS(1110)* - file:///path - absolute path - rfc8089 rfc1738
  * *SC_FILE(1120)* - file:
  * *SC_FMIN(1130)* - file:/path - min rfc8089 - Appendix B
  * *SC_FNONLOCAL(1140)* - file://host/path  non-local - rfc8089 - Appendix B / maps to Posix-App
  * *SC_FSHORT(1150)* - file:<dos-drive>:path - short-form - rfc8089
  * *SC_FUNC(1160)* - file:///// | file://// - share/netapp - rfc8089 - Appendix E.3.2
  * *SC_HTTP(1170)* - http:
  * *SC_KEEP(1180)* - keep literally
  * *SC_MASKALL(1190)* - keep literally
  * *SC_NULLDIR(1200)* - '/./'
  * *SC_PAPP(1210)* - Posix-Net-App  * 2 * '/' + posix-rules + "causal constraints" 
  * *SC_PDOM(1220)* - '//' share/posix-app - 2 * '/' + domain-rules
  * *SC_PSEPP(1230)* - ':'
  * *SC_PSEPW(1240)* - ';'
  * *SC_REPLACE(1250)* - replace an equal set of chars e.g. '/' or '\\'
  * *SC_SEPP(1260)* - n * Posix path.sep
  * *SC_SEPW(1270)* - 1 * win path.sep
  * *SC_SLASH(1280)* - '/'
  * *SC_SLASHPREB(1290)* - '\\' + '/' 
  * *SC_SMB(1300)* - smb:
  * *SC_SQUOTED(1310)* - '
  * *SC_TOEVEN(1320)* - assure count is even
  * *SC_U16(1330)* - unicode-16
  * *SC_U16R(1340)* - unicode-16 raw
  * *SC_U32(1350)* - unicode-32
  * *SC_U32R(1360)* - unicode-32 raw
  * *SC_UNC(1370)* - unc:
  * *SC_UPDIR(1380)* - '/../'
  * *SC_WDOM(1390)* - Win-Domain - 2 * '\\' + domain-rules
  * *SC_CHRCLSSTART(1400)*
  * *SC_CHRCLSEND(1410)*
  * *SC_ANYONECHR(1420)*
  * *SC_ESCAPEDSQUOT(1430)*
  * *SC_ESCAPEDDQUOT(1440)*
  