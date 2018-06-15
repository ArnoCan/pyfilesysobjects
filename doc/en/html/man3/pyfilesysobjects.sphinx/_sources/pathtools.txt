'filesysobjects.pathtools' - Module
===================================

The *filesysobjects.pathtools* module provides advanced operations on paths, sub-paths,
and side branches.

Implementation Details
----------------------

Common Call Parameters
^^^^^^^^^^^^^^^^^^^^^^
The current version calls 'os.path.normpath' by default - when 'raw' is
not selected. This is consistent for all path related parameters including
search paths: start, top, plist, spath, etc.. Thus generally clears double
slashes, but also replaces symbolic links, so later literal post processing
e.g. for match based processing should be normalized too.

Current supported URIs for filenames are: 'file://', 'smb://', and
'cifs://'.
Additionally UNC names and Posix-Netapps are suppored by
the prefixes '\\\\' and '//'.
The syntax formats are interchangeable in accordance to RFC8089 [RFC8089]_
including the Annex.

For application specific URIs refer to `filesysobjects.apppaths <apppaths.html#>`_
The following options are generic and common to multiple interfaces:

matchidx=#idx
"""""""""""""
Matches on the provided index count
only::


   #idx==2 - ignores 0,1 and >2, matches idx==2

matchcnt=#num
"""""""""""""
The maximal number of matches returned when
multiple occur::

   #num==0 - all
   #num>0  - number of matches returned

spath
"""""
An existing path to be added to an entry
from 'plist'. The following cases are supported,
for further specifics refer to the interfaces.

0. Independent path entry - spath is absolute, just added.

1. Subpath of current directory
   spath is relative and present in
   current working directory, added
   py prefixing 'pwd'.

2. Arbitrary side-branch of a provided path
   spath is relative, searched in plist
   for an insertion hook, added when
   found as absolute.

3. Pattern matching - see manual 'Semi-Literals'
   and shortcut tables in manual:

     regexpr:
      Regular expressions are applicable for
      match on 'plist' only. Thus the part to be
      matched on the file system is required to be a
      literal.

     glob:
      Glob expressions are applicable on the file system
      itself only, thus the part to be matched on the
      'plist' is required to be a literal.

4. Is absolute path:
      Is checked to be a sub path of at least one of 'plist',
      than applied.

start
"""""
Start directory or file, when a file is provided the
directory portion is used as the starting pointer.

Each part is compared separately, but as a whole string.

top
"""
The topmost path within a directory tree as an end point
for a search operation. This is defined by the end of
a directory path name string. E.g. the the bottom-up search
beginning at the start directory::

  start=/a/b/c/d/e/f/g

is terminated by::

  top=d

at::

  /a/b/c/d

This is used as a match string for processing literally
on the parts of the provided start directory. The match
is checked after application of
'os.path.normpath'. Providing absolute paths still match,
because of the string, but eventually match multiple times
when equal sub paths exist and the match order is changed
to bottom-up search.

The containment of 'top' within the absolute 'start' path
is verified.

Each part is compared separately, but as a whole string.

plist
"""""
List of strings to be searched. By default first match
is used. Each is split into it's components and matched
separately.

default := sys.path

raw
"""
Suppress normalization by call of 'os.path.normpath'. The
caller has than to take care for appropriate measures for
a feasible match.

Glob Parametters
^^^^^^^^^^^^^^^^
The '*glob*' wildcard definitions comprise a subset of regular expressions
whith some deviation of their semantics.

.. code-block:: python
   :linenos:

   path0 = '/a/b/(x[!opq]*.py'

The resolution of contained path-elements as '*glob'* expressions
is proceeded dynamically by applying the glob module onto the file system nodes.

Regular Expressions
^^^^^^^^^^^^^^^^^^^
The regular expressions support the full scope of the standard Pyhton '*re*' module.
The expressions are used as post scan match-filter onto a set of fetched resource
path names.

.. code-block:: python
   :linenos:

   path0 = '/a/b/(x[^opq]*|XYZ[^abc]*).(py|pyc|pyo)'

The regexpr are by default compiled/loaded once statically during load time of the module.
The regular expressions for the path analysis permit the '*os.path.sep*' of the current platform
thus supports multi-level path patterns.

In order to avoid conflicts of the search patterns with reserved characters such as '/', '\\',
';', and ':', the *filesysobjects* supports two types of quoting, which could be used to
mask arbitrary parts of a path. The quotes parts are kept literally, including non-printable
and unicode characters.

* triple double-quotes

  .. code-block:: python
     :linenos:

     path0 = '/a/b/(x[^"""\\\\/;:"""]*|XYZ[^abc]*).(py|pyc|pyo)'
     path0 = '/a/b/(x"""[^\\\\/;:]"""*|XYZ[^abc]*).(py|pyc|pyo)
     path0 = '/a/b/("""x[^\\\\/;:]*|XYZ[^abc]*""").(py|pyc|pyo)'
     path0 = '/a/b/"""(x[^\\\\/;:]*|XYZ[^abc]*).(py|pyc|pyo)"""'

* triple single-quotes

  .. code-block:: python
     :linenos:

     path0 = "/a/b/(x[^'''\\\\/;:''']*|XYZ[^abc]*).(py|pyc|pyo)"

The quotings could be removed by the common parameter *stripquote*, which removes pairs of triple
quotes.

The interfaces within *pathtools* remove the quotes by default before applying the provided
paths.

Glob Parametters and Regular Expressions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The '*glob*' wildcard definitions comprise a subset of regular expressions
whith some deviation of their semantics.

In the case of a dot for example this could be in addition ambiguous.

.. code-block:: python
   :linenos:

   # file path name: /a/b/xname
   path0 = '/a/b/x.*'

   # regexpr: matches
   # glob:    does not match

or

.. code-block:: python
   :linenos:

   # file path name: /a/b/xname.c
   path0 = '/a/b/x.*'

   # regexpr: matches
   # glob:    does not match

or

.. code-block:: python
   :linenos:

   # file path name: /a/b/x.name.c
   path0 = '/a/b/x.*'

   # regexpr: matches
   # glob:    matches

or

.. code-block:: python
   :linenos:

   # file path name: /a/b/x.name.c
   path0 = '/a/b/x*.*'

   # regexpr: matches
   # glob:    does not match

Generally the regular expressions of Python provide a more flexible set of features.

Performance Optimization
^^^^^^^^^^^^^^^^^^^^^^^^
The internal performance optimization is based on the step-wise scan of the resource tree.
This is the case when regular expressions spanning multiple directory segments are applied.
When active, the regular expressions are - when possible - splitted into segments and
applied for each segment partially.
Due to the provided advanced and complex syntax of *re*, the applied optimization
constraints some elements see :ref:`SEARCHPERFORMANCEOPT`.
This is based mainly on the compiled regular expression

.. code-block:: python
   :linenos:

   _glob_prefix = re.compile(r"""
      (\[[\^][^\]]*\][*]*)                # 1 - [^...]  it is a re
      |(\[[^/\]]*\][*]*)                  # 2 - [...]   a char class without separator
      |(\[[!][^/\]]*[/][^\]]*\][*]*)      # 3 - [!.../...]   a non-def char class with separator
      |(\[[/]*\][*]*)                     # 4 - [/]   a char class with posix-separator ONLY
      |(\[[^/\[\]]*[/][^/\[]*\][*]*)      # 5 - [.../...]   a char class with posix-separator
      |(\[[\\\\]*\][*]*)                  # 6 - [\\\\]   a char class with nt-separator ONLY
      |(\[[^\\\\]*[\\\\][^\\\\]*\][*]*)   # 7 - [...\\\\...]   a char class with nt-separator
      |(?<![\\\\])([/]+)                  # 8 - '/'     class-less n * posix-separator
      |(?<![\\\\])([\\\\]+)               # 9 - '\\'    class-less n * nt-separator
      |([.][*])                           # 10 - '.*'    any char wildcard
      |([*])                              # 11 - wildcard character
      |([^/\[\]]+)                        # 12 - any character
      |(\[)                               # 13 - basically a syntax error, but could be a literal too
      |(\])                               # 14 - basically a syntax error, but could be a literal too
      """, re.X)

As shown, this implies some constraints on the application of the *re* syntax elements.

Whitelists and Blacklists
^^^^^^^^^^^^^^^^^^^^^^^^^
The match parameters provide for positive lists and for negative droplists.
These lists are defined as lists of regular expressions, which are dynamically compiled and applied on the
searched names.

* whitelist parameters select in case of a match.
* blacklist parameters drop in case of a match.

The whitelist parameters select in case of a match, thus these are applied on the names
of files and directories for match.
The input could be either a list of regular expressions, which are applied in the provided order,
or a single regular expression covering multiple filters.

The whitelist parameters are either file name arguments, which contain globs or reqgular expressions,
or parameters for specific interfaces.

The blacklist parameters use a syntax similar to the whitelist parameters, but drop in case of a match.

Module
------

.. automodule:: filesysobjects.pathtools

.. role:: raw-html(raw)
   :format: html

Functions
---------

clearpath
^^^^^^^^^
.. autofunction:: clearpath

expandpath
^^^^^^^^^^
.. autofunction:: expandpath

findpattern
^^^^^^^^^^^
.. autofunction:: findpattern

findrelpath_in_searchpath
^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: findrelpath_in_searchpath

findrelpath_in_searchpath_iter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: findrelpath_in_searchpath_iter

findrelpath_in_uppertree
^^^^^^^^^^^^^^^^^^^^^^^^
Convenience function, uses '*findrelpath_in_searchpath*' and '*set_uppertree_searchpath*'.

.. autofunction:: findrelpath_in_uppertree

findrelpath_in_uppertree_iter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Convenience function, uses '*findrelpath_in_searchpath*' and '*set_uppertree_searchpath*'.

.. autofunction:: findrelpath_in_uppertree_iter

get_subpath_product
^^^^^^^^^^^^^^^^^^^
.. autofunction:: get_subpath_product

glob_to_re
^^^^^^^^^^
.. autofunction:: glob_to_re

**Description:**

The compilation of *glob* expressions into *re* expressions is basically
straight forward. I is required in particular when partial *glob* expressions
have to be used in combination with *re* expressions for match filters on
file path names.
The result is as long unambiguous, as long the input expression is actually a
*glob* expression. The choosen compilation is not neccessarily syntactic idempotent.
The compilation results may look suprisingly, because the input is trusted as
a pure *glob* expression.
So for example the expression

.. code-block:: python
   :linenos:

   /a/.*/b

is compiled to

.. code-block:: python
   :linenos:

   /a/[.].*/b

This is perfectly allright.

* The term '*.\**' has the semantics in the *glob* domain: ::

     A dot folowed by any number of any characters, which is terminated
     by the next os.sep.

* While in the *re* domain the term '*.\**' has a slightly different semantics : ::

     Any character followed by an arbitrary number of any characters,
     which is terminated by the next os.sep.

So the *glob* compiled as:

.. code-block:: python
   :linenos:

   /a/[.].*/b

   # 0. /a/.        =>   /a/[.]

   # 1. /a/[.]*/b   =>   /a/[.].*/b

This will match on any name within '*/a/*' starting with a '.'.

Thus for the design of the reagular expressions the specifics have to be considered.

The possible additional semantic of e.g. null-dir is not considered for the compilation,
but is processed by the normalization interfaces accordingly.

.. code-block:: python
   :linenos:

    '*/./././*'   =>  '*/[.]/[.]/[.]/*'

The semantics with the representation of one/character names is:

.. code-block:: python
   :linenos:

    '*/?/?/?/*'   =>  '*/./././*'

For this reasons the basic compilation is not idempotent, which means that
multiple calls finally change the semantics. The following repetitive
application

.. code-block:: python
   :linenos:

    0. 'a/*/b'       =>  'a/.*/b'
    1. 'a/.*/b'      =>  'a/[.].*/b'
    2. 'a/[.].*/b'   =>  'a/[.][.].*/b'

    and so on...

leads to an unexpected result.

The windows domain requires special attention when prohibited special characters
are used in a multiple platform application.
The back-slash separator requires in general special consideration.

The following escaped characters on POSIX platforms are handled different on
Windows platforms due to the standard file systems restrictions.

.. code-block:: python
   :linenos:

   /\:*?"<>|


Resulting in the non-ambiguous compilation of:

.. code-block:: python
   :linenos:

    0. 'a\\b\\*'        =>  a wildcard, no escape for '*'
    1. 'a\\b\\?'        =>  a single character, no escape for '?'
    2. 'a\\\\b\\\\?'    =>  still the path 'a\\b\\?', no escape for '\\'

The regular expressions may contain in addition control sequences and special
terms of the *re* package. These are not yet supported.

See also *pathtools.split_re_glob*

split_re_glob
^^^^^^^^^^^^^
.. autofunction:: split_re_glob

**Description:**

The interpretation of the paramater *typeprio* resolves the ambiguity for
ambiguous syntax terms.
The ambiguous terms are syntactical present in *glob* and *re*, while in
could be even a *literal*.
The interpretation results in the assignment to the return part with
'*ret[0]*' as a *literal* or *glob* for direct resolution.
The second part '*ret[1]*' as the regular expression *re* for the filtered
resolution on of a search result.

.. code-block:: python
   :linenos:

   ret = [
      [],   # 0: resolved by glob(ret[0])
      []    # 1: resolved by the post-filtered result of glob(ret[0]/*) by ret[1]
   ]

   ret = split_re_glob(expr, typeprio=W_FULL)

The prefered assignment of terms containing the free ambiguous characters is performed in
accordance to the folowing table.


+--------+----+----+-------+--------+---+-------------------------------------+
| type   | .* | /* | [!..] | [^...] | ? | description                         |
+========+====+====+=======+========+===+=====================================+
| W_GLOB | 0  | 0  | 0     | 1      | 0 | split into prefered *glob* and *re* |
+--------+----+----+-------+--------+---+-------------------------------------+
| W_RE   | 1  | 0  | 0     | 1      | 0 | split into prefered *re* and *glob* |
+--------+----+----+-------+--------+---+-------------------------------------+

The assignment to the seconf *re* group for seacrh and filter operations could be
forced by insertion of an unambiguous *re* expression, e.g. by

.. code-block:: python
   :linenos:

   arg = "/a/b/[^^]?/c"  => [['a', 'b'],['[^^]?', 'c']]

The free characters are defined, when these are not masked.
The characters could be masked by

0. enclosing in a character class
1. escaping by '\\'
2. triple quoting ''' or """

For example by

.. code-block:: python
   :linenos:

   arg = "/a/b/[\!abc]/[.]*/\[abc\]/[\^abc]/[?]/"
   arg = "/a/b/['''!'''abc]/'''.'''*/'''[abc]'''/['''^'''abc]/'''?'''/"
   arg = '/a/b/["""!"""abc]/"""."""*/"""[abc]"""/["""^"""abc]/"""?"""/'

In case of ambiguity these could be resolved by forcing specific *re*
syntax via zero-dummy entries. For exampe:

.. code-block:: python
   :linenos:

   /a/b/[^^]{0}c/  => matches: /a/b/c/
                   => with ret = [['a', 'b'], ['[^^]{0}c']]

splitre_separator
^^^^^^^^^^^^^^^^^
.. autofunction:: splitre_separator

stripquotes
^^^^^^^^^^^
.. autofunction:: stripquotes

sub_glob_prefix
^^^^^^^^^^^^^^^
.. autofunction:: sub_glob_prefix


Exceptions
----------

PathToolsError
^^^^^^^^^^^^^^
.. autoexception:: PathToolsError

