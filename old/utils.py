def intinp(txt: str) -> int:
	inp = None
	while type(inp) != int:
		inp = input(txt)
		try:
			inp = int(inp)
		except ValueError:
			print('Gebe eine Zahl ein.')
	return inp

def boolinp(txt: str) -> bool:
	while True:
		inp = input(txt)
		if inp.lower() in ('ja', 'yes', 'true', '1'):
			return True
		elif inp.lower() in ('nein', 'no', 'false', '0'):
			return False
		else:
			print('Gebe deine Entscheidung ein (ja/nein).')
			
def milkinp(txt: str) -> bool:
	"""
	:return True: Gute Milch; False: Schlechte Milch
	"""
	while True:
		inp = input(txt)
		if inp.lower() in ('gut', 'good', '1'):
			return True
		elif inp.lower() in ('schlecht', 'bad', '0'):
			return False
		else:
			print('Gebe deine Entscheidung ein (gut/schlecht).')