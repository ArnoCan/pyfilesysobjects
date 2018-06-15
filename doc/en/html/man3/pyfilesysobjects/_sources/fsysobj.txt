.. _FSYSOBJ_MAIN:

fsysobj
-------

.. _SYNOPSIS_JSONDC:

SYNOPSIS:
^^^^^^^^^
.. parsed-literal::

   :ref:`fsysobj <FSYSOBJ_MAIN>`           :ref:`[OPTIONS] <OPTIONS_FSYSOBJ>` [COMMAND] [CMDOPTIONS] <path-filelist> 
   python :ref:`fsysobj.py <FSYSOBJ_MAIN>` :ref:`[OPTIONS] <OPTIONS_FSYSOBJ>` [COMMAND] [CMDOPTIONS] <path-filelist> 

**Commands**

+--------------------------------------+-----------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------+------------------------------------------------------------------+
| [COMMAND]                            | Context Options                                     | Arguments                                                       | Description                                                 | HowTo                                                            |
+======================================+=====================================================+=================================================================+=============================================================+==================================================================+
| :ref:`find <FSYSOBJ_FIND>`           | :ref:`find-options <OPTIONS_FSYSOBJFIND>`           | :ref:`\<find-path-filelist\> <ARGUMENTS_FSYSOBJFIND>`           | :ref:`find-description <DESCRIPTION_FSYSOBJFIND>`           | `Howto fsysobject find <howto_cli_fsysobj_find.html>`_           |
+--------------------------------------+-----------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------+------------------------------------------------------------------+
| :ref:`findpath <FSYSOBJ_FINDPATH>`   | :ref:`findpath-options <OPTIONS_FSYSOBJFINDPATH>`   | :ref:`\<findpath-file-path-list\> <ARGUMENTS_FSYSOBJFINDPATH>`  | :ref:`findpath-description <DESCRIPTION_FSYSOBJFINDPATH>`   | `Howto fsysobject findpath <howto_cli_fsysobj_findpath.html>`_   |
+--------------------------------------+-----------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------+------------------------------------------------------------------+
| :ref:`lspath <FSYSOBJ_LSPATH>`       | :ref:`lspath-options <OPTIONS_FSYSOBJLSPATH>`       | :ref:`\<lspath-path-filelist\> <ARGUMENTS_FSYSOBJLSPATH>`       | :ref:`lspath-description <DESCRIPTION_FSYSOBJLSPATH>`       | `Howto fsysobject lspath <howto_cli_fsysobj_lspath.html>`_       |
+--------------------------------------+-----------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------+------------------------------------------------------------------+
| :ref:`normalize <FSYSOBJ_NORMALIZE>` | :ref:`normalize-options <OPTIONS_FSYSOBJNORMALIZE>` | :ref:`\<normalize-path-filelist\> <ARGUMENTS_FSYSOBJNORMALIZE>` | :ref:`normalize-description <DESCRIPTION_FSYSOBJNORMALIZE>` | `Howto fsysobject normalize <howto_cli_fsysobj_normalize.html>`_ |
+--------------------------------------+-----------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------+------------------------------------------------------------------+
| :ref:`expand <FSYSOBJ_EXPAND>`       | :ref:`expand-options <OPTIONS_FSYSOBJEXPAND>`       | :ref:`\<expand-path-filelist\> <ARGUMENTS_FSYSOBJEXPAND>`       | :ref:`expand-description <DESCRIPTION_FSYSOBJEXPAND>`       | `Howto fsysobject expand <howto_cli_fsysobj_expand.html>`_       |
+--------------------------------------+-----------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------+------------------------------------------------------------------+
| :ref:`mkpath <FSYSOBJ_MKPATH>`       | :ref:`mkpath-options <OPTIONS_FSYSOBJMKPATH>`       | :ref:`\<mkpath-path-filelist\> <ARGUMENTS_FSYSOBJMKPATH>`       | :ref:`mkpath-description <DESCRIPTION_FSYSOBJMKPATH>`       | `Howto fsysobject mkpath <howto_cli_fsysobj_mkpath.html>`_       |
+--------------------------------------+-----------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------+------------------------------------------------------------------+
| :ref:`convert <FSYSOBJ_CONVERT>`     | :ref:`convert-options <OPTIONS_FSYSOBJCONVERT>`     | :ref:`\<convert-path-filelist\> <ARGUMENTS_FSYSOBJCONVERT>`     | :ref:`convert-description <DESCRIPTION_FSYSOBJCONVERT>`     | `Howto fsysobject convert <howto_cli_fsysobj_convert.html>`_     |
+--------------------------------------+-----------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------+------------------------------------------------------------------+
| :ref:`config <FSYSOBJ_CONFIG>`       | :ref:`config-options <OPTIONS_FSYSOBJCONFIG>`       | :ref:`\<convert-path-filelist\> <ARGUMENTS_FSYSOBJCONVERT>`     | :ref:`convert-description <DESCRIPTION_FSYSOBJCONVERT>`     | `Howto fsysobject config <howto_cli_fsysobj_config.html>`_       |
+--------------------------------------+-----------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------+------------------------------------------------------------------+
| :ref:`os <FSYSOBJ_OS>`               | :ref:`os-options <OPTIONS_FSYSOBJOS>`               | :ref:`\<convert-path-filelist\> <ARGUMENTS_FSYSOBJCONVERT>`     | :ref:`convert-description <DESCRIPTION_FSYSOBJCONVERT>`     | `Howto fsysobject os <howto_cli_fsysobj_os.html>`_               |
+--------------------------------------+-----------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------+------------------------------------------------------------------+
| :ref:`user <FSYSOBJ_USER>`           | :ref:`user-options <OPTIONS_FSYSOBJUSER>`           | :ref:`\<convert-path-filelist\> <ARGUMENTS_FSYSOBJCONVERT>`     | :ref:`convert-description <DESCRIPTION_FSYSOBJCONVERT>`     | `Howto fsysobject user <howto_cli_fsysobj_user.html>`_           |
+--------------------------------------+-----------------------------------------------------+-----------------------------------------------------------------+-------------------------------------------------------------+------------------------------------------------------------------+

.. _OPTIONS_FSYSOBJ:

OPTIONS:
^^^^^^^^
.. index::
   single: options; --appname

.. _appname:

-a --appname
  Name of application. Used for deafults, e.g. configuration file names. :: 

     --appname=<appname>

  default: jsondc

.. index::
   single: options; --configfile

.. _configfile:

-c --configfile
  A single configuration file, see inline comments for details::

     --configfile=<configfile>

  default: jsondc.ini

  The search path for the configuration file is: ::

  0. Environment variable as search path *JSONDATA_PATH*.
  1. User app data, see
     *filesysobjects.osdata.getdir_userappdata()* [filesysobjects]_.
  2. User config data, see
     *filesysobjects.osdata.getdir_userconfigdata()* [filesysobjects]_.
  3. OS config data, see 
     *filesysobjects.osdata.getdir_osconfigdata()* [filesysobjects]_.
  4. Install directory of the package, see 
     *pysourceinfo.fileinfo.getcaller_pathname()* [sourceinfo]_.

.. index::
   single: options; --debug

.. _debug:

-d --debug
  Debug entries, does NOT work with 'python -O ...'.
  Developer output, aimed for filtering.
  When provided mulltiple times the level is raised.

.. index::
   single: options; --help

.. _help:

-h --help
  This help.

.. index::
   single: options; --no-default-path

.. _nodefaultpath:

-n --no-default-path
  Supress load of default path.

  default: False

.. index::
   single: options; --pathlist

.. _pathlist:

-p --pathlist
  Search path for JSON data file(s), standard list for current platform. ::

     --pathlist=<search-path-JSON-data>

  default:= ../dirname(__file__)/:dirname(__file__)/:/etc/:$HOME/

.. index::
   single: options; --print-data

.. _printdata:

-\-print-data
  Pretty print data. ::

     --print-data[=<format>]

       format := (
           'json-line'      # all in one line with JSON syntax
         | 'json-struct'    # tree-structure with JSON syntax
         | 'python-line'    # all in one line with Python syntax
         | 'python-struct'  # tree-structure  with Python syntax
         | 'repr'           # repr() - raw string, Python syntax
         | 'str'            # str() - formatted string, Python syntax
       )

.. index::
   single: options; --selftest

.. _selftest:

-\-selftest
  Performs a basic functional selftest by load, verify, and validate.

  0. jsondata/data.json + jsondata/schema.jsd
  1. jsondata/selftest.json + jsondata/selftest.jsd

.. index::
   single: options; --Version

.. _versiondetails:

-\-Version
  Current version - detailed.

.. index::
   single: options; --verbose

.. _verbose:

-v --verbose
  Verbose, some relevant states for basic analysis.
  When *--selftest* is set, repetition raises the display level.

.. index::
   single: options; --version

.. _version:

-\-version
  Current version - terse.

.. _DESCRIPTION_JSONDC:

DESCRIPTION:
^^^^^^^^^^^^
The *fsysobj* executable provides the commandline interface to the filesys objects library.

EXAMPLES:
^^^^^^^^^

SEEALSO:
^^^^^^^^
`How to CLI jsondc <howto_cli_fsysobj.html>`_

COPYRIGHT:
^^^^^^^^^^
Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez Copyright (C)2016-2018 Arno-Can Uestuensoez
