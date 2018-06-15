'filesysobjects.__init__' - Module
==================================

Module
------

.. automodule:: filesysobjects.__init__

Constants
---------

.. note::

   The displayed numeric values for the enums are for debugging support only
   and may change apperantly, use the symbolic names only.

Python Version
^^^^^^^^^^^^^^
.. index::
   pair: Python; V3K
   pair: Python; ISSTR
   pair: Python; unicode

* **V3K**: Python3.5+, else Python2.7
* **ISSTR**: string and unicode for type comparison
* **unicode**: for Python3, remaps *unicode* to *str*

.. _ENUM_PLATFORM:

Platform Definitions
^^^^^^^^^^^^^^^^^^^^
The internal representation of the platform parameter is an *int* used 
as bit-array for binary logic operations.
The most interfaces support the bit-array representation as well as the
alternatively string name macros as defined by the *sys.platform* interface.
The bit-mask representation sould be preferred, but requires the import
of *filesysobjects*, while the string macros just require the import
of the interfaces. These may also provide advace when used for custom
types or resource paths, e.g. *SNMP*.


Structure of Bit-Masks
""""""""""""""""""""""
The predefined bitmasks are provided as a label of form *RTE_<name>*, which covers
the grouping of bit-mask blocks and the increments within these groups.
The comitted **interface** is the **NAMED ENUMERATION only**, **NOT the numeric value**.
Therefore the values must never be accessed explicitly. 

The general algorithm of the calculation for the bit-mask is a combination of
category bit-masks for bit-blocks and the addition of sub-blocks for context-bitmasks
for the family grouping it's members.
This combines the performance of logical bit-operations with the reduction of the number
of required bits.
This is required due to the vast number of combinations, which else would lead to  
bit arrays of astronomical dimensions. 

The current implementation covers all major - practically almost all - filesystems, UNC, 
and URI resources with a required number of 15-bits, where the 16-th is reserved for future use.
Thus may fit also to 16-bit based platforms such as embedded systems.
This provides more than 30.000 variants platforms for resource paths, which seems future proof.

Bit-Mask Definitions
""""""""""""""""""""
The following additional definitions are introduced.

* The following aliasses are defined in addition:

  +----------------+---------+
  | *sys.platform* | *alias* |
  +================+=========+
  | win32          | win     |
  +----------------+---------+
  | darwin         | osx     |
  +----------------+---------+

* The bit-mask provides the bit for the OS as well as the bit for the 
  base category and the family.  
  The masks contain the actual runtime environment of the execution platform
  as well as the virtual runtime environment of the resource path.
  The values representing the platform could be used as source and target platform. 

  +---------------+----------------+-------------+---------------------------+
  | Syntax Domain | *sys.platform* | Category    | Family                    |
  +===============+================+=============+===========================+
  | Windows       | win            | RTE_WIN32   | RTE_WIN32                 |
  +---------------+----------------+-------------+---------------------------+
  | Cygwin        | cygwin         | RTE_POSIX   | RTE_CYGWIN                |
  +---------------+----------------+-------------+---------------------------+
  | Linux         | linux, linux2  | RTE_POSIX   | RTE_LINUX                 |
  +---------------+----------------+-------------+---------------------------+
  | Solaris       | sunos          | RTE_POSIX   | RTE_SOLARIS               |
  +---------------+----------------+-------------+---------------------------+
  | BSD           | bsd            | RTE_POSIX   | RTE_BSD                   |
  +---------------+----------------+-------------+---------------------------+
  | OS-X          | darwin         | RTE_POSIX   | RTE_OSX                   |
  +---------------+----------------+-------------+---------------------------+
  | UNC           | n.a.           | RTE_UNC     | RTE_OSX                   |
  +---------------+----------------+-------------+---------------------------+
  | URI           | n.a.           | RTE_URI     | all URIs with schemes     |
  +---------------+----------------+-------------+---------------------------+
  | GENERIC       | n.a.           | RTE_GENERIC | abstract representation,  |
  |               |                |             | network, local, and drive |
  +---------------+----------------+-------------+---------------------------+

  For example the *RTE_FILEURI* defines the URI in accordance to [RFC8089]_
  for the data environment, while the the actual runtime execution environemnt
  could be e.g. *RTE_WIN32* or *RTE_LINUX*. 
  When the execution environment bit is provided only, the major filesystem type
  is set for the resource path type.

.. index::
   pair: platform; RTE
   pair: platform; RTE_BSD
   pair: platform; RTE_CYGWIN
   pair: platform; RTE_DARWIN
   pair: platform; RTE_FILEURI
   pair: platform; RTE_FILEURI0
   pair: platform; RTE_FILEURI4
   pair: platform; RTE_FILEURI5
   pair: platform; RTE_FTP
   pair: platform; RTE_GENERIC
   pair: platform; RTE_GIT
   pair: platform; RTE_HTTP
   pair: platform; RTE_HTTPS
   pair: platform; RTE_LDAP
   pair: platform; RTE_LINUX
   pair: platform; RTE_NFS
   pair: platform; RTE_OSX
   pair: platform; RTE_PKCS11
   pair: platform; RTE_POSIX
   pair: platform; RTE_RSYNC
   pair: platform; RTE_SMB
   pair: platform; RTE_SNMP
   pair: platform; RTE_SOLARIS
   pair: platform; RTE_SSH
   pair: platform; RTE_TFTP
   pair: platform; RTE_UNC
   pair: platform; RTE_URI
   pair: platform; RTE_VNC
   pair: platform; RTE_WIN32
   pair: platform; RTE_XMPP

* Enum Values:

  * Base type blocks:

    * **RTE_CYGWIN** - **cygwin**: Cygwin [CYGWIN]_
    * **RTE_POSIX** - **posix**: Posix systems using *fcntl* [POSIX]_.
    * **RTE_WIN32** - **win**: All Windows systems [MS-DTYP]_
    * **RTE_UNC** - **unc**: UNC [MS-DTYP]_

      With back-slash '\\\\': ::

         \\\\path\to\file

    * **RTE_URI**: URI - [RFC3986]_
    * **RTE_GENERIC**: Undefined platform for special cases

    .

  * POSIX base system platforms with implied filesystem resource path types:

    * **RTE_BSD** - **bsd**: BSD, - OpenBSD, FreeBSD, NetBSD - as Posix system [POSIX]_.
    * **RTE_DARWIN** - **darwin**: Darwin/OS-X, as Posix system [POSIX]_, no macpath-legacy.
    * **RTE_LINUX** - **linux**: Linux with specific add-ons - OS, DIST, GNU - as Posix system [POSIX]_.
    * **RTE_OSX** - **osx**: Darwin/OS-X, as Posix system [POSIX]_, no macpath-legacy.
    * **RTE_SOLARIS** - **solaris**: UNIX/Solaris, as Posix system [POSIX]_.

    .

  * Virtual runtime domains of specific resource path syntax:

    * **RTE_FILEURI** - **fileuri**: file-URI [RFC8089]_

      Traditional representation

    * **RTE_FILEURI0** - **fileuri0**: file-URI [RFC8089]_ Appendix E
    
      Minimal representation: ::

         file:/path/to/file
         file:c:/path/to/file
         file://host.example.com/path/to/file

    * **RTE_FILEURI4** - **fileuri4**: file-URI [RFC8089]_ Appendix E

      Traditional representation: ::

         file:///path/to/file
         file:///c:/path/to/file
         file:////host.example.com/path/to/file

    * **RTE_FILEURI5** - **fileuri5**: file-URI [RFC8089]_ Appendix E

      With extra slash '/': ::

         file:///path/to/file
         file:///c:/path/to/file
         file://///host.example.com/path/to/file

    * **RTE_CIFS** - **cifs**: CIFS [SMBCIFS]_
    * **RTE_HTTP** - **https**: virtual add-on bit for URI specific handling, see [RFC3986]_
    * **RTE_HTTPS** - **http**: virtual add-on bit for URI specific handling, see [RFC3986]_
    * **RTE_SMB** - **smb**: SMB [SMBCIFS]_

    * predefinitions:

       * **RTE_FTP**: see [RFC1738]_
       * **RTE_GIT**: see generic [RFC3986]_
       * **RTE_LDAP**: LDAP [RFC1959]_, [RFC2255]_
       * **RTE_NFS**: see [RFC2224]_
       * **RTE_PKCS11**: see [RFC7512]_
       * **RTE_RSYNC**: see [RFC5781]_
       * **RTE_SNMP**: SNMP [RFC4088]_
       * **RTE_SSH**: see [RFCSSHURI]_
       * **RTE_TFTP**: see [RFC3617]_
       * **RTE_VNC**: see [RFC7869]_
       * **RTE_XMPP**: see [RFC5122]_

    .

  * **RTE_GENERIC**: Undefined platform for special cases.

* Control Variables:

  * **RTE**: Current runtime-environment variable.

Calculation of Bit-Masks
""""""""""""""""""""""""
A typical example for the base of the mapping and algorithms is:

.. parsed-literal::

   # category: posix
   RTE_POSIX = 8192  #: Posix systems using *fcntl* [POSIX]_.

   # family: OS-X
   # bit-block: Apple - OS-X
   RTE_DARWIN = RTE_POSIX + 1  #: Darwin/OS-X, as Posix system [POSIX]_, no macpath-legacy.
   RTE_OSX = RTE_POSIX + 2  #: Darwin/OS-X, as Posix system [POSIX]_, no macpath-legacy.

   # family: Sun - Solaris
   RTE_SOLARIS = RTE_POSIX + 16  #: UNIX/Solaris, as Posix system [POSIX]_.

   # family: BSD
   RTE_BSD = RTE_POSIX + 32  #: BSD, - OpenBSD, FreeBSD, NetBSD - as Posix system [POSIX]_.

   # family: Linux
   RTE_LINUX = RTE_POSIX + 64  #: Linux with specific add-ons - OS, DIST, GNU - as Posix system [POSIX]_.
   
   # members" Linux
   RTE_CENTOS  = RTE_LINUX + 1  #: CentOS
   RTE_CENTOS4 = RTE_LINUX + 2  #: CentOS-4
   RTE_CENTOS5 = RTE_LINUX + 3  #: CentOS-5
   RTE_CENTOS6 = RTE_LINUX + 4  #: CentOS-6
   RTE_CENTOS7 = RTE_LINUX + 5  #: CentOS-7
   
   RTE_FEDORA = RTE_LINUX + 32  #: Fedora
   RTE_FEDORA19 = RTE_LINUX + 33  #: Fedora-19
   RTE_FEDORA27 = RTE_LINUX + 34  #: Fedora-27
   
   RTE_DEBIAN = RTE_LINUX + 64  #: Debian
   RTE_DEBIAN6 = RTE_LINUX + 65  #: Debian - squeeze
   RTE_DEBIAN7 = RTE_LINUX + 66  #: Debian - wheezy
   RTE_DEBIAN8 = RTE_LINUX + 67  #: Debian - jessy
   RTE_DEBIAN9 = RTE_LINUX + 68  #: Debian - stretch
   
The calculations are for OS and distributions:

.. parsed-literal::

   #
   # explicit
   #
   if RTE & RTE_POSIX: # use category
      pass
   
   if RTE & RTE_LINUX: # use family
      pass
      
   if RTE & RTE_CENTOS: # use distro
      pass

   if RTE & RTE_CENTOS7: # use release
      pass

   #
   # hierarchical
   #
   if RTE & RTE_POSIX: # use category
      if RTE & RTE_LINUX: # use family
         # do s.th. ...
               
         if RTE & RTE_CENTOS7: # use release
            pass
         else:
            # do s.th. ...

      elif RTE & RTE_BSD: # use family
         # do s.th. else...

         if RTE & RTE_OPENBSD: # use release
            pass
         else:
            # do s.th. else...
               

The calculations are for URI and schemes:

.. parsed-literal::

   if RTE & RTE_URI: # use category
      pass
   
   if RTE & RTE_HTTP: # use scheme
      pass
      



Miscelaneous
^^^^^^^^^^^^
Control Variables:

* **verbose**
* **debug**

Node Types
^^^^^^^^^^
File system node type enums as bit values
[`code <_modules/filesysobjects/__init__.html#>`_].

.. index::
   pair: node-type; T_ALL
   pair: node-type; T_DEV
   pair: node-type; T_DIR
   pair: node-type; T_EXP
   pair: node-type; T_FILE
   pair: node-type; T_HARDL
   pair: node-type; T_LOCAL
   pair: node-type; T_MNT
   pair: node-type; T_NODES
   pair: node-type; T_SYML

* **T_ALL(1)**: All files and empty directories.
* **T_DEV(64)**: Devices nodes.
* **T_DIR(4)**: Directories.
* **T_EXP(256)**: Exported filesystems.
* **T_FILE(2)**:Files.
* **T_HARDL(32)**: Hard links.
* **T_LOCAL(512)**: Local file system entries only.
* **T_MNT(128)**: Mount points.
* **T_NODES(8)**: Files and empty directories. Is superposed by T_FILES and T_DIR.
* **T_SYML(16)**: Symbolic links.

Search Parameters
^^^^^^^^^^^^^^^^^
Search directions control parameters for *findpattern()*.
[`code <_modules/filesysobjects/__init__.html#>`_]

.. index::
   pair: search-param; L_MEM_CACHE_ONE
   pair: search-param; L_TDOWN_WALK
   pair: search-param; L_UP_EXT
   pair: search-param; L_UP_WALK

* **L_MEM_CACHE_ONE(4)**: Caches one node-level only.
* **L_TDOWN_WALK(0)**: See os.walk(topdown=True)
* **L_UP_EXT(3)**: Caches M_UP_WALK, and provides same behavior as M_TDOWN_WALK.
* **L_UP_WALK(1)**: See os.walk(topdown=False)

Search Flow Control
^^^^^^^^^^^^^^^^^^^
Bit values for the search proceeding behaviour of *findpattern()*
[`code <_modules/filesysobjects/__init__.html#>`_].

.. index::
   pair: search-flow; M_ACCURATE
   pair: search-flow; M_ALL
   pair: search-flow; M_FILTERS
   pair: search-flow; M_FILTPAR
   pair: search-flow; M_FIRST
   pair: search-flow; M_IGNORE
   pair: search-flow; M_LAST
   pair: search-flow; M_NEST
   pair: search-flow; M_NOCANON
   pair: search-flow; M_PARAMS
   pair: search-flow; M_REL

* **M_ACCURATE(4)**: ffs.
* **M_ALL(32)**: Returns all matched results.
* **M_FILTERS(1)**: Applies to all filters.
* **M_FILTPAR(3)**: Applies all filters and parameters.
* **M_FIRST(8)**: Breaks after first match.
* **M_IGNORE(0)**: Filters and parameters are ignored.
* **M_LAST(16)**: Matches all, but returns the last only.
* **M_NEST(64)**: Clears nested directory path matches.
* **M_NOCANON(128)**: Do not convert input paths to canonical absolute.
* **M_PARAMS(2)**: Applies to all parameters.
* **M_REL(256)**: Keep relative names.

Control of Pattern Application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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

.. index::
   pair: pattern-control; W_GLOB
   pair: pattern-control; W_LITERAL
   pair: pattern-control; W_RE
   pair: pattern-control; W_RE_FULL

* **W_GLOB(1)** - considers the provided expressions as *glob*s or *literal*
* **W_LITERAL(0)** - considers the provided expressions as *literal* match-patterns
* **W_RE(2)** - considers the provided expressions as *re*, *glob*, or *literal*
* **W_RE_FULL(16)** - disables performance optimization, enables full scale *re* syntax including *groups* and  '*|*' (or)

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


Functions
---------
getspf
^^^^^^
.. autofunction:: getspf

gettpf
^^^^^^
.. autofunction:: gettpf


Exceptions
----------

.. autoclass:: FileSysObjectsError
