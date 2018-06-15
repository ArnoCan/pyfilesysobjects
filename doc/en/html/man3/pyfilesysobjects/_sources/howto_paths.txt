Howto Paths
===========

.. toctree::
   :maxdepth: 2

   howto_paths

The *filesysobjects.paths* module manages files and file related application schemes only.
For URI paths including general application schemes like *http* refer
to the module `filesysobjects.apppaths <apppaths.html#>`_
or the `Howto Appaths <howto_apppaths.html#>`_.

Normalize Paths by *normpathx*
------------------------------
The *os.normpath()* interface provides the normalization of file 
system addresses for the current specific platform, while the
packages *macpath*, *ntpath*, and *posixpath* provide for cross-platform
normalization.
These cover some specifics of their target filesystems, but focus
on pure filesystem entries only.

The *filesysobjects.paths.normpathx* interface covers all platforms including
cross-platform normalization.
This includes network filesystems including application and domain prefixes
for *POSIX* and *UNC*.
The provided options enable the filesystem related URIs of type *file://*.

The call interface is exchangeable with the standard interfaces:

.. code-block:: python
   :linenos:

   path_normalized = filesysobjects.paths.normpathx(path_raw)

   path_normalized = filesysobjects.paths.normpathx(path_raw, tpf='local')  # local filesystem
   path_normalized = filesysobjects.paths.normpathx(path_raw, tpf='posix')  # posix - Linux, MacOS, Unix
   path_normalized = filesysobjects.paths.normpathx(path_raw, tpf='win')    # Windows - NTFS, FATxx
   path_normalized = filesysobjects.paths.normpathx(path_raw, keepsep=True) # keeps trailing seperator

For complete details refer to 
[`API <paths.html#normpathx>`_] / [`code <_modules/filesysobjects/paths.html#normpathx>`_].

Convert 'os.path.sep' / 'os.sep'
--------------------------------
The path separator 'os.path.sep', or for short 'os.sep' cold be seamlessly
converted between all platforms.
The cross-conversion itself is platform independent when the source platform *spf*,
and/or the target platform *tpf* are selected by call parameters.
The conversion is either literally, where no null-direcotry entries are stripped off,
or by stripping the path from redundnacies to the resulting shortest representation.
 
Posix to Windows
^^^^^^^^^^^^^^^^
The raw representation of a POSIX network application path:

.. code-block:: python
   :linenos:

   arg = '//hostname/tests//////a/b/hostname//c////////d/tests/b///c'

could be simply normalized by the call:

.. code-block:: python
   :linenos:

   res = filesysobjects.paths.normpathx(
      arg, 
      spf='posix',  # source platform
      tpf='win',    # target platform
      strip=True    # this is the default
   )

to the representation:

.. code-block:: python
   :linenos:

   arg = r'//hostname/tests//////a/b/hostname//c////////d/tests/b///c'
   res = r'\\hostname\tests\a\b\hostname\c\d\tests\b\c'

When the conversion of the *os.sep* is required only, the call:

.. code-block:: python
   :linenos:

   res = filesysobjects.paths.normpathx(
      arg, 
      spf='posix',  # source platform
      tpf='win',    # target platform
      strip=False   # suppress reduction
   )

results in:

.. code-block:: python
   :linenos:

   arg = r'//hostname/tests//////a/b/hostname//c////////d/tests/b///c'
   res = r'\\hostname\tests\\\\\\a\b\hostname\\c\\\\\\\\d\tests\b\\\c'

Windows to Posix
^^^^^^^^^^^^^^^^

The raw representation of a Windows share path:

.. code-block:: python
   :linenos:

   arg = r'\\hostname\tests\\\\\\a\b\hostname\\c\\\\\\\\d\tests\b\\\c'

could be simply normalized by the call:

.. code-block:: python
   :linenos:

   res = filesysobjects.paths.normpathx(
      arg, 
      spf='win',   # source platform
      tpf='posix', # target platform
      strip=True   # this is the default
   )

to the representation:

.. code-block:: python
   :linenos:

   arg = r'\\hostname\tests\\\\\\a\b\hostname\\c\\\\\\\\d\tests\b\\\c'
   res = r'//hostname/tests/a/b/hostname/c/d/tests/b/c'

When the conversion of the *os.sep* is required only without reduction, the call:

.. code-block:: python
   :linenos:

   res = filesysobjects.paths.normpathx(
      arg, 
      spf='posix',  # source platform
      tpf='win',    # target platform
      strip=False   # suppress reduction
   )

results in:

.. code-block:: python
   :linenos:

   arg = r'\\hostname\tests\\\\\\a\b\hostname\\c\\\\\\\\d\tests\b\\\c'
   res = r'//hostname/tests//////a/b/hostname//c////////d/tests/b///c'


Escape and Unescape Arbitrary Paths
-----------------------------------
The following variants of escaping and unescaping of path strings are supported.

+--------------------------+-----------------------------+-------+-----+
| scope                    |                             | POSIX | win |
+==========================+=============================+=======+=====+
| Python Escape Characters | \\a \\b \\f \\n \\r \\t \\v |       |     |
+--------------------------+-----------------------------+-------+-----+
| backslash                | \\                          |       |     |
+--------------------------+-----------------------------+-------+-----+
| os.path.sep / os.sep     |                             | /     | \\  |
+--------------------------+-----------------------------+-------+-----+
| custom characters        |                             |       |     |
+--------------------------+-----------------------------+-------+-----+

With the following parameters for the interfaces.

+------------------+-------------+--------------------------+-----------+---------+
| scope            | option      | Python Escape Characters | backslash | default |
+==================+=============+==========================+===========+=========+
| `escapepathx`_   | force=True  | X                        | X         |         |
+------------------+-------------+--------------------------+-----------+---------+
|                  | force=False | X                        |           | X       |
+------------------+-------------+--------------------------+-----------+---------+
| `unescapepathx`_ | force=True  | X                        | X         | X       |
+------------------+-------------+--------------------------+-----------+---------+
|                  | force=False |                          | X         |         |
+------------------+-------------+--------------------------+-----------+---------+

.. _escapepathx: paths.html#escapepathx
.. _unescapepathx: paths.html#unescapepathx

In addition parts of the path string could be protected from escaping and unescaping by quotes,
with the interface

.. parsed-literal::

   `filesysobjects.pathtools.stripquotes() <pathtools.html#stripquotes>`_

for the final remove of the quotes.

Escape File Path Names
^^^^^^^^^^^^^^^^^^^^^^
The escaping of file path names is required in various scenes,
but in particular on Windows platforms. 
This is even more required, when *globs* and *re* are included in the path string.
The *filesysobjects* solves this with a minimal remaining fuzz.

The escaping inlcudes the support for regular expressions such as

.. code-block:: python
   :linenos:

   /my/odd/searchpath/[/xyz].*/myfile.z

   \my\odd\searchpath\[\\xyz].*\myfile.z

Which is here a regular expression to be applied on full pathnames including
paths separators.

The syntax allows for quoting and unquoting in Python style by triple-quotes.

.. code-block:: python
   :linenos:

   /my/odd/searchpath/"""[/xyz].*"""/myfile.z
   /my/odd/searchpath/'''[/xyz].*'''/myfile.z


The basic call is:

.. code-block:: python
   :linenos:

   path = '\my\odd\searchpath\a\b\c\[\\xyz].*\myfile.z'

   res = filesysobjects.paths.escapepathx(path)

resulting in:

.. code-block:: python
   :linenos:

   path = '\my\odd\searchpath\a\b\c\[\\xyz].*\myfile.z'
   res  = '\my\odd\searchpath\\a\\b\c\[\\xyz].*\myfile.z'

The basic call escapes the known Python escape-characters by default.
Regular expressions regularly require the escaping of additional characters.
The option '*all*' or '*force*' add the escape of all backslashes to the 
known escape characters. 

.. code-block:: python
   :linenos:

   path = '\my\odd\searchpath\a\b\c\[\\xyz].*\myfile.z'

   res = filesysobjects.paths.escapepathx(
      path,
      all=True   # default is False
      )

resulting in:

.. code-block:: python
   :linenos:

   path = '\my\odd\searchpath\a\b\c\[\\xyz].*\myfile.z'
   res  = '\\my\\odd\\searchpath\\a\\b\\c\\[\\xyz].*\\myfile.z'


For complete details refer to 
[`API <paths.html#escapepathx>`_] / [`code <_modules/filesysobjects/paths.html#escapepathx>`_].

Unescape File Path Names
^^^^^^^^^^^^^^^^^^^^^^^^
The unescaping of file path names reverses the escaping.
The unescaping includes the support for regular expressions such as

.. code-block:: python
   :linenos:

   /my/odd/searchpath/[\\/xyz].*/myfile.z

   \my\odd\searchpath\[\\xyz].*\myfile.z

Which is here a regular expression to be applied on full pathnames including
paths separators.

The syntax allows for quoting and unquoting in Python style by triple-quotes.

.. code-block:: python
   :linenos:

   /my/odd/searchpath/"""[/xyz].*"""/myfile.z
   /my/odd/searchpath/'''[/xyz].*'''/myfile.z

The basic call is:

.. code-block:: python
   :linenos:

   path  = '\my\odd\searchpath\\a\\b\c\[\\xyz].*\myfile.z'

   res = filesysobjects.paths.unescapepathx(path)

resulting in:

.. code-block:: python
   :linenos:

   path = '\my\odd\searchpath\\a\\b\c\[\\xyz].*\myfile.z'
   res  = '\my\odd\searchpath\a\b\c\[\\xyz].*\myfile.z'

The basic call unescapes all possible escape sequences as supported 
by the *escapepathx* call with active *force* option.
This includes the known Python escape-characters as well as any 
non-quoted double back-shlashes. 
The option '*all*' or '*force*' controls the degree of the unescape.

The default call is set to *force=True* for the maximum:

.. code-block:: python
   :linenos:

   path = '\\my\\odd\\searchpath\\a\\b\\c\\"""[\\xyz].*"""\\myfile.z'

   res = filesysobjects.paths.escapepathx(path)

results in:

.. code-block:: python
   :linenos:

   path = '\\my\\odd\\searchpath\\a\\b\\c\\"""[\\xyz].*"""\\myfile.z'
   res  = '\my\odd\searchpath\a\b\c\"""[\\xyz].*"""\myfile.z'

For the removal of the quotes call:

.. code-block:: python
   :linenos:

   res = filesysobjects.pathtools.stripquote(res)
   res  = '\my\odd\searchpath\a\b\c\"""[\\xyz].*"""\myfile.z'

Results in:

.. code-block:: python
   :linenos:

   res  = '\my\odd\searchpath\a\b\c\[\\xyz].*\myfile.z'



The following call limits the unescape default call:

.. code-block:: python
   :linenos:

   path = '\\my\\odd\\searchpath\\a\\b\\c\\[\\xyz].*\\myfile.z'

   res = filesysobjects.paths.escapepathx(
      path,
      all=True   # default is False
      )

resulting in:

.. code-block:: python
   :linenos:

   path = '\\my\\odd\\searchpath\\a\\b\\c\\[\\xyz].*\\myfile.z'
   res  = '\my\odd\searchpath\a\b\c\[\\xyz].*\myfile.z'

For complete details refer to 
[`API <paths.html#unescapepathx>`_] / [`code <_modules/filesysobjects/paths.html#unescapepathx>`_].

Idempotence of Escape-Unescape Sequences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The escape-unescape sequence is not idempotent in general.
This is due to the possiblility of present manual escapes as well
as a mixed-up of separators within the raw path string.
The reverse escaping may e.g. drop the previous present manual
escapes.
Thus the escape-unescape sequence is idempotent inly in case of a complete control
of the escape sequences, and without additional calls like normalization or unquoting.

Split Paths into Directory Items and Files
------------------------------------------
The excessive processing of file path names by traversing over directories
requires frequently the split of the path into its node names components.
This becomes quickly as challanging when *globs* and *re* are involved.
The *filesysobjects* solves this with a minimal remaining fuzz.

The split includes the support for regular expressions same as the other interfaces

.. code-block:: python
   :linenos:

   /my/odd/searchpath/[/xyz].*/myfile.z

   \my\odd\searchpath\[\\xyz].*\myfile.z

Which is here a regular expression to be applied on full pathnames including
paths separators.

The syntax allows for quoting and unquoting in Python style by triple-quotes,
just can spare parts of the path transparently from the split operation.

.. code-block:: python
   :linenos:

   # POSIX
   /my/odd/searchpath/"""this/part/is/spared/[/xyz].*/to/this/point"""/myfile.z
   /my/odd/searchpath/'''this/part/is/spared/[/xyz].*/to/this/point'''/myfile.z

   # Windows
   \my\odd/searchpath\"""this\part\is\spared\[\\xyz].*\to\this\point"""\myfile.z
   \my\odd\searchpath\'''this\part\is\spared\[/xyz].*\to\this\point'''\myfile.z


The basic call:

.. code-block:: python
   :linenos:

   path = '/my/odd/searchpath/"""this/part/is/spared/[/xyz].*/to/this/point"""/myfile.z'

   res = filesysobjects.paths.splitpathx(path)

results in - with kept quotes:

.. code-block:: python
   :linenos:

   path = '/my/odd/searchpath/"""this/part/is/spared/[/xyz].*/to/this/point"""/myfile.z'

   res = [
      '', 'my', 'odd', 'searchpath', '"""this/part/is/spared/[/xyz].*/to/this/point"""', 'myfile.z'
   ]

The call including the option *stripquotes*:

.. code-block:: python
   :linenos:

   path = '/my/odd/searchpath/"""this/part/is/spared/[/xyz].*/to/this/point"""/myfile.z'

   res = filesysobjects.paths.splitpathx(
      path,
      stripquotes=True  # default is False
      )

results in:

.. code-block:: python
   :linenos:

   path = '/my/odd/searchpath/"""this/part/is/spared/[/xyz].*/to/this/point"""/myfile.z'

   res = [
      '', 'my', 'odd', 'searchpath', 'this/part/is/spared/[/xyz].*/to/this/point', 'myfile.z'
   ]

For complete details refer to 
[`API <paths.html#splitpathx>`_] / [`code <_modules/filesysobjects/paths.html#splitpathx>`_].


