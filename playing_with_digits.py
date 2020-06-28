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

	total = 0
	for k, v in enumerate(str(n)):
		total += pow(int(v), k + 1)	
	quotient = total / n
	return quotient if quotient.is_integer() else -1	
