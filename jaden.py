#! python3

def to_jaden_case(string):
	"""Takes a string and capitalizes the first letter
	of every word

	Args:
		string

	Returns:
		capitalized string

	Usage: 
		>>> to_jayden_case("create a new repository")
		    Create A New Repository
	"""
	
	return " ".join([word.capitalize() for word in string.split()])
