def vebonachure(n):
	if n==1 or n==0:
		return 1;
	else:
		return vebonachure(n-1)+vebonachure(n-2)
		
up=vebonachure(20)
down=vebonachure(19)
div=(up*0.1)/down

print div