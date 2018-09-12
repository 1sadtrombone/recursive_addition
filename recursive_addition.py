def add(A, B, R = [], c = 0): #args, result, carry
	i = len(R) #operating on this row. 
	
	if i == 0: #1st run
	#padding numbers if unequal numbers 
		if len(A) < len(B): 
			A += [0] * (len(B) - len(A)) #add a number of 0s equal to the discrepancy in lengths (adds to the right, ie doesn't change value)
		elif len(B) < len(A):
			B += [0] * (len(A) - len(B))

	if i == len(A): #gone through all digits
		if c > 0: R.append(c) #make sure we get the carry from the last run, if any
		return R #finally return value 
	else: 
		R.append((A[i]+B[i]+c)%10) #next digit 
		c = (A[i]+B[i]+c)/10 #next carry
		return add(A, B, R, c) #go onto the next iteration, the next digit

print list(reversed(add([0, 0, 3, 1], [5, 6, 7]))) #inputs in reverse digit order, prints result in forward order
