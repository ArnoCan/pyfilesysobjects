Install
=======

+--------------+--------------+----------------------------------------------------+
| prerequisite | reference    | description                                        |
+==============+==============+====================================================+
| Runtime      | Python       | Python 2.7+, Python 3.5+                           |
+              +--------------+----------------------------------------------------+
|              | OS           | Linux, Mac-OS/OS-X, BSD, UNIX, Cygwin, MS-Windows  |
+              +--------------+----------------------------------------------------+
|              | Devices      | RaspberryPI (2,3): Raspbian, FreeBSD, OpenWRT      |
+--------------+--------------+----------------------------------------------------+
| SDK          | Python       | Python 2.7+, Python 3.5+                           |
+              +--------------+----------------------------------------------------+
|              | bash         | bash-4.x                                           |
+              +--------------+----------------------------------------------------+
|              | documents    | Sphinx >=1.4,Epydoc >=3                            |
+              +--------------+----------------------------------------------------+
|              | OS           | Linux, Mac-OS/OS-X, BSD, UNIX, Cygwin,             |
+--------------+--------------+----------------------------------------------------+
| Download     | PyPI         | https://pypi.python.org/pypi/filesysobjects        |
+              +--------------+----------------------------------------------------+
|              | Sourceforge  | https://sourceforge.net/projects/filesysobjects/   |
+              +--------------+----------------------------------------------------+
|              | github.com   | https://github.com/ArnoCan/filesysobjects/         |
+--------------+--------------+----------------------------------------------------+
| Documents    | pythonhosted | https://pythonhosted.org/filesysobjects/           |
+--------------+--------------+----------------------------------------------------+

**Install**:

+-------------+-------------------------------------------------------------------------+
| environment | description                                                             |
+=============+=========================================================================+
| Runtime     | Standard procedure online local install e.g. into virtual environment:  |
+             +-------------------------------------------------------------------------+
|             | * *pip install filesysobjects*                                          |
|             | * *python setup.py install*                                             |
+             +-------------------------------------------------------------------------+
|             | Standard procedure online local install into user home:                 |
+             +-------------------------------------------------------------------------+
|             | * *python setup.py install --user*                                      |
+             +-------------------------------------------------------------------------+
|             | Custom procedure offline by:                                            |
+             +-------------------------------------------------------------------------+
|             | * *python setup.py install --user --offline*                            |
+-------------+-------------------------------------------------------------------------+
| SDK         | Required for document creation, add '--sdk' option, checks build tools: |
+             +--------------+----------------------------------------------------------+
|             | * *python setup.py install --sdk*                                       |
+             +--------------+----------------------------------------------------------+
|             | Creation of documents, requires Sphinx including 'sphinx-apidoc',       |
|             | and Epydoc:                                                             |
+             +--------------+----------------------------------------------------------+
|             | * *python setup.py build_doc install_project_doc install_doc*           |
+-------------+--------------+----------------------------------------------------------+


* setup.py

  For help on extensions to standard options call online help:: 

    python setup.py --help-filesysobjects
