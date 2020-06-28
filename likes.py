#! python3

def likes(names):
	"""Converts list of names into strings of likes

	Args:
		names (list): List of string names
	
	Returns:
		strings	

	Examples:
		>>> likes(['Pavel', 'Yury', 'Sveta'])
        	'Pavel, Yury and Sveta like this'
	"""
	length = len(names)
	
	d = {
	0: 'No one likes this',
	1: '{} likes this',
	2: '{} and {} like this',
	3: '{}, {} and {} like this',
	4: '{}, {} and {others} others like this'
	}
	
	return d[min(4, length)].format(*names, others = length - 2)  

