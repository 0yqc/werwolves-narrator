from translations import Translations


def inp(txt: str, typ: type | None = None, allowed: tuple | None = None, locale: str = 'en') -> str | bool | int | float:
	"""
	Asks the user a question in the terminal while respecting the typ of the answer as well as the allowed values for the answer.
	
	Type conversion will be attempted first
	
	:param txt: The text to ask the user
	:param typ: The type of the answer
	:param allowed: A tuple of allowed answers
	:param locale: The locale to use for all prints
	:return: The answer in allowed with the type as defined in typ
	"""
	tr = Translations(locale)
	typ_passed = False
	allowed_passed = False
	while (not typ_passed) or (not allowed_passed):
		typ_passed = False
		allowed_passed = False
		inpv = input(txt)
		if not inpv.strip():
			print(tr.misc.inp_empty)
			continue
		if typ == bool:
			if inpv.lower() in (tr.misc.true.lower(), 'true', '1'):
				inpv = True
				typ_passed = True
			elif inpv.lower() in (tr.misc.false.lower(), 'false', '0'):
				inpv = False
				typ_passed = True
			else:
				print(f'{tr.misc.inp_wrong_type} {typ} ({tr.misc.true}/{tr.misc.false})')
		elif typ and typ in (int, float):
			try:
				inpv = typ(inpv)
				typ_passed = True
			except ValueError:
				print(f'{tr.misc.inp_wrong_type} {typ}')
				continue
			except TypeError:
				print(tr.technical.inp_type_takes_no_arguments)
				typ = None
				continue
		else:
			typ_passed = True
		if allowed:
			if inpv in allowed:
				allowed_passed = True
			else:
				print(f'{tr.misc.inp_not_allowed} {', '.join(allowed)}')
				continue
		else:
			allowed_passed = True
	return inpv
