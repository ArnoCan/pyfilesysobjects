.. _FSYSOBJ_NORMALIZE:

fsysobj normalize
-----------------

.. _SYNOPSIS_JSONDC:

SYNOPSIS:
^^^^^^^^^
.. parsed-literal::

  :ref:`fsysobj <FSYSOBJ_MAIN>` :ref:`[OPTIONS] <OPTIONS_FSYSOBJ>` :ref:`normalize <DESCRIPTION_FSYSOBJNORMALIZE>` :ref:`[CMDOPTIONS] <OPTIONS_FSYSOBJNORMALIZE>` :ref:`\<path-filelist\> <ARGUMENTS_FSYSOBJNORMALIZE>` 

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

.. _OPTIONS_FSYSOBJNORMALIZE:

OPTIONS:
^^^^^^^^
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


.. _ARGUMENTS_FSYSOBJNORMALIZE:

ARGUMENTS:
^^^^^^^^^^

.. _DESCRIPTION_FSYSOBJNORMALIZE:

DESCRIPTION:
^^^^^^^^^^^^
The *fsysobj* commandline interface provides access to ...

EXAMPLES:
^^^^^^^^^

SEEALSO:
^^^^^^^^
`How to CLI fsysobj <howto_cli_fsysobj.html>`_
`How to fsysobj normalize <howto_cli_fsysobj_normalize.html>`_

COPYRIGHT:
^^^^^^^^^^
Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez Copyright (C)2016-2018 Arno-Can Uestuensoez
