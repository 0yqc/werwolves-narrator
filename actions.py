import time
import utils
import data as gdata


def character_action(character: str, data: dict) -> dict:
	role = None
	# ap: short for affected person
	for i in range(2):
		dg_second_action = None
		if character == 'doppelgängerin':
			ap = utils.intinp('Wähle deine gedoppelte Person: ')
			data.update({'doubled_person': ap})
			data.update({'doubled_role': data['roles'][ap - 1]})
		elif character in ('amor', 'jaguar'):
			dg_second_action = True
			v1 = utils.intinp('1. Verliebter: ')
			v2 = utils.intinp('2. Verliebter: ')
			data['love'].add((v1, v2))
		elif character == 'wolfskind':
			dg_second_action = True
			print('Wähle dein Idol.')
			input()
		elif character == 'trunkenbold':
			dg_second_action = True
			ap = utils.intinp('Wähle deinen heutigen Nächtigungsort: ')
			data['round_protected'].add(data['roles'].index('trunkenbold'))
			data.update({'round_tb': ap})
		elif character == 'freimaurer':
			input()
		elif character == 'kultführer':
			dg_second_action = True
			data['cult'].add(utils.intinp('Füge eine Person zum Kult hinzu: '))
		elif character in ('priester', 'leibwächter'):
			dg_second_action = True
			data['round_protected'].add(utils.intinp('geschützte Person: '))
		elif character in ('seherin', 'seher'):
			ap = utils.intinp('zu erkenennde Person: ')
			print(data['roles'][ap - 1].title())
			time.sleep(1)
		elif character == 'aura-seherin':
			ap = utils.intinp('zu erkenennde Person: ')
			print('Gut' if data['roles'][ap - 1] in gdata.characters_village else 'Böse')
			time.sleep(1)
		elif character == 'werwolf':
			ap = utils.intinp('Opfer: ')
			data['round_deaths'].add(ap)
			data['round_werwolve_deaths'].add(ap)
			if data['round_2_werwolve_deaths']:
				ap = utils.intinp('2. Opfer: ')
				data['round_deaths'].add(ap)
				data['round_werwolve_deaths'].add(ap)
		elif character == 'hexe':
			print(f'Opfer: {', '.join(f'{data['roles'][i - 1].title()} ({i})' for i in data['round_werwolve_deaths'])}')

		if 'doppelgängerin' in data['roles'] and character == data['doubled_role'] and dg_second_action and i == 0:
			print()
			print('Doppelgängerin-Aktion:')
			role = data['roles'].index('doppelgängerin')
			dg_action = True
		else:
			break
	return data
