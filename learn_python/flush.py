import time
import sys
for i in range(5):
	print "\rHello!",i,
	sys.stdout.flush()
	time.sleep(1)
