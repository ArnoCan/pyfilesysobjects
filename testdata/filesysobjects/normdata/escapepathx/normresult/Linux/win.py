"""
#**************************************************************

Platform         : linux2
Version          : 2.7.5 (default, Nov  3 2014, 14:33:39) 
[GCC 4.8.3 20140911 (Red Hat 4.8.3-7)]
Version-Info     : sys.version_info(major=2, minor=7, micro=5, releaselevel='final', serial=0)

#**************************************************************
"""

norm_result = [
#--- 0
     r'\\w1\\w1\\w2',
     r'\\w2\\w1\\w2',
     r'\\\\w3\\\\w1\\\\w2',
     r'\\\\w4\\\\w1\\\\w2',
     r'\\\\\\w5\\\\\\w1\\\\\\w2',
#--- 5
     r'\\\\\\\\w6\\\\\\\\w1\\\\\\\\w2',
     r'\\\\\\\\\\w7\\\\\\\\w1\\\\\\\\w2',
     r'\\\\\\\\w8\\\\\\\\w1\\\\\\\\w2',
     r'\\\\\\\\\\w9\\\\\\\\\\w1\\\\\\\\\\w2',
     r'\\\\\\\\\\w10\\\\\\\\\\w1\\\\\\\\\\w2',
#--- 10
     r'/w1/w1/w2',
     r'//w2//w1//w2',
     r'///w3///w1///w2',
     r'////w4////w1////w2',
     r'/////w5/////w1/////w2',
#--- 15
     r'//////w6//////w1//////w2',
     r'///////w7///////w1///////w2',
     r'////////w8////////w1////////w2',
     r'/////////w9/////////w1/////////w2',
     r'//////////w10//////////w1//////////w2',
#--- 20
     r'\\/w1/\\w1\\/w2',
     r'\\//w2//\\w1\\//w2',
     r'\\\\///w3\\\\///w1\\\\///w2',
     r'\\\\////w4\\\\////w1\\\\////w2',
     r'\\\\\\/////w5\\\\\\/////w1\\\\\\/////w2',
#--- 25
     r'\\/w1/\\w1\\/w2',
     r'\\/\\/w2\\/\\/w1\\/\\/w2',
     r'\\/\\/\\/\\/w3\\/\\/\\/\\/w1\\/\\/\\/\\/w2',
     r'\\/\\/\\/\\/\\w4\\/\\/\\/\\/\\w1\\/\\/\\/\\/\\w2',
     r'\\/\\/\\/\\/\\/w5\\/\\/\\/\\/\\/w1\\/\\/\\/\\/\\/w2',
#--- 30
     r'\\//w1//\\w1\\//w2',
     r'\\//\\//w2\\//\\//w1\\//\\//w2',
     r'\\///\\///\\///\\///w3\\///\\///\\///\\///w1',
     r'\\////\\////\\////\\////\\w4\\////\\////\\////w1',
     r'\\/////\\/////\\/////\\/////\\/////w5',
#--- 35
     r'\\/w1/\\w1\\/w2',
     r'\\\\/\\\\/w2\\\\/\\\\/w1\\\\/\\\\/w2',
     r'\\\\/\\\\/\\\\/\\\\/w3\\\\/\\\\/\\\\/\\\\/w1',
     r'\\\\\\/\\\\\\/\\\\\\/\\\\\\/\\\\\\w4\\\\\\/\\\\\\/\\\\\\/\\\\\\/\\\\\\w1',
     r'\\\\\\/\\\\\\/\\\\\\/\\\\\\/\\\\\\/w5',
#--- 40
     r'\a',
     r'\b',
     r'\f',
     r'\n',
     r'\r',
#--- 45
     r'\t',
     r'\v',
     r'\\a',
     r'\\b',
     r'\\f',
#--- 50
     r'\\n',
     r'\\r',
     r'\\t',
     r'\\v',
     r'\\\a',
#--- 55
     r'\\\b',
     r'\\\f',
     r'\\\n',
     r'\\\r',
     r'\\\t',
#--- 60
     r'/\v',
     r'/\a',
     r'/\b',
     r'/\f',
     r'/\n',
#--- 65
     r'/\r',
     r'/\t',
     r'/\v',
     r'/\\a',
     r'/\\b',
#--- 70
     r'/\\f',
     r'/\\n',
     r'/\\r',
     r'/\\t',
     r'/\\v',
#--- 75
     r'/\\\a',
     r'/\\\b',
     r'/\\\f',
     r'/\\\n',
     r'/\\\r',
#--- 80
     r'/\\\t',
     r'/\\\v',
     r'\\/\\a',
     r'\\/\\b',
     r'\\/\\f',
#--- 85
     r'\\/\\n',
     r'\\/\\r',
     r'\\/\\t',
     r'\\/\\v',
     r'\\/\a',
#--- 90
     r'\\/\b',
     r'\\/\f',
     r'\\/\n',
     r'\\/\r',
     r'\\/\t',
#--- 95
     r'\\/\v',
     r'\\\\/a',
     r'\\\\/b',
     r'\\\\/f',
     r'\\\\/n',
#--- 100
     r'\\\\/r',
     r'\\\\/t',
     r'\\\\/v',
     r'/\a/\b/\f/\n/\r/\t/\v',
     r'\\a\\b\\f\\n\\r\\t\\v',
#--- 105
     r'\\\a\\\b\\\f\\\n\\\r\\\t\\\v',
     r'\\\\a\\\\b\\\\f\\\\n\\\\r\\\\t\\\\v',
     r'//\a/\b/\f/\n/\r/\t/\v',
     r'/\a/\b/\f/\n/\r/\t/\v',
     r'/\a/\b/\f/\n/\r/\t/\v',
#--- 110
     r'""',
     r'\\"\\"',
     r'\\"\\"',
     r'\\\\"\\\\"',
     r'/"/"',
#--- 115
     r'//"/"',
     r'/"/"',
     r'/"/"',
     r'\\:\\:',
     r'\\:\\:',
#--- 120
     r'\\\\:\\\\:;',
     r'\\\\:;\\\\:',
     r'/:/:;',
     r'//:;/:',
     r'/:/::',
#--- 125
     r'/:/:',
     r'\\ \\ ',
     r'\\ \\ ',
     r'\\\\ \\\\ ',
     r'\\\\ \\\\ ',
#--- 130
     r'/ / ',
     r'// / ',
     r'/ / ',
     r'/ / ',
     r'\\;\\;',
#--- 135
     r'\\\\;\\\\;',
     r'\\\\\\;\\\\\\;',
     r'\\\\\\\\;\\\\\\\\;',
     r'/;/;',
     r'//;/;',
#--- 140
     r'/;/;',
     r'/;/;',
     r'\\\n',
     r'/\\\n/',
     r'/\\\n/A/\\\n',
#--- 145
     r'/\\\n/A',
     r'/\\\n/A/\\\n/B\\\n',
     r'/\\\n/w0/\\\n/w1/\\\n/',
     r'A',
     r'/A/B/',
#--- 150
     r'//A//B/',
     r'///A///B/',
     r'////A////B/',
     r'\u0041\u0042/',
     r'\\A\\B/',
#--- 155
     r'\\\\u0041\\\\u0042/',
     r'!',
     r'/!/"',
     r'//!//"',
     r'///!///"',
#--- 160
     r'////!////"',
     r'!',
     r'\\041\\042',
     r'\\041"',
     r'\\!\\"',
#--- 165
     r'\\\\041\\\\042',
     r'\\\\!\\\\"',
     r'A',
     r'/A/B',
     r'//A//B',
#--- 170
     r'///A///B',
     r'////A////B',
     r'\\x41\\x42',
     r'\\A\\B',
     r'\\\\x41\\\\x42',
#--- 175
     r'\\\\A\\\\B',
     r'\\/',
     r'\\/\\/',
     r'\\/\\/\\/',
     r'\\/\\/\\/\\/',
#--- 180
     r'\\/\\/\\/\\/\\/',
     r'\\\\/',
     r'\\\\/\\\\/',
     r'\\\\/\\\\/\\\\/',
     r'\\\\/\\\\/\\\\/\\\\/',
#--- 185
     r'\\\\/\\\\/\\\\/\\\\/\\\\/',
     r'\\/\\\\',
     r'\\/\\\\/\\\\',
     r'\\/\\\\/\\\\/\\\\',
     r'\\/\\\\/\\\\/\\\\/\\\\',
#--- 190
     r'\\/\\\\/\\\\/\\\\/\\\\/\\\\',
     r'\\\\\\/',
     r'\\\\\\/\\\\\\/',
     r'\\\\\\/\\\\\\/\\\\/',
     r'\\\\\\/\\\\\\/\\\\\\/\\\\\\/',
#--- 195
     r'\\\\\\/\\\\\\/\\\\\\/\\\\\\/\\\\/',
     r'\\\\\\/',
     r'\\\\\\/\\\\/',
     r'\\\\\\/\\\\/\\\\/',
     r'\\\\\\/\\\\/\\\\/\\\\/',
#--- 200
     r'\\\\\\/\\\\/\\/\\\\/\\\\/',
     r'//"\\a\\\\a\\b\\\\b"///"\\\\f\\f"',
     r'/\\a/"\\a\\\\a\\b\\\\b"/\\b/\\f/"\\\\f\\f"',
     r"/\\a/'\\a\\\\a\\b\\\\b'/\\b/\\f/'\\\\f\\f'",
]


