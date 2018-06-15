Abstract
========

The '*filesysobjects*' package provides path and name resolution, advanced search and processing
operations and arbitrary cross-conversion of addresses of file-like resources between platforms
and filesystems.

The provided standard interfaces of the *os.path* package are extended by new functions
for mixed application of local filesystem paths with UNC and URI/URL paths.
This includes the extension of literal names and *globs*, and by the embedded application 
of regular expressions provided by the *re* package.

The supported standards are [POSIX]_/[IEEE]_, [IETF]_, and 
filesystem conventions from the [MSDN]_ and [MSOSPEC]_,
for a detailed list refer to `Resources <filesysobjects_doc.html#resources>`_

The supported platforms are:

* Linux, BSD, Unix, OS-X, Cygwin, and Windows
* Python2.7+, Python3.5+

Cockpit
=======

Command Line Interface
----------------------

Commandline interface for verification and shell binding.
For basic concepts on filesystem addressing refer to
"`Filesystem Address Interfaces on Multiple Platforms <filesysobjects_multiplatform_api.html#>`_",
and 
"`Addresses for File-Like Resources <path_syntax.html#>`_".


fsysobj
^^^^^^^
.. raw:: html

   <div class="indextab">

+------------------------+-----------------------------------------+----------------------------+----------------------------+
| Command Line Interface | HowTo                                   | Call Options               | API                        |
+========================+=========================================+============================+============================+
| `fsysobj - call`_      | `HowTo Use the Command Line Interface`_ | :ref:`fsysobjCLISYNOPSIS`  | `optionparser_fsysobj.py`_ |
+------------------------+-----------------------------------------+----------------------------+----------------------------+
|                        |                                         | :ref:`fsysobjCLIOPTIONS`   |                            |
+------------------------+-----------------------------------------+----------------------------+----------------------------+
|                        |                                         | :ref:`fsysobjCLIARGUMENTS` |                            |
+------------------------+-----------------------------------------+----------------------------+----------------------------+

.. raw:: html

   </div>

pppathvar
^^^^^^^^^
.. raw:: html

   <div class="indextab">

+------------------------+---------------------------------------------+------------------------------+------------------------------+
| Command Line Interface | HowTo                                       | Call Options                 | API                          |
+========================+=============================================+==============================+==============================+
| `pppathvar - call`_    | `HowTo Pretty Print Search Path Variables`_ | :ref:`pppathvarCLISYNOPSIS`  | `optionparser_pppathvar.py`_ |
+------------------------+---------------------------------------------+------------------------------+------------------------------+
|                        |                                             | :ref:`pppathvarCLIOPTIONS`   |                              |
+------------------------+---------------------------------------------+------------------------------+------------------------------+
|                        |                                             | :ref:`pppathvarCLIARGUMENTS` |                              |
+------------------------+---------------------------------------------+------------------------------+------------------------------+

.. raw:: html

   </div>

API
---

.. raw:: html

   <div class="indextab">


+-------------------+------------------------+-----------------------------+-------------------------------------+------------------------------+
| Component         | Standards/References   | HowTo                       | Shortcuts                           | API                          |
+===================+========================+=============================+=====================================+==============================+
| `filesysobjects`_ |                        |                             | :ref:`SC_FILESYSOBJECTS`            | `filesysobjects.__init__`_   |
+-------------------+------------------------+-----------------------------+-------------------------------------+------------------------------+
| `apppath`_        | `POSIX, CIFS, URI...`_ | `HowTo Application Paths`_  | :ref:`SC_FILESYSOBJECTS_APPPATHS`   | `filesysobjects.apppaths`_   |
+-------------------+------------------------+-----------------------------+-------------------------------------+------------------------------+
| `path`_           | `POSIX, CIFS, URI...`_ | `HowTo Paths`_              | :ref:`SC_FILESYSOBJECTS_PATHS`      | `filesysobjects.paths`_      |
+-------------------+------------------------+-----------------------------+-------------------------------------+------------------------------+
| `path tools`_     | `POSIX, CIFS, URI...`_ | `HowTo Pathtools`_          | :ref:`SC_FILESYSOBJECTS_PATHTOOLS`  | `filesysobjects.pathtools`_  |
+-------------------+------------------------+-----------------------------+-------------------------------------+------------------------------+
| `pretty print`_   |                        | `HowTo Pretty Print Paths`_ | :ref:`SC_FILESYSOBJECTS_PPRINT`     | `filesysobjects.pprint`_     |
+-------------------+------------------------+-----------------------------+-------------------------------------+------------------------------+
| `user data`_      |                        | `HowTo User Data`_          | :ref:`SC_FILESYSOBJECTS_USERDATA`   | `filesysobjects.userdata`_   |
+-------------------+------------------------+-----------------------------+-------------------------------------+------------------------------+
| `os data`_        |                        | `HowTo OS Data`_            | :ref:`SC_FILESYSOBJECTS_OSDATA`     | `filesysobjects.osdata`_     |
+-------------------+------------------------+-----------------------------+-------------------------------------+------------------------------+
| `config data`_    |                        | `HowTo Config Data`_        | :ref:`SC_FILESYSOBJECTS_CONFIGDATA` | `filesysobjects.configdata`_ |
+-------------------+------------------------+-----------------------------+-------------------------------------+------------------------------+

For details refer to
"`The filesysobjects API <filesysobjects_api.html#>`_",
"`Filesystem Address Interfaces on Multiple Platforms <filesysobjects_multiplatform_api.html#>`_",
"`Addresses for File-Like Resources <path_syntax.html#>`_",
and
"`The SW-Design of filesysobjects <filesysobjects_design.html#>`_".
.

.. raw:: html

   </div>

Documents
---------

.. raw:: html

   <div class="indextab">

+------------------------+------------------------+
| Artifacts              | Shortcuts              |
+========================+========================+
| Concepts and Design    | :ref:`DEVELOPMENTDOCS` |
+------------------------+------------------------+
| Programming Interfaces | :ref:`DEVELOPMENTAPI`  |
+------------------------+------------------------+
| Example Data           | :ref:`RUNTIMETESTDATA` |
+------------------------+------------------------+

.. raw:: html

   </div>

.. _filesysobjects.__init__: filesysobjects_init.html#
.. _filesysobjects: filesysobjects_init.html#


.. _POSIX, CIFS, URI...: filesysobjects_doc.html#resources

.. _HowTo Application Paths: howto_apppaths.html
.. _HowTo Paths: howto_paths.html 
.. _HowTo Pathtools: howto_pathtools.html
.. _HowTo Pretty Print Paths: howto_pprint.html
.. _HowTo Pretty Print Search Path Variables: howto_pprint.html
.. _HowTo User Data: howto_userdata.html
.. _HowTo OS Data:  howto_osdata.html
.. _HowTo Config Data:  howto_configdata.html

.. _filesysobjects.apppaths: apppaths.html 
.. _filesysobjects.paths: paths.html
.. _filesysobjects.pathtools: pathtools.html
.. _filesysobjects.pprint: pprint.html
.. _filesysobjects.userdata: userdata.html
.. _filesysobjects.osdata: osdata.html
.. _filesysobjects.configdata: configdata.html

.. _apppath: filesysobjects_doc.html#common-path-addresses
.. _path: filesysobjects_doc.html#filesystem-paths
.. _path tools: path_syntax.html#callparamsapi
.. _pretty print: pretty_print.html#
.. _user data: user_data.html
.. _os data: os_data.html
.. _config data: config_data.html

Blueprint
=========

The 'filesysobjects' package provides address calculations for the simplified navigation in 
local and remote filesystem hierarchies.
This comprises functions for the application of object oriented patterns 
onto files, directories, and branches by various notations including multiple protocols.
In general - the application of object oriented concepts combined with advanced search patterns
onto cloud and web based distributed resources.
The support of multiple platforms in particular spans Posix based filesystems and Windows based filesystems.

The filesysobjects API adds this features to the standard libraries by introducing an abstract 
address layer.

|filesysobjectblueprint|
|filesysobjectblueprint_zoom|

.. |filesysobjectblueprint_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/filesysobject-blueprint.png
   :width: 16

.. |filesysobjectblueprint| image:: _static/filesysobject-blueprint.png
   :width: 650

The addressing support also introduces the common canonical representation for 
the supported platforms.
The overall major advances introduced by the *filesysinfo* are:

* **Base for filesystem objects - Files, Directories, and Branches**

  The package provides a set of basic functions for implementing file system items 
  conceptually as classes and objects. Just a few interfaces are required in order to represent 
  some basic OO features on filesystems. This in particular comprises superposition 
  and encapsulation, polymorphism, class and object hierachies.

* **Manage multiple search lists and support 're' and 'glob' for path search**

  Provides the creation and usage of multiple search paths including the
  full scale pattern matching on search paths by '*re*' and '*glob*' 
  [:ref:`details <SYNTAXELEMENTS>`]

* **Iterators and Context Manager**

  Provides in combination with *re* and *glob* the iteration over resource trees
  [:ref:`details <SYNTAXELEMENTS>`]

The current release of the package *filesysobjects* contains the following components.

|layersblueprint|
|layersblueprint_zoom|

.. |layersblueprint_zoom| image:: _static/zoom.png
   :alt: zoom 
   :target: _static/layers-blueprint.png
   :width: 16

.. |layersblueprint| image:: _static/layers-blueprint.png
   :width: 550

* '*apppaths*' - resolution and processing of application resource paths, with optional *globs* and *re* 
* '*configdata*' - file system locations of configuration files
* '*netfiles*' - still experimental
* '*osdata*' - file system locations of system directories
* '*paths*' - resolution and processing of file system paths, with optional *globs* and *re* 
* '*pathtools*' - dynamic sets of file system paths by search and filtering with *globs* and *re* 
* '*userdata*' - file system locations of user data

For further information on concepts, workflows, and the API see
:ref:`'Shortcuts' <shortcs>`

Table of Contents
=================
   
 
.. toctree::
   :maxdepth: 1

   shortcuts
   filesysobjects_doc
   filesysobjects_multiplatform_api
   python_encode_decode
   path_syntax
   reference_cases

   howto

   filesysobjects_design
   filesysobjects_api

   filesysobjects_init
   apppaths
   paths
   pathtools
   userdata
   osdata
   configdata
   netfiles

   FileSysObjects

   install

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* `References <references.html>`_
* :ref:`search`


Resources
=========

.. include:: project.rst

**Online Documents**

* Pythonhosted: https://pythonhosted.org/pyfilesysobjects/

**Licenses**

* Artistic-License-2.0(base license): `ArtisticLicense20.html <_static/ArtisticLicense20.html>`_

* Forced-Fairplay-Constraints(amendments): `licenses-amendments.txt <_static/licenses-amendments.txt>`_ 

  |profileinfo|  [xkcd]_ Support the OpenSource Authors :-)

  .. |profileinfo| image:: _static/profile_info.png 
     :target: _static/profile_info.html
     :width: 48

**Downloads**

* Python Package Index: https://pypi.python.org/pypi/pyfilesysobjects

* Sourceforge.net: https://sourceforge.net/projects/filesysobjects/

* github.com: https://github.com/ArnoCan/filesysobjects/


