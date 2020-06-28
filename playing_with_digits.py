#! python3 

def dig_pow(n, p):
	"""Finds a positive integer k, if it exists, such as the 
	sum of the digits of n taken to the successive powers 
	of p is equal to k * n.
	
	Args: 
		Integer and a exponent 

	Returns: 
		A positive integer if found 

	Example: 
		>>>dig_pow(46288, 1)
		51
	"""

	digits = [int(num) for num in str(n)]
	
	total = 0	
	for i in range(len(digits)):
		total += pow(digits[i], p)
		p += 1
	quotient = total / n
	return int(quotient) if quotient.is_integer() else -1
