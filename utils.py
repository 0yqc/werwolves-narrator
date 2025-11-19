def intinp(txt: str) -> int:
	inp = None
	while type(inp) != int:
		inp = input(txt)
		try:
			inp = int(inp)
		except ValueError:
			print('Gebe eine Zahl ein.')
	return inp
