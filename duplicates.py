#! python3

def duplicate_count(text):
	"""Finds disctinct numbers and letters in a string.
                                                           	
	Args: 
		Alphabets and numeric digits

	Usage: 
		>>>distinct_count('aabcde11')
	       	2 
	"""
	count = {}

	for letters in text.lower():
		count.setdefault(letters, 0)
		count[letters] = count[letters] + 1

	return sum([num > 1 for num in count.values()])
