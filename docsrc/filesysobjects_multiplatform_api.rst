Filesystem Address Interfaces on Multiple Platforms
===================================================
The development and operations of modern applications require
commonly the support of multiple platforms.
This in particular spans Posix based filesystems and Windows based filesystems,
which use different characters as separators for path names and search paths.
Additionaly - even worst - the path name separator '\\' is also the escape character
on both platforms.
This restricts in some cases the applicability of the provided common variables 
'*os.pathsep*' and '*os.path.sep*'.

Extensions exist in addition to the simple local file address,
which provide for application prefixes - for example for shares, network mounts, and URIs. 
A common issue arises here in particular when shared filesystems are accessed by clients and servers.
This is due to the common fact, that the filesystem is transparently used by various clients
operating on different OS.
Again, modern applications work transaparently for local and distributed applications,
provide the transparent processing of file names - resource identifiers - provided by
various formats and semantics.
For local applications as well as distributed applications - in general for cloud applications
including their management and infrastructure interfaces.

The *filesysobjects* API adds this features to the standard libraries
by introducing an abstract address layer.

The common transparent interface last but not least finally saves development efforts as well as
enhances the overall performance by a centralized and neat library.
In particular enhances the quality by well tested interfaces covering the
bunches of the special cases with more than 4500 test
cases included into *filesysobjects* - at the time of writing.

Names and Paths
---------------
Node Names
^^^^^^^^^^
The names of the filesystem nodes - directories and files - require some attention
when implementing a generic file system toolset.
This is in particular of importance, because the seperator characters are different on
the platforms, and have multiple semantics depending on the context, while still
has to be processed as semantic control characters of the pathnames, e.g. as seperator, and
part of an ordinary nodename too - even intermixed.
Thus poses as a little challanges for the design and implementation of an appropriate regular expression.

Chracter Sets
"""""""""""""
The collection and comparison of the valid characters is focussing on modern systems based on OSs with internationalization support.
These provide filesystems which in most cases support unicode characters for file and directory names.
The *filesysobjects* works with any characters set, detecting the filesystem specific reserved characters, and managing the context specific semantics of
the filesystem specific address resolution control characters. For example the colon ':' with multiple semantics as search path seperator(Posix), 
replacement for a '/' in filenames(OS-X), and also a valid character in file and directory names(Posix, OS-X).
While the semi-colon ';' is a shell seperator, it is also a valid character for file and pathnames on all platforms.

The short discussion is required for the analysis of the regexpr due to the vaious placement and resulting context specific semantocs
of multiple characters used as path and search path seperators.

The current most relevant filesystems on the supported OSs provide commonly localization. 

* Major Linux filesystesm like 'ext4' support unicode.
* The newer Micrososft-Windows filesystems support UTF-16.
* The newer filesystems for OS-X support UTF-16.

Therefore from the requirements view of the *filesysobjects* it is basically only required to analyse the reserved characters and words
for each OS/Filesystem. 


Reservered Characters
"""""""""""""""""""""
The following table lists the reserved characters for the supported filesystems and in additionally special characters, which are
frequently reserved for special semantics of shells and applications.


The resulting characters to be processed with specific control semantics as seperators and file access rediredirectors are extracted into the following table.
The table lists whether the characters could occur in file names, while still beeing control characters for the format and resolution processing of the
file path names.
Thus require special attention for the reguylar expressions and the functional tests.  

The following characters are in particular of importance for the *filesysobjects* as seperator for the disassembly and analysis of pathnames.

+------+---------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+-------------------------------------------------+
| char | name          | num | hex | all | avoid | non-portable | non | Posix(2) | Cygwin | BSD | Linux | OS-X | Solaris | Windows | Seamntics                                       |
+======+===============+=====+=====+=====+=======+==============+=====+==========+========+=====+=======+======+=========+=========+=================================================+
| |sl| | **slash**     | 47  | 2F  |     | x     | x            |     | n(1)     | n      | n   | n     | s(0) |         | n       | path sep.                                       |
+------+---------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+-------------------------------------------------+
| |bs| | **backslash** | 92  | 5C  |     | x     | x            |     | v        | n      | v   | v     | v    |         | n       | path sep., esc char, regexpr                    |
+------+---------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+-------------------------------------------------+
| |co| | **colon**     | 58  | 3A  |     | x     | x            |     | v        | v      | v   | v     | s(0) | v       | n       | drive-sep., app-sep, slash-alias(OS-X), regexpr |
+------+---------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+-------------------------------------------------+
| |do| | **dot** (3)   | 46  | 2E  | x   |       |              |     | v        | v      | v   | v     | v    | v       | v       | postfix-separator, regexpr, glob                |
+------+---------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+-------------------------------------------------+

* **v**: valid
* **n**: non-valid
* **s**: special behavior

0. OS-X - Names containing slashes '/' could be created within finder(by '/') and CLI(by ':'), 
   but actually results in names where the '/' and ':' are used 'almost' interchangeably by the shell
   and the finder.

   .. note::

      Names containing a shlash should be avoided, a short example::

         # in finder the name is displayed as '/', could be used for create too
         mkdir ':'  # creates a local subdirectory with name '/'(finder), or ':'(shell)
         
         # ls displays ':', while finder displays '/'
         ls
         
         # access to the local subdirectory named '/'
         echo a > ./:/file0 # uses local subdirectory named '/'
         
         # the following does not work
         echo a > .//file0  # actually uses current directory '.'
         echo a > /file0    # actually uses root directory '/'

      The ':' in addition collides with the 'os.pathsep' on OS-X.

      .. warning::

         Avoid the characters '/', '\\', ';', and ':' in file system node names.

1. The 'JFS' seems to support '/', while the only and one prohibited character is NULL. 

2. The posix based filsystems are e.g. ext2, ext3, ext4, jfs, xfs, and ReiserFS(Hi Hans, hope your OK... [WikiHansReiser]_ )

3. The dot '.' is a valid character, but the two special words '.' and '..' are reserved words on all major filesystems,
   in addition the dot has the special meaning in the context of file postfixes.

The next set of embedded characters within path names is of particular relevance for the glob and 
regexpr feature of wildcard resolution, because these are valid characters for names, and are special
characters for regular expressions.
Thus these require some special attention for the implementation.

+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| char  | name              | num | hex | all | avoid | non-portable | non | Posix(2) | Cygwin | BSD | Linux | OS-X | Solaris | Windows | Seamntics                             |
+=======+===================+=====+=====+=====+=======+==============+=====+==========+========+=====+=======+======+=========+=========+=======================================+
| |sem| | semi-colon        | 59  | 3B  | x   | x     |              |     | v        | v      | v   | v     | v    |         | v       | command-sep, regexpr                  |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |ast| | asterisk          | 42  | 2A  |     | x     | x            |     | v        | v      | v   | v     | v    |         | n       | wildcard, glob, regexpr               |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |qm|  | question mark     | 63  | 3F  |     | x     | x            |     | v        | v      | v   | v     | v    |         | n       | single char shell, regexpr, glob      |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |lt|  | lt                | 60  | 3C  |     | x     | x            |     | v        | v      | v   | v     | v    |         | n       | redirect, regexpr                     |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |gt|  | gt                | 62  | 3E  |     | x     | x            |     | v        | v      | v   | v     | v    |         | n       | redirect, regexpr                     |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |exc| | exclamation point | 33  | 21  | x   | x     |              |     | v        | v      | v   | v     | v    | v       | v       | negation glob, regexpr, glob          |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |td|  | tilde             | 126 | 7E  | x   |       |              |     | v        | v      | v   | v     | v    | v       | v       | regexpr                               |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |amp| | ampersand         | 38  | 26  | x   | x     |              |     | v        | v      | v   | v     | v    | v       | v       | shell fork, redirect, regexpr         |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |lp|  | parenthesis       | 40  | 28  | x   | x     |              |     | v        | v      | v   | v     | v    |         | v       | command group, regexpr                |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |rp|  | parenthesis       | 41  | 29  | x   | x     |              |     | v        | v      | v   | v     | v    |         | v       | command group, regexpr                |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |lc|  | curly brace       | 123 | 7B  | x   | x     |              |     | v        | v      | v   | v     | v    |         | v       | command group, regexpr                |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |rc|  | curly brace       | 125 | 7D  | x   | x     |              |     | v        | v      | v   | v     | v    |         | v       | command group, regexpr                |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |car| | caret             | 94  | 5E  | x   | x     |              |     | v        | v      |     | v     | v    |         | v       | regexpr                               |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |dol| | dollar            | 36  | 24  | x   | x     |              |     | v        | v      | v   | v     | v    |         | v       | shell variable, shell locale, regexpr |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |lb|  | bracket           | 91  | 5B  | x   | x     |              |     | v        | v      | v   | v     | v    |         | v       | regexpr, glob                         |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |rb|  | bracket           | 93  | 5D  | x   | x     |              |     | v        | v      | v   | v     | v    |         | v       | regexpr, glob                         |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+
| |unk| | unknown           | 129 |     | x   | x     |              |     | v        | v      | v   | v     | v    |         | v       | generic replacement encode-err        |
+-------+-------------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+---------------------------------------+

* **v**: valid
* **n**: non-valid
* **s**: special behavior

The following characters are of secondary relevance as building blocks for the syntactical expression of path names, an their processing by shell.
 
+-------+--------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+------------+
| char  | name         | num | hex | all | avoid | non-portable | non | Posix(2) | Cygwin | BSD | Linux | OS-X | Solaris | Windows | Seamntics  |
+=======+==============+=====+=====+=====+=======+==============+=====+==========+========+=====+=======+======+=========+=========+============+
| |sq|  | single quote | 39  | 27  | x   | x     |              |     | v        | v      | v   | v     | v    |         | v       |            |
+-------+--------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+------------+
| |qu|  | quote        | 34  | 22  |     | x     | x            |     | v        | v      | v   | v     | v    |         | n       |            |
+-------+--------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+------------+
| |pi|  | pipe         | 124 | 7C  |     | x     | x            |     | v        | v      | v   | v     | v    |         | n       | redirect   |
+-------+--------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+------------+
| |gra| | grave accent | 96  | 60  | x   | x     |              |     | v        | v      |     | v     | v    |         | v       | shell-exec |
+-------+--------------+-----+-----+-----+-------+--------------+-----+----------+--------+-----+-------+------+---------+---------+------------+

* **v**: valid
* **n**: non-valid
* **s**: special behavior


.. |sl| raw:: html

   <code>/</code>

.. |bs| raw:: html

   <code>&#92;</code>

.. |qm| raw:: html

   <code>?</code>

.. |pe| raw:: html

   <code>%</code>

.. |co| raw:: html

   <code>:</code>

.. |pi| raw:: html

   <code>&#124;</code>

.. |qu| raw:: html

   <code>"</code>

.. |gt| raw:: html

   <code>></code>

.. |lt| raw:: html

   <code><</code>

.. |do| raw:: html

   <code>.</code>

.. |com| raw:: html

   <code>,</code>

.. |sem| raw:: html

   <code>;</code>

.. |sp| raw:: html

   <code>&nbsp;</code>

.. |at| raw:: html

   <code>&#64;</code>


.. |lp| raw:: html

   <code>&#40;</code>

.. |rp| raw:: html

   <code>&#41;</code>

.. |lc| raw:: html

   <code>&#123;</code>

.. |rc| raw:: html

   <code>&#125;</code>

.. |lb| raw:: html

   <code>&#91;</code>

.. |rb| raw:: html

   <code>&#93;</code>

.. |min| raw:: html

   <code>-</code>

.. |un| raw:: html

   <code>_</code>

.. |car| raw:: html

   <code>&#94;</code>

.. |gra| raw:: html

   <code>`</code>

.. |eq| raw:: html

   <code>=</code>

.. |ht| raw:: html

   <code>TAB</code>

.. |lf| raw:: html

   <code>LF</code>

.. |td| raw:: html

   <code>~</code>

.. |num| raw:: html

   <code>#</code>

.. |dol| raw:: html

   <code>$</code>

.. |exc| raw:: html

   <code>!</code>

.. |amp| raw:: html

   <code>&</code>

.. |sq| raw:: html

   <code>'</code>

.. |ast| raw:: html

   <code>*</code>

.. |plu| raw:: html

   <code>+</code>

.. |eur| raw:: html

   <code>&#128;</code>

.. |unk| raw:: html

   <code>&#129;</code>

.. |nul| raw:: html

   <code>NULL</code>


Reserved Names
""""""""""""""
The listed names are reseved and could not be used for application nodes or files.

Common
''''''
The following names are served by almost all OS/File systems:

* '.' - current directory
* '..' - parent directory

Posix
'''''
The posix filesystem reserves less beneath the common dot-names.
Some entries are commonly reserved by the full pathnames such as device nodes
within the */dev* directory and the */etc* directory.
his depends on the filesystem hierarchy standard applied onto the concrete
OS.

Microsoft Windows(TM)
'''''''''''''''''''''
* The following names are reserved by the
  OS: ::

     CON, PRN, AUX, NUL, COM1, COM2, COM3, COM4, COM5, COM6, COM7, COM8, COM9, 
     LPT1, LPT2, LPT3, LPT4, LPT5, LPT6, LPT7, LPT8, LPT9. 

Special Cases
"""""""""""""

Cygwin
''''''
Cygwin [CYGWIN]_ has a specific behavior when it mets characters forbidden in node/file names,
In these cases the characters are replaces by their Unicode equivalent,
see user manual "Forbidden characters in filenames".

This is also the case when one path is expected, but for example 
a search path containing multiple paths with drives is provided.
In those cases the drive letters from the second on are replaces as 'detected filenames'
with their Unicode characters.

.. code-block:: shell
   :linenos:

   $ cygpath -w d://:e:/
   D:\e\

   acue@w7u /cygdrive/e
   $ cygpath -w d://:e:/ | od -c -t x1
   0000000   D   :   \ 357 200 272   e 357 200 272   \  \n
            44  3a  5c  ef  80  ba  65  ef  80  ba  5c  0a
   0000014

The syntax for the recognition of multiple paths requires the paths to be pre-splitted - here by inserting spaces:

.. code-block:: shell
   :linenos:

   $ cygpath -w d:// e:/
   D:\\
   E:\

   $ cygpath -u d:// e:/
   /cygdrive/d/
   /cygdrive/e/

The *filesysobjects* does not adapt this behavior.
Interfaces for the split of search paths are available when requires, e.g. *filesysobjects.paths.splitpathx()*,
and *filesysobjects.paths.splitpathx_pathvar()*.

OS-X - Darwin
'''''''''''''
The following characters - "path-separator-symbolic-name" - are reserved by the OS/File system:

* ':' - colon in node names on HPF/HPF+.
  
  The colon within a node name as visible from the shell is treated as a shlash '/' within
  the *finder*.
  
  This historic legacy [os.path]_ [macpath]_ is not supported by the *filesysobjects*. 
  The *filesysobjects* supports on OS-X the posix standard for local components of file system path names.
  Thus still the application tags and URIs/URLs..

OS/2
''''
The *OS/2* - os2emxpath / Python2 - is not supported by the *filesysobjects*. 

Ambiguous Syntax Elements
"""""""""""""""""""""""""
The application of a common syntax scanner for multiple platforms introduces a number of ambiguities,
which could only be resolved with the appropriate context information.
Thus a static analysis of the syntax for the resource path is restricted to the unambiguous
cases, while the ambigous require additional information.

The application is onto a provided path strings, which has to be analysed in order to split it into it's
logical path parts. Basically the same has to be considered when analysing a single path, which is
for the Python interpreter not obviously a single path.

The concrete ambiguity - which actually 'hurts' - is the multiple use of the colon character ':'.
This is used in the following semantics:

* Posix:

  * path separator - os.pathsep
  * node name element - For example '/my/path:node/file:name.txt' is valid, the same as the corresponding
    search path "/my/path:node/:/any/path", where "path:node" is actually a directory name.
    This search path could not be split by static analysis, but requires dynamic file system lookup.
    Thus a remote offline validation by static analysis is not possible.
  * Node names are permitted to contain semi-colons ';' too, which could also 'hurt', when this
    is used as a replacement for the colon.

* Windows:

  * drive names

* OS-X - HPF/HPF+:

  * represents in nodenames an alias for the slash '/'
  * in addition the posix standard applies

* URI/URL

  * is part of the application prefix


The following is provided non-ambiguous by the parser and scanner without required action:

#. The scanner analyses URI/URL accurately
#. The scanner analyses drive names - seemingly - accurately
#. Special support for the OS-X case is not supported.
#. Remote-lookups are currently not supported.
#. The Windows platform works perfectly by definition for valid files and characters.
   The acces to nodes and files on mounted file systems requires valid character sets.  

The default behavior on Posix based file systems is perfectly applicable, for the cases:

* no colons ':' are used in filenames
* search paths are required by the application only and are configured by semi-colons ';' as 
  path separator (os.pathseparator), but no semi-colons are than contained in file names.

While the Windows platform works perfectly by definition, the Posix platform may work in the
majority of 99%(?) of standard applications from the box.

**The following resolution of ambiguity is provided as default:**

#. **IF** the colon ':' is part of one of the syntax elements URL/URI or DOS drive name,
   use it.
#. **ELSE-IF** the pathname contains one or more semi-colons ';', these are treated as
   path separator for posix based filesystems too, while each colon is treated as a part of node name.
#. **Else** the scanner by default suggestes each 'colon' for posix based filesystems as
   path separator - *os.pathsep*

**The following could be selected by choice:**

#. A calloption disables the forced use of the semi-colon as path separator.
#. A calloption is provided, enabling/disabling the 'colon' as a possible part of a node/file name.   
#. A calloption is provided, enabling the dynamic look-up of node-names containing ':', this
   may result in some performance degree.


Syntax
""""""
The syntax of path descriptions is provided in two constellations, the first is an simple path
pointing to a resource, the second is a search path, which assembles possible locations for requested
resource.
These two scenarios require at least two types of separators for the contained filesystem nodes,
a separator for the path itself, and a separator for the search paths.
The syntax elements of the filenames contain in addition on Posix systems the separator characters,
leading to ambiguity for the static offline analysis of a given path. 
In addition pathnames can contain application prefixes, which are defined either by a specific number of separator
characters, and/or have their own separator character.

The detailed description of the path syntax is provided in the section :ref:`Syntax Elements <SYNTAXELEMENTS>`.


Node Paths
^^^^^^^^^^
Node paths are analysed in accordance to the supported syntax [:ref:`Syntax Elements <SYNTAXELEMENTS>`]
based on the contained nodes.

File and Resource Path Processing Standard APIs
-----------------------------------------------
The Python libraries offer specialized interfaces for file path name processings,
and generic string processing APIs.
The *os* module is the low-level API providing for basic local file and path addressing,
with added functionality by the *string* class.
The *re* package provides the processing of arbitrary strings by regular expressions.

'os' package
^^^^^^^^^^^^
The '*os*' package provides the low-level interfaces tightly coupled to the underlying OS.
This is accompanied by the '*sys*' package covering the underlying system related APIs,
which in parts overlap with features of '*os*'.

os.path.normpath
""""""""""""""""
The 'os.path.normpath()' [normpath]_ interface is a quite important interface
when it comes to canonical file path names across multiple platforms.
But it has still some inconsistencies between multiple platforms.
The interface in particular is fixed on the current runtime environment,
thus lacks the creation of canonical names for crossplatform application.

.. code-block:: python
   :linenos:

   os.path.normpath(<file-path-name>)

The following table lists the native calls.

+----------+------+---------+---------+------+---------+---------+-----------+-----------+
| platform | d:/  | d:/:e:  | d:/:e:/ | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+==========+======+=========+=========+======+=========+=========+===========+===========+
| linux    | d:   | d:/:e:  | d:/:e:  | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+----------+------+---------+---------+------+---------+---------+-----------+-----------+
| BSD      | d:   | d:/:e:  | d:/:e:  | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+----------+------+---------+---------+------+---------+---------+-----------+-----------+
| OS-X     | d:   | d:/:e:  | d:/:e:  | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+----------+------+---------+---------+------+---------+---------+-----------+-----------+
| Solaris  |      |         |         |      |         |         |           |           |
+----------+------+---------+---------+------+---------+---------+-----------+-----------+
| Cygwin   | d:   | d:/:e:  | d:/:e:  | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+----------+------+---------+---------+------+---------+---------+-----------+-----------+
| Windows  | d:\\ | d:\\:e: | d:\\:e: | d:\\ | d:\\:e: | d:\\:e: | d:\\:e:   | d:\\;e:   |
+----------+------+---------+---------+------+---------+---------+-----------+-----------+

With Linux, BSD, Solaris, and OS-X as Posix based platforms.

os.split
""""""""
The split class splits the path from the file name part.

.. code-block:: python
   :linenos:

   os.path.split(<file-path-name>)

This behaves for the literally equal variants of the pathnames on
both platforms slightly different.

+----------+-------------+----------------+----------------+--------------+-----------------+-----------------+-------------------+-------------------+
| platform | d:/         | d:/:e:         | d:/:e:/        | d:\\         | d:\\:e:         | d:\\;e:         | d:\\:e:\\         | d:\\;e:\\         |
+==========+=============+================+================+==============+=================+=================+===================+===================+
| linux    | ('d:', '')  | ('d:', ':e:')  | ('d:/:e:', '') | ('', 'd:\\') | ('', 'd:\\:e:') | ('', 'd:\\;e:') | ('', 'd:\\:e:\\') | ('', 'd:\\;e:\\') |
+----------+-------------+----------------+----------------+--------------+-----------------+-----------------+-------------------+-------------------+
| BSD      | ('d:', '')  | ('d:', ':e:')  | ('d:/:e:', '') | ('', 'd:\\') | ('', 'd:\\:e:') | ('', 'd:\\;e:') | ('', 'd:\\:e:\\') | ('', 'd:\\;e:\\') |
+----------+-------------+----------------+----------------+--------------+-----------------+-----------------+-------------------+-------------------+
| OS-X     | ('d:', '')  | ('d:', ':e:')  | ('d:/:e:', '') | ('', 'd:\\') | ('', 'd:\\:e:') | ('', 'd:\\;e:') | ('', 'd:\\:e:\\') | ('', 'd:\\;e:\\') |
+----------+-------------+----------------+----------------+--------------+-----------------+-----------------+-------------------+-------------------+
| Solaris  |             |                |                |              |                 |                 |                   |                   |
+----------+-------------+----------------+----------------+--------------+-----------------+-----------------+-------------------+-------------------+
| Windows  | ('d:/', '') | ('d:/', ':e:') | ('d:/:e:', '') | ('d:\\', '') | ('d:\\', ':e:') | ('d:\\', ';e:') | ('d:\\:e:', '')   | ('d:\\;e:', '')   |
+----------+-------------+----------------+----------------+--------------+-----------------+-----------------+-------------------+-------------------+

With Linux, BSD, Solaris, and OS-X as Posix based platforms.

string class
^^^^^^^^^^^^
The frequent task required for file system analysis is the split of filepathnames
into it's path components and the filename.
This could be performed e.g. by the interface *string.split()*
and reversed by the interface *string.join()*.

This works good, until it comes to some more sophisticated file system names including
drive letters, application prefixes, network shares, URI, etc., where the things quickly become odd.
Therefore the application of regular expressions offers a more accurate means of
splitting paths, but requires advanced coding for pathsplit and escaping of contained
special characters.

The following call is expected to split a search path - PATH - into it's parts of
single search paths. 

.. code-block:: python
   :linenos:

   <file-path-name>.split(os.pathsep)

resulting in

+----------+------------+---------------------+----------------------+-------------+----------------------+-------------------+------------------------+---------------------+
| platform | d:/        | d:/:e:              | d:/:e:/              | d:\\        | d:\\:e:              | d:\\;e:           | d:\\:e:\\              | d:\\;e:\\           |
+==========+============+=====================+======================+=============+======================+===================+========================+=====================+
| linux    | ['d', '/'] | ['d', '/', 'e', ''] | ['d', '/', 'e', '/'] | ['d', '\\'] | ['d', '\\', 'e', ''] | ['d', '\\;e', ''] | ['d', '\\', 'e', '\\'] | ['d', '\\;e', '\\'] |
+----------+------------+---------------------+----------------------+-------------+----------------------+-------------------+------------------------+---------------------+
| BSD      | ['d', '/'] | ['d', '/', 'e', ''] | ['d', '/', 'e', '/'] | ['d', '\\'] | ['d', '\\', 'e', ''] | ['d', '\\;e', ''] | ['d', '\\', 'e', '\\'] | ['d', '\\;e', '\\'] |
+----------+------------+---------------------+----------------------+-------------+----------------------+-------------------+------------------------+---------------------+
| OS-X     | ['d', '/'] | ['d', '/', 'e', ''] | ['d', '/', 'e', '/'] | ['d', '\\'] | ['d', '\\', 'e', ''] | ['d', '\\;e', ''] | ['d', '\\', 'e', '\\'] | ['d', '\\;e', '\\'] |
+----------+------------+---------------------+----------------------+-------------+----------------------+-------------------+------------------------+---------------------+
| Solaris  |            |                     |                      |             |                      |                   |                        |                     |
+----------+------------+---------------------+----------------------+-------------+----------------------+-------------------+------------------------+---------------------+
| Windows  | ['d:/']    | ['d:/:e:']          | ['d:/:e:/']          | ['d:\\']    | ['d:\\:e:']          | ['d:\\', 'e:']    | ['d:\\:e:\\']          | ['d:\\', 'e:\\']    |
+----------+------------+---------------------+----------------------+-------------+----------------------+-------------------+------------------------+---------------------+

The following call is aimed to split in addition the matched path into a list of
directory components.

.. code-block:: python
   :linenos:

   for px in <file-path-name>.split(os.pathsep):
      px.split(os.path.sep)


regexpr with re
^^^^^^^^^^^^^^^

The most accurate framework for splitting pathnames into it's components is
provided by the *re* package based on string processing of arbitrary
file system path names.
The *re* package is extensively applied by the *filesysobjects* package
[`paths <_modules/filesysobjects/paths.html#>`_].
[`apppaths <_modules/filesysobjects/apppaths.html#>`_].
[`pathtools <_modules/filesysobjects/pathtools.html#>`_].


.. _FILESYSOBJECTSNORMPATHX:

'filesysobjects' package
------------------------
Target Platform Parameter
^^^^^^^^^^^^^^^^^^^^^^^^^
The syntax of the supported file system paths could be categorized into the two major blocks
*posix* and *win*, which are distinguished in particular by the separator characters.
In addition some extra differences exist for the *posix* based file systems. 
The option *tpf* controls the conversion of the path syntax for the various platforms.

The following overview depicts the effect of the option
*tpf*.
The '*local*' parameter of the '*filesysobjects.paths.normpathx()*'
provides the transparent call-through of the local native '*os.normpath()*'.

+---------+-------------+----------+------------------------------------------------------------+
| tpf     | compatible  | cross    | behaviour                                                  |
|         | to normpath | platform |                                                            |
+=========+=============+==========+============================================================+
| keep    | n.a.        | yes      | keeps input literally                                      |
+---------+-------------+----------+------------------------------------------------------------+
| local   | yes         | no       | calls local os.path.normpath()                             |
+---------+-------------+----------+------------------------------------------------------------+
| posix   | no          | yes*     | transforms all separators to '/' or ':'                    |
|         |             | (*pchar) | Portable for IEEE1003.1, 2013/3.276 Portable Character Set |
+---------+-------------+----------+------------------------------------------------------------+
| win     | no          | no       | transforms all separators to '\\' or ';'                   |
+---------+-------------+----------+------------------------------------------------------------+
| default | no          | no       | adapts 'win'(on win) or 'posix'(on posix) to local os      |
+---------+-------------+----------+------------------------------------------------------------+

.. note::
   .

   1. Supports standard Posix. The special semantics of OS-X/Darwin on HFS/HFS+ for the
      colon ':', which is silently exchanged within names by the 'finder' to a slash '/', is not
      supported. The colon is kept literally, while the slash is interpreted as a path name
      separator in accordance to Posix.
   #. Shortcut named options:


'filesysobjects.normpathx'
^^^^^^^^^^^^^^^^^^^^^^^^^^

The 
`filesysobjects.paths.normpathx() <pyfilesysobjects.html#filesysobjects.paths.normpathx>`_
, and 
`filesysobjects.pathtools.splitpathx() <pyfilesysobjects.html#filesysobjects.pathtools.splitpathx>`_
extends the interface provided by *os* and *String* for accurate and advanced processing
of resource paths in accordance to the full scope of standards and/or compatible to the native target
platform, while the *os* and *String* packages/classes provide basic processing of file path names.

Some basic examples are:

+--------------------+------+---------+-----------+------+---------+---------+-----------+-----------+
| platform           | d:/  | d:/:e:  | d:/:e:/   | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+====================+======+=========+===========+======+=========+=========+===========+===========+
| keep               | d:/  | d:/:e:  | d:/:e:/   | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+--------------------+------+---------+-----------+------+---------+---------+-----------+-----------+
| local(on linux)    | d:   | d:/:e:  | d:/:e:    | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+--------------------+------+---------+-----------+------+---------+---------+-----------+-----------+
| local(on win7)     | d:\\ | d:\\:e: | d:\\:e:   | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:   | d:\\;e:   |
+--------------------+------+---------+-----------+------+---------+---------+-----------+-----------+
| posix              | d:/  | d:/:e:  | d:/:e:/   | d:/  | d:/:e:  | d:/;e:  | d:/:e:/   | d:/;e:/   |
+--------------------+------+---------+-----------+------+---------+---------+-----------+-----------+
| win                | d:\\ | d:\\:e: | d:\\:e:\\ | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+--------------------+------+---------+-----------+------+---------+---------+-----------+-----------+
| default(posix/win) |      |         |           |      |         |         |           |           |
+--------------------+------+---------+-----------+------+---------+---------+-----------+-----------+

.. note::
   .

   0. The results from *os.path.normpath()* are as expected, while the cli *cygpath*
      diplays erroneous results e.g. in case of multiple colons ':'.

'filesysobjects.splitpathx'
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+
| platform        | d:/       | d:/:e:          | d:/:e:/              | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+=================+===========+=================+======================+======+=========+=========+===========+===========+
| keep            |           |                 |                      |      |         |         |           |           |
+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+
| local(on linux) | ['d']     | ['d', '/', 'e'] | ['d', '/', 'e', '/'] | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+
| local(on win7)  | ['d:', \\ | d:\\:e:         | d:\\:e:              | d:\\ | d:\\:e: | d:\\:e: | d:\\:e:   | d:\\;e:   |
+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+
| posix           | d:/       | d:/:e:          | d:/:e:/              | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+
| win             |           |                 |                      |      |         |         |           |           |
+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+
| default         | d:        |                 |                      |      |         |         |           |           |
+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+

'filesysobjects.splitpathx_appprefix'
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+
| platform        | d:/       | d:/:e:          | d:/:e:/              | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+=================+===========+=================+======================+======+=========+=========+===========+===========+
| keep            |           |                 |                      |      |         |         |           |           |
+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+
| local(on linux) | ['d']     | ['d', '/', 'e'] | ['d', '/', 'e', '/'] | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+
| local(on win7)  | ['d:', \\ | d:\\:e:         | d:\\:e:              | d:\\ | d:\\:e: | d:\\:e: | d:\\:e:   | d:\\;e:   |
+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+
| posix           | d:/       | d:/:e:          | d:/:e:/              | d:\\ | d:\\:e: | d:\\;e: | d:\\:e:\\ | d:\\;e:\\ |
+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+
| win             |           |                 |                      |      |         |         |           |           |
+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+
| default         | d:        |                 |                      |      |         |         |           |           |
+-----------------+-----------+-----------------+----------------------+------+---------+---------+-----------+-----------+

'filesysobjects.splitpathx_pathvar'
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


+-----------------+------------+---------------------+----------------------+-------------+----------------------+-----------------------+------------------------+-------------------------+
| platform        | d:/        | d:/:e:              | d:/:e:/              | d:\\        | d:\\:e:              | d:\\;e:               | d:\\:e:\\              | d:\\;e:\\               |
+=================+============+=====================+======================+=============+======================+=======================+========================+=========================+
| keep            |            |                     |                      |             |                      |                       |                        |                         |
+-----------------+------------+---------------------+----------------------+-------------+----------------------+-----------------------+------------------------+-------------------------+
| local(on linux) | ['d', '/'] | ['d', '/', 'e', ''] | ['d', '/', 'e', '/'] | ['d', '\\'] | ['d', '\\', 'e', ''] | ['d', '\\;', 'e', ''] | ['d', '\\', 'e', '\\'] | ['d', '\\;', 'd', '\\'] |
+-----------------+------------+---------------------+----------------------+-------------+----------------------+-----------------------+------------------------+-------------------------+
| local(on win7)  | ['d:', '/' | ['d', '/', 'e', ''] |                      |             |                      |                       |                        |                         |
+-----------------+------------+---------------------+----------------------+-------------+----------------------+-----------------------+------------------------+-------------------------+
| posix           | ['d', '/'] | ['d', '/', 'e', ''] | ['d', '/', 'e', '/'] | ['d', '\\'] | ['d', '\\', 'e', ''] | ['d', '\\;', 'e', ''] | ['d', '\\', 'e', '\\'] | ['d', '\\;', 'd', '\\'] |
+-----------------+------------+---------------------+----------------------+-------------+----------------------+-----------------------+------------------------+-------------------------+
| win             |            |                     |                      |             |                      |                       |                        |                         |
+-----------------+------------+---------------------+----------------------+-------------+----------------------+-----------------------+------------------------+-------------------------+
| default         |            |                     |                      |             |                      |                       |                        |                         |
+-----------------+------------+---------------------+----------------------+-------------+----------------------+-----------------------+------------------------+-------------------------+

'filesysobjects' vs. Standard Libraries
---------------------------------------

'normpathx' vs. 'normpath'
^^^^^^^^^^^^^^^^^^^^^^^^^^
The `filesysobjects.paths.normpathx() <pyfilesysobjects.html#filesysobjects.paths.normpathx>`_
extends the interface provided by *os*.
While the   *os* packages provides limited basic processing of file path names,
the '*filesysobjects*' package provides accuracy and extension to full scope of
standard resource path names.

The table compares '*string.split(os.pathsep)*' with 
`filesysobjects.paths.normpathx() <pyfilesysobjects.html#filesysobjects.paths.normpathx>`_.

+----------------------------------+----+----------------+
|                                  | os | filesysobjects |
+==================================+====+================+
| native platform paths            | x  | x              |
+----------------------------------+----+----------------+
| cross-platform paths             |    | x              |
+----------------------------------+----+----------------+
| shares and application addresses |    | x              |
+----------------------------------+----+----------------+
| URI file prefixes                |    | x              |
+----------------------------------+----+----------------+
| native platform escaping         | x  | x              |
+----------------------------------+----+----------------+
| cross-platform escaping          |    | x              |
+----------------------------------+----+----------------+
| mixed paths                      |    | x              |
+----------------------------------+----+----------------+
| *Cygwin*                         |    | x              |
+----------------------------------+----+----------------+



.. _FILESYSOBJECTSSPLITPATH:

'splitpathx' vs. 'split'
^^^^^^^^^^^^^^^^^^^^^^^^
The `filesysobjects.pathtools.splitpathx() <pyfilesysobjects.html#filesysobjects.pathtools.splitpathx>`_
extend the interface provided by *os* and *String* for accurate processing.
While the   *os* and *String* packages/classes provide basic processing of file path names
with limited applicability in particular for non-local filenames,
the '*filesysobjects*' package provides accuracy and extension to the full scope
standard resource path names.

The table compares '*string.split(os.pathsep)*' with 
`filesysobjects.pathtools.splitpathx() <pyfilesysobjects.html#filesysobjects.pathtools.splitpathx>`_.

+----------------------------------+--------+----------------+
|                                  | String | filesysobjects |
+==================================+========+================+
| native platform paths            | x(0)   | x              |
+----------------------------------+--------+----------------+
| cross-platform paths             | x(1)   | x              |
+----------------------------------+--------+----------------+
| shares and application addresses |        | x              |
+----------------------------------+--------+----------------+
| URI file prefixes                |        | x              |
+----------------------------------+--------+----------------+
| mixed paths                      | x(2)   | x              |
+----------------------------------+--------+----------------+
| *Cygwin*                         | x(3)   | x              |
+----------------------------------+--------+----------------+

0. String.split() applicable for local file system paths, no app-prefixes,
   limited shares.
1. String.split() applicable for local file system paths on remote sytem,
   no app-prefixes, limited shares.
2. Simple paths could be handled by multiple calls, one for each platform.
   Applicable for local/native file system paths only, no app-prefixes,
   limited shares.
3. No special support for intermixed *Cygwin* paths.


Resources
---------
The supported standards in accordance to [POSIX]_/[IEEE]_, [IETF]_, and 
filesystem conventions [MSDN]_ and [MSOSPEC]_ are:

* [CIFS]_: Common Internet File System
* [CYGWIN]_: Cygwin.org
* [IEEE1003C412]_: IEEE Std 1003.1(TM), 2013 Edition; Chapter 4.12
* [MS-CIFS]_: Common Internet File System (CIFS) Protocol; Microsoft Inc.
* [MS-DTYP]_: Windows Data Types - Chap. 2.2.57 UNC; Microsoft Inc.
* [MS-SMB]_: Server Message Block (SMB) Protocol; Microsoft Inc.
* [NTFS]_ NTFS Technical Reference
* [os]_: os; Python.org
* [os.path]_: os.path - *os.path.normpath()* variants;Python.org
* [POSIX]_: IEEE Std 1003.1(TM), 2013 Edition
* [RFC1738]_: Uniform Resource Locators (URL)
* [RFC1808]_: Relative Uniform Resource Locators
* [RFC2396]_: Uniform Resource Identifiers (URI): Generic Syntax
* [RFC2648]_: A URN Namespace for IETF Documents
* [RFC3986]_: Uniform Resource Identifier - URI: Generic Syntax
* [RFC4122]_: A Universally Unique IDentifier (UUID) URN Namespace
* [RFC6570]_: URI Template
* [RFC7320]_: URI Design and Ownership
* [SMBCIFS]_: Microsoft SMB Protocol and CIFS Protocol
* [UNC]_: UNC: Common definition in [MS-DTYP]_: Windows Data Types - Chap. 2.2.57 UNC; Microsoft Inc.
* [URISCHEME]_: The file URI Scheme - draft-kerwin-file-scheme-13; IETF
* updates and and additional others...
