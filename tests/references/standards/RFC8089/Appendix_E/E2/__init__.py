""" [RFC8089]_ - Appendix E.2. DOS and Windows Drive Letters

.. seealso:


   On Windows- or DOS-like file systems, an absolute file path can begin
   with a drive letter. To facilitate this, the "local-path" rule in
   Section 2 can be replaced with the following: ::

      local-path = [ drive-letter ] path-absolute

      drive-letter = ALPHA ":"

   The "ALPHA" rule is defined in [RFC5234].
   This is intended to support the minimal representation of a local
   file in a DOS- or Windows-like environment, with no authority field
   and an absolute path that begins with a drive letter. For example:

   * "file:c:/path/to/file"

   URIs of the form "file:///c:/path/to/file" are already supported by
   the "path-absolute" rule.

   Note that comparison of drive letters in DOS or Windows file paths is
   case insensitive. In some usages of file URIs, drive letters are
   canonicalized by converting them to uppercase; other usages treat
   URIs that differ only in the case of the drive letter as identical.

"""
