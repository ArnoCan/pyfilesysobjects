Howto Regular Expressions
=========================

.. toctree::
   :maxdepth: 2

   howto_regexpr

Basic Notation
--------------
The *filesysobjects* supports regular expressions of bython by the standard package *re*.
These are applied on file path names, including path separators, thus could span
multiple directory levels.
The file path name syntax depends deeply on the platform and the used filesystem.
This includes the reserved characters for the syntax and additional characters.
While e.g. the Windows based filesystems such as *NTFS* and *FATxx* reserve a number of characters,
the *Posix* based filesystems permit almost any character, just reserve the path separator and the
null-character. 

Special Dot Notation
^^^^^^^^^^^^^^^^^^^^
Almost all filesystems support the special dot-notation for the current directory '.'
and the parent directory '..'.
This characters are treated though by special semantics for all filesystem name related functions.
The regular expressions use the dot '.' in as a special wildcard character.
Thus the notation of a path with contained regular expressions requires some special handling.
The simples solution is to define a character class, which masks the character as non-dot character. ::
The notation ::

   /my/path/./b

is by default ambiguous because of the application *os.normpath* and/or *filesysobjects.paths.normpathx*,
*filesysobjects.apppaths.normpathx*, which normalises the character sequence '*/./*' to '*/*',
'*\\.\\*' to '*\\*' respectively.
The possible resulting interpratations are:

* the current working directory, resulting in ::

     /my/path/b

* a regular special wildcard character representing a single character :: 

     /my/path/./b   with '.' e.g. [a-zA-Z0-9]

The following Python regular expression notations resolve the ambiguity by breaking
the current directory pattern ::

     /my/path/.{1}/b
     /my/path/[a-zA-Z0-9]/b

