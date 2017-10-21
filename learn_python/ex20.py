#It's a module
from sys import argv

script,input_file=argv

#define the functions
def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count,f):
	print line_count,f.readline()
	
#open the file
current_file=open(input_file)

print "First let's print the whole file:\n"

#call the first functions
print_all(current_file)

print "Now let's rewind,kind of like a tape."

#run the second function to rewind the file
rewind(current_file)

print "Let's print three lines:"

#print the file content line by line
current_line=1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)