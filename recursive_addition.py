A = [0, 0, 3, 1] #1300 (easier to do in reverse, ie lowest value to highest)
B = [5, 6, 7] #765
R = [] #result
c = [0] #carry

def add(R, c):
	i = len(R) #operating on this row. 
	if i == len(A):
		R.append(c[i]) #make sure we get any carries from the last run
		return R #finally return value 
	else:
		R.append((A[i]+B[i]+c[i])%10) #next digit 
		c.append((A[i]+B[i]+c[i])/10) #next carry
		return add(R, c) #is this really recursion? I feel like I could write it out w/o it, and R, c doesn't really need to be passed, they're global.

#padding numbers if unequal number of digits
if len(A) < len(B): 
	A = list(reversed(A)) #need to pad from left, but lists add to the right
	A += [0] * (len(B) - len(A)) #add a number of 0s equal to the discrepancy in lengths
	A = list(reversed(A)) #put it back in usable order
elif len(B) < len(B):
	B = list(reversed(B))
	B += [0] * (len(A) - len(B))
	B = list(reversed(B))

print list(reversed(add(R, c))) #prints result in forward order
