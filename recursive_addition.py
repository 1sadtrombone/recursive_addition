A = [3, 2, 1] #123
B = [5, 6, 7] #765
R = []
c = [0]

def add(R, c):
	i = len(R)
	if i == len(A):
		return R
	else:
		R.append((A[i]+B[i]+c[i])%10)
		c.append((A[i]+B[i]+c[i])/10)
		return add(R, c)	
	
print add(R, c)
