'filesysobjects.paths' - Module
===============================

The *filesysobjects.paths* module provides advanced operations on paths and search paths.

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

Common Call Parameters
^^^^^^^^^^^^^^^^^^^^^^
appre
"""""
keepsep
"""""""
pathsep
"""""""
strip
"""""
Strips null-entries.

default := True

stripquote
""""""""""
Strips special Python style *filesysobject* triple-quotes. ::

   /my/path/with/"""double-quoted"""/dirs => /my/path/with/double-quoted/dirs
   /my/path/with/'''single-quoted'''/dirs => /my/path/with/single-quoted/dirs 

Current version does not support nested triple-quotes, neither homogeneous,
nor heterogeneous.

spf
"""
Source platform, defines the input syntax domain.
For the syntax refer to API in the manual at :ref:`spf <OPTS_SPF>`.
For additional details refer to
:ref:`tpf and spf <TPF_AND_SPF>`,
`filesysobjects.getspf() <filesysobjects_init.html#getspf>`_,
`filesysobjects.gettpf() <filesysobjects_init.html#gettpf>`_,
`paths.normpathx() <paths.html#def-normpathx>`_,
`paths.splitpathx() <paths.html#splitpathx>`_,
and
:ref:`apppaths.normapppathx() <def_normapppathx>`,

default := *RTE* 

tpf
"""
Target platform. 
For the syntax refer to API in the manual at :ref:`tpf <OPTS_TPF>`.
For additional details refer to
:ref:`tpf and spf <TPF_AND_SPF>`,
`filesysobjects.getspf() <filesysobjects_init.html#getspf>`_,
`filesysobjects.gettpf() <filesysobjects_init.html#gettpf>`_,
`paths.normpathx() <paths.html#def-normpathx>`_,
`paths.splitpathx() <paths.html#splitpathx>`_,
and
:ref:`apppaths.normapppathx() <def_normapppathx>`,

default := *spf* ( == *RTE*)

.. role:: raw-html(raw)
   :format: html

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

Module
------

.. automodule:: filesysobjects.paths

Constants
---------

.. note::

   The displayed numeric values for the enums are for debugging support only
   and may change apperantly, use the symbolic names only.

Simple Path Scanner - Parser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The scanner and parser for file path name rules in accordance to  
Posix/IEEE-1003.1 and NTFS/FAT path name specifications.
Adds some minor causal constraints on esoteric cases for ambiguity resolution.

The base for the path compilers of *filesysobjects.paths.normpathx*,
*filesysobjects.paths.splitpathx*, *filesysobjects.paths.escapepathx*,
and the *filesysobjects.paths.unescapepathx*.

* **PATHSCANNER**

  Generic tokenizer for file path names, supports Posix/IEEE-1003.1
  and NTFS/FAT path names.

* **Control Constants - Tokens**:

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

* **Context Maps**:

  * *ASCII_SC_CTRL*

    Map matche groups to appropriate control tokens.

* **Scanner - Parser Registry**

  Set of current registered scanners - parsers.
  To be used for *re* functions.

  .. code-block:: python
     :linenos:

     sub_path_calls = {  #: vector for escaping and normalization
        'b': sub_win,
        'k': sub_keep,
        'keep': sub_keep,
        'posix': sub_posix,
        's': sub_posix,
        'uri': sub_posix,
        'win': sub_win,
        'win32': sub_win,
     }


Miscellaneous
^^^^^^^^^^^^^
* *_CPSPLIT* - static compiled: split pathnames with literal + glob + regexpr.
* *_ENV_SPLIT* - Split-out environment variables for substitution.
* *_ENV_SPLITg* - Entry points into sub strings environment variables and literals.

Functions
---------

escapepathx
^^^^^^^^^^^
.. autofunction:: escapepathx

.. _def_normpathx:

normpathx
^^^^^^^^^
.. autofunction:: normpathx

.. _def_splitpathx:

splitpathx
^^^^^^^^^^
.. autofunction:: splitpathx

splitpathx_posix
^^^^^^^^^^^^^^^^
.. autofunction:: splitpathx_posix

splitpathx_win
^^^^^^^^^^^^^^
.. autofunction:: splitpathx_win

sub_esc
^^^^^^^
.. autofunction:: sub_esc

sub_keep
^^^^^^^^
.. autofunction:: sub_keep

sub_posix
^^^^^^^^^
.. autofunction:: sub_posix

sub_unesc
^^^^^^^^^
.. autofunction:: sub_unesc

sub_win
^^^^^^^
.. autofunction:: sub_win

unescapepathx
^^^^^^^^^^^^^
.. autofunction:: unescapepathx

Exceptions
----------

PathException
^^^^^^^^^^^^^
.. autoclass:: PathException

PathTargetAccessException
^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: PathTargetAccessException
