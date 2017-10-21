# -*- coding:utf-8 -*-
formatter = "%s %s %s %s"

print formatter % (1,2,3,4)
print formatter % (u"我爱祖国","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",#此处的输出是双引号
	"So I said goodnight."#此处输出的仍为单引号
	)
	
	
