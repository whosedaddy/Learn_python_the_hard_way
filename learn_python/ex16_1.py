from sys import argv

script,filename=argv

x=open(filename)

print "Print the ex16_sample's content."
print x.read()