from locale import Translations as Tr

def inp(txt: str, typ: type | None = None, allowed: tuple | None = None):
	"""
	Asks the user a question in the terminal while respecting the typ of the answer as well as the allowed values for the answer.
	
	Type conversion will be attempted first
	
	:param txt: The text to ask the user
	:param typ: The type of the answer
	:param allowed: A tuple of allowed answers
	:return: The answer in allowed with the type as defined in typ
	"""
	while True:
		inp = input(txt)
		if not inp.strip():
			print(Tr.Misc.inp_empty)
			continue
		if typ:
			try:
				inp = typ(inp)
			except ValueError:
				print(f'{Tr.Misc.inp_wrong_type} {typ}')
				continue
			except TypeError:
				print(Tr.Technical.inp_type_takes_no_arguments)
				typ = None
				continue
		if allowed:
			if inp in allowed:
				return inp
			else:
				print(Tr.Misc.input_not_allowed)
		return inp
	