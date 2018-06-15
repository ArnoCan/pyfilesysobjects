Howto Path Tools
================

.. toctree::
   :maxdepth: 2

   howto_pathtools

Expand a Wildcard Path
----------------------
The interface

.. code-block:: python
   :linenos:
   
   filesysobjects.pathtools.expandpath(*paths, **kargs)

Provides the normalization of path lists which may contain regexpr, globs,
and environment variables.
This also splits contained multiple-path entries into each combined path.

The following call expands to all wildcards:

.. code-block:: python
   :linenos:

   arg = tdata + '/b/*/c.sh'
   #
   # some interpretations:
   #
   #   GLOB:'/b/*/c.sh' => as RE: '/b/.+/c.sh' 
   #   RE:'/b/*/c.sh' some equivalents subsets: '/b////c.sh','/b/c.sh', '/bc.sh' 
   #
   res = filesysobjects.pathtools.expandpath(arg, wildcards=W_RE)

   res = filesysobjects.pathtools.expandpath(arg, wildcards=W_GLOB)

The similar call with platform independent normalization bt defining
a *tpf* - *target platform format*, here *posix*.

.. code-block:: python
   :linenos:

   arg = tdata + '/b/*/c.sh'
   arg = filesysobjects.apppaths.normapppathx(arg, tpf='posix')
   
   res = filesysobjects.pathtools.expandpath(arg, wildcards=W_RE, tpf='posix')

See [`API <pathtools.html#expandpath>`_] / [`code <_modules/filesysobjects/pathtools.html#expandpath>`_]


Find with 're' and 'glob' Pattern
---------------------------------
The interface *findpattern* supports a large set of options,
which more comprising in some parts than the *find* utility of *POSIX*.
The missing features are closing step by step.
This includes the library as well as the command line interface.

The following call finds all filesystem entries in the current 
directory:

.. code-block:: python
   :linenos:

   filesysobjects.pathtools.findpattern(level=0)


The following call searches by wildcards the subdirectories of *tdata*.

.. code-block:: python
   :linenos:

   tdata = /my/search/start
   search_path_expr = tdata+os.path.normpath("/'''[^/]'''+/.*/[c]+.sh")

   filesysobjects.pathtools.findpattern(
      tdata,
      wildcards=search_path_expr
      )

See [`API <pathtools.html#findpattern>`_] / [`code <_modules/filesysobjects/pathtools.html#findpattern>`_]

Find Relative Sub-Paths in Search Paths
---------------------------------------
The interface *findrelpath_in_searchpath* supports the search
of relative subpaths to each entry within a list of search paths.

The following call finds all filesystem entries within a specific
subpath:

.. code-block:: python
   :linenos:

   filesysobjects.pathtools.findrelpath_in_searchpath(
      rpath,         # relative path
      plist,         # path list to be searched
      subsplit=True  # sets split of contained search path-strings
      )

See [`API <pathtools.html#findrelpath-in-searchpath>`_] / [`code <_modules/filesysobjects/pathtools.html#findrelpath_in_searchpath>`_]

