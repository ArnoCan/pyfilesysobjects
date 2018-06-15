Howto User Data
===============

.. toctree::
   :maxdepth: 2

   howto_userdata

Get Current User Name
---------------------
The current logon user name could be
retrieved by the call: 

.. code-block:: pyhton
   :linenos:

   import filesysobjects.userdata
   
   filesysobjects.userdata.getcurrent_username()

For complete details refer to 
[`API <userdata.html#getcurrent-username>`_] / [`code <_modules/filesysobjects/userdata.html#ConfigPath.getcurrent_username>`_].

Get HOME Directory
------------------
The current logon user home directory could be
retrieved by the call: 

.. code-block:: pyhton
   :linenos:

   import filesysobjects.userdata
   
   filesysobjects.userdata.gethome()

For complete details refer to 
[`API <userdata.html#gethome>`_] / [`code <_modules/filesysobjects/userdata.html#ConfigPath.gethome>`_].

Get User HOME Directories
-------------------------
The specific HOME directory of an user could be
retrieved by the call: 

.. code-block:: pyhton
   :linenos:

   import filesysobjects.userdata
   
   filesysobjects.userdata.getdir_userhome()  # default is current user
   filesysobjects.userdata.getdir_userhome('userx')

For complete details refer to 
[`API <userdata.html#getdir-userhome>`_] / [`code <_modules/filesysobjects/userdata.html#ConfigPath.getdir_userhome>`_].

Get User Data Directories
-------------------------
The specific data directory of an user could be
retrieved by the call: 

.. code-block:: pyhton
   :linenos:

   import filesysobjects.userdata
   
   filesysobjects.userdata.getdir_userdata()  # default is current user
   filesysobjects.userdata.getdir_userdata('userx')

For complete details refer to 
[`API <userdata.html#getdir-userdata>`_] / [`code <_modules/filesysobjects/userdata.html#ConfigPath.getdir_userdata>`_].

Get User Configuration Directories
----------------------------------
The specific configuration directory of an user could be
retrieved by the call: 

.. code-block:: pyhton
   :linenos:

   import filesysobjects.userdata
   
   filesysobjects.userdata.getdir_userconfigdata()  # default is current user
   filesysobjects.userdata.getdir_userconfigdata('userx')

For complete details refer to 
[`API <userdata.html#getdir-userconfigdata>`_] / [`code <_modules/filesysobjects/userdata.html#ConfigPath.getdir_userconfigdata>`_].

Get User App Configuration Directories
--------------------------------------
The specific application directory within a user context could be
retrieved by the call: 

.. code-block:: pyhton
   :linenos:

   import filesysobjects.userdata
   
   filesysobjects.userdata.getdir_userappconfigdata()  # default is current user
   filesysobjects.userdata.getdir_userappconfigdata('userx')

For complete details refer to 
[`API <userdata.html#getdir-userappconfigdata>`_] / [`code <_modules/filesysobjects/userdata.html#ConfigPath.getdir_userappconfigdata>`_].

Get User App Data Directories
-----------------------------
The specific application data within the context of an user could be
retrieved by the call: 

.. code-block:: pyhton
   :linenos:

   import filesysobjects.userdata
   
   filesysobjects.userdata.getdir_userappdata()  # default is current user
   filesysobjects.userdata.getdir_userappdata('appx', 'usery')

For complete details refer to 
[`API <userdata.html#getdir-userappdata>`_] / [`code <_modules/filesysobjects/userdata.html#ConfigPath.getdir_userappdata>`_].
   