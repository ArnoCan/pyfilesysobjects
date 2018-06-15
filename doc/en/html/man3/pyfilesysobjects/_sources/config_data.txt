Config Data
===========

Configuration Persistency
-------------------------
The configuration of applications and services frequently require some specific
configured information.
These are either stored in a repository, or within
simple configuration files. 
The configuration files are common on all current platforms.

The location and the file syntax varies by platform and application.
In particular the location of the configuration file is different
on platforms and for several applications.
Which requires some context specific routines for the location.

See `filesysobjects.configdata <configdata.html>`_.

Locating Configuration Files
----------------------------
A major feature is the automatic location
of configuration files.
Each platform supports specific locations which are more or less
different. The applications add frequently further differences in
dependency of the runtime platforms.

The *filesysobjects.configdata* [filesysobjects]_ module provides an abstraction layer,
which encapsulates platform specific standard directory locations by a set
of abstract interfaces, but still supports the addition of arbitrary custom locations.

So the automatic location could be processed by a single call only, which
also handels the priority in case of redundant files. ::

   ini_file = filesysobjects.configdata.ConfigPath().get_config_filepath('myini.ini')
   conf_file = filesysobjects.configdata.ConfigPath().get_config_filepath('myconf.conf')


Examples
--------
For typical applications refer to the `HowTo <howto_configdata.html>`_,
and the packages [epyunit]_ and [syscalls]_. 

References
----------

* PyFileSysObjects - [filesysobjects]_ 

* PySourceInfo - [sourceinfo]_ 

* Python2 ConfigParser - [ConfigParser]_ 

* Python3 configparser - [configparser]_ 

