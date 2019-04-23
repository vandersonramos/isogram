import re

def is_isogram(text):
	"""
		Checks if the parameter is an isogram and return True or False.
		Empty parameter is considered an isogram
	"""	
	if not text:
		return True

	if has_number(text):
		return False

	text = text.lower()
	return len(text) == len(set(text)) if text else False

def has_number(word):
	"""
	  Checks if the parameter contains any number and return True or False
	"""
	return bool(re.search(r'\d+', word))