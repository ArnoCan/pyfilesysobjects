Howto Application Paths
=======================

.. toctree::
   :maxdepth: 2

   howto_apppaths

Apppaths manages common URI paths including general application schemes like *http*.
For local filesytem and network filesystem related paths refer
to the module `filesysobjects.paths <paths.html#>`_.
or the `Howto Paths <howto_paths.html#>`_.

General Type Support for Normalization
--------------------------------------
The module *filesysobjects.apppaths* extends the modules *filesysobjects.paths* by
common URI paths.
This includes provided basic standard application shemes, which could be easily
extended by custom URIs.

The *os.normpath()* interface provides the normalization of file 
system addresses for the current specific platform, while the
packages *macpath*, *ntpath*, and *posixpath* provide for cross-platform
normalization.
These cover some specifics of their target filesystems, but focus
on pure filesystem entries only.

The *filesysobjects.apppaths.normapppathx* interface extends these by *URI*s
covers all platforms including cross-platform normalization.
The current release covers the types: ::

   types := ('share', 'ldsys', 'rfsys', 'lfsys', 'smb', 'http', 'https')

* *file* - file URI - [RFC8089]_
* *http* - URI http - [RFC3986]_
* *https* - URI https - [RFC3986]_
* *ldsys* - local drive based filesystems - FAT, NTFS
* *lfsys* - local filesystems
* *rfsys* - remote filesystem
* *share* - network shares - on all platforms
* *smb* - Server Message Block filesystems, includ *CIFS* - [SMB]_
* *uri* - Currently hyper text by *HTTP* and *HTTPS*

The *normapppathx* interface in particular provides the *os.pathsep*
of the common search path syntax.
The call interface is exchangeable with the standard interface 'os.normpath'.

.. code-block:: python
   :linenos:

   path_normalized = filesysobjects.paths.normapppathx(path_raw)

For complete details refer to 
[`API <apppaths.html#normapppathx>`_] / [`code <_modules/filesysobjects/apppaths.html#normapppathx>`_].

Normalize Application Paths
---------------------------
The *normapppath* interface provides the intermixed crossplatform filesystem paths
and URIs with various application schemes.
This includes also the support of search paths.

POSIX
^^^^^
The local filesystem path could easily be converted into a file URI in
accordance to [RFC8089]_ by the call.

.. code-block:: python
   :linenos:

   arg = '/my/odd/searchpath/"""[/xyz].*"""/myfile.z'

   res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=True,     # activate application prefix
            spf='posix',     # source platform POSIX, default is local platform
            tpf='fileuri',   # target platform FILEURI, default is local platform
            strip=True,      # strip null-entries
            )
 
resulting in:
  
.. code-block:: python
   :linenos:

   arg = '/my/odd/searchpath/"""[/xyz].*"""/myfile.z'
   res = 'file:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'

The reverse conversion is similar by altering the option '*apppre*'

.. code-block:: python
   :linenos:

   arg = 'file:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'

   res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=False,    # deactivate application prefix
            spf='fileuri',   # target platform FILEURI, default is local platform
            tpf='posix',     # source platform POSIX, default is local platform
            strip=True,      # strip null-entries
            )
 
results in:
  
.. code-block:: python
   :linenos:

   arg = 'file:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'
   res = '/my/odd/searchpath/"""[/xyz].*"""/myfile.z'

Refer to the default values for a shorter call signature 
[`API <apppaths.html#normapppathx>`_] / [`code <_modules/filesysobjects/apppaths.html#normapppathx>`_].

Windows
^^^^^^^
The local filesystem path could easily be converted into a file URI in
accordance to [RFC8089]_ by the call.

.. code-block:: python
   :linenos:

   arg = r'\my\odd\searchpath\"""[/xyz].*"""\myfile.z'

   res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=True,     # activate application prefix
            spf='win',     # source platform Windows, default is local platform
            tpf='fileuri',   # target platform FILEURI, default is local platform
            strip=True,      # strip null-entries
            )
 
resulting in:
  
.. code-block:: python
   :linenos:

   arg = r'\my\odd\searchpath\"""[/xyz].*"""\myfile.z'
   res = 'file:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'

The reverse conversion is similar by altering the option '*apppre*'

.. code-block:: python
   :linenos:

   arg = 'file:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'

   res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=True,     # activate application prefix
            spf='fileuri',   # target platform FILEURI, default is local platform
            tpf='win',       # source platform Windows, default is local platform
            strip=True,      # strip null-entries
            )
 
results in:
  
.. code-block:: python
   :linenos:

   arg = 'file:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'
   res = r'\my\odd\searchpath\"""[/xyz].*"""\myfile.z'

Refer to the default values for a shorter call signature 
[`API <apppaths.html#normapppathx>`_] / [`code <_modules/filesysobjects/apppaths.html#normapppathx>`_].

UNC-Shares and Network POSIX-Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The UNC network shared and POSIX network application paths could easily cross-converted.

.. code-block:: python
   :linenos:

   arg = r'\\my\odd\searchpath\"""[/xyz]""".*\myfile.z'

   res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=True,     # activate application prefix
            spf='win',       # source platform Windows, default is local platform
            tpf='posix',     # target platform POSIX, default is local platform
            strip=True,      # strip null-entries
            )
 
resulting in:
  
.. code-block:: python
   :linenos:

   arg = r'\\my\odd\searchpath\"""[/xyz].*"""\myfile.z'
   res = r'//my/odd/searchpath/"""[/xyz].*"""/myfile.z'

The reverse conversion is similar by altering the option '*apppre*'

.. code-block:: python
   :linenos:

   arg = r'//my/odd/searchpath/"""[/xyz].*"""/myfile.z'

   res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=True,     # activate application prefix
            spf='posix',     # target platform FILEURI, default is local platform
            tpf='win',       # source platform POSIX, default is local platform
            strip=True,      # strip null-entries
            )
 
results in:
  
.. code-block:: python
   :linenos:

   arg = r'//my/odd/searchpath/"""[/xyz].*"""/myfile.z'
   res = r'\\my\odd\searchpath\"""[/xyz].*"""\myfile.z'

Refer to the default values for a shorter call signature 
[`API <apppaths.html#normapppathx>`_] / [`code <_modules/filesysobjects/apppaths.html#normapppathx>`_].

HTTP
^^^^
The local filesystem path could easily be converted into a http URI in
accordance to [RFC3869]_ by the call.

.. code-block:: python
   :linenos:

   arg = r'\my\odd\searchpath\"""[/xyz].*"""\myfile.z'

   res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=True,     # activate application prefix
            spf='win',       # source platform Windows, default is local platform
            tpf='http',      # target platform FILEURI, default is local platform
            strip=True,      # strip null-entries
            )
 
resulting in:
  
.. code-block:: python
   :linenos:

   arg = r'\my\odd\searchpath\"""[/xyz].*"""\myfile.z'
   res = 'http:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'

The reverse conversion is similar by altering the option '*apppre*'

.. code-block:: python
   :linenos:

   arg = 'http:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'

   res = filesysobjects.apppaths.normapppathx(
            arg,             # the path to be converted
            apppre=True,     # activate application prefix
            spf='http',      # target platform FILEURI, default is local platform
            tpf='win',       # source platform Windows, default is local platform
            strip=True,      # strip null-entries
            )
 
results in:
  
.. code-block:: python
   :linenos:

   arg = 'http:///my/odd/searchpath/"""[/xyz].*"""/myfile.z'
   res = r'\my\odd\searchpath\"""[/xyz].*"""\myfile.z'

Refer to the default values for a shorter call signature 
[`API <apppaths.html#normapppathx>`_] / [`code <_modules/filesysobjects/apppaths.html#normapppathx>`_].

Split Application Paths
-----------------------
Similar to *paths.splitpathx*

For complete details refer to 
[`API <apppaths.html#splitapppathx>`_] / [`code <_modules/filesysobjects/apppaths.html#splitapppathx>`_].

POSIX
^^^^^

Windows
^^^^^^^

HTTP
^^^^

UNC-Shares and Network POSIX-Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
