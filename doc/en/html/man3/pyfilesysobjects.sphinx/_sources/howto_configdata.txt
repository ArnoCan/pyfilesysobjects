Howto Config Data
=================

.. toctree::
   :maxdepth: 2

   howto_configdata

Get Config File Path Name
-------------------------
The absolute file path name of the configuration file within common
standard search paths could be retrieved by the call:

.. code-block:: python
   :linenos:

   import filesysobjects.configdata
   
   ini_file = filesysobjects.configdata.ConfigPath().get_config_filepath('myini.ini')
   conf_file = filesysobjects.configdata.ConfigPath().get_config_filepath('myconf.conf')

For complete details refer to 
[`API <configdata.html#get-config-filepath>`_] / [`code <_modules/filesysobjects/configdata.html#ConfigPath.get_config_filepath>`_].

Get List of all Config Files
----------------------------

The list of absolute file path names of all matching configuration files
could be retrieved by the call:

.. code-block:: python
   :linenos:

   import filesysobjects.configdata
   
   ini_file_list = filesysobjects.configdata.ConfigPath().get_config_filepath_list('myini.ini')
   conf_file_list = filesysobjects.configdata.ConfigPath().get_config_filepath_list('myconf.conf')

For complete details refer to 
[`API <configdata.html#get-config-filepath-list>`_] / [`code <_modules/filesysobjects/configdata.html#ConfigPath.get_config_filepath_list>`_].

Get List of all Search Paths
----------------------------
The list of current search paths could be retrieved by the call:

.. code-block:: python
   :linenos:

   import filesysobjects.configdata
   
   standard_search_list = filesysobjects.configdata.ConfigPath().get_config_path_list()

   modified_search = filesysobjects.configdata.ConfigPath(
                        prepend='/my/search/path/0',
                        apppend='/my/search/path/1',
                        )
   modified_search_list = modified_search.get_config_path_list()

   #
   # modified_search_list = [ '/my/search/path/0', ...., '/my/search/path/1']
   #


For complete details refer to 
[`API <configdata.html#get-config-path-list>`_] / [`code <_modules/filesysobjects/configdata.html#ConfigPath.get_config_path_list>`_].
   