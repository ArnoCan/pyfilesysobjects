Howto Pretty Print Paths
========================

.. toctree::
   :maxdepth: 3

   howto_pprint

The *filesysobjects.pprint* module provides pretty printers for resource 
addresses.
This includes vatious targets formats of string output, including console display,
and formats of syntaxes for automated processing such as *INI*, *CONF*, *JSON*, *XML*, and *YAML*.

About Source Platform and Target Platform
-----------------------------------------
The platform defines the representation syntax of the resource path.
E.g. the *spf='win32'* defines the *os.pathsep=';'*, and the default *os.sep='\\'*,
while the *spf='posix'* defines the *os.pathsep=':'*, and the default *os.sep='/'*,
the latter *category* of platforms is e.g. the same for the *family* of 
the platforms Linux as *spf='linux'* or *spf='RTE_LINUX'*.

For additional details refer to `Platform Definitions <filesysobjects_init.html#platform>`_.

The Source Platform - *spf*
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Target Platform - *tpf*
^^^^^^^^^^^^^^^^^^^^^^^^^^^
 
Pretty Print Search Parths
--------------------------

Output for *awk* scripts
^^^^^^^^^^^^^^^^^^^^^^^^
List *ARRAY* syntax
"""""""""""""""""""

Output for *bash* scripts
^^^^^^^^^^^^^^^^^^^^^^^^^
*PATH* syntax
"""""""""""""

List *ARRAY* syntax
"""""""""""""""""""

Output for *CONF* Files
^^^^^^^^^^^^^^^^^^^^^^^

Output for *CFG* Files
^^^^^^^^^^^^^^^^^^^^^^

Output for *INI* Files
^^^^^^^^^^^^^^^^^^^^^^

*ini* syntax
""""""""""""

*ini0* syntax
"""""""""""""

*ini1* syntax
"""""""""""""

*ini2* syntax
"""""""""""""

Output as *JSON*
^^^^^^^^^^^^^^^^

Output as *LUA*
^^^^^^^^^^^^^^^

Output for *properties*  Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Output as *Python* Syntax
^^^^^^^^^^^^^^^^^^^^^^^^^

Output as *XML*
^^^^^^^^^^^^^^^

Output as *YAML*
^^^^^^^^^^^^^^^^

