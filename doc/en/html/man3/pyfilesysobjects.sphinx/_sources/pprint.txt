'filesysobjects.pprint' - Module
================================

The *filesysobjects.pprint* module provides pretty printer for paths.


Module
------

.. automodule:: filesysobjects.pprint

.. role:: raw-html(raw)
   :format: html

Classes
-------

PPPathVar
^^^^^^^^^
Features
""""""""
The class *PPPathVar* creates formatted printable strings for search path variables.
The provided output formats comprise screen display formats and output strings of
various data representation syntaxes such as *JSON*, *XML*, and *YAML*.
The search path is therefore split into it's entries and formatted in order
to display and/or integrate the data into larger data structures. 

The output string of the following input demonstrates the available
output variants: ::

  posix: path = "/path/entry/0:/path/entry/1"
  win32: path = "\\path/entry\\0;\\path\\entry\\1" 

* **format=console**

  The conversion results by default in the output of 'format=console':
  
  .. parsed-literal::
   
     |   MYPATH = [
     |       "/path/entry/0",
     |       "/path/entry/1",
     |   ]
     |
     ^ left paper border

  The settings of the output parameters were:
   
  .. parsed-literal::

     |...MYPATH = [
     |...::::"/path/entry/0",
     |...::::"/path/entry/1",
     |...]
     |
     ^ left paper border

  with the parameters:

  .. parsed-literal::
   
     <format>:         the output format, here 'format="console"'
     'MYPATH':         the prefix, here 'prefix=MYPATH'
     '=':              the assignchar, here 'assignchar="="'
     "/path/entry/0":  first path entry
     "/path/entry/1":  second path entry
     '.' * n:          'n' offset, here n=3 - 'offset=3' 
     '.':              offsetchar, here 'offsetchar="."'
     ':' * m:          'm' indent, here m=4 - 'indent=4' 
     ':':              indentchar, here 'indentchar=":"'

* **format=ini**

  The same input results for the output 'format=INI' [multiconf]_ in:

  .. parsed-literal::

     |   MYPATH = /path/entry/0 /path/entry/1
     |
     ^ left paper border

     offsetchar := ' '  # space
     indentchar := ' '  # space
     pathsep    := ' '  # space

  Does not require specific support of the parser.

* **format=inix0**

  The same input results for the output 'format=INIX' [multiconf]_ in:

  .. parsed-literal::

     |   MYPATH = 
     |       :/path/entry/0
     |       :/path/entry/1
     |
     ^ left paper border

     offsetchar := ' '  # space
     indentchar := ' '  # space

  Requires the support of the *INI* file parser, e.g. see [multiconf]_.

* **format=inix1**

  The same input results for the special output 'format=INIX1' [multiconf]_ in:

  .. parsed-literal::

     |   MYPATH = /path/entry/0
     |   MYPATH = /path/entry/1
     |
     ^ left paper border

     offsetchar := ' '  # space
     indentchar := ' '  # space

  Requires the support of the *INI* file parser, e.g. see [multiconf]_.

* **format=inix2**

  The same input results for the special output 'format=INIX2' [multiconf]_ in:

  .. parsed-literal::

     |   MYPATH0 = /path/entry/0
     |   MYPATH1 = /path/entry/1
     |
     ^ left paper border

     offsetchar := ' '  # space
     indentchar := ' '  # space

  Does not require specific support of the parser.

* **format=json**

  The same input for output 'format=JSON':

  .. parsed-literal::

     |   "MYPATH": [
     |       "/path/entry/0",
     |       "/path/entry/1"
     |   ]
     |
     ^ left paper border

     offsetchar := ' '  # space
     indentchar := ' '  # space

* **format=python**

  The same input for output 'format=python'.
  This format is a synonym for 'format=json'.

  .. parsed-literal::

     |   "MYPATH": [
     |       "/path/entry/0",
     |       "/path/entry/1"
     |   ]
     |
     ^ left paper border

     offsetchar := ' '  # space
     indentchar := ' '  # space

* **format=xml**

  The same input for output 'format=XML': 

  .. parsed-literal::

     |   <MYPATH>
     |       <entry idx=0>/path/entry/0</entry>
     |       <entry idx=1>/path/entry/1</entry>
     |   </MYPATH>
     |
     ^ left paper border

     offsetchar := ' '  # space
     indentchar := ' '  # space

* **format=yaml**

  The same input for output 'format=YAML':

  .. parsed-literal::

     |   MYPATH:
     |       - /path/entry/0
     |       - /path/entry/1
     |
     ^ left paper border

     offsetchar := ' '  # space
     indentchar := ' '  # space

Class
"""""
.. autoclass:: PPPathVar

Methods
"""""""

__init__
''''''''
.. automethod:: PPPathVar.__init__

__str__
'''''''
.. automethod:: PPPathVar.__str__

__repr__
''''''''
.. automethod:: PPPathVar.__repr__

Exceptions
----------

PathToolsError
^^^^^^^^^^^^^^
.. autoexception:: filesysobjects.PrettyPrintError

