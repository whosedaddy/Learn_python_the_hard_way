import random
i=[[],[],[],[]]

for m in range(4):
	for j in range(4):
		i[m]=random.choice([0,0,2,2,4])
	
print i