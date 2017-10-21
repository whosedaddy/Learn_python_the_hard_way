#put a module
from sys import argv

#value the script and filename
script,filename=argv

#open the filename and value the txt
txt=open(filename)

#output a string about the txtname
print "Here's your file %r:"%filename
#output the txt's content that is filename's content
print txt.read()

#output a prompt
print "Type the filename again:"
#input the filename
file_again=raw_input(">")
#open the filename and calue the txt_again
txt_again=open(file_again)

#output the content again
print txt_again.read()
