Howto OS Data
=============

.. toctree::
   :maxdepth: 2

   howto_osdata

Get Directory with OS Configuration
-----------------------------------
The os specific common shared configuration directory could be
retrieved by the call: 

.. code-block:: pyhton
   :linenos:

   import filesysobjects.osdata
   
   filesysobjects.osdata.getdir_osconfigdata()

For complete details refer to 
[`API <osdata.html#getdir-osconfigdata>`_] / [`code <_modules/filesysobjects/osdata.html#ConfigPath.getdir_osconfigdata>`_].

Get Directory with Application Configuration
--------------------------------------------
The os specific directory to be used by applications for
context specific configuration data could be
retrieved by the call: 

.. code-block:: pyhton
   :linenos:

   import filesysobjects.osdata
   
   filesysobjects.osdata.getdir_osappconfigdata()

For complete details refer to 
[`API <osdata.html#getdir-osappconfigdata>`_] / [`code <_modules/filesysobjects/osdata.html#ConfigPath.getdir_osappconfigdata>`_].

Get Directory with Application Data
-----------------------------------
The application specific directory for configuration data could be
retrieved by the call: 

.. code-block:: pyhton
   :linenos:

   import filesysobjects.osdata
   
   filesysobjects.osdata.getdir_osappdata()

For complete details refer to 
[`API <osdata.html#getdir-osappdata>`_] / [`code <_modules/filesysobjects/osdata.html#ConfigPath.getdir_osappdata>`_].
