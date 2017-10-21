# -*- coding:utf-8 -*-
tabby_cat="\tI'm tabbed in."#\t表示缩进八个字符
persian_cat="I'm split\non a line."#\n表示换行
backslash_cat="I'm\\a\\cat."#\\双斜线表示输出一个斜线


fat_cat="""
I'll do a list:
\t* Cat food 
\t* Fishes 
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

single_quote='\''
double_quote='\"'

print "%r"%"\""
print "%r"%"\'"

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r"%i,