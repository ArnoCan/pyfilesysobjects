Normative References
====================

The following list is a short sum-up of example code verified by *filesysobjects*.
For a detailed list of the standards refer to `References <references.html#>`_
and :ref:`filesysobjects standards <FILESYSOBJECTS_REFERENCES>`   
This also lists defacto standards.

.. toctree::
   :maxdepth: 2

   reference_cases

IEEE-1003
---------

[IEEE1003]_ The Single UNIX Specification (SUS) - IEEE-1003.1 - 2013 

.. toctree::
   :maxdepth: 2

   reference_ieee1003


+---------------------------------------+--------------+
| [reference]                           | [doc/source] |
+=======================================+==============+
| 3.170 Filename                        | [IEEE1003]_  |
+---------------------------------------+--------------+
| 3.267 Pathname                        | [IEEE1003]_  |
+---------------------------------------+--------------+
| 3.278 Portable Filename Character Set | [IEEE1003]_  |
+---------------------------------------+--------------+

MS-CIFS
-------

Refer to SMB.

* Message Block (SMB) Protocol [SMB]_ [MS-SMB]_ [MS-SMB2]_ ([SAMBA]_)

* SMB File Sharing URI Scheme [SMBURI]_ - outdated

* Common Internet File System [CIFS]_

MS-SMB
------

* Message Block (SMB) Protocol [SMB]_ [MS-SMB]_ [MS-SMB2]_ ([SAMBA]_)

* SMB File Sharing URI Scheme [SMBURI]_ - outdated

* Common Internet File System [CIFS]_

+-------------------------------+--------------+
| [reference]                   | [doc/source] |
+===============================+==============+
| 2.2.1.1.1 Pathname Extensions | [MS-SMB2]_   |
+-------------------------------+--------------+

RFC1738
-------

[RFC1738]_ Uniform Resource Locators (URL) - Updated by RFC8089


+-----------------------------------+--------------+
| [reference]                       | [doc/source] |
+===================================+==============+
| 3.1 Common_Internet_Scheme_Syntax | [RFC1738]_   |
+-----------------------------------+--------------+
| 3.2 FTP                           | [RFC1738]_   |
+-----------------------------------+--------------+
| 3.3 HTTP                          | [RFC1738]_   |
+-----------------------------------+--------------+
| 3.10 Files                        | [RFC1738]_   |
+-----------------------------------+--------------+

RFC3986
-------
[RFC3986]_ Uniform Resource Identifier (URI): Generic Syntax

+-----------------------------------------+--------------+
| [reference]                             | [doc/source] |
+=========================================+==============+
| 4.5. Suffix Reference                   | [RFC3986]_   |
+-----------------------------------------+--------------+
| 5.2.3. Merge Paths                      | [RFC3986]_   |
+-----------------------------------------+--------------+
| 5.2.4. Remove Dot Segments              | [RFC3986]_   |
+-----------------------------------------+--------------+
| 5.4. Reference Resolution Examples      | [RFC3986]_   |
+-----------------------------------------+--------------+
| 5.4.1. Normal Examples                  | [RFC3986]_   |
+-----------------------------------------+--------------+
| 5.4.2. Abnormal Examples                | [RFC3986]_   |
+-----------------------------------------+--------------+
| 6.2.2. Syntax Based Normalization       | [RFC3986]_   |
+-----------------------------------------+--------------+
| 6.2.2.1. Case Normalization             | [RFC3986]_   |
+-----------------------------------------+--------------+
| 6.2.2.2. Percent Encoding Normalization | [RFC3986]_   |
+-----------------------------------------+--------------+
| 6.2.2.3. Path Segment Normalization     | [RFC3986]_   |
+-----------------------------------------+--------------+
| 6.2.3. Scheme Base Normalization        | [RFC3986]_   |
+-----------------------------------------+--------------+
| 6.2.4. Protocol Based Normalization     | [RFC3986]_   |
+-----------------------------------------+--------------+
| 7.4. Rare IP Address Formats            | [RFC3986]_   |
+-----------------------------------------+--------------+
| 7.6. Semantic Attacks                   | [RFC3986]_   |
+-----------------------------------------+--------------+

RFC8089
-------

[RFC8089]_ The “file” URI Scheme

+------------------------------------------------------+--------------+
| [reference]                                          | [doc/source] |
+======================================================+==============+
| Appendix A. Differences from Previous Specifications | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Local Files                                          | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Non-local Files                                      | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Appendix C. Similar Technologies                     | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Appendix D. System-Specific Operations               | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Appendix D.1. POSIX Systems                          | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Appendix D.2. DOS- and Windows-Like Systems          | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Appendix D.3. Mac OS X Systems                       | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Appendix E. Nonstandard Syntax Variations            | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Appendix E.1. User Information                       | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Appendix E.2. DOS and Windows Drive Letters          | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Appendix E.3. UNC Strings                            | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Appendix E.4. Backslash as Separator                 | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Appendix F. Collected Nonstandard Rules              | [RFC8089]_   |
+------------------------------------------------------+--------------+
| Appendix F. Collected Nonstandard Rules              | [RFC8089]_   |
+------------------------------------------------------+--------------+


UNC
---
[UNC]_ UNC: Common definition in [MS-DTYP] Windows Data Types - Chap. 2.2.57 UNC

+-------------+--------------+
| [reference] | [doc/source] |
+=============+==============+
| 2.2.57 UNC  | [UNC]_       |
+-------------+--------------+

Valuable Drafts
===============

draft-kerwin-file-scheme-13
---------------------------
[URISCHEME]_ The file URI Scheme - draft-kerwin-file-scheme-13; IETF;

.. warning::

   This draft is expired and replaced by [RFC8089]_, but still valuable as
   example and for verification.

.. toctree::
   :maxdepth: 2

   reference_draft_file_scheme

draft-crhertel-smb-url-12
-------------------------
 
[SMBURI]_ SMB File Sharing URI Scheme - outdated

.. warning::

   This draft is expired, but still valuable as
   example and for verification.

.. toctree::
   :maxdepth: 2

   reference_draft_smb_url
   