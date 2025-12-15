import time, random
import actions, utils
import data as gdata


def inp_characters(n: int) -> tuple:
	characters_game = []
	while n > 0:
		inp = input('Character: ').strip().lower()
		if not inp:
			print('Not enough roles')
			continue
		if inp in gdata.abreviations:
			inp = gdata.abreviations[inp]
		if not inp in gdata.abreviations.values():
			continue
		if inp in ['dorfbewohner', 'werwolf', 'vampir', 'freimaurer']:
			count = utils.intinp('Anzahl: ')
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


def main():
	players = utils.intinp('Anzahl Spieler: ')
	characters_game = gen_roles(inp_characters(players))
	data: dict = {
		'roles': characters_game,
		'alive': list(range(len(characters_game))),
		'alive_roles': list(characters_game),
		'love': [],
		'cult': [],
		'witch_potions': {'heal': True, 'death': True},
		'doubled_person': None,
		'doubled_role': None,
		'round_protected': [],
		'round_deaths': [],
		'round_werwolve_deaths': [], # also included in round_deaths
		'round_2_werwolve_deaths': False,
		'round_vampire_deaths': [], # not included in round_deaths
		'round_verfluchter_werwolve': False,
		'round_verfluchter_vampire': False,
		'round_trunkenbold': None,
		'round_trunkenbold_doubled': False,
		'round_altevettel': [],
		'round_beschwörerin': [],
		'round_goethe': [],
		'round_milch': {},
	}
	nightnum = 0
	while True:
		input('Nacht starten: ')
		current_night = []
		if nightnum == 0:
			for character in gdata.characters_first_night:
				if not character in current_night and character in data['alive_roles']:
					current_night.append(character)
		for character in gdata.characters_night:
			if not character in current_night and character in data['alive_roles']:
				current_night.append(character)
		if nightnum % 2:
			for character in gdata.characters_alternate_night:
				if not character in current_night and character in data['alive_roles']:
					current_night.append(character)
		
		time.sleep(2)
		print('\n')
		print('Das Dorf schläft ein!')
		for current_character in current_night:
			time.sleep(2)
			print('\n')
			print(f'{current_character.title()} ({data['roles'].index(current_character) + 1}): Wache auf!')
			data = actions.character_action(current_character, data)
			print(f'{current_character.title()}: Schlafe wieder ein.')
		print('\n')
		print('Das Dorf wacht auf.')
		data = actions.after_night(data)
		nightnum += 1


if __name__ == "__main__":
	main()
