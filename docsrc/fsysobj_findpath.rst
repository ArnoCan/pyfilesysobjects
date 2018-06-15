.. _FSYSOBJ_FINDPATH:

fsysobj findpath
----------------

.. _SYNOPSIS_FSYSOBJFINDPATH:

SYNOPSIS:
^^^^^^^^^
.. parsed-literal::

  :ref:`fsysobj <FSYSOBJ_MAIN>` :ref:`[OPTIONS] <OPTIONS_FSYSOBJ>` :ref:`findpath <DESCRIPTION_FSYSOBJFINDPATH>` :ref:`[CMDOPTIONS] <OPTIONS_FSYSOBJFINDPATH>` :ref:`\<path-filelist\> <ARGUMENTS_FSYSOBJFINDPATH>` 

+-------------+--------------------------------------+------------------------------------------+--------------------------+
| input data  | :ref:`--search-paths <searchpaths>`, |                                          |                          |
+-------------+--------------------------------------+------------------------------------------+--------------------------+
| filter      | :ref:`--whitelist <whitelist>`,      | :ref:`--blacklist <blacklist>`,          |                          |
+-------------+--------------------------------------+------------------------------------------+--------------------------+
|             | :ref:`--timea <timea>`,              | :ref:`--timec <timec>`,                  | :ref:`--timem <mtimem>`, |
+-------------+--------------------------------------+------------------------------------------+--------------------------+
|             | :ref:`--owner <owner>`,              |                                          |                          |
+-------------+--------------------------------------+------------------------------------------+--------------------------+
|             | :ref:`--access <access>`,            |                                          |                          |
+-------------+--------------------------------------+------------------------------------------+--------------------------+
|             | :ref:`--type <type>`,                | :ref:`--hardlink-count <hardlinkcount>`, |                          |
+-------------+--------------------------------------+------------------------------------------+--------------------------+
| output data | :ref:`--format <format>`,            |                                          |                          |
+-------------+--------------------------------------+------------------------------------------+--------------------------+


.. _OPTIONS_FSYSOBJFINDPATH:

OPTIONS:
^^^^^^^^
.. index::
   single: options; --format

.. _format:

-\-format

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
   single: options; --whitelist

.. _whitelist:

-\-whitelist

.. index::
   single: options; --blacklist

.. _blacklist:

-\-blacklist

.. index::
   single: options; --search-paths

.. _searchpaths:

-\-search-paths

  Search path for JSON data file(s), standard list for current platform. ::

     --pathlist=<search-path-JSON-data>

  default:= ../dirname(__file__)/:dirname(__file__)/:/etc/:$HOME/


.. _ARGUMENTS_FSYSOBJFINDPATH:

ARGUMENTS:
^^^^^^^^^^

.. _DESCRIPTION_FSYSOBJFINDPATH:

DESCRIPTION:
^^^^^^^^^^^^
The *fsysobj* commandline interface provides access to ...

EXAMPLES:
^^^^^^^^^

SEEALSO:
^^^^^^^^
`How to CLI fsysobj <howto_cli_fsysobj.html>`_
`How to fsysobj findpath <howto_cli_fsysobj_findpath.html>`_

COPYRIGHT:
^^^^^^^^^^
Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez Copyright (C)2016-2018 Arno-Can Uestuensoez
