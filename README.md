filesysobjects
==============

The 'filesysobjects' package provides cross-platform-utilities for path addresses
of file like resources. This includes the search and navigation features on file
system structures with the application of regular expressions for pathnames 
intermixed with globs.

* filesysobjects - constants

* filesysobjects.apppaths - application resource path processing

* filesysobjects.paths - file systems path processing

* filesysobjects.pathtools - search, enumeration, and iteration operations

* filesysobjects.userdata - user directories

* filesysobjects.osdata - OS directories

* filesysobjects.configdata - config directories


Supported platforms are:

* Linux, BSD, Unix, Mac-OS/OS-X, and Windows

* Python2.7, Python3.5+

**Online documentation**:

* https://pyfilesysobjects.sourceforge.io/


**Runtime-Repository**:

* PyPI: https://pypi.org/project/pyfilesysobjects/

  Install: *pip install pyfilesysobjects*, see also 'Install'.

**Downloads**:

* sourceforge.net: https://sourceforge.net/projects/pyfilesysobjects/files/

* bitbucket.org: https://bitbucket.org/acue/pyfilesysobjects

* github.com: https://github.com/ArnoCan/pyfilesysobjects/

* pypi.org: https://pypi.org/project/pyfilesysobjects/


Project Data
------------

* PROJECT: 'filesysobjects'

* MISSION: Standard conform utilities for paths of file systems and URIs.

* VERSION: 00.01

* RELEASE: 00.01.034

* STATUS: alpha

* AUTHOR: Arno-Can Uestuensoez

* COPYRIGHT: Copyright (C) 2010,2011,2015-2018 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

* LICENSE: Artistic-License-2.0 + Forced-Fairplay-Constraints


Python support:

*  Python2.7, and Python3.5+


OS-Support:

* Linux: Fedora, CentOS, Debian, and Raspbian 

* BSD - OpenBSD, and FreeBSD

* OS-X: Snow Leopard

* Windows: Win7, Win10

* Cygwin

* UNIX: Solaris



**Current Release**


Major Changes:

* Changed interface to notation.

* Python2.6 support dropped.

* Python3.5+ support introduced.

* Added advanced file and path search by *glob* and *re* - *findpattern()*.

* Added rfc3986 - level-1 with basic *normapppathx()* and *splitapppathx()*.

* Conformity tests for rfc1738, rfc3986, rfc8089, UNC, MS-SMB/MS-CIFS, IEEE/1003.1, see references section of doc.

ToDo:

* Introduction of dynamic plugins

* Support for name spaces of Windows

Known Issues:

* Quoting/masking in http paths currently does not work, %-codes has to be used. Queries and fragments are OK.

* Some minor non-compliance for rare esoteric cases.

* Old style MacOS path names and special handling of ':' by HPF/cli/finder are not supported.

* OpenVMS path names are not supported.

