import time

characters = {
	'd': 'dorfbewohner',

	'w': 'werwolf',
	'v': 'vampir',

	'fm': 'freimaurer',

	'wj': 'wolfsjunges',
	'wk': 'wolfskind',
	'vf': 'verfluchter',
	'ww': 'weißer werwolf',

	'dg': 'doppelgängerin',

	'tb': 'trunkenbold',
	'ge': 'gerber',

	'h': 'hexe',
	'm': 'magier',
	'kf': 'kultführer',

	's': 'seherin',
	's2': 'seher',
	'as': 'aura-seherin',
	'sl': 'seher-lehrling',

	'a': 'amor',
	'j': 'jäger',
	'ja': 'jaguar',

	'p': 'priester',
	'lw': 'leibwächter',

	'av': 'alte vettel',
	'b': 'beschwörerin',
	'g': 'goethe',
	'mm': 'milchmann',
}
first_night = [
	'doppelgängerin',
	'freimaurer',
	'amor',
	'jaguar',
	'wolfskind',
]
night = [
	'trunkenbold',
	'kultführer',
	'priester',
	'leibwächter',
	'seherin',
	'seher',
	'aura-seherin',
	'werwolf',
	'hexe',
	'magier',
	'vampir',
	'alte vettel',
	'beschwörerin',
	'goethe',
	'milchmann'
]
second_night = [
	'weißer werwolf'
]

def intinp(txt: str) -> int:
	inp = None
	while type(inp) != int:
		inp = input(txt)
		try:
			inp = int(inp)
		except ValueError:
			print('Gebe eine Zahl ein.')
	return inp

def inp_characters(n: int) -> tuple:
	characters_game = []
	while n > 0:
		inp = input('Character: ').strip().lower()
		if not inp:
			print('Not enough roles')
			continue
		if inp in characters:
			inp = characters[inp]
		if not inp in characters.values():
			continue
		if inp in ['dorfbewohner', 'werwolf', 'vampir', 'freimaurer']:
			count = intinp('Anzahl: ')
		else:
			count = 1
		n -= count
		if n >= 0:
			for _ in range(count):
				characters_game.append(inp)
		else:
			print('Too many roles')
	return tuple(characters_game)

def gen_roles(characters_game: tuple) -> dict:


def character_action(character: str, data: dict) -> dict:
	person = data['roles'].index(character)
	if character == 'doppelgängerin':
		gd = intinp('Wähle deine gedoppelte Person: ')
		if 'connected' in data:
			data['connected'].append((gd,person))
		else:
			data.update({'connected': [(gd,person)]})
	elif character == 'freimaurer':
		input()
	elif character in ('amor', 'jaguar'):
		v1 = intinp('1. Verliebter: ')
		v2 = intinp('2. Verliebter: ')
		if 'connected' in data:
			data['connected'].append((v1,v2))
		else:
			data.update({'connected': [(v1, v2)]})
	elif character == 'wolfskind':
		print('Wähle dein Idol.')
		input()
	elif character == 'trunkenbold':
		pass
	return data


def main():
	players = intinp('Anzahl Spieler: ')
	characters_game = inp_characters(players)
	gen_roles(characters_game)
	data = {}
	for current_character in first_night:
		if current_character in characters_game:
			print('\n')
			print(f'{current_character.title()}: Wache auf!')
			data = character_action(current_character, data)
			print(f'{current_character.title()}: Schlafe wieder ein.')
			time.sleep(3)
	print(data)


if __name__ == "__main__":
	main()
