import time, random

from charset_normalizer.cd import characters_popularity_compare

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
characters_first_night = [
	'doppelgängerin',
	'freimaurer',
	'amor',
	'jaguar',
	'wolfskind',
]
characters_night = [
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
characters_alternate_night = [
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


def gen_roles(characters_game: tuple) -> tuple:
	characters_game = list(characters_game)
	random.shuffle(characters_game)
	print('\n')
	print('Rolen:')
	for i in range(len(characters_game)):
		print(f'{i + 1}: {characters_game[i].title()}')
	return tuple(characters_game)


def character_action(character: str, data: dict) -> dict:
	role = None
	for i in range(2):
		dg_second_action = None
		if character == 'doppelgängerin':
			gd = intinp('Wähle deine gedoppelte Person: ')
			data.update({'doubled_person': gd})
			data.update({'doubled_role': data['roles'][gd - 1]})
		elif character == 'freimaurer':
			input()
		elif character in ('amor', 'jaguar'):
			dg_second_action = True
			v1 = intinp('1. Verliebter: ')
			v2 = intinp('2. Verliebter: ')
			data['love'].append((v1, v2))
		elif character == 'wolfskind':
			dg_second_action = True
			print('Wähle dein Idol.')
			input()
		elif character == 'trunkenbold':
			dg_second_action = True
			no = intinp('Wähle deinen heutigen Nächtigungsort: ')
			data['protected'].append(data['roles'].index('trunkenbold'))
			data.update({'round_tb': no})
		if character == data['doubled_role'] and dg_second_action and i == 0:
			print()
			print('Doppelgängerin-Aktion:')
			role = data['roles'].index('doppelgängerin')
		else:
			break
	return data


def main():
	players = intinp('Anzahl Spieler: ')
	characters_game = gen_roles(inp_characters(players))
	data: dict = {
		'love': [],
		'protected': [],
	}
	data.update({'roles': characters_game})
	nightnum = 0
	while True:
		current_night = set(characters_night)
		if nightnum == 0:
			current_night.add(characters_first_night)
		if nightnum % 2:
			current_night.add(characters_alternate_night)
		time.sleep(3)
		print('\n')
		print('Das Dorf schläft ein!')
		for current_character in current_night:
			if current_character in characters_game:
				time.sleep(3)
				print('\n')
				print(f'{current_character.title()}: Wache auf!')
				data = character_action(current_character, data)
				print(f'{current_character.title()}: Schlafe wieder ein.')
		print('\n')
		print('Das Dorf wacht auf.')
		print(data)
		nightnum += 1

if __name__ == "__main__":
	main()
