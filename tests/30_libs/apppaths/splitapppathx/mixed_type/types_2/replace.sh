#A0="'file://///'+filesysobjects.paths.normpathx('hostname/share/a/b/c')"
#A1="'share','hostname', 'share', filesysobjects.paths.normpathx('a/b/c')"


#SMB
# B0="'smb://'+filesysobjects.paths.normpathx('hostname/share/a/b/c')"
# B1="'smb','hostname', 'share', filesysobjects.paths.normpathx('a/b/c')"

#CIFS
# B0="'cifs://'+filesysobjects.paths.normpathx('hostname/share/a/b/c')"
# B1="'cifs','hostname', 'share', filesysobjects.paths.normpathx('a/b/c')"

#share
# B0="'file://///'+filesysobjects.paths.normpathx('hostname/share/a/b/c')"
# B1="'share','hostname', 'share', filesysobjects.paths.normpathx('a/b/c')"

#FILE_DRIVE
# B0="'file://'+'d:'+filesysobjects.paths.normpathx('hostname/share/a/b/c')"
# B1="'ldsys','', 'd:', filesysobjects.paths.normpathx('hostname/share/a/b/c')"

#FILE_'lfsys'
# B0="'file://'+filesysobjects.paths.normpathx('/hostname/share/a/b/c')"
# B1="'lfsys','', '', filesysobjects.paths.normpathx('/hostname/share/a/b/c')"

#DRIVE_PATH
# B0="filesysobjects.paths.normpathx('d:/hostname/share/a/b/c')"
# B1="'ldsys','', 'd:', filesysobjects.paths.normpathx('/hostname/share/a/b/c')"

#DRIVE_ROOT
A0="filesysobjects.paths.normpathx('d:/hostname/share/a/b/c')"
A1="'ldsys','', 'd:', filesysobjects.paths.normpathx('/hostname/share/a/b/c')"
B0="filesysobjects.paths.normpathx('d:/')"
B1="'ldsys','', 'd:', filesysobjects.paths.normpathx('/')"




find . -type f -name '*.py' -exec sed -i "s|$A0|$B0|g" {} \;
find . -type f -name '*.py' -exec sed -i "s|$A1|$B1|g" {} \;

#find . -type f -name '*.py' -exec sed -n "s|$A0|$B0|gp" {} \;
#find . -type f -name '*.py' -exec sed -n "s|$A1|$B1|gp" {} \;
